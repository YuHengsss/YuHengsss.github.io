#!/usr/bin/env bash
# Refresh the citation data shown on the homepage.
#
# Google Scholar answers GitHub Actions runners with HTTP 403, so the scheduled
# workflow cannot fetch the data. Run this script from a normal machine instead
# (any clone of this repository, with push access):
#
#     bash google_scholar_crawler/update_from_local.sh
#
# It reads the Scholar profile once and force-pushes the JSON files to the
# google-scholar-stats branch, which the citation badges on the page read from.
set -euo pipefail
cd "$(dirname "$0")"
export GOOGLE_SCHOLAR_ID="${GOOGLE_SCHOLAR_ID:-sn2PeEkAAAAJ}"
remote="$(git -C .. remote get-url origin)"

rm -rf results
python main.py > /dev/null
cd results
git init -q
git add ./*.json
git commit -q -m "Updated Citation Data"
git push -q "$remote" HEAD:google-scholar-stats --force
cd ..
rm -rf results
echo "citation data pushed to google-scholar-stats"
