"""Fetch citation counts from a Google Scholar profile page.

Writes into results/:
  gs_data.json            total citations and per-paper counts (keyed by Scholar publication id)
  gs_data_shieldsio.json  shields.io endpoint file for the total
  cite_<id>.json          one shields.io endpoint file per paper; <id> is the part of the
                          Scholar publication id after the colon

A single request to the public profile page is used instead of the scholarly package:
Scholar stalls scholarly's multi-request crawl on CI runners.
"""
import json
import os
import re
import signal
import sys
from datetime import datetime

import requests
from bs4 import BeautifulSoup

# Never hold the runner: give up after 3 minutes.
if hasattr(signal, 'SIGALRM'):
    signal.alarm(180)

scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID', '').strip()
if not scholar_id:
    raise SystemExit('GOOGLE_SCHOLAR_ID is empty: set it as a repository secret.')

URL = 'https://scholar.google.com/citations'
HEADERS = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'),
    'Accept-Language': 'en-US,en;q=0.9',
}


def fetch(cstart):
    resp = requests.get(
        URL,
        params={'user': scholar_id, 'hl': 'en', 'cstart': cstart, 'pagesize': 100},
        headers=HEADERS,
        timeout=30,
    )
    print(f'GET cstart={cstart}: HTTP {resp.status_code}, {len(resp.text)} chars, final url {resp.url.split("?")[0]}')
    if resp.status_code != 200 or 'gsc_a_tr' not in resp.text:
        title = re.search(r'<title>(.*?)</title>', resp.text, re.S)
        print('page title:', title.group(1).strip()[:200] if title else None)
        raise SystemExit('Google Scholar did not return the profile page (blocked or rate limited).')
    return BeautifulSoup(resp.text, 'html.parser')


publications = {}
citedby = None
name = None
cstart = 0
while True:
    soup = fetch(cstart)
    if cstart == 0:
        name_el = soup.select_one('#gsc_prf_in')
        name = name_el.get_text(strip=True) if name_el else ''
        stats = soup.select('#gsc_rsb_st td.gsc_rsb_std')
        citedby = int(stats[0].get_text(strip=True)) if stats else 0
        hindex = int(stats[2].get_text(strip=True)) if len(stats) > 2 else None
        i10index = int(stats[4].get_text(strip=True)) if len(stats) > 4 else None
    rows = soup.select('tr.gsc_a_tr')
    for row in rows:
        link = row.select_one('a.gsc_a_at')
        if link is None:
            continue
        m = re.search(r'citation_for_view=([^&]+)', link.get('href', ''))
        if not m:
            continue
        pub_id = m.group(1)
        cites = row.select_one('.gsc_a_ac')
        cites_text = cites.get_text(strip=True) if cites else ''
        year = row.select_one('.gsc_a_y')
        publications[pub_id] = {
            'author_pub_id': pub_id,
            'num_citations': int(cites_text) if cites_text.isdigit() else 0,
            'bib': {
                'title': link.get_text(strip=True),
                'pub_year': year.get_text(strip=True) if year else '',
            },
        }
    if len(rows) < 100:
        break
    cstart += 100

if not publications:
    raise SystemExit('No publications parsed from the profile page.')

author = {
    'scholar_id': scholar_id,
    'name': name,
    'citedby': citedby,
    'hindex': hindex,
    'i10index': i10index,
    'updated': str(datetime.now()),
    'publications': publications,
}
print(json.dumps(author, indent=2, ensure_ascii=True))

os.makedirs('results', exist_ok=True)
with open('results/gs_data.json', 'w', encoding='utf-8') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

with open('results/gs_data_shieldsio.json', 'w', encoding='utf-8') as outfile:
    json.dump({'schemaVersion': 1, 'label': 'citations', 'message': f'{citedby}'}, outfile)

for pub_id, pub in publications.items():
    with open(f"results/cite_{pub_id.split(':')[-1]}.json", 'w', encoding='utf-8') as outfile:
        json.dump({'schemaVersion': 1, 'label': 'citations', 'message': f"{pub['num_citations']}"}, outfile)

print(f'wrote {len(publications)} per-paper files; total citations {citedby}', file=sys.stderr)
