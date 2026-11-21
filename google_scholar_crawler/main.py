from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os
import signal

# Google Scholar sometimes stalls requests from CI runners; fail after 10 minutes
# instead of holding the runner until the 6-hour job limit.
if hasattr(signal, 'SIGALRM'):
    signal.alarm(600)

scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID', '').strip()
if not scholar_id:
    raise SystemExit('GOOGLE_SCHOLAR_ID is empty: set it as a repository secret.')

author: dict = scholarly.search_author_id(scholar_id)
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

# One shields.io endpoint file per paper, named by the part of the Scholar
# publication id after the colon, e.g. results/cite_u5HHmVD_uO8C.json
for pub_id, pub in author['publications'].items():
    paper_data = {
      "schemaVersion": 1,
      "label": "citations",
      "message": f"{pub.get('num_citations', 0)}",
    }
    with open(f"results/cite_{pub_id.split(':')[-1]}.json", 'w') as outfile:
        json.dump(paper_data, outfile, ensure_ascii=False)
