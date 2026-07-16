#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator PROCEDURA_IDCC_TSO_v7.html — kompletna, samowystarczalna instrukcja z ekranami.

Warstwy:
  • NAWIGACJA — szybki start, spis treści i 41 skróconych kroków działania.
  • DETAL     — szczegółowe instrukcje, scenariusze, tabele i osadzone materiały ekranowe.

Źródła:
  Inwentarz_IDCC.md            — narzędzia N01–N22, legenda, ryzyka U01–U23, procedury P01–P06, buckety, mapa relacji
  popup_content_IDCC.json      — katalog 78 plików FIDx (opis, ścieżka, źródło, TET/CET, profil)
  CCM/staticHints-IDCC-all.txt — 974 stany / 71 plików (sytuacja + procedury awaryjne)
  screens_manifest.json        — 309 screenów (opis, mapowanie, podpis, jakość)
"""
import json, re, html, base64, mimetypes, os
from pathlib import Path
from collections import defaultdict, OrderedDict
import markdown

ROOT = Path(__file__).parent
OUT = ROOT / os.environ.get('PROCEDURA_OUTPUT', 'PROCEDURA_IDCC_TSO_v7.html')
STICKERS_OUT = ROOT / os.environ.get('PROCEDURA_STICKERS_OUTPUT', 'STICKERY_IDCC.md')
FINAL_LAYOUT = os.environ.get('PROCEDURA_LAYOUT', '').strip().lower() == 'measured-flow'
INCLUDE_COMMENTS = os.environ.get('PROCEDURA_INCLUDE_COMMENTS', '1') != '0'
BODY_CLASS = 'edition-final' if FINAL_LAYOUT else 'edition-standard'

# Metryka wydania roboczego. Pola formalne pozostają jawnie puste, ponieważ
# materiały źródłowe nie wskazują autora, zatwierdzającego ani dat zatwierdzenia.
DOC_META = {
    'working_id': 'PROCEDURA_IDCC_TSO_v7',
    'formal_code': '—',
    'version': '7',
    'date': '—',
    'status': '☒ Draft ☐ Final',
    'document_type': 'Połączony dokument roboczy NOR/BUP',
    'author': '—',
    'approver': '—',
    'approval_date': '—',
}


def esc(s): return html.escape(str(s or ''))


_ASSET_CACHE = {}
def asset_uri(file):
    """Osadza lokalny obraz jako data URI, aby wynikowy HTML był jednym plikiem."""
    rel = Path(file)
    path = (ROOT / rel).resolve()
    try:
        path.relative_to(ROOT.resolve())
    except ValueError as exc:
        raise ValueError(f'Zasób poza katalogiem procedury: {file}') from exc
    if not path.is_file():
        raise FileNotFoundError(f'Brak obrazu wymaganego przez procedurę: {file}')
    key = str(rel).replace('\\', '/')
    if key not in _ASSET_CACHE:
        mime = mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
        payload = base64.b64encode(path.read_bytes()).decode('ascii')
        _ASSET_CACHE[key] = f'data:{mime};base64,{payload}'
    return _ASSET_CACHE[key]

# ── 1. screeny: manifest → grupy obszarów ─────────────────────────────────
MAN = json.load(open(ROOT/'screens_manifest.json', encoding='utf-8'))
FIGURE_NUMBERS = {item['file']: index for index, item in enumerate(MAN, 1)}
assert len(MAN) == 309 and len(FIGURE_NUMBERS) == len(MAN), (
    'Manifest musi zawierać 309 unikalnych plików ekranowych')
try:
    from PIL import Image
except ImportError as exc:
    raise RuntimeError('Generator wymaga pakietu Pillow do odczytu naturalnych wymiarów obrazów') from exc

_invalid_image_dimensions = []
for _m in MAN:
    try:
        with Image.open(ROOT/_m['file']) as _im:
            _m['_wh'] = _im.size
        if not all(isinstance(value, int) and value > 0 for value in _m['_wh']):
            raise ValueError(f'nieprawidłowy rozmiar {_m["_wh"]}')
    except Exception as exc:
        _invalid_image_dimensions.append((_m.get('file', '?'), str(exc)))
assert not _invalid_image_dimensions, (
    f'Nie można odczytać naturalnych wymiarów obrazów: {_invalid_image_dimensions[:10]}')

def area_of(f):
    if f.startswith('screens/ccm'):       return 'ccm'
    if f.startswith('screens/bup'):        return 'bup'
    if f.startswith('screens/nor'):        return 'nor'
    if f.startswith('screens/ac_zp'):      return 'aczp'
    if f.startswith('screens_fid607'):     return 'fid607'
    if f.startswith('screens_kreatoridcf'):return 'kreator'
    return 'other'
SCR = defaultdict(list)
for m in MAN:
    m['area'] = area_of(m['file'])
    SCR[m['area']].append(m)
def natkey(s):
    return [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', s)]
for a in SCR: SCR[a].sort(key=lambda m: natkey(m['file']))
BYFILE = {m['file']: m for m in MAN}

def is_good(m):
    if m.get('quality') in ('duplicate','blurred'): return False
    if re.search(r'nieczyteln|duplikat', m.get('caption',''), re.I): return False
    return True

def img(file, cap=None, cls='shot'):
    """Osadza obraz z numerem stabilnym względem kolejności screens_manifest.json."""
    m = BYFILE.get(file, {})
    cap = cap or m.get('caption') or m.get('shows') or ''
    number = FIGURE_NUMBERS.get(file)
    if number is None:
        raise KeyError(f'Brak numeru rysunku dla zasobu: {file}')
    width, height = m.get('_wh', (0, 0))
    size_attrs = f' width="{width}" height="{height}"' if width and height else ''
    size_style = f' style="--screen-width:{width}px"' if width else ''
    size_note = f'<span class="caption-size">Oryginalny rozmiar: {width} × {height} pikseli</span>' if width and height else ''
    return (f'<figure class="{cls}" data-figure-number="{number}"{size_style}><img loading="lazy" src="{asset_uri(file)}" alt="{esc(cap)}" '
            f'data-source="{esc(file)}"{size_attrs} tabindex="0" role="button" aria-label="Powiększ rysunek {number}: {esc(cap)}">'
            f'<figcaption><span class="caption-label">Rysunek {number}</span>'
            f'<span class="caption-text">{esc(cap)}</span>{size_note}</figcaption></figure>')

def gallery(area, title, intro='', only=None, exclude=None):
    items = [m for m in SCR.get(area,[]) if is_good(m)]
    if only:    items = [m for m in items if m['file'] in only]
    if exclude: items = [m for m in items if m['file'] not in exclude]
    if not items: return ''
    shots = items
    figs = ''.join(img(m['file']) for m in shots)
    return (f'<details class="gal screen-gallery" open><summary>{esc(title)} — {len(shots)} ekranów'
            f' · kliknij ekran, aby powiększyć</summary>'
            f'{("<p>"+esc(intro)+"</p>") if intro else ""}<div class="grid">{figs}</div></details>')

def featured(file):
    """Pojedynczy wyróżniony screen w kroku (jeśli istnieje)."""
    return img(file) if file in BYFILE else ''


def source_archive():
    """Zachowuje komplet materiałów: duplikaty i nieczytelne ujęcia są oddzielone od instrukcji."""
    items = [m for m in MAN if not is_good(m)]
    if not items:
        return ''
    figs = ''.join(img(m['file'], cap='Materiał archiwalny — ' + (m.get('caption') or m.get('shows') or m['file'])) for m in items)
    return (f'<details class="gal source-archive"><summary>Archiwum materiałów ekranowych — '
            f'{len(items)} duplikatów lub ujęć pomocniczych</summary>'
            '<p class="note">Materiały pozostawiono dla kompletności. Ze względu na jakość lub powtórzenie '
            'nie stanowią samodzielnych kroków instrukcji.</p><div class="grid">' + figs + '</div></details>')

# ── 2. katalog plików FIDx ────────────────────────────────────────────────
FILES = json.load(open(ROOT/'popup_content_IDCC.json', encoding='utf-8'))

# ── 3. staticHints → stany per kod ────────────────────────────────────────
def parse_hints():
    t = (ROOT/'CCM'/'staticHints-IDCC-all.txt').read_text(encoding='utf-8')
    # podziel na bloki kluczy 'NAZWA^KOD': [ ... ],
    blocks = re.split(r"\n    '([^']+)':\s*\[", t)
    res = OrderedDict()
    # blocks: [pre, key1, body1, key2, body2, ...]
    for i in range(1, len(blocks), 2):
        key = blocks[i]; body = blocks[i+1]
        code = key.split('^')[-1]
        states = []
        # każdy obiekt stanu { ... }
        for obj in re.findall(r'\{\s*status:\s*\[(.*?)\](.*?)\}', body, re.S):
            statuses_raw, rest = obj
            cols = re.findall(r"colName:\s*'((?:[^'\\]|\\.)*)',\s*status:\s*DashboardItemStatus\.([A-Z_]+)", statuses_raw)
            def field(name):
                m = re.search(name + r":\s*'((?:[^'\\]|\\.)*)'", rest, re.S)
                return m.group(1).replace("\\'","'").replace('\\"','"') if m else ''
            states.append({
                'cols': [(c.replace("\\'","'"), s) for c,s in cols],
                'sit': field('situationDescription'),
                'proc': field('emergencyProcedures'),
            })
        res.setdefault(code, states)
    return res
HINTS = parse_hints()

STATUS_PL = {  # enum → etykieta PL + klasa koloru
 'SUCCESS':('Sukces','ok'),'FORCEDSUCCESS':('Sukces ręczny (R)','ok'),
 'SENTMANUALLY':('Wysłany ręcznie (W)','ok'),'SENTMANUALLYAFTERCET':('Wysłany ręcznie po CET (W↑)','warn'),
 'CONN_AFTER_CET':('Dostarczone po CET','warn'),'WARNING':('Ostrzeżenie — zbliża się TET','warn'),
 'FAILURE':('Błąd / awaria','err'),'ACKNOTRECEIVED':('Brak ACK','err'),'FILESIZEBAD':('Zły rozmiar pliku','err'),
 'EXCEEDED':('Przekroczono CET','err'),'PROCESSRUNNING':('Przetwarzanie w toku','run'),'UNKNOWN':('Brak / nieznany','idle'),
}
def status_badge(enum):
    lab,cls = STATUS_PL.get(enum,(enum,'idle'))
    return f'<span class="st st-{cls}" title="{esc(enum)}">{esc(lab)}</span>'

# enum → graficzny kafelek (img_ccm/tiles) — taki jak na pulpicie CCM
ENUM2TILE = {
 'SUCCESS':'zielony.png','FORCEDSUCCESS':'zielony_R.png','SENTMANUALLY':'ciemnozielony_W.png',
 'SENTMANUALLYAFTERCET':'W_po_CET.png','CONN_AFTER_CET':'fioletowy.png','WARNING':'pomarańczowy.png',
 'FAILURE':'czerwony.png','ACKNOTRECEIVED':'czerwony_q.png','FILESIZEBAD':'czerwony_excl.png',
 'EXCEEDED':'czarny.png','PROCESSRUNNING':'szary_q.png','UNKNOWN':'szary.png',
}
def status_tile(cn, enum):
    """Kafelek graficzny + etykieta kolumny pod spodem; pełny opis statusu w tooltipie."""
    lab,_ = STATUS_PL.get(enum,(enum,'idle'))
    tile = ENUM2TILE.get(enum,'puste.png')
    return (f'<span class="tcell" title="{esc(cn)}: {esc(lab)} ({esc(enum)})">'
            f'<img class="tile" src="{asset_uri(f"img_ccm/tiles/{tile}")}" alt="{esc(lab)}" data-source="img_ccm/tiles/{esc(tile)}">'
            f'<span class="tlab">{esc(cn)}</span></span>')


def state_tone(cols):
    """Najwyższy priorytet operacyjny wiersza: czerwony > żółty > fioletowy > zielony."""
    enums = {enum for _, enum in cols}
    if enums & {'FAILURE', 'ACKNOTRECEIVED', 'FILESIZEBAD', 'EXCEEDED'}:
        return 'danger', 'ZAGROŻENIE'
    if enums & {'WARNING', 'SENTMANUALLYAFTERCET', 'CONN_AFTER_CET'}:
        return 'warning', 'UWAGA'
    if 'PROCESSRUNNING' in enums:
        return 'running', 'W TOKU'
    if enums and enums <= {'SUCCESS', 'FORCEDSUCCESS', 'SENTMANUALLY'}:
        return 'success', 'PRAWIDŁOWO'
    return 'neutral', 'INFORMACJA'

# ── 4. Inwentarz markdown → HTML (referencja: narzędzia/ryzyka/procedury/buckety) ─
md = markdown.Markdown(extensions=['tables','attr_list','md_in_html','sane_lists'])
INW = (ROOT/'Inwentarz_IDCC.md').read_text(encoding='utf-8')
def inw_slice(start, end, prefix=''):
    """Wytnij fragment Inwentarza między nagłówkami i przekonwertuj do HTML."""
    md.reset()
    body = prefix + INW.split(start)[1].split(end)[0]
    return md.convert(body)
TOOLS_HTML = inw_slice('# 1. Narzędzia', '# 2. Stany kafelków', '# 1. Narzędzia')

# ── v5_2: slicer sekcji starej procedury (gotowe, skondensowane treści) ──────
V52 = (ROOT/'PROCEDURA_IDCC_TSO_v5_2.html').read_text(encoding='utf-8')

def _div_balance(body):
    d = body.count('<div') - body.count('</div>')
    while d < 0 and body.rstrip().endswith('</div>'):
        body = body.rstrip()[:-6]; d += 1
    if d < 0:   # nadmiarowe zamknięcia w środku — zneutralizuj od końca
        for _ in range(-d):
            k = body.rfind('</div>'); body = body[:k] + body[k+6:]
    if d > 0:
        body += '</div>' * d
    return body

def v52_slice(start_id, end_id=None, start_h3=None, end_h3=None):
    """Wycina sekcję v5_2 między <h2 id=start_id> a <h2 id=end_id> (lub między
    nagłówkami h3 o podanych prefiksach tekstu) i degraduje nagłówki o 1 poziom."""
    if start_h3:
        i = V52.find(start_h3)
        j = V52.find(end_h3) if end_h3 else V52.find('<h2', i)
        body = '<h3>' + V52[i:j]
        i2 = body.rfind('<h3>', 0, len(body))
    else:
        i = V52.find(f'<h2 id="{start_id}"')
        j = V52.find(f'<h2 id="{end_id}"') if end_id else V52.find('<h2', i+10)
        if j == -1:
            cands = [V52.find(m, i) for m in ('</main>', '<footer', '</body>', '</html>')]
            cands = [c for c in cands if c != -1]
            j = min(cands) if cands else len(V52)
        body = V52[i:j]
        body = body.replace('</body>', '').replace('</html>', '')
    body = re.sub(r'<h4', '<h5', body); body = re.sub(r'</h4>', '</h5>', body)
    body = re.sub(r'<h3', '<h4', body); body = re.sub(r'</h3>', '</h4>', body)
    body = re.sub(r'<h2 ', '<h3 ', body); body = re.sub(r'</h2>', '</h3>', body)
    body = body.replace(' class="anchor-target"', '')
    return _div_balance(body)

def v52_h3block(prefixes):
    """Sklej wybrane podsekcje h3 (po prefiksie tytułu) z całego v5_2."""
    out = []
    for p in prefixes:
        m = re.search(r'<h3[^>]*>\s*' + re.escape(p), V52)
        if not m: continue
        i = m.start(); j = V52.find('<h3', i+5)
        j2 = V52.find('<h2', i+5)
        if j == -1 or (j2 != -1 and j2 < j): j = j2
        seg = V52[i:j]
        seg = re.sub(r'<h4', '<h5', seg); seg = re.sub(r'</h4>', '</h5>', seg)
        seg = re.sub(r'<h3', '<h4', seg); seg = re.sub(r'</h3>', '</h4>', seg)
        out.append(_div_balance(seg.replace(' class="anchor-target"', '')))
    return '\n'.join(out)

# ── pełna baza ryzyk R01–R29 (markdown → HTML, degradacja nagłówków) ─────────
RYZ = (ROOT/'Ryzyka_pelna_baza_IDCC.md').read_text(encoding='utf-8')
RYZ = RYZ[RYZ.find('<a id="R01">'):]          # pomiń nagłówek i spis treści
md.reset()
RYZ_HTML = md.convert(RYZ)
RYZ_HTML = re.sub(r'<h2', '<h5', RYZ_HTML); RYZ_HTML = re.sub(r'</h2>', '</h5>', RYZ_HTML)
RYZ_HTML = re.sub(r'<h1', '<h4 class="risk-h"', RYZ_HTML); RYZ_HTML = re.sub(r'</h1>', '</h4>', RYZ_HTML)

def load_frag7(name):
    p = ROOT / name
    if not p.is_file():
        raise FileNotFoundError(f'Brak wymaganego fragmentu procedury: {name}')
    return p.read_text(encoding='utf-8')


# rejestr narzędzi: kod Nxx → unikalna nazwa (krótka, bez numeru)
CODE2NAME = {}
for code, full in re.findall(r'^### N(\d+) — (.+)$', INW, re.M):
    CODE2NAME[code] = full.split(' (')[0].strip()   # krótka unikalna nazwa

def linkify_refs(s):
    """Escapuje tekst i zamienia 'Nazwa [Nxx]' / 'Nazwa (Nxx)' na hiperłącze do definicji narzędzia."""
    s = esc(s)
    s = re.sub(r'([^→+,\[]+?)\s*\[N(\d+)(?:/N?\d+)?\]',
               lambda m: f'<a href="#N{m.group(2)}">{m.group(1).strip()}</a>', s)   # [Nxx] i [N07/N08]
    s = re.sub(r'([^()→+,]+?)\s*\(N(\d+)(?:/N?\d+)?\)',
               lambda m: f'<a href="#N{m.group(2)}">{m.group(1).strip()}</a>', s)   # (Nxx) i (N07/N08)
    return s

def denumber(h):
    """Usuwa widoczne kody Nxx: nagłówki tracą prefiks, tekst każdego linku #Nxx = unikalna nazwa, reszta kodów znika."""
    h = re.sub(r'<a href="#N(\d+)">.*?</a>',
               lambda m: f'<a href="#N{m.group(1)}">{esc(CODE2NAME.get(m.group(1), m.group(0)))}</a>', h)
    h = re.sub(r'(<h3[^>]*>)\s*N\d+\s*—\s*', r'\1', h)         # nagłówek narzędzia bez "Nxx —"
    h = re.sub(r'\s*\[N\d+(?:/N?\d+)?\]', '', h)               # resztki [Nxx]/[N07/N08]
    h = re.sub(r'\s*\((?:N\d+)(?:/N?\d+)?\)', '', h)           # resztki (Nxx)/(N07/N08)
    # gołe kody Nxx w tekście (poza atrybutami) → hiperłącze z nazwą narzędzia
    h = re.sub(r'(>[^<>]*?)\bN(\d{2})\b',
               lambda m: m.group(1) + (f'<a href="#N{m.group(2)}">{esc(CODE2NAME[m.group(2)])}</a>'
                                       if m.group(2) in CODE2NAME else 'N'+m.group(2)), h)
    return h

# ── 5. STICKERY (karty skrócone) ──────────────────────────────────────────
STICKERS = [
 ('#sec-proces','📘','Proces IDCC','Kroki istotne dla PSE: IDCC(a) i wspólnie (b)–(d), pliki FIDx, automatyczne fallbacki i działania backupowe.'),
 ('#proc-mail','📧','Szablony maili','19 szablonów operacyjnych Core ID (EN) + kiedy użyć; oznaczone granice PSE.'),
 ('#sec-narzedzia','🧰','Narzędzia','CCM, Core CC Tool, Perun4V, MinIO, ZP, Connector, Kreatory, sFTP, wsparcie.'),
 ('#sec-legenda','🎨','Legenda statusów','13 kafelków → enum statusu. Kolor + znacznik = sytuacja pliku.'),
 ('#sec-katalog','🗂️','Katalog plików FIDx','78 plików: opis, ścieżka, źródło, TET/CET, profil + warianty stanów.'),
 ('#sec-ccm','🖥️','Czynności w CCM','C.1–C.5: pulpit, info, wysyłka przed/po CET, status ręczny, błędy walidacji.'),
 ('#sec-nor','✅','Walidacja domeny — NOR','Tryb normalny DA: schemat decyzyjny, Perun4V, raporty CNEC/LTA.'),
 ('#sec-bup','🛟','Walidacja domeny — BUP','Tryb backup DA: CCA, F320, paczki ZIP, redukcja IVA, RLTA w ZP.'),
 ('#sec-fid607','🔑','GLSK (FIDx-607) — stany','32 stany kafelka: sukces, w toku, błędy, wysyłka ręczna.'),
 ('#sec-kreator','🛠️','Kreator IDCF','Publikacja GLSK/CBCORA/RA → Connector → MinIO → weryfikacja w CCM.'),
 ('#sec-aczp','📄','AC w ZP (FIDx-831)','Ręczna obsługa Allocation Constraints, tabela NTC/ATC, wersjonowanie.'),
 ('#sec-procedury','🧭','Procedury P01–P06','Reagowanie na ryzyka + procedury narzędziowe krok po kroku.'),
 ('#sec-ryzyka','⚠️','Ryzyka U01–U23','Katalog ryzyk, kody ACK, ścieżka zgłoszenia: CIZ / WPO / PSE-I.'),
 ('#sec-minio','🗄️','Buckety MinIO + mapa relacji','Pełna mapa lokalizacji plików; narzędzie ↔ ryzyko ↔ procedura.'),
]
def sticker_board():
    cards = ''.join(
        f'<a class="sticker" href="{href}"><span class="ic">{ic}</span>'
        f'<span class="ti">{esc(t)}</span><span class="de">{esc(d)}</span>'
        f'<span class="go">▸ pełna instrukcja</span></a>'
        for href,ic,t,d in STICKERS)
    return f'<div class="board">{cards}</div>'

def mini_sticker(href, txt):
    return f'<a class="mini" href="{href}">▸ {esc(txt)}</a>'

# ── 6. Sekcja: katalog plików ─────────────────────────────────────────────
ITER_ORDER = ['IDCC(a)','IDCC(b)','IDCC(c)','IDCC(d)','—']
def iter_key(f):
    it = (f.get('iteracja') or '—').strip()
    return ITER_ORDER.index(it) if it in ITER_ORDER else len(ITER_ORDER)

def file_card(f, card_id=None):
    code = f['kod']
    card_id = card_id or f'file-{code}'
    states = HINTS.get(code, [])
    meta = (f'<div class="meta"><span><b>Kod:</b> {esc(code)}</span>'
            f'<span><b>Profil:</b> {esc(f.get("profil"))}</span>'
            f'<span><b>TET:</b> {esc(f.get("target_end_time"))}</span>'
            f'<span><b>CET:</b> {esc(f.get("critical_end_time"))}</span>'
            f'<span><b>Źródło:</b> {linkify_refs(f.get("zrodlo"))}</span>'
            f'<span><b>Wersja:</b> {esc(f.get("wersja"))}</span></div>')
    body = (f'<p class="definition">{esc(f.get("opis_pliku"))}</p>'
            f'<p class="path"><b>Przebieg komunikacji przy publikacji pliku:</b> {linkify_refs(f.get("sciezka_pliku"))}</p>')
    st_html = ''
    if states:
        rows = ''
        for s in states:
            tiles = ''.join(status_tile(cn,en) for cn,en in s['cols'])
            tone, tone_label = state_tone(s['cols'])
            rows += (f'<tr class="state-row state-{tone}"><td class="stcol">'
                     f'<span class="state-label label-{tone}">{tone_label}</span>{tiles}</td>'
                     f'<td>{esc(s["sit"])}</td><td>{s["proc"]}</td></tr>')
        st_html = (f'<details class="states"><summary>Warianty stanów ({len(states)})</summary>'
                   f'<table class="sttab"><thead><tr><th>Status kafelka</th><th>Sytuacja</th>'
                   f'<th>Działania awaryjne</th></tr></thead><tbody>{rows}</tbody></table></details>')
    return (f'<div class="fcard" id="{esc(card_id)}"><h4>{esc(f.get("nazwa_przeplywu"))} '
            f'<span class="code">{esc(code)}</span></h4>{meta}{body}{st_html}</div>')

def section_katalog():
    groups = defaultdict(list)
    for f in FILES: groups[(f.get('iteracja') or '—')].append(f)
    out = ''
    card_occurrences = defaultdict(int)
    for it in sorted(groups, key=lambda i: ITER_ORDER.index(i) if i in ITER_ORDER else 99):
        fs = groups[it]
        cards = []
        for file_data in sorted(fs, key=lambda x: x['kod']):
            code = file_data['kod']
            card_occurrences[code] += 1
            occurrence = card_occurrences[code]
            card_id = f'file-{code}' if occurrence == 1 else f'file-{code}-{occurrence}'
            cards.append(file_card(file_data, card_id))
        out += f'<h3>{esc(it)} — {len(fs)} plików</h3><div class="fgrid">{"".join(cards)}</div>'
    return out

# ── 7. Złożenie HTML ──────────────────────────────────────────────────────
CSS = """
:root{
 --paper:#edf1f5;--panel:#ffffff;--ink:#14243a;--fg:#263548;--mut:#647183;
 --rule:#d9e0e7;--rule2:#bcc7d2;--navy:#123b63;--acc:#155f97;--accbg:#eaf2f8;
 --ok:#146b2d;--okb:#e6f2e9;--warn:#8a5700;--warnb:#fbf1dc;--err:#b3261e;--errb:#fae9e7;
 --run:#5b3fa8;--runb:#efeaf8;--idle:#67707e;--idleb:#edf0f3;
 --yellow:#f4c542;--teal:#0f766e;--tealbg:#e6f5f2;
 --sans:'Aptos','Segoe UI',Arial,sans-serif;
 --cond:'Aptos Display','Segoe UI Semibold','Arial Narrow',sans-serif;
 --serif:Georgia,'Times New Roman',serif;
 --mono:'Cascadia Mono','SFMono-Regular',Consolas,'Courier New',monospace;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font:15px/1.58 var(--sans);color:var(--fg);background:var(--paper)}
p{margin:.58em 0}
main ul,main ol{margin:.62em 0;padding-left:1.48em}
main li{margin:.36em 0}
main ul>li::marker{color:var(--acc);font-size:.92em}
main ol>li::marker{color:var(--navy);font-family:var(--mono);font-weight:700}
main ul ul>li::marker{color:var(--mut)}
::selection{background:#ffe79a;color:var(--ink)}
:target{animation:hl 2.2s ease-out 1}
h2:target,h3:target,h4:target,div:target,section:target{scroll-margin-top:24px}
@keyframes hl{0%{background:#fff3bf;box-shadow:0 0 0 8px #fff3bf}100%{background:transparent;box-shadow:0 0 0 8px transparent}}
.wrap{display:flex;max-width:1640px;margin:0 auto;min-height:100vh}
/* ── nawigacja procedury: pięć formalnych grup A–E ── */
nav:not(.section-links){position:sticky;top:0;align-self:flex-start;width:310px;height:100vh;overflow:auto;
background:linear-gradient(180deg,#102f4c 0%,var(--ink) 100%);padding:24px 15px 42px;font-size:13px;
scrollbar-width:thin;scrollbar-color:#50708e transparent}
nav:not(.section-links)>h2{font:700 11px/1 var(--mono);letter-spacing:.18em;text-transform:uppercase;color:#a9c3d8;
margin:0 5px 17px;padding:0 0 12px;border-bottom:1px solid rgba(255,255,255,.18)}
nav:not(.section-links) a{display:grid;grid-template-columns:28px 1fr;gap:8px;align-items:start;color:#dce7f0;text-decoration:none;
padding:6px 8px;border-left:3px solid transparent;border-radius:0 4px 4px 0;line-height:1.35}
nav:not(.section-links) a>span{font:700 10.5px/1.6 var(--mono);color:#8fb2ce}
nav:not(.section-links) a:hover,nav:not(.section-links) a:focus-visible{background:rgba(255,255,255,.09);border-left-color:var(--yellow);color:#fff;outline:none}
.nav-start{margin-bottom:18px;background:rgba(255,255,255,.05)}
.nav-group{margin:0 0 17px}.nav-group-heading{display:flex;align-items:center;gap:8px;margin:0 7px 5px;padding-bottom:5px;
border-bottom:1px solid rgba(255,255,255,.12);color:#fff;font:700 11px var(--cond);letter-spacing:.035em}
.nav-group-heading span{display:grid;place-items:center;width:22px;height:22px;background:#fff;color:var(--navy);border-radius:2px;font:800 11px var(--mono)}
.nav-group-heading b{font-weight:700}
/* ── kolumna główna: dokument operacyjny ── */
main{flex:1;min-width:0;padding:34px 48px 72px;max-width:1260px;background:var(--panel);
border-right:1px solid var(--rule);box-shadow:0 0 36px rgba(20,36,58,.08)}
h1{font:750 32px/1.14 var(--cond);letter-spacing:.005em;color:var(--ink);margin:.25em 0 .1em}
h2{font:730 23px/1.2 var(--cond);letter-spacing:.005em;color:var(--ink);margin-top:2.4em;padding-bottom:8px;border-bottom:2px solid var(--navy)}
h3{font:700 18px/1.3 var(--cond);letter-spacing:.005em;color:var(--navy);margin-top:1.8em}
h4{font:700 15px/1.35 var(--sans);color:var(--acc);margin:1.2em 0 .38em}
h5{font:700 13.5px var(--sans);color:var(--ink);margin:.9em 0 .25em}
code{font:500 .92em var(--mono);background:var(--idleb);border:1px solid var(--rule);
border-radius:3px;padding:0 5px;color:var(--ink);word-break:break-all}
a{color:var(--acc)}
main a:not(.quickcard):not(.mini){color:var(--acc);text-decoration-line:underline;text-decoration-thickness:1px;text-decoration-color:rgba(21,95,151,.38);text-underline-offset:2px}
main a:not(.quickcard):not(.mini):hover{color:var(--navy);text-decoration-color:currentColor}
main a:focus-visible{outline:3px solid var(--yellow);outline-offset:2px;border-radius:2px}
.lead{font:400 16px/1.68 var(--serif);color:#455367;font-style:italic}
.lead code,.lead b,.lead strong{font-style:normal}
.compact-list{margin:.45em 0;padding-left:1.35em}
.compact-list>li{margin:.42em 0}
.sub-list{margin:.35em 0 .15em;padding-left:1.35em}
.sub-list>li{margin:.28em 0}
.cell-list{margin:0;padding-left:1.2em}
.cell-list>li{margin:.22em 0}
.action-table td:nth-last-child(2){min-width:280px}
.deadline-target{display:inline-block;color:var(--warn)!important;font-weight:850!important;background:var(--warnb);border:1px solid #e2c784;border-radius:3px;padding:0 .25em;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.deadline-critical{display:inline-block;color:var(--err)!important;font-weight:850!important;background:var(--errb);border:1px solid #dfa39f;border-radius:3px;padding:0 .25em;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.process-note-muted{margin:10px 0 14px;padding:10px 13px;border:1px solid var(--rule2);border-left:4px solid #9aa1aa;border-radius:5px;background:#f1f2f3;color:#535c67;font-size:13.5px}
.flow-diagram{display:grid;align-items:stretch;gap:8px;margin:13px 0;padding:14px;border:1px solid var(--rule2);border-radius:8px;background:linear-gradient(145deg,#f5f7f8,#eef2f4)}
.flow-three{grid-template-columns:minmax(145px,1fr) auto minmax(145px,1fr) auto minmax(145px,1fr)}
.flow-four{grid-template-columns:minmax(125px,1fr) auto minmax(125px,1fr) auto minmax(125px,1fr) auto minmax(125px,1fr)}
.flow-node{display:flex;flex-direction:column;justify-content:center;min-height:72px;padding:10px 12px;border:1px solid #bac6cf;border-top:4px solid var(--acc);border-radius:6px;background:#fff;text-align:center}
.flow-node strong{color:var(--navy);font:750 13.5px var(--cond)}.flow-node span{margin-top:4px;color:var(--mut);font-size:11.5px;line-height:1.35}
.flow-node-hub{border-top-color:var(--run);background:var(--runb)}.flow-node-hub strong{color:var(--run)}
.flow-arrow{align-self:center;color:var(--acc);font:900 22px var(--mono)}
.flow-label{margin:12px 0 5px;color:var(--navy);font-size:13px}
.flow-label strong{font-family:var(--cond);letter-spacing:.015em}
.file-list{margin:.55em 0 1.15em;padding-left:1.45em}
.file-list>li{margin:.8em 0;padding-left:.15em}
.file-list>li>strong:first-child{color:var(--navy);font-family:var(--cond)}
.file-list .flow-diagram{margin:7px 0 10px}
.input-stage{margin:18px 0 28px;padding:18px 20px;border:1px solid var(--rule2);border-top:5px solid var(--navy);border-radius:8px;background:#fff;box-shadow:0 3px 12px rgba(26,34,48,.06)}
.input-stage>h3:first-child{margin-top:0;padding-bottom:7px;border-bottom:1px solid var(--rule2)}
.input-stage .box{margin:12px 0;padding:11px 14px;border-radius:6px;background:#f3f5f6;border-left:5px solid #9aa5ae}
.input-stage .box-warn{background:var(--warnb);border-left-color:#d18c00}.input-stage .box-info{background:var(--accbg);border-left-color:var(--acc)}
.mode-legend{padding:10px 12px;border:1px solid var(--rule2);border-radius:6px;background:#f5f6f7;color:var(--mut)}
.mode-badge{display:inline-block;border-radius:4px;padding:2px 7px;font:800 10.5px var(--mono);letter-spacing:.045em;white-space:nowrap;vertical-align:1px}
.mode-auto{color:var(--run);background:var(--runb);border:1px solid #b8ace0}.mode-backup{color:var(--err);background:var(--errb);border:1px solid #dda6a2}.mode-process{color:var(--idle);background:var(--idleb);border:1px solid #c9c4b8}
.mandatory-note{display:inline-block;color:#761912;background:var(--errb);border:1px solid #dda6a2;border-radius:4px;padding:3px 7px;font-weight:850}
.file-timings td:nth-child(n+4){white-space:nowrap}.file-timings th:nth-child(n+4),.file-timings td:nth-child(n+4){text-align:center}
.deadline-rule{margin:16px 0;padding:0 16px 14px;border:1px solid #d8a44f;border-left:7px solid #d18c00;border-radius:7px;background:linear-gradient(105deg,var(--warnb),#fff 72%);box-shadow:0 2px 8px rgba(154,91,0,.08)}
.deadline-rule h4{margin:0 -16px 12px;padding:9px 14px;color:var(--ink);background:rgba(255,210,63,.32);border-bottom:1px solid #e2c784}
.deadline-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.deadline-tet,.deadline-cet{display:grid;grid-template-columns:auto 1fr;gap:10px;align-items:start;padding:10px 12px;border-radius:6px;background:#fff;border:1px solid var(--rule2)}
.deadline-tet>strong,.deadline-cet>strong{font:850 14px var(--mono);padding:2px 7px;border-radius:4px}
.deadline-tet>strong{color:var(--warn);background:var(--warnb)}
.deadline-cet{border-color:#dfa39f;background:var(--errb)}
.deadline-cet>strong{color:#fff;background:var(--err)}
.deadline-cet>span{color:#761912;font-weight:650}
.scope-list{display:flex;flex-wrap:wrap;gap:5px;margin-top:6px}
.scope-yes,.scope-no{display:inline-block;border-radius:4px;padding:2px 8px;font:700 11px var(--mono)}
.scope-yes{color:var(--ok);background:var(--okb);border:1px solid #acd0b5}
.scope-no{color:var(--err);background:var(--errb);border:1px solid #e0aaa6}
.glossary td:first-child{width:38%;white-space:normal}
.glossary td:first-child em{color:var(--mut)}
.file-summary td:first-child{width:62px;text-align:center;font:700 12px var(--mono)}
.term-name{font-weight:700;color:var(--ink)}
.definition{margin:6px 0}.definition::before{content:"Definicja · ";font:700 10.5px var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--mut)}
.tag{display:inline-block;font:600 11px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;
background:var(--ink);color:var(--yellow);border-radius:3px;padding:5px 10px;margin-right:10px;vertical-align:3px}
/* ── powiązania i nagłówek rozdziału ── */
.mini{display:inline-block;font:650 11.5px var(--sans);background:#fff;
color:var(--navy);text-decoration:none;border:1px solid var(--rule2);border-radius:3px;padding:4px 9px;margin:0 6px 6px 0}
.mini:hover{background:var(--accbg);border-color:var(--acc)}
.procedure-section{position:relative;margin:44px 0 72px;padding:0 0 24px;border-bottom:1px solid var(--rule)}
.procedure-section>.section-header{margin:0 0 15px;padding:19px 22px 17px;border:1px solid var(--rule2);border-left:6px solid var(--navy);background:#f6f8fa}
.section-kicker{display:flex;align-items:center;gap:10px;margin-bottom:8px}
.section-number{display:inline-grid;place-items:center;min-width:35px;height:27px;padding:0 7px;background:var(--navy);color:#fff;border-radius:2px;font:800 11px var(--mono);letter-spacing:.06em}
.section-category{font:750 10.5px var(--mono);letter-spacing:.11em;text-transform:uppercase;color:var(--mut)}
.procedure-section>.section-header h2{margin:0;padding:0;border:0;font-size:25px;text-transform:none;letter-spacing:0}
.section-summary{max-width:860px;margin:7px 0 0;color:var(--mut);font-size:14px}
.section-links{position:static;width:auto;height:auto;overflow:visible;display:flex;flex-wrap:wrap;align-items:center;gap:0;margin:0 0 20px;padding:9px 11px;background:#f9fafb;border:1px solid var(--rule);border-radius:4px;font-size:12px}
.section-links>b{margin:0 12px 6px 0;font:750 10px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--mut)}
/* ── komponenty informacji operacyjnej ── */
.procedure-facts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:9px;margin:12px 0}
.procedure-fact{padding:9px 12px;border:1px solid var(--rule);border-left:4px solid var(--idle);background:#f7f8fa;border-radius:0 4px 4px 0}
.procedure-fact strong:first-child{color:var(--ink)}
li.procedure-fact,li.pse-action,li.backup-action,li.iva-extension{list-style:none;margin:10px 0 10px -1.45em}
li.procedure-fact::marker,li.pse-action::marker,li.backup-action::marker,li.iva-extension::marker{content:""}
.pse-action{padding:11px 13px;border:1px solid #a9c4d9;border-left:6px solid var(--acc);border-radius:0 5px 5px 0;background:var(--accbg)}
.pse-action>strong:first-child{display:block;margin-bottom:3px;color:var(--navy);font:800 10.5px var(--mono);letter-spacing:.08em;text-transform:uppercase}
.backup-action{padding:11px 13px;border:1px solid #dfa9a5;border-left:6px solid var(--err);border-radius:0 5px 5px 0;background:var(--errb)}
.backup-action>strong:first-child{display:block;margin-bottom:3px;color:var(--err);font:800 10.5px var(--mono);letter-spacing:.08em;text-transform:uppercase}
.iva-extension{padding:11px 13px;border:1px solid #d7b36d;border-left:6px solid var(--warn);border-radius:0 5px 5px 0;background:var(--warnb)}
.iva-extension>strong:first-child{display:block;margin-bottom:3px;color:var(--warn);font:800 10.5px var(--mono);letter-spacing:.08em;text-transform:uppercase}
.fact-cause{border-left-color:var(--warn);background:var(--warnb)}.fact-time{border-left-color:var(--idle)}.fact-file{border-left-color:var(--acc);background:var(--accbg)}
/* ── semantyka operacyjna ── */
.signal{font-weight:800;border-radius:3px;padding:0 .22em;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.signal-danger{color:var(--err);background:var(--errb)}
.signal-warning{color:var(--warn);background:var(--warnb)}
.signal-success{color:var(--ok);background:var(--okb)}
.signal-action{color:var(--acc);background:var(--accbg)}
.semantic-key{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;margin:12px 0 22px}
.key-item{display:flex;align-items:center;gap:9px;min-height:54px;padding:9px 11px;border:1px solid var(--rule2);border-radius:7px;background:#fff;font-size:12.5px}
.key-item b{display:block;font-family:var(--cond);font-size:13px}.key-dot{width:12px;height:32px;border-radius:9px;flex:none}
.key-success .key-dot{background:var(--ok)}.key-warning .key-dot{background:#e0a000}
.key-danger .key-dot{background:var(--err)}.key-action .key-dot{background:var(--acc)}
.key-success b{color:var(--ok)}.key-warning b{color:var(--warn)}.key-danger b{color:var(--err)}.key-action b{color:var(--acc)}
/* ── badge statusów ── */
.st{display:inline-block;border-radius:4px;padding:1px 8px;font:600 12px var(--sans);white-space:nowrap}
.st-ok{background:var(--okb);color:var(--ok)}.st-warn{background:var(--warnb);color:var(--warn)}
.st-err{background:var(--errb);color:var(--err)}.st-run{background:var(--runb);color:var(--run)}
.st-idle{background:var(--idleb);color:var(--idle)}
/* ── katalog plików ── */
.fgrid{display:grid;grid-template-columns:1fr;gap:12px}
.fcard{border:1px solid var(--rule2);border-top:3px solid var(--navy);border-radius:6px;
padding:14px 16px;background:var(--panel);box-shadow:0 1px 0 var(--rule)}
.fcard h4{margin:.1em 0;color:var(--ink);font-family:var(--cond);font-size:16px}
.fcard h4 .code{font:600 11.5px var(--mono);background:var(--ink);color:#f0ead9;border-radius:3px;
padding:2px 8px;letter-spacing:.05em;vertical-align:2px}
.fcard .meta{display:flex;flex-wrap:wrap;gap:5px 18px;font:12.5px var(--mono);color:var(--mut);margin:7px 0}
.fcard .opis{margin:6px 0}.fcard .path{font-size:13px;color:var(--mut)}
.legend-card{border-top-width:4px!important}.legend-success{border-top-color:var(--ok)!important;background:linear-gradient(90deg,var(--okb),#fff 55%)}
.legend-warning{border-top-color:#d18c00!important;background:linear-gradient(90deg,var(--warnb),#fff 55%)}
.legend-danger{border-top-color:var(--err)!important;background:linear-gradient(90deg,var(--errb),#fff 55%)}
.legend-neutral{border-top-color:var(--idle)!important}
/* ── tabele: jeden styl w całym dokumencie ── */
main table{width:100%;border-collapse:collapse;font-size:13px;margin:8px 0}
main table th,main table td{border:1px solid var(--rule2);padding:6px 9px;text-align:left;vertical-align:top}
main table th{background:var(--ink);color:#efe9da;font:600 11px var(--mono);letter-spacing:.1em;text-transform:uppercase;border-color:var(--ink)}
main table tbody tr:nth-child(even) td{background:rgba(15,62,99,.035)}
main table caption{display:none}
.sttab,.ref table,table.ref{width:100%;border-collapse:collapse;font-size:13px;margin:8px 0}
.sttab th,.sttab td,.ref th,.ref td,table.ref th,table.ref td{border:1px solid var(--rule2);padding:6px 9px;text-align:left;vertical-align:top}
.sttab th,.ref th,table.ref th{background:var(--ink);color:#efe9da;font:600 11px var(--mono);letter-spacing:.1em;text-transform:uppercase;border-color:var(--ink)}
.sttab tbody tr:nth-child(even) td,.ref tbody tr:nth-child(even) td{background:rgba(15,62,99,.035)}
.state-row td{transition:background .15s ease}.state-row td:first-child{border-left-width:5px}
.state-danger td{background:rgba(179,38,30,.045)!important}.state-danger td:first-child{border-left-color:var(--err)}
.state-warning td{background:rgba(224,160,0,.065)!important}.state-warning td:first-child{border-left-color:#d18c00}
.state-success td{background:rgba(26,127,55,.045)!important}.state-success td:first-child{border-left-color:var(--ok)}
.state-running td{background:rgba(91,63,168,.045)!important}.state-running td:first-child{border-left-color:var(--run)}
.state-neutral td:first-child{border-left-color:var(--idle)}
.state-label{display:block;width:max-content;margin:0 0 7px;padding:2px 7px;border-radius:3px;font:800 11px var(--mono);letter-spacing:.07em}
.label-danger{color:var(--err);background:var(--errb)}.label-warning{color:var(--warn);background:var(--warnb)}
.label-success{color:var(--ok);background:var(--okb)}.label-running{color:var(--run);background:var(--runb)}
.label-neutral{color:var(--idle);background:var(--idleb)}
.stcol{white-space:normal}
.tcell{display:inline-flex;flex-direction:column;align-items:center;gap:3px;margin:2px 10px 2px 0;vertical-align:top}
.tcell .tile{width:30px;height:30px;border:1px solid var(--rule2);border-radius:6px;display:block;background:#fff}
.tcell .tlab{font:10.5px var(--mono);color:var(--mut);max-width:84px;text-align:center;line-height:1.2}
details{margin:8px 0}
summary{cursor:pointer;font:600 13.5px var(--sans);color:var(--acc);padding:7px 10px;
background:var(--accbg);border:1px solid var(--rule);border-radius:5px;list-style:none}
summary::before{content:"▸ ";font-family:var(--mono);color:var(--navy)}
details[open]>summary::before{content:"▾ "}
details[open]>summary{border-radius:5px 5px 0 0}
details.states>summary{font-size:12.5px;display:inline-block;padding:3px 10px}
/* ── zrzuty ekranu: naturalny rozmiar, pełne proporcje, bez kadrowania ── */
.grid{display:flex;flex-direction:column;align-items:stretch;gap:22px;margin:16px 0 6px}
figure.shot{width:min(100%,calc(var(--screen-width,100%) + 18px));max-width:100%;align-self:center;margin:0 auto;
border:1px solid var(--rule2);border-top:4px solid var(--acc);border-radius:7px;background:#fff;padding:8px 8px 0;
box-shadow:0 2px 0 var(--rule),0 7px 18px rgba(26,34,48,.09);transition:transform .18s ease,box-shadow .18s ease}
figure.shot:hover{transform:translateY(-3px);box-shadow:0 3px 0 var(--rule),0 12px 26px rgba(26,34,48,.15)}
figure.shot img{display:block;width:auto;height:auto;max-width:100%;max-height:none;margin:0 auto;background:#fafbfc;
border:1px solid var(--rule);object-fit:initial;cursor:zoom-in}
figure.shot img:focus-visible{outline:4px solid var(--yellow);outline-offset:3px;border-color:var(--navy)}
figure.shot figcaption{display:grid;grid-template-columns:auto 1fr auto;align-items:start;gap:8px 12px;padding:9px 5px 11px;color:#4e5968}
.caption-label{display:inline-block;padding:2px 7px;border-radius:3px;background:var(--accbg);color:var(--acc);
font:800 10px var(--mono);letter-spacing:.07em;text-transform:uppercase;white-space:nowrap}
.caption-text{font:650 12.5px/1.45 var(--sans);text-align:left}.caption-size{font:500 10.5px/1.4 var(--mono);color:var(--mut);white-space:nowrap}
/* ── kroki C.x ── */
.step{border:1px solid var(--ink);background:var(--panel);border-radius:0 6px 6px 0;
border-left:6px solid var(--navy);padding:11px 15px;margin:14px 0;box-shadow:3px 3px 0 rgba(15,62,99,.12)}
.step .n{font:700 12px var(--mono);background:var(--ink);color:var(--yellow);border-radius:3px;padding:2px 8px;margin-right:6px}
.feat{max-width:560px;margin:10px 0}
details.gal{border:1px solid var(--rule);border-radius:7px;background:rgba(255,255,255,.55);padding:0 10px 10px}
details.gal>summary{margin:0 -10px 6px;padding:9px 12px;font-family:var(--cond);font-size:14px}
details.gal[open]>summary{color:var(--navy);background:#e4eff7;border-color:#bed1df}
/* ── callout: czytelny poziom ważności ── */
.callout{position:relative;background:var(--warnb);border:1px solid #e0b55c;border-radius:0 6px 6px 0;
padding:11px 15px 11px 26px;margin:14px 0;font-size:14px;overflow:hidden}
.callout::before{content:"";position:absolute;left:0;top:0;bottom:0;width:11px;
background:repeating-linear-gradient(-45deg,var(--yellow) 0 9px,var(--ink) 9px 18px)}
.callout-danger{color:#761912;background:var(--errb);border-color:#d88984;font-weight:650}
.callout-danger::before{background:repeating-linear-gradient(-45deg,var(--err) 0 9px,#64120d 9px 18px)}
.callout-success{color:#125f2a;background:var(--okb);border-color:#8fc59d}
.callout-success::before{background:var(--ok)}
.note{font-size:13px;color:var(--mut)}
/* ── referencje md ── */
.ref h1{font:700 20px var(--cond);text-transform:uppercase;color:var(--ink);border-bottom:2px solid var(--ink);padding-bottom:5px}
.ref h2{font:650 17px var(--cond);text-transform:none;letter-spacing:0;border-bottom:1px solid var(--rule2)}
.ref h3{font-size:15px;margin-top:1.2em}
.proc h3{font-size:18px;border-bottom:1px solid var(--rule2);padding-bottom:5px;margin-top:1.9em}
.proc h4{font-size:15px;color:var(--acc);margin:1.15em 0 .3em}
.proc h5{font-size:13.5px;margin:.85em 0 .2em}
.proc table{display:block;overflow-x:auto;white-space:normal}
/* ── maile ── */
.mailtpl{border:1px solid var(--rule2);border-top:4px solid var(--navy);border-radius:6px;
padding:13px 16px;margin:16px 0;background:var(--panel)}
.mailtpl h4{margin:.1em 0 .4em;font-family:var(--cond);font-size:16px;color:var(--ink)}
.mailtpl .when{font-size:13px;color:var(--mut);margin:.2em 0 .6em}
.mailtpl table{margin:6px 0}
.mailbody{background:#fbf9f2;border:1px solid var(--rule);border-left:3px solid var(--rule2);
border-radius:4px;padding:12px 16px;font:13.5px/1.6 var(--serif);margin-top:8px}
.psemark{display:inline-block;background:var(--errb);color:var(--err);font:700 11px var(--mono);
border-radius:3px;padding:2px 8px;margin-left:8px;vertical-align:middle}
/* ── diagram architektury ── */
.architecture-flow{margin:14px 0;padding:16px;border:1px solid var(--rule2);border-radius:9px;background:linear-gradient(160deg,#f7fafc,#edf4f8);box-shadow:0 3px 12px rgba(15,62,99,.08)}
.architecture-layer{padding:12px;border:1px solid var(--rule2);border-radius:7px;background:#fff}
.architecture-layer h4{margin:0 0 10px;color:var(--ink);text-align:center;font:750 13px var(--cond);letter-spacing:.08em;text-transform:uppercase}
.architecture-tools{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:9px}
.architecture-tool{min-height:74px;padding:10px;border:1px solid #b8ccdc;border-top:4px solid var(--acc);border-radius:6px;background:var(--accbg);text-align:center}
.architecture-tool strong{display:block;color:var(--navy);font:750 14px var(--cond)}
.architecture-tool span{display:block;margin-top:4px;color:var(--mut);font-size:11.5px;line-height:1.35}
.architecture-external .architecture-tools{grid-template-columns:repeat(2,minmax(0,1fr));max-width:720px;margin:0 auto}
.architecture-external .architecture-tool{border-top-color:var(--run);background:var(--runb)}
.architecture-external .architecture-tool strong{color:var(--run)}
.connector-hub{max-width:620px;margin:0 auto;padding:12px 18px;border:2px solid var(--navy);border-radius:7px;background:var(--navy);color:#fff;text-align:center;box-shadow:0 4px 0 rgba(15,62,99,.16)}
.connector-hub strong{display:block;font:800 17px var(--cond)}
.connector-hub span{display:block;color:#cfe3f4;font-size:12px}
.architecture-arrows{display:grid;grid-template-columns:repeat(4,1fr);max-width:900px;margin:2px auto;text-align:center;color:var(--acc);font:900 24px/1 var(--mono)}
.architecture-arrows-external{grid-template-columns:repeat(2,1fr);max-width:560px;color:var(--run)}
.architecture-note{margin:12px 0 0;padding:9px 12px;border-left:4px solid var(--acc);background:#fff;color:var(--navy);font-weight:650}
/* ── nagłówek i narzędzia dokumentu ── */
.hero{position:relative;margin:0 0 24px;padding:26px 30px 24px;color:#fff;background:var(--navy);
border-top:7px solid var(--err);border-radius:0 0 6px 6px;box-shadow:0 7px 22px rgba(20,36,58,.18)}
.hero .eyebrow{font:750 10.5px var(--mono);letter-spacing:.16em;text-transform:uppercase;color:#b9d0e2}
.hero h1{color:#fff;font-size:34px;margin:.45em 0 .15em;max-width:850px;text-transform:none}
.hero .subtitle{max-width:760px;color:#dcebf3;font-size:16px;margin:0}
.hero-meta{display:flex;flex-wrap:wrap;gap:8px 18px;margin-top:18px;padding-top:13px;
border-top:1px solid rgba(255,255,255,.24);font:650 10.5px var(--mono);letter-spacing:.055em;color:#f4f6f8}
.quickgrid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin:18px 0 24px}
.quickcard{display:flex;flex-direction:column;min-height:118px;padding:15px 16px;border:1px solid var(--rule2);
border-top:4px solid var(--navy);border-radius:8px;background:#fff;color:var(--fg);text-decoration:none;
box-shadow:0 3px 10px rgba(26,34,48,.06);transition:transform .16s ease,box-shadow .16s ease}
.quickcard:hover{transform:translateY(-3px);box-shadow:0 8px 20px rgba(26,34,48,.12)}
.quickcard .qicon{font-size:24px}.quickcard b{font-family:var(--cond);color:var(--ink);margin:6px 0 3px}
.quickcard small{color:var(--mut);line-height:1.35}
.quickcard.success{border-top-color:var(--ok)}.quickcard.success .qicon,.quickcard.success b{color:var(--ok)}
.quickcard.warning{border-top-color:#d18c00}.quickcard.warning .qicon,.quickcard.warning b{color:var(--warn)}
.quickcard.emergency{border-top-color:var(--err)}.quickcard.emergency .qicon,.quickcard.emergency b{color:var(--err)}
.quickcard.action{border-top-color:var(--acc)}.quickcard.action .qicon,.quickcard.action b{color:var(--acc)}
.doc-tools{position:sticky;top:10px;z-index:20;display:flex;flex-wrap:wrap;align-items:center;gap:7px;
margin:0 0 18px;padding:8px 10px;background:rgba(255,253,247,.94);backdrop-filter:blur(8px);
border:1px solid var(--rule2);border-radius:8px;box-shadow:0 4px 16px rgba(26,34,48,.09)}
.doc-tools .tool-label{margin-right:auto;font:700 10px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--mut)}
.doc-tools button{appearance:none;border:1px solid var(--rule2);border-radius:5px;background:#fff;color:var(--navy);
padding:6px 10px;font:600 11.5px var(--sans);cursor:pointer}.doc-tools button:hover{background:var(--accbg);border-color:var(--acc)}
.offline-badge{display:inline-flex;align-items:center;gap:6px;padding:4px 8px;background:var(--tealbg);color:var(--teal);
border-radius:999px;font:700 10.5px var(--mono)}
/* ── powiększanie zrzutów ekranu ── */
.screen-dialog{width:min(96vw,1500px);max-width:none;height:min(94vh,1000px);border:0;border-radius:10px;padding:48px 18px 16px;background:#101722;color:#fff;box-shadow:0 25px 80px rgba(0,0,0,.55)}
.screen-dialog::backdrop{background:rgba(5,12,20,.82);backdrop-filter:blur(4px)}
.screen-dialog img{width:100%;height:calc(100% - 48px);object-fit:contain;display:block}
.screen-dialog p{margin:8px 48px 0 4px;color:#dbe7f1;font:600 13px var(--sans)}
.screen-dialog button{position:absolute;right:14px;top:10px;width:34px;height:34px;border:1px solid #617083;border-radius:50%;background:#1d2a3b;color:#fff;font-size:22px;cursor:pointer}
/* ── druk ── */
@page{size:A4;margin:12mm}
@media print{
 body{background:#fff}
 nav,.doc-tools,.screen-dialog{display:none!important}.wrap{display:block}main{max-width:none;padding:0;border:none;box-shadow:none;background:#fff}
 .hero{box-shadow:none;print-color-adjust:exact}.quickgrid{grid-template-columns:repeat(2,1fr)}
 figure.shot:hover{transform:none}
 .signal,.state-row,.state-label,.semantic-key,.legend-card,.risk-h,.callout,.quickcard,.pse-action,.backup-action,.iva-extension,.procedure-fact,.section-number,.procedure-section>.section-header{-webkit-print-color-adjust:exact;print-color-adjust:exact}
 details{display:block}details>summary{display:none}
 .grid{display:flex;flex-direction:column}
 figure.shot{width:min(100%,calc(var(--screen-width,100%) + 18px));break-inside:avoid;page-break-inside:avoid}
 figure.shot img{width:auto;height:auto;max-width:100%;max-height:225mm;margin:0 auto;object-fit:contain}
 .fcard,.mailtpl,.step,.stick,.quickcard{break-inside:avoid}
}
@media(max-width:1100px){.quickgrid,.semantic-key{grid-template-columns:repeat(2,minmax(0,1fr))}.architecture-tools{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:900px){nav:not(.section-links){display:none}main{max-width:none;padding:18px;border:none}.doc-tools{top:4px}.procedure-section>.section-header{padding:16px 17px}}
@media(max-width:560px){.quickgrid,.semantic-key,.deadline-grid,.procedure-facts,.architecture-tools,.architecture-external .architecture-tools{grid-template-columns:1fr}.architecture-arrows{grid-template-columns:1fr}.architecture-arrows span:not(:first-child){display:none}.flow-three,.flow-four{grid-template-columns:1fr}.flow-arrow{transform:rotate(90deg)}.hero{padding:22px 20px}.hero h1{font-size:28px}.procedure-section>.section-header h2{font-size:22px}.section-kicker{align-items:flex-start;flex-direction:column;gap:5px}.caption-size{grid-column:2;white-space:normal}.caption-text{grid-column:2}.caption-label{grid-row:1 / span 2}}
"""

FINAL_CSS = r"""
/* ── wydanie finalne: system „Mierzony Przepływ” ── */
body.edition-final{
 --paper:#efede5;--panel:#fffefa;--ink:#132a43;--fg:#24364a;--mut:#677684;
 --rule:#d6d8d4;--rule2:#b9c0c4;--navy:#173f63;--acc:#1e668f;--accbg:#e8f0f4;
 --warn:#9a6208;--warnb:#f8eedb;--err:#b72e2a;--errb:#f8e9e6;
 --ok:#28704d;--okb:#e7f1ea;--run:#62549a;--runb:#eeebf6;
 --sans:'Noto Sans','Segoe UI',Arial,sans-serif;
 --cond:'Noto Sans','Segoe UI Semibold',Arial,sans-serif;
 --serif:'Noto Sans','Segoe UI',Arial,sans-serif;
 --mono:'Noto Sans Mono','Cascadia Mono',Consolas,monospace;
 background:#e8e8e3;font-size:15.25px;line-height:1.62;
}
.edition-final .wrap{max-width:1720px;background:var(--panel)}
.edition-final nav:not(.section-links){width:318px;background:#10283e;padding:27px 16px 46px;border-right:1px solid #28455e}
.edition-final nav:not(.section-links)>h2{margin:0 7px 22px;padding-bottom:15px;color:#aebdca;letter-spacing:.16em}
.edition-final .nav-group{margin-bottom:22px}
.edition-final .nav-group-heading{gap:10px;margin:0 7px 7px;padding-bottom:7px;font-size:11.5px}
.edition-final .nav-group-heading span{width:25px;height:25px;border-radius:0;background:transparent;color:#f6f4ec;border:1px solid #879aaa}
.edition-final nav:not(.section-links) a{grid-template-columns:31px 1fr;padding:7px 9px;border-left-width:2px;border-radius:0;color:#dce3e7}
.edition-final nav:not(.section-links) a>span{color:#8ca6b9}
.edition-final .nav-start{margin-bottom:23px;background:transparent;border-top:1px solid rgba(255,255,255,.14);border-bottom:1px solid rgba(255,255,255,.14)}
.edition-final main{max-width:1340px;padding:38px 58px 82px;border:0;box-shadow:18px 0 50px rgba(19,42,67,.08)}
.edition-final h1,.edition-final h2,.edition-final h3,.edition-final h4{font-family:var(--cond)}
.edition-final h3{margin-top:2em;font-size:18px}.edition-final h4{margin-top:1.35em}
.edition-final .hero{display:grid;grid-template-columns:minmax(0,1fr) 315px;gap:32px;min-height:330px;margin:0 0 25px;padding:31px 34px;color:var(--ink);background:var(--paper);border:1px solid var(--ink);border-top:8px solid var(--err);border-radius:0;box-shadow:none;overflow:hidden}
.edition-final .hero-copy{position:relative;z-index:2;align-self:end}
.edition-final .hero .eyebrow{color:var(--mut);font-size:10px;letter-spacing:.18em}
.edition-final .hero h1{max-width:690px;margin:.55em 0 .22em;color:var(--ink);font-size:42px;line-height:1.08;letter-spacing:-.025em}
.edition-final .hero .subtitle{max-width:700px;color:#40566a;font-size:15.5px;line-height:1.58}
.edition-final .hero-meta{gap:7px 19px;margin-top:24px;padding-top:14px;border-top:1px solid var(--ink);color:var(--navy);font-size:10px}
.edition-final .hero-visual{position:relative;min-height:260px;border-left:1px solid var(--rule2);background:repeating-linear-gradient(0deg,transparent 0 27px,rgba(19,42,67,.11) 27px 28px)}
.edition-final .hero-visual::before,.edition-final .hero-visual::after{content:"";position:absolute;border-radius:50%;border:2px solid var(--navy);right:-58px;bottom:-92px}
.edition-final .hero-visual::before{width:294px;height:294px}.edition-final .hero-visual::after{width:196px;height:196px;right:-9px;bottom:-43px;border-color:var(--err);border-width:5px}
.edition-final .hero-rails{display:grid;grid-template-columns:repeat(5,1fr);height:100%}
.edition-final .hero-rails span{position:relative;border-right:1px solid rgba(19,42,67,.18)}
.edition-final .hero-rails span::before{content:attr(data-label);position:absolute;top:7px;left:9px;font:700 11px var(--mono);color:var(--mut)}
.edition-final .hero-rails span:nth-child(4)::after{content:"40 / 25";position:absolute;right:8px;bottom:9px;font:700 13px var(--mono);color:var(--err)}
.edition-final .callout{border-radius:0}.edition-final .callout::before{width:8px;background:var(--warn)}
.edition-final .callout-danger::before{background:var(--err)}
.edition-final .doc-tools{top:8px;margin-bottom:24px;padding:8px 12px;background:rgba(255,254,250,.96);border-radius:0;box-shadow:0 7px 22px rgba(19,42,67,.08)}
.edition-final .doc-tools button{border-radius:0;padding:6px 11px}.edition-final .offline-badge{border-radius:2px}
.edition-final .quickgrid{gap:0;margin:23px 0 28px;border:1px solid var(--rule2)}
.edition-final .quickcard{min-height:112px;padding:15px 17px;border:0;border-right:1px solid var(--rule2);border-top:5px solid var(--navy);border-radius:0;box-shadow:none}
.edition-final .quickcard:last-child{border-right:0}.edition-final .quickcard:hover{transform:none;background:#f7f8f5;box-shadow:inset 0 -4px 0 var(--acc)}
.edition-final .quickcard .qicon{font:700 20px var(--mono)}.edition-final .quickcard b{margin:9px 0 3px;font-size:14px}
.edition-final .semantic-key{gap:0;margin:0 0 35px;border:1px solid var(--rule2)}
.edition-final .key-item{min-height:58px;border:0;border-right:1px solid var(--rule2);border-radius:0;background:#fbfbf7}
.edition-final .key-item:last-child{border-right:0}.edition-final .key-dot{width:5px;height:34px;border-radius:0}
.edition-final .procedure-section{--group-color:var(--navy);margin:66px 0 92px;padding-bottom:38px;border-bottom:1px solid var(--ink)}
.edition-final .procedure-section[data-group="A"]{--group-color:#6f7e89}.edition-final .procedure-section[data-group="B"]{--group-color:var(--acc)}
.edition-final .procedure-section[data-group="C"]{--group-color:var(--navy)}.edition-final .procedure-section[data-group="D"]{--group-color:var(--warn)}
.edition-final .procedure-section[data-group="E"]{--group-color:var(--err)}
.edition-final .procedure-section>.section-header{display:grid;grid-template-columns:82px 1fr;margin:0 0 19px;padding:22px 0 19px;border:0;border-top:2px solid var(--ink);border-bottom:1px solid var(--rule2);border-radius:0;background:transparent}
.edition-final .section-kicker{grid-row:1 / span 2;display:block;margin:0;padding-right:17px;border-right:5px solid var(--group-color)}
.edition-final .section-number{display:block;min-width:0;height:auto;padding:0;background:transparent;color:var(--ink);font:500 42px/1 var(--cond);letter-spacing:-.04em;text-align:left}
.edition-final .section-category{display:block;margin-top:12px;color:var(--group-color);font-size:9px;line-height:1.35;letter-spacing:.1em}
.edition-final .procedure-section>.section-header h2{align-self:end;margin:0;padding:0 0 4px 22px;font-size:27px;line-height:1.18;letter-spacing:-.012em}
.edition-final .section-summary{align-self:start;margin:0;padding-left:22px;max-width:900px;font-size:13.5px;line-height:1.5}
.edition-final .section-links{margin:0 0 25px;padding:9px 12px;border-radius:0;background:#f6f6f2}
.edition-final .mini{border-radius:0;background:transparent;border-color:var(--rule2)}
.edition-final .procedure-fact,.edition-final .pse-action,.edition-final .backup-action,.edition-final .iva-extension{border-radius:0;box-shadow:none}
.edition-final .pse-action{border-color:#9fb8c8;border-left-color:var(--acc)}.edition-final .backup-action{border-color:#d8aaa6;border-left-color:var(--err)}
.edition-final .input-stage,.edition-final .fcard,.edition-final .mailtpl,.edition-final .step,.edition-final details.gal{border-radius:0;box-shadow:none}
.edition-final .input-stage{border-top-width:4px}.edition-final .step{border-left-width:5px;box-shadow:none}
.edition-final main table{margin:12px 0 20px;font-size:12.8px}.edition-final main table th,.edition-final main table td{padding:7px 9px}
.edition-final main table th{background:var(--ink);color:#fffefa;font:650 10.5px var(--sans);letter-spacing:.045em;text-transform:none}
.edition-final main table tbody tr:nth-child(even) td{background:#f4f5f2}
.edition-final figure.shot{border-radius:0;border-top-width:3px;box-shadow:0 8px 24px rgba(19,42,67,.1)}
.edition-final figure.shot:hover{transform:none;box-shadow:0 11px 30px rgba(19,42,67,.15)}
.edition-final .caption-label{border-radius:0}.edition-final summary{border-radius:0}
.edition-final .architecture-flow,.edition-final .architecture-layer,.edition-final .architecture-tool,.edition-final .connector-hub,.edition-final .flow-diagram,.edition-final .flow-node{border-radius:0;box-shadow:none}
.edition-final .stick{transform:none!important;border-radius:0;background:#fffefa;outline-color:var(--rule2);box-shadow:none}
.edition-final footer{font-size:12px!important;line-height:1.55}
@media(max-width:900px){.edition-final main{padding:18px}.edition-final .hero{grid-template-columns:1fr}.edition-final .hero-visual{min-height:160px;border-left:0;border-top:1px solid var(--rule2)}.edition-final .quickgrid{grid-template-columns:repeat(2,1fr)}.edition-final .semantic-key{grid-template-columns:repeat(2,1fr)}.edition-final .procedure-section>.section-header{grid-template-columns:68px 1fr}}
@media(max-width:560px){.edition-final .hero h1{font-size:32px}.edition-final .quickgrid,.edition-final .semantic-key{grid-template-columns:1fr}.edition-final .quickcard,.edition-final .key-item{border-right:0;border-bottom:1px solid var(--rule2)}.edition-final .procedure-section>.section-header{grid-template-columns:1fr}.edition-final .section-kicker{grid-row:auto;display:flex;align-items:center;gap:10px;padding:0 0 10px;border-right:0;border-bottom:4px solid var(--group-color)}.edition-final .section-number{font-size:30px}.edition-final .section-category{margin:0}.edition-final .procedure-section>.section-header h2,.edition-final .section-summary{padding-left:0}.edition-final .procedure-section>.section-header h2{padding-top:13px}}
@media print{
 body.edition-final{font-size:10.4pt;background:#fff}.edition-final main{padding:0}.edition-final .hero{grid-template-columns:minmax(0,1fr) 58mm;height:249mm;min-height:249mm;margin:0;padding:15mm 11mm;border:1px solid var(--ink);border-top:5px solid var(--err);box-sizing:border-box;break-after:page}.edition-final .hero-copy{align-self:center}.edition-final .hero-visual{display:block;min-height:0}.edition-final .hero h1{font-size:26pt}.edition-final .quickgrid,.edition-final .semantic-key,.edition-final .doc-tools{display:none!important}
 .edition-final .procedure-section{margin:0 0 14mm;padding:0 0 8mm;break-before:page}.edition-final .procedure-section:first-of-type{break-before:auto}.edition-final .procedure-section>.section-header{margin-bottom:5mm;padding:4mm 0;break-after:avoid}.edition-final h2,.edition-final h3,.edition-final h4,.edition-final h5{break-after:avoid;page-break-after:avoid}.edition-final p,.edition-final li{orphans:3;widows:3}.edition-final tr,.edition-final figure,.edition-final .pse-action,.edition-final .backup-action,.edition-final .iva-extension{break-inside:avoid;page-break-inside:avoid}.edition-final main table{font-size:8.2pt}.edition-final main table th,.edition-final main table td{padding:1.6mm 2mm}.edition-final .procedure-section:last-of-type{margin-bottom:0;padding-bottom:0}.edition-final footer{margin-top:4mm;break-inside:avoid}
}
"""

def legend_section():
    tiles = [
     ('zielony.png','Sukces (SUCCESS)','Plik wysłany i potwierdzony ACK — przebieg nominalny.'),
     ('zielony_R.png','Sukces ręczny (FORCEDSUCCESS, „R")','Dyspozytor ustawił status ręcznie po weryfikacji w systemie centralnym.'),
     ('ciemnozielony_W.png','Wysłany ręcznie (SENTMANUALLY, „W")','Wysyłka ręczna z poziomu CCM.'),
     ('W_po_CET.png','Wysłany ręcznie po CET (W↑)','Wysyłka ręczna po Critical End Time.'),
     ('fioletowy.png','Dostarczone / łączenie po CET (CONN_AFTER_CET)','Dostarczenie po CET — akceptowalne.'),
     ('pomarańczowy.png','Ostrzeżenie (WARNING)','Zbliża się Target End Time.'),
     ('czerwony.png','Błąd / awaria (FAILURE)','Brak wysyłki lub negatywny ACK.'),
     ('czerwony_q.png','Brak ACK (ACKNOTRECEIVED, „?")','Wysłano, brak potwierdzenia odbioru.'),
     ('czerwony_excl.png','Zły rozmiar pliku (FILESIZEBAD, „!")','Rozmiar poniżej progu technologicznego.'),
     ('czarny.png','Przekroczono CET (EXCEEDED)','Minął Critical End Time — wymagana interwencja.'),
     ('szary_q.png','Przetwarzanie (PROCESSRUNNING, „?")','Proces w toku.'),
     ('szary.png','Brak / nieznany (UNKNOWN)','Kolumna nieaktywna / brak danych.'),
     ('puste.png','Puste','Brak pozycji.'),
    ]
    cells = ''
    danger_tiles = {'czerwony.png','czerwony_q.png','czerwony_excl.png','czarny.png'}
    warning_tiles = {'W_po_CET.png','fioletowy.png','pomarańczowy.png'}
    success_tiles = {'zielony.png','zielony_R.png','ciemnozielony_W.png'}
    for fn,lab,desc in tiles:
        p = f'img_ccm/tiles/{fn}'
        tone = 'danger' if fn in danger_tiles else 'warning' if fn in warning_tiles else 'success' if fn in success_tiles else 'neutral'
        cells += (f'<div class="fcard legend-card legend-{tone}" style="display:flex;gap:12px;align-items:center">'
                  f'<img src="{asset_uri(p)}" alt="{esc(lab)}" data-source="{esc(p)}" style="width:42px;height:42px;flex:none;border:1px solid var(--rule);border-radius:6px">'
                  f'<div><b>{esc(lab)}</b><br><small style="color:var(--mut)">{esc(desc)}</small></div></div>')
    grid = f'<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:10px">{cells}</div>'
    legendshot = featured('screens/ccm/ccm-017.png')
    return grid + (f'<h3>Pełna legenda na pulpicie</h3>{legendshot}' if legendshot else '')

def ccm_section():
    s = []
    s.append('<p class="lead">Pulpit dyspozytorski CCM (<code>ccm.spsm.pse.pl</code>) — główne miejsce '
             'monitorowania statusów wszystkich plików IDCC i ręcznej interwencji.</p>')
    s.append(featured('screens/ccm/ccm-004.png'))
    steps = [
     ('C.1','Otwarcie właściwego pulpitu i wybór doby',
      'Zaloguj się do CCM. Wybierz pulpit „IDCC FB Pulpit dyspozytorski” lub „IDCC (do 3C) z ATC i SFTP”. '
      'Z kalendarza ustaw dobę monitorowaną. Ustaw tryb odświeżania (ultraszybki 10 s / szybki 30 s / wolny 5 min).',
      ['screens/ccm/ccm-001.png','screens/ccm/ccm-011.png','screens/ccm/ccm-012.png']),
     ('C.2','Identyfikacja wiersza, kolumny i kafelka',
      'Odszukaj wiersz pliku (FIDx-…) i kolumnę kanału (CCTool wysł. / CCTool zwalid. / MinIO / sFTP/ZP). '
      'Kolor i znacznik kafelka = aktualny status (patrz <a href="#sec-legenda">legenda</a>).',
      ['screens/ccm/ccm-015.png']),
     ('C.3','Wyświetlenie informacji o pliku',
      'PPM na kafelku → „Informacje”. Popup pokazuje opis pliku, ścieżkę, TET/CET, kod ACK i ewentualny błąd walidacji.',
      ['screens/ccm/ccm-057.png','screens/ccm/ccm-093.png']),
     ('C.4','Wysłanie pliku przed Critical End Time',
      'PPM na kafelku → „Wyślij” (lub „Wyślij do CCTool”). Wskaż plik, potwierdź. Obserwuj postęp do komunikatu „Plik wysłany”.',
      ['screens/ccm/ccm-110.png','screens/ccm/ccm-113.png','screens/ccm/ccm-116.png']),
     ('C.5','Wysłanie pliku po Critical End Time / status ręczny',
      'Po CET użyj „Wyślij po CET”. Status ręczny: PPM → „Status ręczny” → wybór (Nowa wersja / Tylko zmiana statusu); '
      'cofnięcie przez „Przywróć poprzedni status”.',
      ['screens/ccm/ccm-058.png','screens/ccm/ccm-061.png','screens/ccm/ccm-064.png']),
    ]
    for n,t,d,shots in steps:
        feats = ''.join(featured(x) for x in shots if x in BYFILE)
        sid = 'ccm-' + n.replace('.','').lower()
        s.append(f'<div class="step" id="{sid}"><span class="n">{n}.</span> <b>{esc(t)}</b><br>{esc(d)}</div>'
                 f'<div class="grid">{feats}</div>')
    s.append('<div class="callout callout-danger"><b>ZAGROŻENIE — najczęstsze błędy walidacji:</b> „Za mały rozmiar pliku!” (rozmiar poniżej progu MinIO), '
             'kod 39 (zły FID w nazwie), kod 40 (zła data w nazwie), blokada wersji backup („wersja musi być wyższa od docelowej”).</div>')
    used = {x for _,_,_,sh in steps for x in sh} | {'screens/ccm/ccm-004.png','screens/ccm/ccm-017.png'}
    s.append(gallery('ccm','Pulpit CCM', exclude=used))
    return ''.join(s)

def domena_section(area, title, intro):
    s = [f'<p class="lead">{esc(intro)}</p>']
    s.append(gallery(area, title))
    return ''.join(s)

def fid607_section():
    s = ['<p class="lead">Plik GLSK (Generation and Load Shift Keys, FIDx-607) — 32 udokumentowane stany kafelka '
         '(para lewy×prawy kanał): sukces, przetwarzanie, oczekiwanie, błędy oraz wysyłka ręczna.</p>']
    s.append(gallery('fid607','GLSK 607 — stany kafelka'))
    return ''.join(s)

def kreator_section():
    s = ['<p class="lead">KreatorIDCF_CGMES — publikacja środków zaradczych RA oraz plików GLSK/CBCORA '
         'przez Connector → MinIO, z weryfikacją w CCM.</p>']
    order = ['screens_kreatoridcf/panel.png','screens_kreatoridcf/03_wybrane_pliki_gsk.png',
             'screens_kreatoridcf/06_wybrane_pliki_cbcora.png','screens_kreatoridcf/okno_publikacji.png',
             'screens_kreatoridcf/okno_postep.png','screens_kreatoridcf/log_publikacji.png',
             'screens_kreatoridcf/00_monitor_normal.jpg','screens_kreatoridcf/11_ccm_weryfikacja.png']
    labels = ['1. Panel IDCF: GLSK / CBCORA / RA + „Publikuj Connector”','2. Wybór plików GLSK (.uct)',
              '3. Wybór plików CBCORA (.epc)','4. Okno „Pliki do publikacji” — wersje',
              '5. Postęp: wysyłka na MinIO + pakowanie ZIP','6. LOG: „Publikacja zakończona”',
              '7. Monitor: statusy zadań (OK / BŁĄD)','8. Weryfikacja w pulpicie CCM (IDCC FB)']
    figs = ''.join(img(f, cap=l) for f,l in zip(order,labels) if f in BYFILE)
    s.append(f'<div class="grid">{figs}</div>')
    return ''.join(s)

def aczp_section():
    s = ['<p class="lead">Plik AC (Allocation Constraints, FIDx-831) — ręczna obsługa w aplikacji ZP: '
         'tabela ograniczeń NTC/ATC, wersjonowanie, zatwierdzanie.</p>']
    figs = ''.join(img(f) for f in ['screens/ac_zp/image1.png','screens/ac_zp/image2.png'] if f in BYFILE)
    s.append(f'<div class="grid">{figs}</div>')
    return ''.join(s)

def section(id_, title, tag, body, stickers=None):
    presentation = SECTION_PRESENTATION[id_]
    group_code = presentation['group']
    group_title = NAV_GROUPS[group_code]['title']
    bar = ''
    if stickers:
        chips = ''.join(mini_sticker(h,t) for h,t in stickers)
        bar = (f'<nav class="section-links" aria-label="Powiązane rozdziały">'
               f'<b>Powiązane rozdziały</b>{chips}</nav>')
    return (
        f'<section id="{id_}" class="procedure-section" data-group="{group_code}">'
        f'<header class="section-header">'
        f'<div class="section-kicker"><span class="section-number">{esc(tag)}</span>'
        f'<span class="section-category">{esc(group_code)} · {esc(group_title)}</span></div>'
        f'<h2>{esc(title)}</h2><p class="section-summary">{esc(presentation["summary"])}</p>'
        f'</header>{bar}{body}</section>')

# Nawigacja i treść powstają z jednego rejestru SECTIONS zdefiniowanego po
# zbudowaniu wszystkich sekcji. Dzięki temu numeracja i spis treści nie rozchodzą się.

proces_body = f"""
<ul class="compact-list">
  <li><strong>Proces:</strong> IDCC (<em>Intraday Capacity Calculation</em>) w regionie Core.</li>
  <li><strong>Rola PSE:</strong> TSO.</li>
  <li><strong>Działania:</strong> dostarczanie danych wejściowych, monitorowanie plików i reakcja na zdarzenia awaryjne.</li>
</ul>

<h3>Architektura procesu i przepływ danych</h3>
<div class="architecture-flow" role="img" aria-label="Dwukierunkowy przepływ plików między narzędziami KDM, Connector 2.0 oraz systemami zewnętrznymi">
  <div class="architecture-layer architecture-kdm">
    <h4>KDM — narzędzia PSE</h4>
    <div class="architecture-tools">
      <div class="architecture-tool"><strong>ZP</strong><span>AC</span></div>
      <div class="architecture-tool"><strong>CCM</strong><span>monitorowanie i obsługa plików</span></div>
      <div class="architecture-tool"><strong>PLANS / Kreator</strong><span>IGM, GLSK, CBCORA, RA</span></div>
      <div class="architecture-tool"><strong>MinIO</strong><span>paczki i raporty</span></div>
    </div>
  </div>
  <div class="architecture-arrows" aria-hidden="true"><span>↕</span><span>↕</span><span>↕</span><span>↕</span></div>
  <div class="connector-hub"><strong>Connector 2.0</strong><span>dwukierunkowe wysyłanie i odbieranie plików</span></div>
  <div class="architecture-arrows architecture-arrows-external" aria-hidden="true"><span>↕</span><span>↕</span></div>
  <div class="architecture-layer architecture-external">
    <h4>Systemy zewnętrzne</h4>
    <div class="architecture-tools">
      <div class="architecture-tool"><strong>Perun4V + sFTP</strong><span>Individual Validation, IVA i raporty</span></div>
      <div class="architecture-tool"><strong>Core CC Tool</strong><span>pliki procesu, ACK i wyniki</span></div>
    </div>
  </div>
  <p class="architecture-note"><strong>Przebieg standardowy:</strong> pliki wysyłane i odbierane automatycznie między PSE a systemami zewnętrznymi przechodzą przez Connector 2.0, który obsługuje oba systemy zewnętrzne. <strong>Tryb awaryjny:</strong> procedura dopuszcza ręczne pobranie lub Manual Upload bezpośrednio w Core CC Tool przez Message Viewer.</p>
</div>

<h3>Iteracje procesu</h3>
<table class="ref"><thead><tr><th>Iteracja</th><th>Charakter</th><th>Zakres</th></tr></thead><tbody>
<tr><td><b>IDCC(a)</b></td><td>Pełny przebieg centralny + wyznaczanie ATC</td><td>AC, ATC Based Validation, Final NTC</td></tr>
<tr><td><b>IDCC(b)–(d)</b></td><td>Kolejne iteracje śróddzienne (ID2/ID3C/ID3)</td><td>GLSK, CGM, RefProg, CB, IVA, NTC, paczki PERUN</td></tr>
</tbody></table>

<h3>Wejścia PSE i bramki czasowe</h3>
<ul class="compact-list">
  <li><strong>TET:</strong> docelowy termin zakończenia.</li>
  <li><strong>Po przekroczeniu TET:</strong> należy poinformować operatora procesu Capacity Calculation, uzgodnić możliwość zakończenia kroku do <strong class="deadline-critical">CET</strong> i zastosować właściwe działanie opisane dla danego zdarzenia: automatyczny fallback, działanie backupowe albo działanie procesowe.</li>
  <li><strong>Szczegóły:</strong> <a href="#sec-legenda">legenda statusów</a> i <a href="#sec-katalog">katalog plików</a>.</li>
</ul>
"""

# pełny opis procesu (na podstawie Core IDCC BPD v5.0 + perspektywa PSE z v5_2) — fragmenty z agentów
TH_PL = {
 'Backup ID':'Kod backup','Description':'Opis','Process Step':'Krok procesu',
 'Solution/Action':'Rozwiązanie/Działanie','Owner':'Właściciel','Tool':'Narzędzie',
 'Email Template #':'Szablon e-mail #','Party':'Strona','Party code':'Kod strony',
 'Mandatory':'Obligatoryjność','MessageFlow number':'Nr MessageFlow','Receiver':'Odbiorca',
}
def load_frag(name):
    p = ROOT / name
    if not p.is_file():
        raise FileNotFoundError(f'Brak wymaganego fragmentu procedury: {name}')
    h = p.read_text(encoding='utf-8')
    for en, pl in TH_PL.items():   # ujednolić nagłówki tabel na polski
        h = re.sub(r'(<th[^>]*>)\s*' + re.escape(en) + r'\s*(</th>)', r'\1' + pl + r'\2', h)
    # Normalizacja rejestru inżynierskiego
    h = re.sub(r'Happy\s+Day', 'Stan poprawny / nominalny', h)
    h = re.sub(r'(?i)bra\s+diostepu', 'brak dostępu', h)
    return h

# ══════════════════════════ MONTAŻ DOKUMENTU v7 ══════════════════════════════
# Sekcja 1 zachowuje historyczną kotwicę sec-cel i formalną strukturę
# 1.1–1.2 wymaganą dla procedury dyspozytorskiej.
cel_body = f'''
<div class="intro-block" id="intro-summary">
<h3>1.1 Podsumowanie i cel</h3>
<p>Niniejsza procedura określa czynności, które należy wykonać po stronie PSE w roli TSO podczas realizacji procesu IDCC w regionie Core.</p>
<ul class="compact-list">
  <li>należy dostarczać wymagane dane wejściowe;</li>
  <li>należy monitorować proces i stany plików w CCM;</li>
  <li>należy przeprowadzić Individual Validation (IVA) wyznaczonych zdolności przesyłowych;</li>
  <li>w razie zdarzenia nienominalnego należy zastosować właściwe działanie i powiadomienie.</li>
</ul>
<p><strong>Cały proces IDCC jest procesem automatycznym, jednak nadal wymaga kontroli i nadzoru po stronie dyspozytora.</strong></p>
</div>
<div class="intro-block" id="intro-governance">
<h3>1.2 Zakres czynności</h3>
<table class="ref"><thead><tr><th>Obszar</th><th>Zakres</th></tr></thead><tbody>
<tr><td><strong>Zakres działań</strong></td><td>Operator procesu Capacity Calculation koordynuje przebieg centralny. Dyspozytor PSE wykonuje i monitoruje czynności przypisane TSO. Coreso pełni rolę Merging Entity w etapach scalania danych.</td></tr>
<tr><td><strong>Czynności PSE</strong></td><td>Dostarczanie danych wejściowych, monitorowanie, walidacja, obsługa plików, działania ręczne oraz reakcja na zdarzenia związane z procesem IDCC.</td></tr>
</tbody></table>
</div>
{load_frag('process2_glos.html')}
'''

proces_body2 = proces_body + load_frag('process2_a.html') + load_frag('process2_bcd.html')

katalog_body = section_katalog() + load_frag7('frag7_maski.html')

happyday_body = (load_frag7('frag7_happyday.html')
 + '<details class="gal"><summary>Szczegółowy przebieg i użycie narzędzi (opis rozszerzony)</summary>'
 + v52_slice('s5','s6') + v52_slice('s6','s7') + '</details>')

def _inject_ids(html_, mapping):
    for pref, hid in mapping:
        pattern = re.compile(r'<h4(?P<attrs>[^>]*)>(?P<label>\s*' + re.escape(pref) + ')')
        def replace_heading(match):
            attrs = re.sub(r'\s+id=(?:"[^"]*"|\'[^\']*\')', '', match.group('attrs'))
            return f'<h4{attrs} id="{hid}">{match.group("label")}'
        html_ = pattern.sub(replace_heading, html_, count=1)
    return html_

ccm_ext = v52_h3block(['7M.1.','7M.3.','7M.7.','7M.8.','7M.9.','7M.10.','7M.11.','7M.12.','7M.13.','7M.14.'])
ccm_ext = _inject_ids(ccm_ext, [('7M.1.','ccm-tryby'),('7M.3.','ccm-profile'),('7M.7.','ccm-scen'),
 ('7M.8.','ccm-ack'),('7M.9.','ccm-powiadomienia'),('7M.10.','ccm-eksport'),('7M.11.','ccm-idcf'),
 ('7M.12.','ccm-c6plus'),('7M.13.','ccm-uprawnienia'),('7M.14.','ccm-awarie')])
ccm_body = ccm_section() + '<h3 id="ccm-ext">Rozszerzenia CCM (katalog 7M)</h3>' + ccm_ext

def prepare_input_stage(body):
    """Formatuje odziedziczone sekcje danych wejściowych i rozróżnia tryby reakcji."""
    body = re.sub(r'<hr class="section-divider">', '', body)
    body = body.replace('4A.3. Fallback przy braku CGM',
                        '4A.3. Automatyczny fallback przy braku CGM')
    body = body.replace(
        '<p>Jeżeli Combined DACF nie jest dostępny (IDCC(b)), stosuje się następującą kolejność fallbacku:</p>',
        '<p class="mode-legend"><span class="mode-badge mode-auto">FALLBACK AUTOMATYCZNY</span> '
        'jest wykonywany przez system centralny i nie wymaga reakcji dyspozytora PSE. '
        'Przed jego uruchomieniem wykorzystywane są kolejne dostępne warianty danych procesowych:</p>')
    body = body.replace(
        '<li><strong>Coreso DACF</strong> — jeżeli dostępny, używany jako backup;</li>',
        '<li><strong>Coreso DACF</strong> — pierwszy dostępny wariant danych procesowych;</li>')
    body = body.replace(
        '<li><strong>TSCNET DACF</strong> — jeżeli Coreso DACF niedostępny;</li>',
        '<li><strong>TSCNET DACF</strong> — kolejny wariant, jeżeli Coreso DACF jest niedostępny;</li>')
    body = body.replace(
        '<li><strong>Automatyczny fallback CCCt</strong> — jeżeli żaden CGM nie jest dostępny, CCCt używa ostatniego dostępnego CGM lub DA Domain jako fallback.</li>',
        '<li><span class="mode-badge mode-auto">FALLBACK AUTOMATYCZNY</span> — jeżeli żaden CGM nie jest dostępny, CCCt automatycznie używa ostatniego dostępnego CGM albo DA Domain.</li>')
    body = body.replace(
        '<p>Dla IDCC(c–d): jeżeli TSCNET IDCF z target run nie jest dostępny, używany jest CGM z poprzedniego IDCF run.</p>',
        '<p>Dla IDCC(c)–(d), jeżeli TSCNET IDCF z target run nie jest dostępny, CCCt automatycznie wykorzystuje CGM z poprzedniego IDCF run.</p>')
    body = body.replace(
        'Po zamknięciu bramki TSO Data Gathering CCCt dystrybuuje <strong>Merged CB</strong> — PSE sprawdza poprawność scalenia.',
        'Po zamknięciu bramki TSO Data Gathering CCCt dystrybuuje <strong>Merged CB</strong>; w tym kroku nie jest wymagana ręczna czynność PSE.')
    body = body.replace(
        'Po zamknięciu bramki CCCt dystrybuuje <strong>Merged GLSK</strong> — PSE sprawdza poprawność scalenia.',
        'Po zamknięciu bramki CCCt dystrybuuje <strong>Merged GLSK</strong>; w tym kroku nie jest wymagana ręczna czynność PSE.')
    body = re.sub(
        r'<span style="color:var\(--pse-red\);font-weight:700;">MANDATORY</span>',
        '<strong class="mandatory-note">UWAGA: MANDATORY</strong>', body)
    return f'<div class="input-stage">{body}</div>'

igm_body = ''.join([
    prepare_input_stage(v52_slice('s4a','s4b')),
    prepare_input_stage(v52_slice('s4b','s4c')),
    prepare_input_stage(v52_slice('s4c','s4d')),
    prepare_input_stage(v52_slice('s4d','s5')),
])

walidacja_body = (load_frag7('frag7_walidacja.html')
 + '<h4>Ekrany — tryb normalny (NOR)</h4>' + gallery('nor','Walidacja NOR')
 + '<h4>Ekrany — tryb backupowy (BUP)</h4>' + gallery('bup','Walidacja BUP')
 + '<h4 id="wal-glsk">GLSK (FIDx-607) — katalog 32 stanów kafelka</h4>' + gallery('fid607','GLSK 607 — stany kafelka'))

ops_body = v52_slice('s8','s9')

kreator_body = kreator_section() + '<h3 id="aczp">AC w ZP (FIDx-831)</h3>' + aczp_section()

ryzyka_body = ('<ul class="compact-list">'
 '<li><strong>Zakres:</strong> 29 ryzyk operacyjnych R01–R29.</li>'
 '<li><strong>Każde ryzyko:</strong> wpływ, procedura działania i skrót decyzyjny.</li>'
 '<li><strong>Zgłoszenie:</strong> CIZ, WPO i PSE-I.</li>'
 '</ul>'
 + '<div class="ref riskbase">' + RYZ_HTML + '</div>'
 + '<details class="gal"><summary>Mapowanie U-kodów (U01–U23) i tabela kodów ACK</summary><div class="ref">'
 + inw_slice('# 3. Ryzyka', '# 4. Procedury', '# 3. Ryzyka') + '</div></details>')

kontakty_body = '''<h3 id="kontakty">Kontakty operacyjne</h3>
<p class="lead">Komplet kontaktów wymaganych przy realizacji scenariuszy opisanych w tej procedurze.</p>
<table class="ref">
  <thead><tr><th>Podmiot / narzędzie</th><th>E-mail / kanał</th><th>Telefon</th><th>Zakres</th></tr></thead>
  <tbody>
    <tr><td><strong>TSCNET — operator procesu Capacity Calculation</strong></td><td>operator@tscnet.eu</td><td>+49 89 45554 201</td><td>Obsługa CCCt; decyzje dotyczące działania backupowego lub zatrzymania procesu</td></tr>
    <tr><td><strong>Coreso — Merging Entity</strong></td><td>day-ahead.engineer@coreso.eu</td><td>+32 2 743 21 10</td><td>Scalanie CGM i merging package</td></tr>
    <tr><td><strong>Helpdesk CCC</strong></td><td>idcc.helpdesk@unicorn.com</td><td>+420 221 400 540</td><td>CCCt: GUI, pliki i obliczenia</td></tr>
    <tr><td><strong>USY ECP/EDX</strong></td><td>global-ecp@unicorn.com</td><td>+420 221 400 902</td><td>Kanał ECP/EDX</td></tr>
    <tr><td><strong>Raport CCA</strong></td><td>kdm6@pse.pl</td><td>—</td><td>Skrzynka raportów walidacji</td></tr>
    <tr><td><strong>PSE Innowacje</strong></td><td>zgłoszenie przez CIZ/WPO</td><td>—</td><td>Connector 2.0, SFTP, MinIO</td></tr>
  </tbody>
</table>'''
minio_body = ('<div class="ref">' + inw_slice('# 5. Buckety','# 7. TODO','# 5. Buckety') + '</div>' + kontakty_body)

checklisty_body = (v52_slice('aneks')
 + '<h3>Komplet materiałów ekranowych</h3>'
 + '<p class="note">W procedurze wykorzystano wszystkie materiały z manifestu ekranów. Ujęcia pomocnicze, '
   'duplikaty i materiały o ograniczonej czytelności są zachowane oddzielnie poniżej.</p>'
 + source_archive())

# ── STICKERY: krótkie kroki + hiperłącza (jedno źródło → sekcja HTML + MD) ───
STICKER_STEPS = [
 ('🟢 Start dyżuru', [
   ('Zaloguj się do CCM, otwórz pulpit IDCC i ustaw dobę', '#ccm-c1'),
   ('Sprawdź bramki czasowe bieżącej iteracji', '#hlbp-zbiorcza'),
   ('Przejdź checklistę przed iteracją', '#aneks'),
 ]),
 ('👁 Monitorowanie IDCC(b)/(c)/(d)', [
   ('Wykonaj 6 kroków przebiegu nominalnego', '#hd-6krokow'),
   ('Perun4V: sprawdź timestampy (0 Failed)', '#maski-perun'),
   ('Oceń raport CCA z kdm6 (TS + zasadność IVA)', '#hd-6krokow'),
   ('Rozpoznaj status kafelka wg legendy', '#sec-legenda'),
   ('Sprawdź opis pliku i stany w katalogu', '#sec-katalog'),
 ]),
 ('👁 Monitorowanie IDCC(a)', [
   ('Monitoruj FID1-928: v2 zielona po 13:15 D-1', '#hd-a'),
   ('Brak v2 po 14:30 → MinIO cca/… → telefon do operatora procesu', '#hd-a'),
   ('Pilnuj AC (FID1-831) z ZP i finalnych NTC (FID1-921)', '#aczp'),
   ('Kroki PSE w iteracji (a) wg BPD', '#proc-a'),
 ]),
 ('📤 Wysyłka ręczna i status R', [
   ('Wyślij plik przed CET: PPM → Wyślij', '#ccm-c4'),
   ('Wyślij po CET: PPM → Wyślij po CET', '#ccm-c5'),
   ('Ustaw / przywróć status ręczny R', '#ccm-c5'),
   ('Sprawdź maskę pliku przed wysyłką', '#maski-iva'),
 ]),
 ('⚠️ Kafelki alarmowe', [
   ('Czerwony „?" (brak ACK) → Message Viewer CCCt', '#R04'),
   ('Czerwony „!" (za mały plik) → procedura B2', '#hd-b2'),
   ('Czarny agregat (brak ZIP) → procedura B3', '#hd-b3'),
   ('ACK Rejected → odczytaj kod (20/21/30)', '#ccm-ack'),
   ('Scenariusze backupowe S.1–S.13', '#ccm-scen'),
 ]),
 ('🧯 Walidacja — problemy', [
   ('ERR-I (część TS) → czekaj na IVA BACKUP v2+', '#hd-erri'),
   ('Process failed (0 TS) → wyślij BACKUP v1', '#hd-pf'),
   ('Brak SFTP >30 min → ręczna walidacja B1', '#hd-b1'),
   ('Awaria ECP/EDX → Manual Upload IVA (B4)', '#hd-b4'),
   ('Tryb backup BUP (paczka ręczna, F308)', '#wal-bup'),
 ]),
 ('🛠 Awarie narzędzi', [
   ('Brak dostępu do CCM', '#R01'),
   ('Brak dostępu do Core CC Tool', '#R03'),
   ('Ręczny upload do CCCt (Manual Upload)', '#P01'),
   ('Pobranie pliku ze źródła (aplikacja ZP)', '#P02'),
   ('Ręczne uruchomienie obliczeń Perun4V', '#P03'),
   ('Obsługa MinIO / Perun4V / CCCt — pełna instrukcja', '#sec-ops'),
 ]),
 ('📦 Dane wejściowe PSE', [
   ('Dostarcz IGM do RCC (DACF/IDCF)', '#s4a'),
   ('TSO Data Gathering — komplet plików', '#s4b'),
   ('Wygeneruj i wyślij CB (FIDx-617)', '#s4c'),
   ('Wygeneruj i wyślij GLSK (FIDx-607)', '#s4d'),
   ('Publikacja z Kreatora IDCF (GLSK/CBCORA/RA)', '#sec-kreator'),
 ]),
 ('📣 Komunikacja i reakcja', [
   ('Wybierz właściwy szablon maila Core ID', '#proc-mail'),
   ('Telefony i adresy: CCC / USY / kdm6', '#kontakty'),
   ('Znajdź ryzyko i skrót działania (R01–R29)', '#sec-ryzyka'),
   ('Automatyczne fallbacki i działania backupowe iteracji (b)–(d)', '#proc-bcd'),
 ]),
]

def stickery_section_html():
    cards = ''
    for title, steps in STICKER_STEPS:
        lis = ''.join(f'<li><a href="{h}">{esc(t)}</a></li>' for t,h in steps)
        cards += f'<div class="stick"><h4>{esc(title)}</h4><ol>{lis}</ol></div>'
    return ('<p class="lead">Karty skrócone do druku/naklejenia: wyłącznie krótkie kroki działania. '
            'Każdy krok jest hiperłączem do właściwego miejsca w pełnej procedurze powyżej.</p>'
            f'<div class="stickgrid">{cards}</div>')

def anchored_mail_templates():
    """Dodaje kotwice do przykładów maili bez zmiany treści źródłowych szablonów."""
    source = load_frag('process2_mail.html')
    return re.sub(
        r'(?=<div class="mailtpl">\s*<h4>(\d{2})\s+—)',
        lambda match: f'<span class="mail-anchor" id="mail-{match.group(1)}"></span>',
        source)


MAIL_TEMPLATES_HTML = anchored_mail_templates()

# Centralna mapa prezentacji oddziela treść techniczną od architektury informacji.
# Historyczne identyfikatory pozostają bez zmian, a rozdziały są grupowane jak
# w procedurze operacyjnej: od podstaw i przygotowania, przez realizację, po rejestry.
NAV_GROUPS = {
    'A': {'title': 'Informacje formalne', 'summary': 'Cel, zakres i definicje dokumentu.'},
    'B': {'title': 'Przygotowanie procesu', 'summary': 'Warunki, dane wejściowe i bramki czasowe.'},
    'C': {'title': 'Realizacja procesu', 'summary': 'Przebieg nominalny, walidacja i tryby backupowe.'},
    'D': {'title': 'Obsługa operacyjna', 'summary': 'Narzędzia i czynności wykonywane przez dyspozytora.'},
    'E': {'title': 'Załączniki i rejestry', 'summary': 'Pliki, statusy, ryzyka, komunikacja i karty skrócone.'},
}
SECTION_PRESENTATION = {
    'sec-cel': {'group': 'A', 'summary': 'Przeznaczenie procedury, zakres odpowiedzialności PSE oraz wspólny słownik pojęć.'},
    'sec-checklisty': {'group': 'B', 'summary': 'Kontrole dostępu, kompletności danych i gotowości stanowiska przed rozpoczęciem iteracji.'},
    'sec-igm': {'group': 'B', 'summary': 'Dane przygotowywane i dostarczane przez PSE wraz z właściwymi kanałami publikacji.'},
    'sec-harmonogram': {'group': 'B', 'summary': 'Bramki procesu, czasy TET i CET oraz punkty kontrolne dla kolejnych iteracji.'},
    'sec-proces': {'group': 'C', 'summary': 'Przebieg IDCC(a)–(d) ograniczony do kroków i decyzji istotnych dla PSE.'},
    'sec-happyday': {'group': 'C', 'summary': 'Sekwencja przebiegu prawidłowego oraz przejście do właściwego działania backupowego.'},
    'sec-walidacja': {'group': 'C', 'summary': 'Individual Validation w trybach NOR i BUP wraz z kontrolą plików oraz wyników.'},
    'sec-ccm': {'group': 'D', 'summary': 'Monitorowanie statusów, wysyłka ręczna i obsługa zdarzeń w pulpicie CCM.'},
    'sec-ops': {'group': 'D', 'summary': 'Instrukcje obsługi MinIO, Perun4V i Core CC Tool w przebiegu standardowym i awaryjnym.'},
    'sec-kreator': {'group': 'D', 'summary': 'Publikacja GLSK, CBCORA i RA z Kreatora IDCF oraz obsługa AC w aplikacji ZP.'},
    'sec-narzedzia': {'group': 'D', 'summary': 'Role systemów, kanały komunikacyjne i zależności między narzędziami procesu.'},
    'sec-katalog': {'group': 'E', 'summary': 'Katalog FIDx z opisami, maskami nazw, ścieżkami i dopuszczalnymi stanami plików.'},
    'sec-legenda': {'group': 'E', 'summary': 'Jednoznaczna interpretacja kolorów i znaczników statusów widocznych w CCM.'},
    'sec-procedury': {'group': 'E', 'summary': 'Procedury P01–P06 dla najczęstszych czynności ręcznych i trybów zastępczych.'},
    'sec-ryzyka': {'group': 'E', 'summary': 'Rejestr ryzyk R01–R29, kodów pomocniczych i wymaganych reakcji operacyjnych.'},
    'sec-mail': {'group': 'E', 'summary': 'Nienaruszone wzorce 19 wiadomości operacyjnych wykorzystywanych w procesie Core ID.'},
    'sec-minio': {'group': 'E', 'summary': 'Mapa bucketów MinIO, relacji plików oraz komplet kontaktów operacyjnych.'},
    'sec-stickery': {'group': 'E', 'summary': 'Karty szybkiego działania prowadzące bezpośrednio do pełnych kroków procedury.'},
}

# Jeden rejestr jest źródłem numeracji rozdziałów, spisu treści i treści dokumentu.
# Identyfikatory historyczne pozostają bez zmian, aby zachować wszystkie odsyłacze.
SECTIONS = [
    ('sec-cel', 'Wstęp', cel_body,
     [('#sec-checklisty', 'przygotowanie procesu'), ('#sec-proces', 'przegląd procesu')]),
    ('sec-checklisty', 'Warunki wstępne i checklisty dyżurowe', checklisty_body,
     [('#sec-igm', 'dane wejściowe'), ('#sec-stickery', 'szybkie kroki')]),
    ('sec-igm', 'Dane wejściowe', igm_body,
     [('#sec-kreator', 'Kreator IDCF'), ('#sec-katalog', 'katalog plików')]),
    ('sec-harmonogram', 'Harmonogram operacyjny (CCCt)', load_frag7('frag7_harmonogram.html'),
     [('#sec-proces', 'przegląd procesu'), ('#sec-katalog', 'TET/CET plików')]),
    ('sec-proces', 'Przegląd procesu IDCC — kroki istotne dla PSE', proces_body2,
     [('#sec-happyday', 'przebieg nominalny'), ('#sec-walidacja', 'walidacja')]),
    ('sec-happyday', 'Przebieg nominalny i scenariusze backupowe', happyday_body,
     [('#sec-harmonogram', 'harmonogram'), ('#sec-ryzyka', 'ryzyka')]),
    ('sec-walidacja', 'Walidacja domeny FBA (NOR / BUP / GLSK)', walidacja_body,
     [('#sec-happyday', 'scenariusze B1–B4'), ('#sec-ops', 'Perun4V')]),
    ('sec-ccm', 'Monitorowanie i czynności w CCM (C.1–C.12 + katalog 7M)', ccm_body,
     [('#sec-legenda', 'legenda statusów'), ('#sec-ryzyka', 'ryzyka')]),
    ('sec-ops', 'Obsługa MinIO, Perun4V i Core CC Tool', ops_body,
     [('#sec-narzedzia', 'narzędzia'), ('#sec-procedury', 'procedury')]),
    ('sec-kreator', 'Kreator IDCF i AC w ZP', kreator_body,
     [('#sec-igm', 'CB/GLSK'), ('#sec-katalog', 'FIDx-831')]),
    ('sec-narzedzia', 'Narzędzia i protokoły komunikacyjne', '<div class="ref">'+TOOLS_HTML+'</div>',
     [('#sec-ops', 'obsługa MinIO/Perun/CCCt'), ('#sec-ryzyka', 'ryzyka')]),
    ('sec-katalog', 'Katalog plików FIDx — opisy, stany i maski', katalog_body,
     [('#sec-legenda', 'legenda'), ('#sec-ccm', 'obsługa w CCM')]),
    ('sec-legenda', 'Legenda statusów kafelków', legend_section(),
     [('#sec-ccm', 'monitoring w CCM'), ('#sec-katalog', 'stany plików')]),
    ('sec-procedury', 'Procedury P01–P06', '<div class="ref">'+inw_slice('# 4. Procedury','# 5. Buckety','# 4. Procedury')+'</div>',
     [('#sec-ryzyka', 'ryzyka'), ('#sec-ccm', 'CCM')]),
    ('sec-ryzyka', 'Ryzyka R01–R29, U-kody i kody ACK', ryzyka_body,
     [('#sec-procedury', 'procedury'), ('#sec-mail', 'szablony wiadomości')]),
    ('sec-mail', 'Szablony wiadomości operacyjnych (Core ID)', '<div class="proc">'+MAIL_TEMPLATES_HTML+'</div>',
     [('#kontakty', 'kontakty'), ('#sec-ryzyka', 'ryzyka')]),
    ('sec-minio', 'Buckety MinIO, mapa relacji i kontakty', minio_body,
     [('#sec-katalog', 'pliki'), ('#sec-narzedzia', 'MinIO')]),
    ('sec-stickery', 'Karty szybkiego działania', stickery_section_html(),
     [('#top', 'początek dokumentu')]),
]

SECTION_NUMBERS = {id_: f'{index:02d}' for index, (id_, _, _, _) in enumerate(SECTIONS, 1)}
nav_parts = ['<a class="nav-start" href="#top"><span>00</span>Start dokumentu</a>']
for group_code, group_meta in NAV_GROUPS.items():
    group_sections = [item for item in SECTIONS if SECTION_PRESENTATION[item[0]]['group'] == group_code]
    nav_heading_id = f'nav-group-{group_code.lower()}'
    nav_parts.append(
        f'<section class="nav-group" aria-labelledby="{nav_heading_id}">'
        f'<h3 class="nav-group-heading" id="{nav_heading_id}"><span>{group_code}</span>'
        f'<b>{esc(group_meta["title"])}</b></h3>')
    nav_parts.extend(
        f'<a href="#{id_}"><span>{SECTION_NUMBERS[id_]}</span>{esc(title)}</a>'
        for id_, title, _, _ in group_sections)
    nav_parts.append('</section>')
nav_html = ''.join(nav_parts)
toc_html = ''
sections_html = ''.join(
    section(id_, title, SECTION_NUMBERS[id_], body, stickers)
    for id_, title, body, stickers in SECTIONS)

hero_visual_html = ''
if FINAL_LAYOUT:
    rails = ''.join(f'<span data-label="{label}"></span>' for label in 'ABCDE')
    hero_visual_html = f'<div class="hero-visual" aria-hidden="true"><div class="hero-rails">{rails}</div></div>'

cover_html = f'''
<header class="hero">
  <div class="hero-copy">
    <div class="eyebrow">FBA_TSO_IDCC · PSE S.A. · KDM · REGION CORE</div>
    <h1>Procedura operacyjna dyspozytora — proces IDCC</h1>
    <p class="subtitle">Kompletna instrukcja przygotowania, realizacji i obsługi procesu z perspektywy PSE, uporządkowana w pięciu częściach operacyjnych A–E.</p>
    <div class="hero-meta"><span>WYDANIE v{esc(DOC_META['version'])}</span><span>5 CZĘŚCI · 18 ROZDZIAŁÓW</span><span>309 ZASOBÓW EKRANOWYCH</span><span>TRYB OFFLINE</span></div>
  </div>
  {hero_visual_html}
</header>
<div class="callout callout-danger"><strong>Dokument roboczy — niezatwierdzony do formalnego wydania</strong></div>
<div class="callout">
  <strong>Klauzula ogólna dla przebiegu NOR.</strong>
  Jako generalną zasadę przyjęto – w przypadku pojawienia się zdarzenia wykraczającego poza normalny przebieg procedury użytkownik wykonuje kolejne czynności zgodnie z częścią backupową niniejszego połączonego dokumentu roboczego, w szczególności sekcjami <a href="#sec-happyday">„Przebieg nominalny i scenariusze backupowe”</a>, <a href="#sec-procedury">„Procedury P01–P06”</a> oraz <a href="#sec-ryzyka">„Ryzyka R01–R29”</a>.
</div>
<details class="gal document-metadata">
  <summary>Metryka dokumentu i historia wersji</summary>
  <h3>Metryka dokumentu</h3>
  <table class="ref"><tbody>
    <tr><th>Identyfikator roboczy</th><td>{esc(DOC_META['working_id'])}</td><th>Typ</th><td>{esc(DOC_META['document_type'])}</td></tr>
    <tr><th>Formalny kod NOR/BUP</th><td>{esc(DOC_META['formal_code'])}</td><th>Data (DD/MM/YYYY)</th><td>{esc(DOC_META['date'])}</td></tr>
    <tr><th>Wersja robocza</th><td>{esc(DOC_META['version'])}</td><th>Status</th><td><strong>{esc(DOC_META['status'])}</strong></td></tr>
  </tbody></table>
  <p class="note">Brak formalnego kodu pary NOR/BUP i daty wydania w przekazanych materiałach. Pola pozostawiono jawnie nieuzupełnione.</p>
  <h3>Zatwierdzono</h3>
  <table class="ref"><tbody>
    <tr><th>Opracował</th><td>{esc(DOC_META['author'])}</td></tr>
    <tr><th>Zatwierdził</th><td>{esc(DOC_META['approver'])}</td></tr>
    <tr><th>Data zatwierdzenia</th><td>{esc(DOC_META['approval_date'])}</td></tr>
  </tbody></table>
  <p class="note">Pola wymagają uzupełnienia przez właściciela dokumentu przed nadaniem statusu Final.</p>
  <h3>Poprzednie wersje</h3>
  <table class="ref"><thead><tr><th>Wersja</th><th>Data</th><th>Zakres zmian</th></tr></thead><tbody>
    <tr><td>—</td><td>—</td><td>Brak zatwierdzonej historii wersji w przekazanych materiałach.</td></tr>
  </tbody></table>
  <p class="note">Wersja 7 jest roboczym identyfikatorem bieżącego, scalonego opracowania.</p>
</details>'''

doc = f"""<!doctype html><html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#0f3e63">
<title>Procedura IDCC TSO v7 — kompletna instrukcja z ekranami</title>
<style>{CSS}{FINAL_CSS if FINAL_LAYOUT else ''}
/* v5_2 compat */
.tbl-wrap{{overflow-x:auto}}
.subhead{{font:600 12px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--navy);margin:1em 0 .35em}}
.branch{{border-left:3px solid var(--rule2);padding:7px 13px;margin:9px 0;background:rgba(15,62,99,.03);border-radius:0 6px 6px 0}}
.sdot{{display:inline-block;width:12px;height:12px;border-radius:3px;vertical-align:middle;margin-right:4px;border:1px solid rgba(0,0,0,.15)}}
.tile-state img{{vertical-align:middle}}
.risk-h{{border:1px solid #e1aaa6!important;border-left:7px solid var(--err)!important;border-radius:5px;
padding:10px 12px!important;margin-top:1.7em!important;font-family:var(--cond);font-size:17px!important;
text-transform:none;letter-spacing:0;color:var(--err)!important;background:linear-gradient(90deg,var(--errb),#fff 75%)}}
.risk-h::before{{content:"⚠ ZAGROŻENIE · ";font:800 10px var(--mono);letter-spacing:.08em}}
.riskbase h5{{color:var(--acc);margin-top:10px;padding-left:9px;border-left:3px solid var(--acc)}}
/* ── arkusz naklejek ── */
.stickgrid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:26px;margin:26px 4px;padding:6px}}
.stick{{position:relative;background:#fffdf2;border:1px solid var(--rule2);border-left:7px solid var(--yellow);
border-radius:8px;padding:14px 17px 15px;box-shadow:0 3px 10px rgba(26,34,48,.13);
outline:2px dashed var(--rule2);outline-offset:7px;break-inside:avoid;transition:transform .18s ease,box-shadow .18s ease}}
.stick:nth-child(odd){{transform:rotate(-.45deg)}}
.stick:nth-child(even){{transform:rotate(.4deg)}}
.stick:hover{{transform:rotate(0) translateY(-3px);box-shadow:0 9px 22px rgba(26,34,48,.19)}}
.stick::after{{content:"✂";position:absolute;top:-21px;right:2px;font-size:13px;color:var(--rule2);transform:rotate(-90deg)}}
.stick h4{{margin:.05em 0 .55em;font:700 15px var(--cond);letter-spacing:.02em;color:var(--ink);
border-bottom:1px solid var(--rule);padding-bottom:7px}}
.stick ol{{margin:0;padding-left:20px}}
.stick li{{margin:5px 0;font-size:13.5px;line-height:1.4}}
.stick li::marker{{font:600 11px var(--mono);color:var(--warn)}}
.stick a{{color:var(--acc);text-decoration-line:underline;text-decoration-thickness:1px;text-decoration-color:rgba(14,86,136,.42);text-underline-offset:2px}}
.stick a:hover{{color:var(--navy);text-decoration-color:currentColor}}
</style></head><body class="{BODY_CLASS}">
<div class="wrap">
<nav aria-label="Spis treści"><h2>Spis treści · A–E</h2>{nav_html}</nav>
<main id="top">
{cover_html}
{toc_html}
<div class="doc-tools" aria-label="Narzędzia dokumentu">
  <span class="tool-label">Widok</span><span class="offline-badge">● jeden plik · offline</span>
  <button type="button" onclick="showScreenMode()">Ekrany + główne kroki</button>
  <button type="button" onclick="document.querySelectorAll('details').forEach(function(item){{item.open=true}})">Pełna treść</button>
  <button type="button" onclick="document.querySelectorAll('details').forEach(function(item){{item.open=false}})">Sam skrót</button>
  <button type="button" onclick="printProcedure()">Drukuj / PDF</button>
</div>
<div class="quickgrid" aria-label="Szybki start">
  <a class="quickcard action" href="#sec-checklisty"><span class="qicon">✓</span><b>Start dyżuru</b><small>Checklista, dostęp i właściwa doba.</small></a>
  <a class="quickcard success" href="#sec-happyday"><span class="qicon">●</span><b>Przebieg prawidłowy</b><small>6 kroków i zielone punkty kontrolne.</small></a>
  <a class="quickcard emergency" href="#sec-ryzyka"><span class="qicon">!</span><b>Zagrożenie / awaria</b><small>Reakcja, działanie backupowe i powiadomienie.</small></a>
  <a class="quickcard warning" href="#sec-stickery"><span class="qicon">↗</span><b>41 szybkich działań</b><small>Skrót → pełny krok i ekran.</small></a>
</div>
<div class="semantic-key" aria-label="Znaczenie kolorów">
  <div class="key-item key-success"><span class="key-dot"></span><span><b>ZIELONY · PRAWIDŁOWO</b>monitoruj, bez interwencji</span></div>
  <div class="key-item key-warning"><span class="key-dot"></span><span><b>ŻÓŁTY · UWAGA</b>termin lub stan przejściowy</span></div>
  <div class="key-item key-danger"><span class="key-dot"></span><span><b>CZERWONY · ZAGROŻENIE</b>należy działać i powiadomić właściwą rolę</span></div>
  <div class="key-item key-action"><span class="key-dot"></span><span><b>NIEBIESKI · DZIAŁANIE</b>krok operatora</span></div>
</div>
{sections_html}
<dialog id="screen-dialog" class="screen-dialog" aria-label="Powiększony zrzut ekranu">
  <button type="button" aria-label="Zamknij powiększenie">×</button><img alt="Powiększony zrzut ekranu"><p></p>
</dialog>
<footer style="margin:3em 0 2em;color:var(--mut);font-size:13px;border-top:1px solid var(--rule);padding-top:14px">
<strong>PROCEDURA_IDCC_TSO_v7</strong> · jeden samowystarczalny dokument · {len(MAN)} zasobów ekranowych w manifeście ·
{sum(len(v) for v in HINTS.values())} wariantów stanów · {len(FILES)} opisów plików · 19 szablonów wiadomości.
Wszystkie instrukcje, kontakty i materiały ekranowe potrzebne do realizacji opisanych działań znajdują się powyżej.
Każde ryzyko zgłaszać do: <b>CIZ, WPO, PSE-I (PSE Innowacje)</b>.</footer>
<script>
const semanticPatterns = {{
  danger: /CET|KRYTYCZNE|STOP|brak (?:ACK|potwierdzenia odbioru|pliku|wyniku)|brak dostępu|awaria|błąd procesu|negatywn(?:y|e) (?:ACK|potwierdzenie odbioru)|plik niezwalidowany|niepoprawn[yae]|niezgodn[yae]|niedostarczon[yae]|timeout|odrzucon[yae]|Rejected|Process failed|przekroczono (?:CET|krytyczny termin zakończenia)|minął (?:CET|krytyczny termin zakończenia)|nie wysyłaj/giu,
  warning: /UWAGA|OSTRZEŻENIE|zbliża się (?:TET|CET|docelowy termin zakończenia|krytyczny termin zakończenia)|ERR-I|po (?:CET|krytycznym terminie zakończenia)|tryb backupowy|IVA BACKUP|fallback/giu,
  success: /PRAWIDŁOWO|SUKCES|SUCCESSFUL|proces poprawny|stan prawidłowy|brak działań|potwierdzon[ey] (?:ACK|potwierdzenie odbioru)|Processed/giu,
  action: /ZGŁOŚ|ZADZWOŃ|SPRAWDŹ|POWIADOM|WYŚLIJ(?: PLIK)? RĘCZNIE|POBIERZ(?: POPRAWNY)? PLIK|ODCZYTAJ KOD (?:ACK|potwierdzenia odbioru)|USTAW STATUS|URUCHOM(?: PONOWNIE)? OBLICZENIA|PRZEJDŹ DO SCENARIUSZA/giu
}};
const semanticPattern = /CET|KRYTYCZNE|STOP|brak (?:ACK|potwierdzenia odbioru|pliku|wyniku)|brak dostępu|awaria|błąd procesu|negatywn(?:y|e) (?:ACK|potwierdzenie odbioru)|plik niezwalidowany|niepoprawn[yae]|niezgodn[yae]|niedostarczon[yae]|timeout|odrzucon[yae]|Rejected|Process failed|przekroczono (?:CET|krytyczny termin zakończenia)|minął (?:CET|krytyczny termin zakończenia)|nie wysyłaj|UWAGA|OSTRZEŻENIE|zbliża się (?:TET|CET|docelowy termin zakończenia|krytyczny termin zakończenia)|ERR-I|po (?:CET|krytycznym terminie zakończenia)|tryb backupowy|IVA BACKUP|fallback|PRAWIDŁOWO|SUKCES|SUCCESSFUL|proces poprawny|stan prawidłowy|brak działań|potwierdzon[ey] (?:ACK|potwierdzenie odbioru)|Processed|ZGŁOŚ|ZADZWOŃ|SPRAWDŹ|POWIADOM|WYŚLIJ(?: PLIK)? RĘCZNIE|POBIERZ(?: POPRAWNY)? PLIK|ODCZYTAJ KOD (?:ACK|potwierdzenia odbioru)|USTAW STATUS|URUCHOM(?: PONOWNIE)? OBLICZENIA|PRZEJDŹ DO SCENARIUSZA/giu;
function semanticClass(text) {{
  for (const [name, pattern] of Object.entries(semanticPatterns)) {{
    pattern.lastIndex = 0;
    if (pattern.test(text)) return 'signal signal-' + name;
  }}
  return 'signal';
}}
function applySemanticHighlights() {{
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {{
    acceptNode(node) {{
      if (!node.nodeValue.trim() || node.parentElement.closest('script,style,code,pre,.signal,.deadline-critical,.deadline-target,.screen-dialog')) return NodeFilter.FILTER_REJECT;
      semanticPattern.lastIndex = 0;
      return semanticPattern.test(node.nodeValue) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
    }}
  }});
  const nodes = [];
  while (walker.nextNode()) nodes.push(walker.currentNode);
  nodes.forEach(node => {{
    const fragment = document.createDocumentFragment();
    let cursor = 0;
    semanticPattern.lastIndex = 0;
    for (const match of node.nodeValue.matchAll(semanticPattern)) {{
      fragment.append(node.nodeValue.slice(cursor, match.index));
      const span = document.createElement('span');
      span.className = semanticClass(match[0]);
      span.textContent = match[0];
      fragment.append(span);
      cursor = match.index + match[0].length;
    }}
    fragment.append(node.nodeValue.slice(cursor));
    node.replaceWith(fragment);
  }});
}}
function setupScreenViewer() {{
  const dialog = document.getElementById('screen-dialog');
  const fullImage = dialog.querySelector('img');
  const caption = dialog.querySelector('p');
  function openScreen(image) {{
    fullImage.src = image.src;
    fullImage.alt = image.alt;
    caption.textContent = image.alt;
    if (dialog.showModal) dialog.showModal(); else dialog.setAttribute('open', '');
  }}
  document.addEventListener('click', event => {{
    const image = event.target.closest('figure.shot img');
    if (image) openScreen(image);
  }});
  document.addEventListener('keydown', event => {{
    const image = event.target.closest && event.target.closest('figure.shot img');
    if (image && (event.key === 'Enter' || event.key === ' ')) {{
      event.preventDefault();
      openScreen(image);
    }}
  }});
  dialog.querySelector('button').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => {{ if (event.target === dialog) dialog.close(); }});
}}
applySemanticHighlights();
setupScreenViewer();
function showScreenMode() {{
  document.querySelectorAll('details').forEach(item => {{ item.open = item.classList.contains('screen-gallery'); }});
}}

let printDetailState = null;
function openDetailsForPrint() {{
  if (printDetailState === null) {{
    printDetailState = Array.from(document.querySelectorAll('details'), item => item.open);
  }}
  document.querySelectorAll('details').forEach(item => {{ item.open = true; }});
  document.querySelectorAll('img[loading="lazy"]').forEach(img => {{ img.loading = 'eager'; }});
}}
function restoreDetailsAfterPrint() {{
  if (printDetailState === null) return;
  document.querySelectorAll('details').forEach((item, index) => {{ item.open = printDetailState[index]; }});
  printDetailState = null;
}}
async function printProcedure() {{
  openDetailsForPrint();
  const images = Array.from(document.images);
  await Promise.allSettled(images.map(img => img.decode ? img.decode() : Promise.resolve()));
  window.print();
}}
window.addEventListener('beforeprint', openDetailsForPrint);
window.addEventListener('afterprint', restoreDetailsAfterPrint);
</script>
</main></div></body></html>"""

# Fragmenty archiwalne mogą zawierać wcięte puste wiersze; wynik ma przechodzić
# kontrolę whitespace bez modyfikowania widocznej treści.
doc = re.sub(r'[ \t]+(?=\n)', '', doc)

# Chroń osadzone dane binarne przed normalizacją tekstu i linków. Zwykłe zamiany
# napisów mogłyby przypadkowo trafić w ciąg base64 i uszkodzić obraz.
_embedded_sources = []
def _protect_asset(match):
    _embedded_sources.append(match.group(1))
    return f'src="__EMBEDDED_ASSET_{len(_embedded_sources) - 1}__"'
doc = re.sub(r'src="(data:[^"]+)"', _protect_asset, doc, flags=re.I)

doc = denumber(doc)
doc = re.sub(r'Happy\s+Day', 'Stan poprawny / nominalny', doc)
doc = re.sub(r'(?i)bra\s+diostepu', 'brak dostępu', doc)

# Nazwy dokumentów źródłowych nie są odsyłaczami dla dyspozytora — ich treść jest już
# scalona powyżej. Pozostają wyłącznie nazwy plików operacyjnych, które faktycznie trzeba obsłużyć.
for old, new in {
    'Dane referencyjne do ręcznej obsługi plików (źródło: QuickRef / Procedura skrócona v4.1, HLBP CCCt 4.2).':
        'Dane operacyjne do ręcznej obsługi plików — komplet masek, numerów i ścieżek.',
    'Operacyjna esencja dyżuru wg Procedury skróconej v4.1 i QuickRef (HLBP CCCt 4.2 v1).':
        'Operacyjna sekwencja dyżuru — warunki wstępne i kolejne punkty kontrolne.',
    'AC manuall ZP.docx': 'instrukcja obsługi ZP (treść włączona do tej procedury)',
    'PDF: Instrukcja Użytkownika obsługującego proces ID': 'Ekran instruktażowy obsługi procesu ID',
    'CCM Instrukcja Użytkownika': 'instrukcja obsługi CCM',
    'Core CC Tool Operator Manual 4.1': 'instrukcja obsługi Core CC Tool',
    'PROCEDURA_IDCC_TSO_v5_2': 'wcześniejszy materiał operacyjny',
}.items():
    doc = doc.replace(old, new)

# Rozstrzygnięcie dawnych notatek roboczych. Niepewne działania zastępujemy bezpieczną,
# zamkniętą ścieżką operacyjną zamiast pozostawiać pytania do innych dokumentów.
doc = doc.replace(
    '<em>(❓ dokładna ścieżka — do weryfikacji w CCM Instrukcji Dyspozytora v2.6, rozdz. „Zmiana statusu dokumentu na wysłany ręcznie")</em>',
    '<span class="note">Pełna sekwencja i ekrany: <a href="#ccm-c5">C.5 — status ręczny i wysyłka po CET</a>.</span>')
doc = doc.replace('<em>(❓ do weryfikacji dla IDCC — patrz TODO)</em>',
                  '<span class="note">Katalog operacyjny IDCC.</span>')
doc = doc.replace('<em>(❓ do weryfikacji dla IDCC)</em>',
                  '<span class="note">Katalog operacyjny IDCC.</span>')
doc = doc.replace(
    'Pobierz IVA z <code>perun/</code> → ręcznie skopiuj/wgraj do <code>cca/</code> <em>(❓ czy dozwolone — do weryfikacji)</em>',
    'Nie kopiuj plików ręcznie między bucketami bez zgody zespołu utrzymania. Wyślij IVA ręcznie przez CCM jako Backup i zgłoś incydent przez CIZ/WPO/PSE-I')
doc = doc.replace('tymczasowo ręczne kopiowanie <em>(❓)</em>',
                  'bez ręcznego kopiowania między bucketami → wysyłka przez CCM + zgłoszenie CIZ/WPO/PSE-I')
doc = doc.replace('<em>(❓ kanał kontaktu — patrz TODO)</em>',
                  '<strong>— zgłoszenie przez CIZ/WPO/PSE-I</strong>')
doc = doc.replace(
    '<strong>Dostarczenie computed AACs do XBID</strong> przez narzędzie lokalne <em>(❓ jakie narzędzie konkretnie — do weryfikacji)</em>',
    '<strong>Brak AAC:</strong> nie wysyłaj danych samodzielnie nieuzgodnionym narzędziem. Zadzwoń do CCC, zgłoś incydent przez CIZ/WPO/PSE-I, wykonaj uzgodnione polecenie stanowiskowe i potwierdź realizację mailowo')
doc = re.sub(
    r'<tr>\s*<td><code>mam/</code></td>\s*<td>\(do uzupełnienia\)</td>\s*<td>❓.*?</td>\s*<td>—</td>\s*</tr>',
    '<tr><td><code>mam/</code></td><td>Poza zakresem operacji IDCC</td>'
    '<td>Nie wykonuj operacji w tym buckecie; każde wskazanie tej lokalizacji zgłoś przez CIZ/WPO/PSE-I.</td>'
    '<td>Brak czynności dyspozytora</td></tr>', doc, flags=re.S)
doc = re.sub(
    r'<code>\\\\uo-data\\ZUO\\Pion_UOD\\Wydzial_DP\\MODELE\\5_DYSP\\FBA\\Pliki wejściowe do DA FBA\\rrrMMdd\\PERUN\\</code>\s*<em>\(BUP DA\)</em>\s*<em>\(❓ analogiczna ścieżka dla IDCC — do weryfikacji\)</em>',
    lambda _: (r'<code>\\uo-data\ZUO\Pion_UOD\Wydzial_DP\MODELE\5_DYSP\FBA\Pliki wejściowe do ID FBA\rrrMMdd\PERUN\</code> '
               r'<em>(BUP DA)</em>'),
    doc)

# Nazwy i numery stron materiałów źródłowych są zbędne — właściwe instrukcje i ekrany
# są już w procedurze. Zachowujemy znaczenie operacyjne, usuwamy metadane redakcyjne.
doc = re.sub(r'<blockquote>\s*<p>📖.*?</p>\s*</blockquote>', '', doc, flags=re.S)
doc = re.sub(r'<strong>Źródło:</strong>.*?(?=<strong>U-kod:</strong>)', '', doc, flags=re.S)
doc = re.sub(r'📷\s*CCM Instrukcja v2\.6,\s*(?:Rys\.\s*[\d–-]+|sekcja „[^”]+”)\s*—\s*',
             '📷 Ekran w <a href="#sec-ccm">sekcji Czynności w CCM</a> — ', doc)
doc = re.sub(r'<em>CCM Instrukcja v2\.6,.*?</em>',
             '<a href="#sec-ccm">Odpowiedni ekran znajduje się w sekcji Czynności w CCM</a>',
             doc, flags=re.S)
doc = re.sub(r'<em>PDF Dyspozytora v2\.6,\s*s\.\s*\d+\s*—\s*.*?</em>',
             '<a href="#sec-ccm">Odpowiedni ekran i status znajdują się w sekcji Czynności w CCM</a>',
             doc, flags=re.S)
doc = re.sub(r'instrukcja IDCC_bcd v4\.1 official', 'tabela wartości operacyjnych w tej sekcji', doc, flags=re.I)
doc = doc.replace('szczegółowe timingi w źródle harmonogram operacyjny.',
                  'wariant pominięto w harmonogramie dyżurowym.')
doc = doc.replace('Korekty względem draftu harmonogram operacyjny', 'Obowiązujące wartości operacyjne')
doc = doc.replace('między draftem harmonogram operacyjny a wartościami operacyjnymi',
                  'między wartościami pomocniczymi a tabelą zbiorczą')
doc = doc.replace('Procedury skróconej v4.1', 'niniejszej procedury')
doc = doc.replace('instrukcji v4.1', 'tabeli wartości operacyjnych')
# Zachowaj techniczną nazwę instrukcji FBA_TSO_BUP_03 oraz jej wersję.
doc = doc.replace('Pełna instrukcja narzędzia: IDCF_InstrUżytk_v5',
                  'Pełna instrukcja narzędzia znajduje się w <a href="#sec-kreator">sekcji Kreator IDCF</a>')
doc = re.sub(r'<li><strong>Pełna instrukcja narzędzia:</strong>\s*<code>IDCF_InstrUżytk_v5</code>.*?</li>',
             '<li><strong>Instrukcja narzędzia:</strong> wykonaj kroki i skorzystaj z ekranów w '
             '<a href="#sec-kreator">sekcji Kreator IDCF i AC w ZP</a>.</li>', doc, flags=re.S)
doc = re.sub(r'<em>BUP DA Rys\. dla Ryzyka 9 \(\)</em>',
             '<a href="#sec-walidacja">Ekrany BUP DA w Perun4V znajdują się w sekcji Walidacja FBA</a>', doc)
doc = doc.replace('Dla pełnych kart ryzyk patrz rozdział 9.',
                  'Pełne karty ryzyk znajdują się w <a href="#sec-ryzyka">sekcji Ryzyka R01–R29</a>.')
# BUP DA i NOR DA są technicznymi nazwami trybów i pozostają bez zmian.
doc = re.sub(r'HTML\s*§\s*[\d.]+(?:\s*R\d+)?', 'odpowiednia sekcja tej procedury', doc)
doc = re.sub(r'\bRys\.\s*\d+(?:[–-]\d+)?', 'ekran w tej procedurze', doc)
doc = re.sub(r',?\s*str\.\s*\d+(?:[–-]\d+)?', '', doc)
doc = re.sub(r'§Ryzyko\s*\d+', 'scenariusz ryzyka', doc)

doc = re.sub(r'\bCore IDCC BPD(?: v\d+(?:\.\d+)*)?\b', 'opis procesu IDCC', doc)
doc = re.sub(r'\bHLBP(?: CCCt)?(?: \d+(?:\.\d+)*(?: v\d+)?)?\b', 'harmonogram operacyjny', doc)
doc = re.sub(r'\bQuickRef\b', 'zestawienie operacyjne', doc)
doc = re.sub(r'\bProcedura skrócona v4\.1\b', 'niniejsza procedura', doc)
doc = doc.replace('(wg Confluence)', '(kroki obowiązujące w tej procedurze)')
doc = doc.replace('Confluence', 'niniejsza procedura')
doc = doc.replace('wg BPD', 'zgodnie z opisem procesu')
doc = doc.replace('w BPD', 'w opisie procesu')
doc = doc.replace('z BPD', 'z opisu procesu')
doc = doc.replace('BPD', 'opis procesu')
doc = doc.replace('Core ID CCM 6th RfA', 'zasady monitorowania CCM')
# Ujednolicenie widocznego rozwinięcia GLSK zgodnie z nazewnictwem operacyjnym.
doc = doc.replace('Generation Load Shift Keys', 'Generation and Load Shift Keys')
doc = doc.replace('Generation Load Shift Key', 'Generation and Load Shift Keys')
doc = doc.replace('Harmonogram harmonogram operacyjny (CCCt 4.2) — bramki czasowe',
                  'Harmonogram operacyjny — bramki czasowe')
doc = doc.replace(
    'Fazy procesu i bramki istotne dla PSE, wyciąg z harmonogram operacyjny draft timings CCCt 4.2 v1. '
    'Wiersze podświetlone = fazy główne; pozostałe = bramki, w których działa lub które monitoruje PSE. '
    'Wartości operacyjne skorygowane wg tabeli wartości operacyjnych — patrz tabela zbiorcza i ramka korekt.',
    'Fazy procesu i bramki istotne dla PSE. Wiersze podświetlone oznaczają fazy główne; pozostałe wskazują '
    'bramki, w których działa lub które monitoruje PSE. Obowiązujące wartości zawiera tabela zbiorcza poniżej.')
doc = re.sub(
    r'<p style="font-size:12px;color:var\(--pse-gray\);text-align:center;margin-top:32px;">\s*'
    r'FBA_TSO_IDCC · Wersja 5\.1.*?</p>',
    '<p class="note">Checklista dyżurowa jest integralną częścią wydania v7. Wszystkie czynności ręczne '
    'należy odnotować w dokumentacji dyżurowej.</p>', doc, flags=re.S)
doc = doc.replace('szczegółowe timingi w źródle harmonogram operacyjny.',
                  'wariant pominięto w harmonogramie dyżurowym.')
doc = doc.replace('Korekty względem draftu harmonogram operacyjny', 'Obowiązujące wartości operacyjne')
doc = doc.replace('między draftem harmonogram operacyjny a wartościami operacyjnymi',
                  'między wartościami pomocniczymi a tabelą zbiorczą')
doc = re.sub(r'<em>BUP DA Rys\. dla Ryzyka 9 \(\)</em>',
             '<a href="#sec-walidacja">Ekrany BUP DA w Perun4V znajdują się w sekcji Walidacja FBA</a>', doc)
# Ujednolicenie historycznych kotwic ze scalonych fragmentów.
doc = re.sub(r'href="#r(\d{2})"', lambda m: f'href="#R{m.group(1)}"', doc)
doc = doc.replace('href="#s3"', 'href="#sec-proces"')
doc = doc.replace('href="Procedura_KreatorIDCF_GLSK_CBCORA.html"', 'href="#sec-kreator"')
doc = doc.replace(
    'Pełną procedurę obsługi Kreatora IDCF zawiera <a href="#sec-kreator">Procedura_KreatorIDCF_GLSK_CBCORA.html</a>.',
    'Pełne kroki obsługi wraz z ekranami znajdują się w <a href="#sec-kreator">sekcji Kreator IDCF i AC w ZP</a>.')
doc = doc.replace(' (np. w <code>Przyklady_FID1-831.md</code>)', '')
doc = re.sub(r'href="Inwentarz_IDCC\.md#([^"]+)"', r'href="#\1"', doc)
doc = re.sub(r'href="Karta_ryzyk_IDCC\.md#([^"]+)"', r'href="#\1"', doc)
doc = doc.replace('href="Karta_ryzyk_IDCC.md"', 'href="#sec-ryzyka"')
doc = doc.replace('Karta_ryzyk_IDCC.md', 'baza ryzyk w tej procedurze')

# Czytelne role operacyjne w całej procedurze; szablony maili pozostają bez zmian.
doc = doc.replace('telefon do CCC', 'telefon do operatora procesu Capacity Calculation')
doc = doc.replace('Telefon do CCC', 'Telefon do operatora procesu Capacity Calculation')
doc = doc.replace('poinformuj telefonicznie CCC', 'poinformuj telefonicznie operatora procesu Capacity Calculation')
doc = doc.replace('poinformuj CCC', 'poinformuj operatora procesu Capacity Calculation')
doc = doc.replace('czekaj na instrukcje CCC', 'czekaj na instrukcję operatora procesu Capacity Calculation')
doc = doc.replace('USY/CCC', 'Helpdesk CCC')
doc = doc.replace('przekazuje wejścia', 'wysyła pliki wejściowe')
doc = doc.replace('potwierdza obecność danych do CCC', 'potwierdza obecność danych operatorowi procesu Capacity Calculation')
doc = doc.replace('potwierdza obecność AAC do CCC', 'potwierdza obecność AAC operatorowi procesu Capacity Calculation')
doc = doc.replace('potwierdzają wynik do CCC', 'potwierdzają wynik operatorowi procesu Capacity Calculation')

def preserve_operational_naming(text):
    """Zachowuje angielskie nazwy procesów i skróty; rozwija tylko polskie oznaczenia redakcyjne."""
    text = re.sub(r'(?<!Ryzyko )\bR(\d{2})\b', r'Ryzyko R\1', text)
    text = re.sub(r'(?<!Procedura )\bP(\d{2})\b', r'Procedura P\1', text)
    text = re.sub(r'(?<!Ryzyko pomocnicze )\bU(\d{2})\b', r'Ryzyko pomocnicze U\1', text)
    text = re.sub(r'\bPPM\b', 'prawy przycisk myszy', text, flags=re.I)
    text = re.sub(r'\bLPM\b', 'lewy przycisk myszy', text, flags=re.I)
    text = re.sub(r'Ryzyka\s+Ryzyko\s+R(\d{2})[–-]Ryzyko\s+R(\d{2})', r'Ryzyka R\1–R\2', text)
    text = re.sub(r'Ryzyko\s+R(\d{2})[–-]Ryzyko\s+R(\d{2})', r'Ryzyka R\1–R\2', text)
    text = re.sub(r'Procedury\s+Procedura\s+P(\d{2})[–-]Procedura\s+P(\d{2})', r'Procedury P\1–P\2', text)
    text = re.sub(r'Procedura\s+P(\d{2})[–-]Procedura\s+P(\d{2})', r'Procedury P\1–P\2', text)
    return text.replace('Ryzyko Ryzyko ', 'Ryzyko ').replace('Procedura Procedura ', 'Procedura ')

def preserve_visible_operational_terms(html_doc):
    protected = []
    block_pattern = re.compile(
        r'<(?P<tag>code|pre|script|style)\b[^>]*>.*?</(?P=tag)>|'
        r'<(?P<special_tag>[a-z][\w:-]*)\b[^>]*class="[^"]*\b(?:mailbody|path)\b[^"]*"[^>]*>'
        r'.*?</(?P=special_tag)>|'
        r'<h4>\s*\d{2}\s+—.*?</h4>|'
        r'<table\b[^>]*class="[^"]*\bref\b[^"]*"[^>]*>'
        r'(?:(?!</table>).)*?<th>Subject</th>(?:(?!</table>).)*?</table>|'
        r'https?://[^\s<>"\']+|'
        r'\b[\w.+-]+@[\w.-]+\.[a-z]{2,}\b|'
        r'(?<![\w./-])[\w./-]+\.(?:xml|zip|json|csv|xlsx?|docx?|pdf|html?|md|txt)\b|'
        r'\bIDCC\s+\(do 3C\)\s+z\s+ATC\s+i\s+SFTP(?:\s+Pulpit dyspozytorski)?\b|'
        r'\bIDCC\s+FB(?:\s+Pulpit dyspozytorski)?\b|'
        r'\bIDCC\([a-e]\)(?:\s*[–-]\s*(?:IDCC)?\([a-e]\))?',
        re.I | re.S)
    def protect(match):
        protected.append(match.group(0))
        return f'__PROTECTED_TEXT_{len(protected) - 1}__'
    work = block_pattern.sub(protect, html_doc)
    parts = re.split(r'(<[^>]+>)', work)
    work = ''.join(part if part.startswith('<') else preserve_operational_naming(part) for part in parts)
    work = re.sub(
        r'\b(alt|aria-label)="([^"]*)"',
        lambda m: f'{m.group(1)}="{preserve_operational_naming(m.group(2))}"', work)
    for index, block in enumerate(protected):
        work = work.replace(f'__PROTECTED_TEXT_{index}__', block)
    return work

doc = preserve_visible_operational_terms(doc)


def formalize_procedural_language(segment):
    """Nadaje instrukcjom formę „należy”, chroniąc kody, ścieżki i nazwy poleceń UI."""
    protected = []
    block_re = re.compile(
        r'<(?P<tag>code|pre|script|style)\b[^>]*>.*?</(?P=tag)>|'
        r'<(?P<ui_tag>strong|b)\b[^>]*>\s*'
        r'(?:Wyślij(?: po CET| do CCTool)?|Status ręczny|Ustaw status ręcznie|'
        r'Przywróć poprzedni status|Informacje|Pobierz(?: XML)?|Nowa wersja|'
        r'Manual Upload|Upload file|Apply|Local Login|Message Viewer)\s*</(?P=ui_tag)>|'
        r'<(?P<special>[a-z][\w:-]*)\b[^>]*class="[^"]*\b(?:mailbody|path)\b[^"]*"[^>]*>'
        r'.*?</(?P=special)>|'
        r'(?P<ui>(?:prawy|lewy) przycisk myszy'
        r'(?:\s+na\s+[^<→\n]{1,100})?\s*→\s*'
        r'(?:Wyślij(?: po CET| do CCTool)?|Status ręczny|Ustaw status ręcznie|'
        r'Przywróć poprzedni status|Informacje|Pobierz(?: XML)?))',
        re.I | re.S)

    def protect(match):
        protected.append(match.group(0))
        return f'__FORMAL_BLOCK_{len(protected) - 1}__'

    work = block_re.sub(protect, segment)

    # Powtarzalne sekwencje wieloczasownikowe są redagowane jako całe zdania.
    work = re.sub(
        r'\bpobierz/wygeneruj\s+(?:plik\s+)?ręcznie ze źródła i wgraj(?: ręcznie)?\s+'
        r'przez Manual Upload \(GUI Core CC Tool\)\s*/\s*wyślij z CCM(?: \(Wyślij\))?',
        'plik należy pobrać lub wygenerować ręcznie ze źródła, a następnie wgrać przez '
        'Manual Upload (GUI Core CC Tool) lub wysłać z CCM',
        work, flags=re.I)
    work = re.sub(
        r'\bpobierz/wygeneruj ręcznie i wgraj przez Manual Upload \(GUI Core CC Tool\)',
        'plik należy pobrać lub wygenerować ręcznie, a następnie wgrać przez '
        'Manual Upload (GUI Core CC Tool)',
        work, flags=re.I)
    work = re.sub(
        r'\bOtwórz aplikacji ZP,\s*przejdź do bilansu i sprawdź wersję pliku:',
        'Należy otworzyć aplikację ZP, przejść do bilansu i sprawdzić wersję pliku:',
        work, flags=re.I)
    work = re.sub(
        r'\bUstaw\s*/\s*przywróć status ręczny R\b',
        'Należy ustawić lub przywrócić status ręczny R', work, flags=re.I)

    replacements = {
        'sprawdź': 'należy sprawdzić', 'pobierz': 'należy pobrać',
        'wyślij': 'należy wysłać', 'wybierz': 'należy wybrać',
        'zgłoś': 'należy zgłosić', 'otwórz': 'należy otworzyć',
        'ustaw': 'należy ustawić', 'kliknij': 'należy kliknąć',
        'monitoruj': 'należy monitorować', 'zadzwoń': 'należy zadzwonić',
        'poinformuj': 'należy poinformować', 'potwierdź': 'należy potwierdzić',
        'zweryfikuj': 'należy zweryfikować', 'uruchom': 'należy uruchomić',
        'przejdź': 'należy przejść', 'odczytaj': 'należy odczytać',
        'wczytaj': 'należy wczytać', 'spróbuj': 'należy spróbować',
        'wykorzystaj': 'należy wykorzystać', 'wykonaj': 'należy wykonać',
        'czekaj': 'należy odczekać', 'oceń': 'należy ocenić',
        'wgraj': 'należy wgrać', 'wygeneruj': 'należy wygenerować',
        'popraw': 'należy poprawić', 'ponów': 'należy ponowić',
        'zapisz': 'należy zapisać', 'porównaj': 'należy porównać',
        'skontaktuj': 'należy skontaktować', 'odśwież': 'należy odświeżyć',
        'zaloguj': 'należy zalogować', 'upewnij': 'należy upewnić',
        'użyj': 'należy użyć', 'rozwiń': 'należy rozwinąć',
        'zidentyfikuj': 'należy zidentyfikować', 'wprowadź': 'należy wprowadzić',
        'zaznacz': 'należy zaznaczyć', 'przeciągnij': 'należy przeciągnąć',
        'dodaj': 'należy dodać', 'usuń': 'należy usunąć',
        'cofnij': 'należy cofnąć', 'odnotuj': 'należy odnotować',
        'eskaluj': 'należy eskalować', 'zastosuj': 'należy zastosować',
    }
    parts = re.split(r'(<[^>]+>)', work)
    pattern = re.compile(
        r'(?P<prefix>^\s*|[.!?;:]\s+|→\s*)'
        r'(?P<verb>' + '|'.join(map(re.escape, replacements)) + r')\b',
        re.I)

    def replace_verb(match):
        replacement = replacements[match.group('verb').lower()]
        if match.group('verb')[0].isupper():
            replacement = replacement[0].upper() + replacement[1:]
        return match.group('prefix') + replacement

    work = ''.join(
        part if part.startswith('<') else pattern.sub(replace_verb, part)
        for part in parts)
    for index, block in enumerate(protected):
        work = work.replace(f'__FORMAL_BLOCK_{index}__', block)
    return work


# Szablony wiadomości są materiałem normatywnym w języku angielskim i nie podlegają
# redakcji; forma „należy” obejmuje pozostałe sekcje proceduralne.
_formal_mail_start = doc.find('<section id="sec-mail"')
_formal_mail_end = doc.find('</section>', _formal_mail_start) + len('</section>')
doc = (formalize_procedural_language(doc[:_formal_mail_start])
       + doc[_formal_mail_start:_formal_mail_end]
       + formalize_procedural_language(doc[_formal_mail_end:]))


def normalize_operational_terms(segment):
    """Ujednolica terminologię operacyjną bez naruszania nazw technicznych."""
    protected_monitoring = '__CAPACITY_CALCULATION_MONITORING__'
    segment = segment.replace('Capacity Calculation Monitoring', protected_monitoring)
    segment = re.sub(
        r'\bwymaga eskalacji do\b',
        'wymaga powiadomienia', segment, flags=re.I)
    segment = re.sub(
        r'\bEskalacja\b',
        lambda match: 'Powiadomienie' if match.group(0)[0].isupper() else 'powiadomienie',
        segment, flags=re.I)
    segment = re.sub(
        r'\bAAC Fallback\s+—',
        'Działanie backupowe AAC —', segment, flags=re.I)
    segment = re.sub(
        r'\bAAC Fallback\b',
        'działanie backupowe AAC', segment, flags=re.I)
    segment = re.sub(
        r'\bfallback gdy walidacja zawiodła\b',
        'działanie backupowe po niepowodzeniu walidacji', segment, flags=re.I)
    segment = re.sub(
        r'\b(?:przez lokalne narzędzie|przez narzędzie lokalne)\b',
        'przez ZP', segment, flags=re.I)
    segment = re.sub(
        r'\bMonitoring\b', 'Monitorowanie', segment)
    segment = re.sub(
        r'\bmonitoring\b', 'monitorowanie', segment)
    segment = re.sub(
        r'\bTryb backup\b', 'Tryb backupowy', segment)
    segment = re.sub(
        r'\btryb backup\b', 'tryb backupowy', segment)
    return segment.replace(protected_monitoring, 'Capacity Calculation Monitoring')


def normalize_procedure_components(segment):
    """Ujednolica etykiety i wizualnie oddziela decyzje od zwykłych punktorów."""
    label_replacements = {
        '<strong>Warunek:</strong>': '<strong>Przyczyna:</strong>',
        '<strong>Termin:</strong>': '<strong>Czas:</strong>',
        '<strong>Terminy:</strong>': '<strong>Czas:</strong>',
        '<strong>Termin AC:</strong>': '<strong>Termin dostarczenia pliku:</strong>',
        '<strong>Termin pliku:</strong>': '<strong>Termin dostarczenia pliku:</strong>',
    }
    for old, new in label_replacements.items():
        segment = segment.replace(old, new)

    def add_class(match):
        attrs = match.group('attrs')
        label = re.sub(r'\s+', ' ', match.group('label')).strip()
        if label.startswith('Działanie PSE'):
            component_class = 'pse-action'
        elif label.startswith(('Działanie backupowe', 'Działania backupowe', 'IVA BACKUP')):
            component_class = 'backup-action'
        elif label == 'Przyczyna':
            component_class = 'procedure-fact fact-cause'
        elif label == 'Czas':
            component_class = 'procedure-fact fact-time'
        else:
            component_class = 'procedure-fact fact-file'
        class_match = re.search(r'\bclass="([^"]*)"', attrs)
        if class_match:
            existing = class_match.group(1).split()
            additions = [name for name in component_class.split() if name not in existing]
            if additions:
                attrs = (attrs[:class_match.start(1)]
                         + class_match.group(1) + ' ' + ' '.join(additions)
                         + attrs[class_match.end(1):])
        else:
            attrs += f' class="{component_class}"'
        return f'<li{attrs}><strong>{label}:</strong>'

    return re.sub(
        r'<li(?P<attrs>[^>]*)>\s*<strong>(?P<label>'
        r'Działanie PSE|Działanie backupowe[^:<]*|Działania backupowe|IVA BACKUP|'
        r'Przyczyna|Czas|Termin dostarczenia pliku[^:<]*)\s*:</strong>',
        add_class, segment, flags=re.I)


# Szablony wiadomości są chronione także przed normalizacją terminologii i komponentów.
_terms_mail_start = doc.find('<section id="sec-mail"')
_terms_mail_end = doc.find('</section>', _terms_mail_start) + len('</section>')
doc = (normalize_procedure_components(normalize_operational_terms(doc[:_terms_mail_start]))
       + doc[_terms_mail_start:_terms_mail_end]
       + normalize_procedure_components(normalize_operational_terms(doc[_terms_mail_end:])))


def highlight_deadlines(segment):
    """Oznacza widoczne TET i CET wraz z godziną spójnymi ramkami terminów."""
    protected = []
    block_re = re.compile(
        r'<(?P<tag>code|pre|script|style)\b[^>]*>.*?</(?P=tag)>|'
        r'<(?P<marked>[a-z][\w:-]*)\b[^>]*class="[^"]*\bdeadline-(?:target|critical)\b[^"]*"[^>]*>'
        r'.*?</(?P=marked)>',
        re.I | re.S)

    def protect(match):
        protected.append(match.group(0))
        return f'__DEADLINE_BLOCK_{len(protected) - 1}__'

    def mark(match):
        deadline_class = 'deadline-target' if match.group(1).upper() == 'TET' else 'deadline-critical'
        return f'<span class="{deadline_class}">{match.group(0)}</span>'

    work = block_re.sub(protect, segment)
    parts = re.split(r'(<[^>]+>)', work)
    work = ''.join(
        part if part.startswith('<') else re.sub(
            r'\b(TET|CET)(?:\s+\d{1,2}:\d{2})?', mark, part, flags=re.I)
        for part in parts)
    for index, block in enumerate(protected):
        work = work.replace(f'__DEADLINE_BLOCK_{index}__', block)
    return work


# Treść normatywna szablonów wiadomości pozostaje bez zmian.
_deadline_mail_start = doc.find('<section id="sec-mail"')
_deadline_mail_end = doc.find('</section>', _deadline_mail_start) + len('</section>')
doc = (highlight_deadlines(doc[:_deadline_mail_start])
       + doc[_deadline_mail_start:_deadline_mail_end]
       + highlight_deadlines(doc[_deadline_mail_end:]))


def _heading_text(markup):
    """Zwraca krótki, widoczny tytuł najbliższej sekcji do podpisu tabeli."""
    text = html.unescape(re.sub(r'<[^>]+>', ' ', markup))
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'^\d+\s+', '', text)
    return text or 'Zestawienie danych operacyjnych'


def _number_table_segment(segment, start_number=1):
    """Numeruje tabele i nadaje stabilny klucz oparty na sekcji i indeksie lokalnym."""
    token_re = re.compile(
        r'(?P<section><section\b[^>]*\bid="([^"]+)"[^>]*>)|'
        r'(?P<heading><h[2-5]\b[^>]*>.*?</h[2-5]>)|'
        r'(?P<table><table\b[^>]*>)',
        re.I | re.S)
    output, cursor, number = [], 0, start_number
    current_heading = 'Metryka dokumentu'
    current_section = 'front'
    local_counts = defaultdict(int)
    for match in token_re.finditer(segment):
        output.append(segment[cursor:match.start()])
        token = match.group(0)
        if match.group('section'):
            current_section = match.group(2)
            output.append(token)
        elif match.group('heading'):
            current_heading = _heading_text(token)
            output.append(token)
        else:
            local_counts[current_section] += 1
            table_key = f'{current_section}-table-{local_counts[current_section]}'
            if 'data-table-number=' not in token:
                token = (token[:-1] + f' data-table-number="{number}" '
                         f'data-table-key="{table_key}" '
                         f'aria-label="Tabela {number}. {esc(current_heading)}">')
            output.append(token)
            number += 1
        cursor = match.end()
    output.append(segment[cursor:])
    return ''.join(output), number


def _number_mail_tables(segment, start_number):
    """Opisuje tabele szablonów atrybutami, nie zmieniając ich normatywnej treści."""
    number = start_number
    local_index = 0

    def annotate(match):
        nonlocal number, local_index
        local_index += 1
        token = match.group(0)
        table_key = f'sec-mail-table-{local_index}'
        token = (token[:-1] + f' data-table-number="{number}" '
                 f'data-table-key="{table_key}" '
                 f'aria-label="Tabela {number}. Szablon wiadomości operacyjnej">')
        number += 1
        return token

    return re.sub(r'<table\b[^>]*>', annotate, segment, flags=re.I), number, local_index


# Wszystkie tabele otrzymują ciągły numer, stabilny klucz i etykietę dostępną
# dla technologii asystujących. Numeracja nie dodaje widocznych podpisów, dzięki
# czemu tabele zachowują wcześniejszy, jednolity styl graficzny. Treść 19 wzorców
# wiadomości pozostaje bez zmian.
_mail_section_start = doc.find('<section id="sec-mail"')
_mail_section_end = doc.find('</section>', _mail_section_start) + len('</section>')
assert _mail_section_start >= 0 and _mail_section_end > _mail_section_start, (
    'Nie można wydzielić sekcji szablonów wiadomości przed numeracją tabel')
_doc_before_mail, _next_table_number = _number_table_segment(doc[:_mail_section_start])
_doc_mail, _next_table_number, MAIL_TABLE_COUNT = _number_mail_tables(
    doc[_mail_section_start:_mail_section_end], _next_table_number)
_doc_after_mail, _next_table_number = _number_table_segment(
    doc[_mail_section_end:], _next_table_number)
doc = _doc_before_mail + _doc_mail + _doc_after_mail
NUMBERED_TABLE_COUNT = _next_table_number - 1

def _restore_asset(match):
    return f'src="{_embedded_sources[int(match.group(1))]}"'
doc = re.sub(r'src="__EMBEDDED_ASSET_(\d+)__"', _restore_asset, doc)

# warstwa komentarzy recenzenta (offline, localStorage + eksport JSON/MD)
# Wydanie finalnego składu jest czyste; źródłowy wariant v7 zachowuje recenzowanie.
_cw = (ROOT/'_comments_widget.html')
if INCLUDE_COMMENTS and _cw.exists():
    doc = doc.replace('</body>', _cw.read_text(encoding='utf-8') + '\n</body>')

# ── walidacja kompletności i samowystarczalności ─────────────────────────────
all_ids = re.findall(r'id="([^"]+)"', doc)
ids = set(all_ids)
duplicate_ids = sorted({identifier for identifier in all_ids if all_ids.count(identifier) > 1})
assert not duplicate_ids, f"Powielone identyfikatory HTML: {duplicate_ids}"
missing = [h for _,steps in STICKER_STEPS for _,h in steps if h.lstrip('#') not in ids]
assert not missing, f"Brakujące kotwice stickerów: {missing}"

internal_links = set(re.findall(r'href="#([^"]+)"', doc))
missing_internal = sorted(internal_links - ids)
assert not missing_internal, f"Brakujące kotwice odnośników wewnętrznych: {missing_internal}"

relative_images = re.findall(r'<img\b[^>]*\bsrc="(?!data:)([^"]+)"', doc, re.I)
assert not relative_images, f"Nieosadzone obrazy: {relative_images[:10]}"
embedded_uris = set(re.findall(r'<img\b[^>]*\bsrc="(data:[^"]+)"', doc, re.I))
invalid_uris = []
for uri in embedded_uris:
    try:
        header, payload = uri.split(',', 1)
        assert ';base64' in header
        base64.b64decode(payload, validate=True)
    except Exception as exc:
        invalid_uris.append((uri[:60], str(exc)))
assert not invalid_uris, f"Uszkodzone osadzone obrazy: {invalid_uris[:5]}"
external_resources = re.findall(r'<(?:link|script|img)\b[^>]*(?:href|src)="https?://[^"]+"', doc, re.I)
assert not external_resources, f"Zewnętrzne zasoby sieciowe: {external_resources[:5]}"
document_links = re.findall(r'href="[^"]+\.(?:pdf|docx?|xlsx?|html?|md|txt|csv|json)(?:#[^"]*)?"', doc, re.I)
assert not document_links, f"Odnośniki do innych dokumentów: {document_links[:10]}"

embedded_manifest = set(re.findall(r'data-source="([^"]+)"', doc))
missing_screens = sorted({m['file'] for m in MAN} - embedded_manifest)
assert not missing_screens, f"Screeny z manifestu nieobecne w procedurze: {missing_screens}"

shot_figures = re.findall(r'<figure class="shot"[^>]*>.*?</figure>', doc, re.I | re.S)
assert shot_figures, "Brak pełnowymiarowych figur ze zrzutami ekranu"

def _valid_shot_figure(figure):
    source_match = re.search(r'data-source="([^"]+)"', figure, re.I)
    number_match = re.search(r'data-figure-number="(\d+)"', figure, re.I)
    dimensions_match = re.search(
        r'<img\b[^>]*\bwidth="(\d+)"[^>]*\bheight="(\d+)"', figure, re.I)
    caption_match = re.search(
        r'<span class="caption-text">(.*?)</span>', figure, re.I | re.S)
    if not source_match or not number_match or not dimensions_match or not caption_match:
        return False
    source = html.unescape(source_match.group(1))
    expected = BYFILE.get(source, {}).get('_wh')
    expected_number = FIGURE_NUMBERS.get(source)
    actual = tuple(map(int, dimensions_match.groups()))
    caption = html.unescape(re.sub(r'<[^>]+>', ' ', caption_match.group(1))).strip()
    if (not expected or actual != expected or not caption
            or int(number_match.group(1)) != expected_number):
        return False
    width, height = expected
    return (f'style="--screen-width:{width}px"' in figure
            and f'class="caption-label">Rysunek {expected_number}</span>' in figure
            and 'class="caption-size">'
                f'Oryginalny rozmiar: {width} × {height} pikseli</span>' in figure)

invalid_shot_figures = [
    index for index, figure in enumerate(shot_figures, 1) if not _valid_shot_figure(figure)
]
assert not invalid_shot_figures, (
    f"Figury bez wiarygodnych naturalnych wymiarów lub pełnego podpisu: "
    f"{invalid_shot_figures[:10]}")

figure_pairs = {
    (html.unescape(source), int(number))
    for number, source in re.findall(
        r'<figure class="shot"\s+data-figure-number="(\d+)"[^>]*>.*?data-source="([^"]+)"',
        doc, re.I | re.S)
}
assert len({source for source, _ in figure_pairs}) == 309, (
    'Dokument musi zawierać 309 unikalnych źródeł rysunków')
invalid_figure_numbers = sorted(
    (source, number, FIGURE_NUMBERS.get(source))
    for source, number in figure_pairs
    if FIGURE_NUMBERS.get(source) != number)
assert not invalid_figure_numbers, (
    f'Numeracja rysunków nie odpowiada kolejności manifestu: {invalid_figure_numbers[:10]}')

all_numbered_tables = re.findall(
    r'<table\b[^>]*data-table-number="(\d+)"[^>]*data-table-key="([^"]+)"[^>]*>',
    doc, re.I)
assert len(all_numbered_tables) == NUMBERED_TABLE_COUNT == len(re.findall(r'<table\b', doc, re.I)), (
    f'Nie wszystkie tabele dokumentu otrzymały numer: {len(all_numbered_tables)}/{NUMBERED_TABLE_COUNT}')
assert NUMBERED_TABLE_COUNT == 150, (
    f'Dokument finalny musi zachować dokładnie 150 tabel; wykryto {NUMBERED_TABLE_COUNT}')
assert [int(number) for number, _ in all_numbered_tables] == list(range(1, NUMBERED_TABLE_COUNT + 1)), (
    'Numeracja tabel nie jest ciągła w kolejności dokumentu')
table_keys = [key for _, key in all_numbered_tables]
assert len(table_keys) == len(set(table_keys)), 'Stabilne klucze tabel muszą być unikalne'
non_mail_doc = (doc[:doc.find('<section id="sec-mail"')]
                + doc[doc.find('</section>', doc.find('<section id="sec-mail"')) + len('</section>'):])
non_mail_table_labels = re.findall(
    r'<table\b[^>]*data-table-number="\d+"[^>]*aria-label="Tabela \d+\. [^"]+"',
    non_mail_doc, re.I)
assert len(non_mail_table_labels) == NUMBERED_TABLE_COUNT - MAIL_TABLE_COUNT, (
    'Tabele poza szablonami wiadomości muszą mieć spójne etykiety dostępności')
assert not re.search(r'<caption\b', doc, re.I), (
    'Przywrócony styl graficzny nie używa widocznych podpisów nad tabelami')
_mail_validation_start = doc.find('<section id="sec-mail"')
_mail_validation_end = doc.find('</section>', _mail_validation_start) + len('</section>')
mail_section = doc[_mail_validation_start:_mail_validation_end]
mail_table_numbers = re.findall(
    r'<table\b[^>]*data-table-number="(\d+)"[^>]*data-table-key="sec-mail-table-\d+"',
    mail_section, re.I)
assert len(mail_table_numbers) == MAIL_TABLE_COUNT == 24, (
    'Wszystkie 24 tabele szablonów wiadomości muszą mieć numer i stabilny klucz')

required_document_structure = [
    '<header class="hero">',
    '<span>WYDANIE v7</span>',
    '<details class="gal document-metadata">',
    '<summary>Metryka dokumentu i historia wersji</summary>',
    'Dokument roboczy — niezatwierdzony do formalnego wydania',
    '<strong>Klauzula ogólna dla przebiegu NOR.</strong>',
    'Brak formalnego kodu pary NOR/BUP i daty wydania w przekazanych materiałach.',
    'Pola wymagają uzupełnienia przez właściciela dokumentu przed nadaniem statusu Final.',
    'Wersja 7 jest roboczym identyfikatorem bieżącego, scalonego opracowania.',
    '<h3>1.1 Podsumowanie i cel</h3>',
    '<h3>1.2 Zakres czynności</h3>',
    '<th>Obszar</th><th>Zakres</th>',
    '<th>Formalny kod NOR/BUP</th><td>—</td>',
    'Cały proces IDCC jest procesem automatycznym, jednak nadal wymaga kontroli i nadzoru po stronie dyspozytora.',
    '<strong class="deadline-critical">CET</strong> (ang. <em>Critical End Time</em>)',
]
missing_document_structure = [item for item in required_document_structure if item not in doc]
assert not missing_document_structure, (
    f'Brak wymaganych elementów struktury dokumentu: {missing_document_structure}')
forbidden_formal_graphics = [
    'class="cover-sheet"', 'class="draft-banner"', 'class="cover-meta-grid"',
    'class="cover-block', '<section class="formal-toc"',
]
found_formal_graphics = [item for item in forbidden_formal_graphics if item in doc]
assert not found_formal_graphics, (
    f'Pozostały elementy formalnej oprawy graficznej PSE: {found_formal_graphics}')
if FINAL_LAYOUT:
    assert '<body class="edition-final">' in doc and 'class="hero-visual"' in doc, (
        'Wydanie finalnego składu nie zawiera kompletnej warstwy Mierzony Przepływ')
    assert not INCLUDE_COMMENTS, (
        'Wydanie finalnego składu musi być generowane bez widgetu recenzenckiego')
assert doc.count('<section id="sec-') == len(SECTIONS), (
    'Liczba wyrenderowanych sekcji nie odpowiada centralnemu rejestrowi')
for index, (section_id, title, _, _) in enumerate(SECTIONS, 1):
    number = f'{index:02d}'
    presentation = SECTION_PRESENTATION[section_id]
    expected_opening = (f'<section id="{section_id}" class="procedure-section" '
                        f'data-group="{presentation["group"]}">')
    expected_heading = f'<h2>{esc(title)}</h2>'
    section_start = doc.find(expected_opening)
    section_header_end = doc.find('</header>', section_start)
    section_header_markup = doc[section_start:section_header_end]
    section_header_text = html.unescape(re.sub(r'<[^>]+>', ' ', section_header_markup))
    section_header_text = re.sub(r'\s+', ' ', section_header_text).strip()
    assert (section_start >= 0 and '<h2>' in section_header_markup
            and '<p class="section-summary">' in section_header_markup), (
        f'Niepoprawny nagłówek, kategoria lub opis sekcji: {section_id}')
    assert f'<a href="#{section_id}"><span>{number}</span>{esc(title)}</a>' in nav_html, (
        f'Brak sekcji w automatycznej nawigacji: {section_id}')
for group_code, group_meta in NAV_GROUPS.items():
    nav_heading_id = f'nav-group-{group_code.lower()}'
    assert (f'<section class="nav-group" aria-labelledby="{nav_heading_id}">'
            f'<h3 class="nav-group-heading" id="{nav_heading_id}"><span>{group_code}</span>'
            f'<b>{esc(group_meta["title"])}</b></h3>') in nav_html, (
        f'Brak semantycznej grupy w automatycznej nawigacji: {group_code}')

shot_css_rules = [
    re.sub(r'\s+', '', rule.lower())
    for rule in re.findall(r'figure\.shot img\{([^}]+)\}', doc, re.I | re.S)
]
assert shot_css_rules, "Brak reguły CSS dla pełnowymiarowych zrzutów ekranu"
screen_shot_css = shot_css_rules[0]
required_screen_css = ('width:auto', 'height:auto', 'max-width:100%', 'max-height:none',
                       'margin:0auto', 'object-fit:initial')
missing_screen_css = [
    declaration for declaration in required_screen_css if declaration not in screen_shot_css
]
assert not missing_screen_css, (
    f"Brak ekranowych reguł zachowania proporcji zrzutów: {missing_screen_css}")
assert all('object-fit:cover' not in rule for rule in shot_css_rules), (
    "Pełnowymiarowe zrzuty ekranu nie mogą używać kadrującego object-fit: cover")
all_styles = '\n'.join(re.findall(r'<style\b[^>]*>(.*?)</style>', doc, re.I | re.S))
assert not re.search(r'object-fit\s*:\s*cover\b', all_styles, re.I), (
    "Arkusz stylów nie może zawierać kadrującego object-fit: cover")
print_shot_css = [
    rule for rule in shot_css_rules[1:]
    if all(declaration in rule for declaration in (
        'width:auto', 'height:auto', 'max-width:100%', 'max-height:225mm',
        'margin:0auto', 'object-fit:contain'))
]
assert print_shot_css, (
    "Brak niekadrującej reguły druku mieszczącej wysoki zrzut na stronie A4")

visible_doc = re.sub(r'src="data:[^"]+"', 'src="[embedded]"', doc, flags=re.I)
visible_doc = re.sub(r'<(?:style|script)\b.*?</(?:style|script)>', ' ', visible_doc, flags=re.I | re.S)
visible_doc = html.unescape(re.sub(r'<[^>]+>', ' ', visible_doc))
visible_doc = re.sub(r'\s+', ' ', visible_doc)

required_comment_patterns = [
    '<h3>1.2 Zakres czynności</h3>',
    '<div class="input-stage">',
    'id="ac-publish-flow"',
    '<p class="flow-label"><strong>Przebieg komunikacji przy publikacji pliku:</strong></p>',
    '<div class="flow-node"><strong>ZP</strong><span>przygotowanie AC (FID1-831)</span></div>',
    '<div class="flow-node flow-node-hub"><strong>Connector 2.0</strong><span>transport pliku</span></div>',
    '<div class="flow-node"><strong>Core CC Tool</strong><span>odbiór i walidacja</span></div>',
    'id="igm-rcc-flow"',
    'id="mode-definitions"',
    'id="tet-cet-action"',
    '<div class="process-note-muted">',
    'informuje o dalszych krokach drogą mailową — <a href="#mail-01">wiadomość nr 1</a>',
    'PSE wysyła brakujące DA AAC bezpośrednio do XBID',
    '<span class="deadline-target">TET 13:50</span>',
    'Platforma Udostępniania Transmisyjnych (PuTo)',
    '<table class="ref file-summary file-timings"',
    '<span class="mode-badge mode-auto">FALLBACK AUTOMATYCZNY</span>',
    '<span class="mode-badge mode-backup">DZIAŁANIE BACKUPOWE</span>',
    '<span class="mode-badge mode-process">DZIAŁANIE PROCESOWE</span>',
    'UWAGA: MANDATORY',
    '<div class="pse-action">',
    '<div class="backup-action">',
    '<strong>Przyczyna:</strong>',
    '<strong>Czas:</strong>',
    '<strong>Termin dostarczenia pliku:</strong>',
    '<strong>Czas dostępności wyniku centralnego:</strong>',
    '<li class="iva-extension">',
    'standardowe okno Individual Validation trwa 40 min',
    'PSE nie przedłuża tego okna samodzielnie.',
    '<h3 class="nav-group-heading" id="nav-group-a"><span>A</span><b>Informacje formalne</b></h3>',
    '<h3 class="nav-group-heading" id="nav-group-e"><span>E</span><b>Załączniki i rejestry</b></h3>',
    'class="procedure-section" data-group="C"',
    '<p class="section-summary">',
]
missing_comment_patterns = [pattern for pattern in required_comment_patterns if pattern not in doc]
assert not missing_comment_patterns, (
    f'Brak elementów wymaganych przez nowe komentarze: {missing_comment_patterns}')
required_unified_style = [
    'main ul,main ol{',
    'main ul>li::marker{',
    'main table{width:100%;border-collapse:collapse;',
    'main table th,main table td{',
    'main a:not(.quickcard):not(.mini){',
    '.deadline-target{display:inline-block;',
    '.deadline-critical{display:inline-block;',
    '<ul class="file-list">',
]
missing_unified_style = [pattern for pattern in required_unified_style if pattern not in doc]
assert not missing_unified_style, (
    f'Brak elementów ujednoliconego stylu: {missing_unified_style}')
assert doc.count('<ul class="file-list">') == 2, (
    'We Wstępie pliki dostarczane i monitorowane muszą być zapisane jako dwie listy punktowane')
forbidden_new_graphics = ['input-card-grid', 'class="input-card', 'class="flow-caption"']
found_new_graphics = [item for item in forbidden_new_graphics if item in doc]
assert not found_new_graphics, (
    f'Pozostały niespójne komponenty kart lub podpisów schematów: {found_new_graphics}')
assert doc.count('<div class="input-stage">') == 4, (
    'Każdy z czterech etapów danych wejściowych musi mieć spójne formatowanie')
expected_mail_anchors = {
    f'mail-{number:02d}' for number in (*range(1, 15), *range(16, 21))
}
actual_mail_anchors = set(re.findall(
    r'<span class="mail-anchor" id="(mail-\d{2})"></span>', doc))
assert actual_mail_anchors == expected_mail_anchors, (
    f'Niepoprawny zestaw kotwic 19 wiadomości: {sorted(actual_mail_anchors)}')

operational_markup = re.sub(
    r'<(?:style|script)\b.*?</(?:style|script)>', ' ', non_mail_doc,
    flags=re.I | re.S)
operational_text = html.unescape(re.sub(r'<[^>]+>', ' ', operational_markup))
operational_text = re.sub(r'\s+', ' ', operational_text)
forbidden_comment_phrases = [
    'Działanie operatora procesu Capacity Calculation:',
    'brak lub negatywny ACK — ID1_1',
    'przekazuje mail #1',
    'lokalnym narzędziem',
    'przez lokalne narzędzie',
    'przez narzędzie lokalne',
    'Do końca okna: możliwość aktualizacji EC/ATC',
    'PSE prowadzi walidację przez co najmniej 25 min',
    'Zasada eskalacji',
    'Zarządzane / regulowane przez',
    'Regulowane przez',
    '1.3 Narzędzia i protokoły komunikacyjne',
    'PSE sprawdza poprawność scalenia',
    'AAC Fallback',
    'fallback gdy walidacja zawiodła',
    'Ścieżka:',
]
remaining_comment_phrases = [
    phrase for phrase in forbidden_comment_phrases
    if phrase.lower() in operational_text.lower()
]
assert not remaining_comment_phrases, (
    f'Pozostały frazy wskazane do usunięcia: {remaining_comment_phrases}')
_process_comment_start = doc.find('<section id="sec-proces"')
_process_comment_end = doc.find('</section>', _process_comment_start) + len('</section>')
process_comment_markup = doc[_process_comment_start:_process_comment_end]
assert 'Ścieżka: ZP → Connector 2.0 → Core CC Tool → PuTo' not in process_comment_markup, (
    'Schemat publikacji AC w przeglądzie procesu nie może prowadzić przez PuTo')
assert '<strong>Cel:</strong>' not in process_comment_markup, (
    'Opisy Individual Validation nie mogą powtarzać celu zdefiniowanego w słowniku')
final_ntc_match = re.search(
    r'<h4>Final ID ATC Extraction</h4>(.*?)(?=<h4>)', process_comment_markup, re.S)
assert (final_ntc_match
        and '<strong>Czas dostępności wyniku centralnego:</strong>' in final_ntc_match.group(1)
        and not re.search(
            r'<strong>Termin dostarczenia pliku:</strong>\s*'
            r'<span class="deadline-target">TET 14:45</span>.*?CET 14:55',
            final_ntc_match.group(1), re.S)), (
    'Wynik FID1-921 ma być monitorowany jako wynik centralny, a nie dostarczany przez PSE')
legacy_component_labels = re.findall(
    r'<strong>\s*(?:Warunek|Termin|Terminy|Termin AC|Termin pliku|Termin wyniku centralnego)\s*:</strong>',
    operational_markup, re.I)
assert not legacy_component_labels, (
    f'Pozostały stare etykiety komponentów operacyjnych: {legacy_component_labels[:10]}')
assert doc.count('class="iva-extension"') == 2, (
    'Warunek zachowania minimalnego okna IVA musi być opisany osobno dla IDCC(a) i IDCC(b)–(d)')
assert doc.count('class="pse-action"') >= 5, (
    'Działania PSE nie zostały konsekwentnie wydzielone w osobnych ramkach')
assert doc.count('class="backup-action"') >= 2, (
    'Działania backupowe nie zostały konsekwentnie oddzielone od zwykłych punktorów')
assert 'standardowe okno IVA trwa 40 min' in process_comment_markup, (
    'Brak standardowego czasu 40 min dla IVA w iteracjach IDCC(b)–(d)')
assert process_comment_markup.count('co najmniej 25 min') >= 3, (
    'Opis IVA musi zachowywać gwarantowane minimum 25 min')
assert process_comment_markup.count('nie przedłuża') >= 2, (
    'Opis IVA musi jednoznacznie wskazywać, że PSE nie przedłuża okna samodzielnie')
assert not re.search(r'PSE\s+(?:może|powinno|ma)\s+przedłuż', operational_text, re.I), (
    'Procedura nie może przypisywać PSE samodzielnego przedłużania okna IVA')
assert not re.search(r'\beskalac\w*', operational_text, re.I), (
    'Termin „eskalacja” musi być zastąpiony reakcją, działaniem lub powiadomieniem')

tet_without_targets = re.sub(
    r'<span class="deadline-target">.*?</span>', ' ', operational_markup,
    flags=re.I | re.S)
tet_without_targets = html.unescape(re.sub(r'<[^>]+>', ' ', tet_without_targets))
assert not re.search(r'\bTET\b', tet_without_targets), (
    'Każde widoczne TET poza chronionymi szablonami wiadomości musi być pomarańczowe')

cet_without_critical = re.sub(
    r'<(?:span|strong) class="deadline-critical">.*?</(?:span|strong)>', ' ',
    operational_markup, flags=re.I | re.S)
cet_without_critical = html.unescape(re.sub(r'<[^>]+>', ' ', cet_without_critical))
assert not re.search(r'\bCET\b', cet_without_critical), (
    'Każde widoczne CET poza chronionymi szablonami wiadomości musi mieć czerwoną ramkę')

banned_references = ['Core_Operational_Contact_List.xlsx', 'AC manuall ZP.docx',
                     'PROCEDURA_IDCC_TSO_v5_2', 'QuickRef', 'Operator Manual',
                     'Inwentarz_IDCC.md', 'Karta_ryzyk_IDCC.md', 'Confluence', 'BPD',
                     'CCM Instrukcja', 'IDCC_bcd', 'IDCF_InstrUżytk', 'Procedury skróconej',
                     'HTML §', 'Rys. dla Ryzyka',
                     'Procedura_KreatorIDCF_GLSK_CBCORA.html', 'Przyklady_FID1-831.md',
                     'PDF Dyspozytora', 'draft timings', 'Status: DRAFT', 'Na podstawie:']
found_references = [term for term in banned_references if term.lower() in visible_doc.lower()]
assert not found_references, f"Pozostały odwołania do dokumentów źródłowych: {found_references}"

unresolved_markers = ['❓', 'TODO', 'do uzupełnienia', 'czy dozwolone',
                      'jakie narzędzie konkretnie', 'do dopytania']
found_unresolved = [term for term in unresolved_markers if term.lower() in visible_doc.lower()]
assert not found_unresolved, f"Pozostały nierozstrzygnięte kroki: {found_unresolved}"

forbidden_formalization = [
    'należy pobrać/wygeneruj',
    'Należy otworzyć aplikacji ZP',
    'Należy ustawić / przywróć',
    'prawy przycisk myszy → Należy wysłać',
    'lewy przycisk myszy → Należy wysłać',
]
found_bad_formalization = [
    phrase for phrase in forbidden_formalization if phrase.lower() in visible_doc.lower()
]
assert not found_bad_formalization, (
    f'Formalizacja uszkodziła gramatykę lub nazwę polecenia UI: {found_bad_formalization}')
damaged_mouse_commands = re.findall(
    r'(?:prawy|lewy) przycisk myszy[^→]{0,100}→\s*Należy\s+'
    r'(?:wysłać|pobrać|ustawić|przywrócić|otworzyć)',
    visible_doc, re.I)
assert not damaged_mouse_commands, (
    f'Nazwy poleceń UI po LPM/PPM zostały sformalizowane: {damaged_mouse_commands[:10]}')
assert 'prawy przycisk myszy → Wyślij' in visible_doc, (
    'Nazwa polecenia UI „Wyślij” po prawym przycisku myszy musi pozostać bez zmian')

formal_instruction_count = len(re.findall(r'\bnależy\b', visible_doc, re.I))
residual_imperative_count = len(re.findall(
    r'\b(?:sprawdź|pobierz|wyślij|wybierz|zgłoś|otwórz|ustaw|kliknij|monitoruj|'
    r'zadzwoń|poinformuj|potwierdź|zweryfikuj|uruchom|przejdź|odczytaj|wczytaj|'
    r'spróbuj|wykorzystaj|wykonaj)\b', visible_doc, re.I))
assert formal_instruction_count >= 500 and formal_instruction_count > residual_imperative_count, (
    'Forma techniczno-urzędowa „należy” nie dominuje w instrukcjach proceduralnych: '
    f'należy={formal_instruction_count}, imperatywy={residual_imperative_count}')

legacy_labels = [
    'Procedura IDCC TSO v7',
    '<strong>IVA</strong> (ang. <em>Individual Validation Adjustment</em>)',
    '<strong>CGM</strong> (ang. <em>Common Grid Model</em>)',
    '<strong>IGM</strong> (ang. <em>Individual Grid Model</em>)',
    '<strong>AAC</strong> (ang. <em>Already Allocated Capacity</em>)',
    '<strong>NTC</strong> (ang. <em>Net Transfer Capacity</em>)',
    '<strong>ATC</strong> (ang. <em>Available Transfer Capacity</em>)',
    '<strong>CCCt</strong> (ang. <em>Core Capacity Calculation Tool</em>)',
    '<strong><span class="deadline-target">TET</span></strong> (ang. <em>Target End Time</em>)',
    '<strong class="deadline-critical">CET</strong> (ang. <em>Critical End Time</em>)',
    '<strong>GLSK</strong> (ang. <em>Generation and Load Shift Keys</em>)',
    'BUP DA',
    'NOR DA',
    'FBA_TSO_NOR_03',
    'FBA_TSO_BUP_03',
]
missing_legacy_labels = [label for label in legacy_labels if label not in doc]
assert not missing_legacy_labels, (
    f"Nie przywrócono dawnego angielskiego nazewnictwa: {missing_legacy_labels}")

forbidden_label_translations = [
    '<title>Procedura wyznaczania zdolności śróddziennych',
    '2 · Proces wyznaczania zdolności śróddziennych',
    '8 · Czynności na pulpicie monitorowania',
    '10 · Walidacja przepływowa',
    '<td>korekta walidacyjna</td><td>Individual Validation Adjustment</td>',
    '<td>wspólny model sieci</td><td>Common Grid Model',
    '<td>indywidualny model sieci</td><td>Individual Grid Model',
    '<td>zdolność przesyłowa netto</td><td>Net Transfer Capacity</td>',
    '<td>dostępna zdolność przesyłowa</td><td>Available Transfer Capacity</td>',
]
found_label_translations = [term for term in forbidden_label_translations if term in doc]
assert not found_label_translations, (
    f"Angielskie nazwy lub skróty zostały przetłumaczone: {found_label_translations}")

required_editorial_patterns = [
    '<h3 id="proc-pse">Słownik</h3>',
    '<th>Termin</th><th>Definicja</th>',
    '<h4>Pliki dostarczane przez TSO</h4>',
    '<span class="scope-yes">IDCC(b)</span>',
    '<span class="scope-yes">IDCC(c)</span>',
    '<span class="scope-yes">IDCC(d)</span>',
    '<span class="scope-yes">IDCC(e)</span>',
    '<span class="scope-no">nie dotyczy IDCC(a)</span>',
    '<th>FID</th><th>Definicja pliku</th>',
    '<p class="definition">',
    '<div class="deadline-rule" id="tet-cet-action">',
    '<strong class="deadline-critical">CET</strong>',
    '<div class="architecture-flow"',
    '<h4>KDM — narzędzia PSE</h4>',
    '<strong>Connector 2.0</strong>',
    '<h4>Systemy zewnętrzne</h4>',
    '<strong>Perun4V + sFTP</strong>',
    '<strong>Core CC Tool</strong>',
    '<ul class="cell-list">',
    'PSE nie wysyła plików merged w tym kroku',
    'brak odrębnego progu opóźnienia',
    '<strong>Helpdesk CCC</strong>',
    '<strong>Przebieg standardowy:</strong>',
    '<strong>Tryb awaryjny:</strong>',
    'Manual Upload bezpośrednio w Core CC Tool przez Message Viewer',
    'PSE wysyła wymagane AAC do XBID',
    '<code>ID2_5</code>',
    '<code>ID3C_5</code> / <code>ID3_5</code>',
]
missing_editorial_patterns = [pattern for pattern in required_editorial_patterns if pattern not in doc]
assert not missing_editorial_patterns, (
    f"Brak wymaganych elementów zwięzłego stylu: {missing_editorial_patterns}")

forbidden_editorial_patterns = [
    'Najpierw kolor i screen',
    'Zasada generalna',
    'PSE — skróty, zakres i pliki wejściowe',
    '<h4>Skróty i pojęcia</h4>',
    '<h4>Zakres PSE i bramki czasowe</h4>',
    '<h4>Kluczowe pliki PSE per iteracja</h4>',
    'Notacja czasów w tabeli poniżej',
    'Kompletna, samowystarczalna instrukcja eksploatacyjna TSO',
    'Generation Load Shift Key',
    'Zakres: dane PSE, walidacja, pliki i granice',
    'przekazuje wejścia przez Message Viewer',
    'PSE informuje USY/CCC',
    'progu late',
    'NTC do XBID — target / late',
    'ponowna wysyłka IGM wyłącznie',
    'poprawienie i ponowne wysłanie odrzuconego pliku',
    'PSE/TSO wgrywa obliczone AAC do XBID',
    'Szyna Transportowa CN2',
    'SYSTEMY CENTRALNE CORE',
    'telefon do CCC',
    'TSCNET (CCC)',
    'Coreso (CCC)',
    'Wszystkie pliki wysyłane i odbierane między PSE a systemami zewnętrznymi przechodzą przez Connector 2.0',
    'PSE dostarcza wymagane pliki do XBID',
]
found_editorial_patterns = [pattern for pattern in forbidden_editorial_patterns if pattern in doc]
assert not found_editorial_patterns, (
    f"Pozostały elementy wskazane do usunięcia: {found_editorial_patterns}")

assert doc.count('<ul class="cell-list">') >= 25, (
    'Wieloetapowe działania w tabelach nie zostały zapisane punktami')
assert doc.count('class="architecture-tool"') == 6, (
    'Schemat musi zawierać cztery narzędzia KDM i dwa systemy zewnętrzne')

assert doc.count('(ang. <em>') >= 20, (
    'Angielskie rozwinięcia terminów słownikowych nie zostały zapisane kursywą')

source_mail_html = (ROOT / 'process2_mail.html').read_text(encoding='utf-8')
normalized_mail_section = re.sub(
    r' data-table-number="\d+" data-table-key="sec-mail-table-\d+" '
    r'aria-label="Tabela \d+\. Szablon wiadomości operacyjnej"',
    '', mail_section)
normalized_mail_section = re.sub(
    r'<span class="mail-anchor" id="mail-\d{2}"></span>', '', normalized_mail_section)
assert source_mail_html in normalized_mail_section, (
    'Po pominięciu neutralnych atrybutów numeracji kompletna sekcja 19 szablonów '
    'wiadomości musi pozostać identyczna ze źródłem')
source_when = re.findall(
    r'<p class="when">.*?</p>', source_mail_html, re.I | re.S)
output_when = re.findall(r'<p class="when">.*?</p>', normalized_mail_section, re.I | re.S)
assert output_when == source_when, (
    'Opisy użycia szablonów wiadomości nie zachowują dawnego nazewnictwa')
source_mail_bodies = re.findall(
    r'<div class="mailbody">.*?</div>', source_mail_html, re.I | re.S)
output_mail_bodies = re.findall(
    r'<div class="mailbody">.*?</div>', normalized_mail_section, re.I | re.S)
assert len(source_mail_bodies) == 19 and output_mail_bodies == source_mail_bodies, (
    'Treść 19 szablonów wiadomości musi pozostać identyczna ze źródłem')

damaged_filename_terms = re.findall(
    r'[\w./-]+[-_](?:wyznaczanie zdolności śróddziennych|pulpit monitorowania|'
    r'aplikacja Zdolności Przesyłowe|dostępna zdolność przesyłowa)'
    r'(?:[-_.][^\s<"]*)?', doc, re.I)
assert not damaged_filename_terms, (
    f"Pełna nazwa została błędnie wstawiona do nazwy technicznej: "
    f"{damaged_filename_terms[:10]}")

OUT.write_text(doc, encoding='utf-8')
print('Zapisano:', OUT)
print('Rozmiar:', OUT.stat().st_size, 'B |', doc.count('<figure'), 'figur |',
      doc.count('class="icell"'), 'ikon |', len(FILES), 'plików |',
      sum(len(v) for v in HINTS.values()), 'stanów |', len(embedded_manifest),
      'osadzonych zasobów | walidacja offline OK')

# ── STICKERY_IDCC.md (ten sam wsad) ──────────────────────────────────────────
DOCNAME = OUT.name
lines = ['# KARTY IDCC — szybkie kroki działania', '',
         f'Każdy krok linkuje do pełnej procedury `{DOCNAME}`.', '']
for title, steps in STICKER_STEPS:
    lines.append(f'## {title}'); lines.append('')
    for t,h in steps:
        lines.append(f'1. [{t}]({DOCNAME}{h})')
    lines.append('')
ST = STICKERS_OUT
ST.write_text('\n'.join(lines), encoding='utf-8')
print('Zapisano:', ST, f'({len(STICKER_STEPS)} grup, {sum(len(s) for _,s in STICKER_STEPS)} kroków)')
