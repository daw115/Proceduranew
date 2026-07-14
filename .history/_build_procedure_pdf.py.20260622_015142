#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PDF głównej instrukcji IDCC z PROCEDURA_IDCC_TSO_v5_2.html.
   - dokłada brakujące kotwice (id) do czynności (5.1, C.6–C.12, 8.1/8.2/8.3),
   - renderuje WeasyPrint (media=print → sidebar/topbar ukryte),
   - id → named destinations + nagłówki h1–h4 → zakładki PDF (bookmarks),
   - wypisuje mapę kotwica→strona (do hiperłączy w mailu).
   Uruchom: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 _build_procedure_pdf.py
"""
import os
os.environ.setdefault('DYLD_FALLBACK_LIBRARY_PATH', '/opt/homebrew/lib')
import re, json, pathlib
import weasyprint
from pypdf import PdfReader

ROOT = pathlib.Path('/Volumes/SSD/CLAUDE_WORK/Procedura')
SRC  = ROOT / 'PROCEDURA_IDCC_TSO_v5_2.html'
OUT  = ROOT / 'PROCEDURA_IDCC_TSO_v5_2.pdf'

# (prefiks nagłówka w źródle) -> nowy id kotwicy
ANCHORS = [
    ('<h3>5.1.',  's5common'),
    ('<h4>C.6.',  's7c6'),
    ('<h4>C.7.',  's7c7'),
    ('<h4>C.8.',  's7c8'),
    ('<h4>C.9.',  's7c9'),
    ('<h4>C.10.', 's7c10'),
    ('<h4>C.11.', 's7c11'),
    ('<h4>C.12.', 's7c12'),
    ('<h3>8.1.',  's8minio'),
    ('<h3>8.2.',  's8perun'),
    ('<h3>8.3.',  's8core'),
]

# Nadpisanie druku: porządne @page (marginesy, stopka klasyfikacji + numer strony),
# twardy ukryt sidebar/topbar/edytora, łamanie sekcji przed <h2>.
PRINT_CSS = '''
<style id="pdf-print-overrides">
@page {
  size: A4; margin: 16mm 14mm 18mm;
  @bottom-left { content:"Klasyfikacja: Informacja służbowa GK PSE / GK PSE Confidential"; font-size:7pt; color:#97a3b0; }
  @bottom-right{ content:"Procedura IDCC TSO v5.2 · str. " counter(page); font-size:7pt; color:#97a3b0; }
}
.sidebar,.topbar,.editor-bar,.search-panel{ display:none !important; }
.main{ margin-left:0 !important; }
body{ -weasy-hyphens:none; }
h2{ break-before: page; bookmark-level: 1; }
h1{ bookmark-level: 1; }
h3{ bookmark-level: 2; break-after: avoid; }
h4{ bookmark-level: 3; break-after: avoid; }
table,.risk-card,.box,ol.steps,figure,img{ break-inside: avoid; }
img{ max-width:100% !important; height:auto !important; }
a{ color:#0052CC; }
</style>
'''

def add_anchors(html):
    added = []
    for prefix, aid in ANCHORS:
        if f'id="{aid}"' in html:
            continue
        # <h3>5.1. ->  <h3 id="s5common" class="anchor-target">5.1.
        tag = prefix[:3]               # <h3 / <h4
        repl = f'{tag} id="{aid}" class="anchor-target">{prefix[4:]}'
        new = html.replace(prefix, repl, 1)
        if new != html:
            html, ok = new, True
        else:
            ok = False
        added.append((aid, ok))
    return html, added

def build():
    html = SRC.read_text(encoding='utf-8')
    html, added = add_anchors(html)
    # persist kotwice w źródle (idempotentnie) + wstrzyknij print-overrides
    if '<style id="pdf-print-overrides">' not in html:
        html = html.replace('</head>', PRINT_CSS + '</head>', 1)
    SRC.write_text(html, encoding='utf-8')
    print('Kotwice dodane:', ', '.join(f'{a}{"" if ok else "(JUŻ/BRAK)"}' for a, ok in added))

    weasyprint.HTML(string=html, base_url=str(ROOT)).write_pdf(str(OUT))

    r = PdfReader(str(OUT))
    nd = r.named_destinations
    pages = {}
    for name, dest in nd.items():
        try:
            pages[name] = r.get_destination_page_number(dest) + 1
        except Exception:
            pass
    (ROOT / 'anchors_pages.json').write_text(
        json.dumps(pages, ensure_ascii=False, indent=2), encoding='utf-8')

    want = ['top','s3','s4','s4a','s4b','s4c','s4d','s5','s5common','s5a','s5b','s5iva','s5atc',
            's6','s6fba','s6atc','s7','s7c1','s7c2','s7c3','s7c4','s7c5','s7dash',
            's7c6','s7c7','s7c8','s7c9','s7c10','s7c11','s7c12',
            's8','s8minio','s8perun','s8core','s9','s10','s11','aneks']
    print(f'PDF: {OUT}  ({OUT.stat().st_size:,} B) | strony={len(r.pages)} | named_dests={len(nd)}')
    print('--- kotwica → strona ---')
    for w in want:
        print(f'  #{w:<10} -> str. {pages.get(w, "BRAK")}')

if __name__ == '__main__':
    build()
