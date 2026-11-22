#!/usr/bin/env bash
# Baut report/report.html aus den ODT-Tabellen in data/ und rendert das PDF (Chromium).
set -euo pipefail
cd "$(dirname "$0")/.."
python3 tools/build.py tools/template.html report/report.html
cd report
chromium --headless --no-pdf-header-footer --print-to-pdf=W2-PM-FINAL-Report-PM2-PM3.pdf report.html
