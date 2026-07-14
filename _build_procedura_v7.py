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
import json, re, html, base64, mimetypes
from pathlib import Path
from collections import defaultdict, OrderedDict
import markdown

ROOT = Path(__file__).parent
OUT  = ROOT / 'PROCEDURA_IDCC_TSO_v7.html'


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
try:
    from PIL import Image
    for _m in MAN:
        try:
            with Image.open(ROOT/_m['file']) as _im: _m['_wh'] = _im.size
        except Exception:
            _m['_wh'] = (0, 0)
except ImportError:
    for _m in MAN: _m['_wh'] = (9999, 9999)

def is_micro(m):
    """Wycinek pojedynczej ikony/przycisku — pokazywany w pasku ikon, nie jako figura."""
    w, h = m.get('_wh', (9999, 9999))
    return w < 140 and h < 140
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
    """Osadza obraz bezpośrednio w HTML jako data URI wraz z podpisem."""
    m = BYFILE.get(file, {})
    cap = cap or m.get('caption') or m.get('shows') or ''
    return (f'<figure class="{cls}"><img loading="lazy" src="{asset_uri(file)}" alt="{esc(cap)}" '
            f'data-source="{esc(file)}" tabindex="0" role="button" aria-label="Powiększ ekran: {esc(cap)}">'
            f'<figcaption>{esc(cap)}</figcaption></figure>')

def gallery(area, title, intro='', only=None, exclude=None):
    items = [m for m in SCR.get(area,[]) if is_good(m)]
    if only:    items = [m for m in items if m['file'] in only]
    if exclude: items = [m for m in items if m['file'] not in exclude]
    if not items: return ''
    shots = [m for m in items if not is_micro(m)]
    icons = [m for m in items if is_micro(m)]
    figs = ''.join(img(m['file']) for m in shots)
    strip = ''
    if icons:
        cells = ''.join(
            f'<span class="icell" title="{esc(m.get("caption") or m.get("shows") or "")}">'
            f'<img src="{asset_uri(m["file"])}" alt="{esc(m.get("caption") or "")}" data-source="{esc(m["file"])}">'
            f'<small>{esc((m.get("caption") or "")[:60])}</small></span>' for m in icons)
        strip = (f'<p class="iconshead">Elementy interfejsu (ikony i przyciski, rozmiar rzeczywisty):</p>'
                 f'<div class="iconstrip">{cells}</div>')
    return (f'<details class="gal screen-gallery" open><summary>{esc(title)} — {len(shots)} ekranów'
            f'{f" + {len(icons)} ikon" if icons else ""} · kliknij ekran, aby powiększyć</summary>'
            f'{("<p>"+esc(intro)+"</p>") if intro else ""}<div class="grid">{figs}</div>{strip}</details>')

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
    return p.read_text(encoding='utf-8') if p.exists() else f'<!-- brak {name} -->'


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
 ('#sec-proces','📘','Proces IDCC','Kroki istotne dla PSE: IDCC(a) i wspólnie (b)–(d), pliki FIDx, fallbacki.'),
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

def file_card(f):
    code = f['kod']
    states = HINTS.get(code, [])
    meta = (f'<div class="meta"><span><b>Kod:</b> {esc(code)}</span>'
            f'<span><b>Profil:</b> {esc(f.get("profil"))}</span>'
            f'<span><b>TET:</b> {esc(f.get("target_end_time"))}</span>'
            f'<span><b>CET:</b> {esc(f.get("critical_end_time"))}</span>'
            f'<span><b>Źródło:</b> {linkify_refs(f.get("zrodlo"))}</span>'
            f'<span><b>Wersja:</b> {esc(f.get("wersja"))}</span></div>')
    body = (f'<p class="opis">{esc(f.get("opis_pliku"))}</p>'
            f'<p class="path"><b>Ścieżka:</b> {linkify_refs(f.get("sciezka_pliku"))}</p>')
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
    return (f'<div class="fcard" id="file-{esc(code)}"><h4>{esc(f.get("nazwa_przeplywu"))} '
            f'<span class="code">{esc(code)}</span></h4>{meta}{body}{st_html}</div>')

def section_katalog():
    groups = defaultdict(list)
    for f in FILES: groups[(f.get('iteracja') or '—')].append(f)
    out = ''
    for it in sorted(groups, key=lambda i: ITER_ORDER.index(i) if i in ITER_ORDER else 99):
        fs = groups[it]
        cards = ''.join(file_card(f) for f in sorted(fs, key=lambda x: x['kod']))
        out += f'<h3>{esc(it)} — {len(fs)} plików</h3><div class="fgrid">{cards}</div>'
    return out

# ── 7. Złożenie HTML ──────────────────────────────────────────────────────
CSS = """
:root{
 --paper:#f3f0e7;--panel:#fffdf7;--ink:#1a2230;--fg:#232b38;--mut:#5d6572;
 --rule:#ded7c7;--rule2:#c9c0ad;--navy:#0f3e63;--acc:#0e5688;--accbg:#e9f1f7;
 --ok:#146b2d;--okb:#e6f2e9;--warn:#9a5b00;--warnb:#faf0dc;--err:#b3261e;--errb:#f9e9e7;
 --run:#5b3fa8;--runb:#efeaf8;--idle:#67707e;--idleb:#edeae2;
 --yellow:#ffd23f;--teal:#0f766e;--tealbg:#e6f5f2;
 --sans:'Aptos','Segoe UI',Arial,sans-serif;
 --cond:'Aptos Display','Segoe UI Semibold','Arial Narrow',sans-serif;
 --serif:Georgia,'Times New Roman',serif;
 --mono:'Cascadia Mono','SFMono-Regular',Consolas,'Courier New',monospace;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font:14.5px/1.5 var(--sans);color:var(--fg);background:var(--paper);
background-image:linear-gradient(rgba(15,62,99,.045) 1px,transparent 1px),
linear-gradient(90deg,rgba(15,62,99,.045) 1px,transparent 1px);background-size:28px 28px}
p{margin:.55em 0}ul,ol{margin:.55em 0;padding-left:1.45em}li{margin:.24em 0}
::selection{background:var(--yellow);color:var(--ink)}
:target{animation:hl 2.2s ease-out 1}
h2:target,h3:target,h4:target,div:target,section:target{scroll-margin-top:24px}
@keyframes hl{0%{background:#fff3bf;box-shadow:0 0 0 8px #fff3bf}100%{background:transparent;box-shadow:0 0 0 8px transparent}}
.wrap{display:flex;max-width:1560px;margin:0 auto}
/* ── nawigacja: panel sterowniczy ── */
nav{position:sticky;top:0;align-self:flex-start;width:272px;height:100vh;overflow:auto;
background:linear-gradient(180deg,var(--navy) 0%,var(--ink) 130%);padding:22px 14px 40px;font-size:13px;
scrollbar-width:thin;scrollbar-color:#3f6b93 transparent}
nav h2{font:600 11px/1 var(--mono);letter-spacing:.22em;text-transform:uppercase;color:#8fb3d1;
margin:0 0 14px 8px;padding-bottom:10px;border-bottom:1px solid rgba(255,255,255,.16)}
nav a{display:block;color:#dbe7f1;text-decoration:none;padding:5px 9px;border-left:3px solid transparent;
border-radius:0 5px 5px 0;line-height:1.35}
nav a:hover{background:rgba(255,255,255,.08);border-left-color:var(--yellow);color:#fff}
/* ── kolumna główna: karta dokumentu ── */
main{flex:1;min-width:0;padding:34px 44px 60px;max-width:1200px;background:var(--panel);
border-left:1px solid var(--rule2);border-right:1px solid var(--rule2);
box-shadow:0 0 44px rgba(26,34,48,.08)}
h1{font:700 30px/1.12 var(--cond);text-transform:uppercase;letter-spacing:.015em;color:var(--ink);margin:.25em 0 .1em}
h2{font:700 21px/1.2 var(--cond);text-transform:uppercase;letter-spacing:.03em;color:var(--ink);
margin-top:2.6em;padding-bottom:8px;border-bottom:2px solid var(--ink);position:relative}
h2::after{content:"";position:absolute;left:0;right:0;bottom:-5px;height:1px;background:var(--rule2)}
h3{font:600 17.5px/1.25 var(--cond);letter-spacing:.01em;color:var(--navy);margin-top:1.7em}
h4{font:600 15px var(--sans);color:var(--acc);margin:1.15em 0 .35em}
h5{font:600 13.5px var(--sans);color:var(--ink);margin:.9em 0 .25em}
code{font:500 .92em var(--mono);background:var(--idleb);border:1px solid var(--rule);
border-radius:4px;padding:0 5px;color:var(--ink);word-break:break-all}
a{color:var(--acc)}
.lead{font:400 16.5px/1.65 var(--serif);color:#454e5c;font-style:italic}
.lead code,.lead b,.lead strong{font-style:normal}
.tag{display:inline-block;font:600 11px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;
background:var(--ink);color:var(--yellow);border-radius:3px;padding:5px 10px;margin-right:10px;vertical-align:3px}
/* ── chipy skrótów sekcji ── */
.mini{display:inline-block;font:600 11.5px var(--mono);letter-spacing:.02em;background:var(--panel);
color:var(--navy);text-decoration:none;border:1px solid var(--rule2);border-bottom-width:2px;
border-radius:4px;padding:3px 10px;margin:0 6px 6px 0}
.mini:hover{background:var(--accbg);border-color:var(--acc)}
.stickerbar{display:flex;flex-wrap:wrap;gap:0;margin:.5em 0 1.3em;padding:10px 12px;
background:repeating-linear-gradient(90deg,transparent 0 6px,rgba(15,62,99,.03) 6px 12px),var(--paper);
border:1px solid var(--rule);border-radius:6px}
.stickerbar b{width:100%;font:600 10.5px var(--mono);letter-spacing:.18em;text-transform:uppercase;
color:var(--mut);margin-bottom:7px}
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
/* ── tabele ── */
.sttab,.ref table,table.ref{width:100%;border-collapse:collapse;font-size:13px;margin:8px 0}
.sttab th,.sttab td,.ref th,.ref td,table.ref th,table.ref td{border:1px solid var(--rule2);
padding:6px 9px;text-align:left;vertical-align:top}
.sttab th,.ref th,table.ref th{background:var(--ink);color:#efe9da;font:600 11px var(--mono);
letter-spacing:.1em;text-transform:uppercase;border-color:var(--ink)}
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
/* ── screeny: duże, dominujące karty ── */
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,380px),1fr));gap:18px;margin:14px 0 4px}
figure.shot{margin:0;border:1px solid var(--rule2);border-top:4px solid var(--acc);border-radius:7px;background:#fff;padding:8px 8px 0;
box-shadow:0 2px 0 var(--rule),0 7px 18px rgba(26,34,48,.09);transition:transform .18s ease,box-shadow .18s ease}
figure.shot:hover{transform:translateY(-3px);box-shadow:0 3px 0 var(--rule),0 12px 26px rgba(26,34,48,.15)}
figure.shot img{width:100%;display:block;background:#fafbfc;border:1px solid var(--rule);cursor:zoom-in}
figure.shot img:focus-visible{outline:4px solid var(--yellow);outline-offset:3px;border-color:var(--navy)}
figure.shot figcaption{font:600 11.5px/1.4 var(--sans);color:#4e5968;padding:8px 5px 10px}
.iconshead{font:600 11px var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--mut);margin:16px 0 7px}
.iconstrip{display:flex;flex-wrap:wrap;gap:10px;align-items:flex-start}
.iconstrip .icell{display:inline-flex;flex-direction:column;align-items:center;gap:4px;
border:1px solid var(--rule2);border-radius:6px;padding:9px 11px;background:#fff;max-width:150px}
.iconstrip img{width:auto;height:auto;max-width:130px;max-height:80px}
.iconstrip small{font:10px var(--mono);color:var(--mut);text-align:center;line-height:1.25}
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
.arch{background:var(--ink);border:1px solid var(--ink);border-radius:8px;padding:16px 18px;
font:11.5px/1.28 var(--mono);overflow-x:auto;margin:12px 0;white-space:pre;color:#cfe3f4;
box-shadow:inset 0 0 60px rgba(0,0,0,.35)}
/* ── okładka i narzędzia dokumentu ── */
.hero{position:relative;overflow:hidden;margin:0 0 28px;padding:28px 30px 26px;color:#fff;
background:linear-gradient(125deg,var(--ink),var(--navy) 58%,#0b6b79);border-radius:10px;
box-shadow:0 12px 30px rgba(15,62,99,.22)}
.hero::after{content:"";position:absolute;width:270px;height:270px;right:-90px;top:-120px;
border:46px solid rgba(255,255,255,.07);border-radius:50%}
.hero .eyebrow{font:700 11px var(--mono);letter-spacing:.17em;text-transform:uppercase;color:#b8d9ec}
.hero h1{position:relative;color:#fff;font-size:34px;margin:.45em 0 .2em;max-width:800px;text-transform:none}
.hero .subtitle{position:relative;max-width:760px;color:#dcebf3;font-size:16px;margin:0}
.hero-meta{position:relative;display:flex;flex-wrap:wrap;gap:8px 18px;margin-top:18px;padding-top:14px;
border-top:1px solid rgba(255,255,255,.22);font:600 11px var(--mono);letter-spacing:.06em;color:#f5f1df}
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
section{position:relative;padding-top:4px}
section>h2{background:linear-gradient(90deg,rgba(15,62,99,.07),transparent 72%);padding:11px 12px 11px 0}
figure.shot img{max-height:760px;object-fit:contain}
/* ── powiększanie screenów ── */
.screen-dialog{width:min(96vw,1500px);max-width:none;height:min(94vh,1000px);border:0;border-radius:10px;padding:48px 18px 16px;background:#101722;color:#fff;box-shadow:0 25px 80px rgba(0,0,0,.55)}
.screen-dialog::backdrop{background:rgba(5,12,20,.82);backdrop-filter:blur(4px)}
.screen-dialog img{width:100%;height:calc(100% - 48px);object-fit:contain;display:block}
.screen-dialog p{margin:8px 48px 0 4px;color:#dbe7f1;font:600 13px var(--sans)}
.screen-dialog button{position:absolute;right:14px;top:10px;width:34px;height:34px;border:1px solid #617083;border-radius:50%;background:#1d2a3b;color:#fff;font-size:22px;cursor:pointer}
/* ── druk ── */
@media print{
 body{background:#fff}
 nav,.doc-tools,.screen-dialog{display:none!important}.wrap{display:block}main{max-width:none;padding:0;border:none;box-shadow:none;background:#fff}
 .hero{box-shadow:none;print-color-adjust:exact}.quickgrid{grid-template-columns:repeat(2,1fr)}
 figure.shot:hover{transform:none}
 .signal,.state-row,.state-label,.semantic-key,.legend-card,.risk-h,.callout,.quickcard{-webkit-print-color-adjust:exact;print-color-adjust:exact}
 details{display:block}details>summary{display:none}
 .grid{grid-template-columns:repeat(2,1fr)}
 .fcard,.mailtpl,.step,.stick,.quickcard{break-inside:avoid}
}
@media(max-width:1100px){.quickgrid,.semantic-key{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:900px){nav{display:none}main{padding:18px;border:none}.doc-tools{top:4px}}
@media(max-width:560px){.quickgrid,.semantic-key{grid-template-columns:1fr}.hero{padding:22px 20px}.hero h1{font-size:28px}.grid{grid-template-columns:1fr}}
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
    s = ['<p class="lead">Plik GLSK (Generation Load Shift Keys, FIDx-607) — 32 udokumentowane stany kafelka '
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
    bar = ''
    if stickers:
        chips = ''.join(mini_sticker(h,t) for h,t in stickers)
        bar = f'<div class="stickerbar"><b>Skrót / powiązane</b>{chips}</div>'
    return (f'<section id="{id_}"><h2><span class="tag">{esc(tag)}</span>{esc(title)}</h2>{bar}{body}</section>')

# nawigacja
NAV = [('Start','#top'),('Tablica kart','#board'),
 ('1 · Proces IDCC','#sec-proces'),('2 · Narzędzia','#sec-narzedzia'),('3 · Legenda statusów','#sec-legenda'),
 ('4 · Katalog plików','#sec-katalog'),('5 · Czynności w CCM','#sec-ccm'),
 ('6 · Walidacja NOR','#sec-nor'),('7 · Walidacja BUP','#sec-bup'),('8 · GLSK 607','#sec-fid607'),
 ('9 · Kreator IDCF','#sec-kreator'),('10 · AC w ZP','#sec-aczp'),
 ('11 · Procedury','#sec-procedury'),('12 · Ryzyka','#sec-ryzyka'),('13 · MinIO / relacje','#sec-minio')]
nav_html = ''.join(f'<a href="{h}">{esc(t)}</a>' for t,h in NAV)

proces_body = f"""
<p class="lead">IDCC (Intraday Capacity Calculation) — cykliczne, śróddzienne wyznaczanie zdolności przesyłowych
w regionie Core. PSE jako TSO dostarcza dane wejściowe, monitoruje strumienie plików i interweniuje przy awariach.</p>

<h3>Architektura procesu i przepływ danych</h3>
<pre class="arch">
  ┌────────────────────────────────────────────────────────────────────────┐
  │                        KRAJOWA DYSPOZYCJA MOCY                         │
  │                                                                        │
  │  ┌──────────────┐      ┌────────────────────────┐      ┌────────────┐  │
  │  │  System ZP   │      │ CCM (Pulpit Monitor)   │      │ PLANS /    │  │
  │  │  (Pliki AC)  │      │ https://ccm.spsm.pse.pl│      │ Kreator    │  │
  │  └──────┬───────┘      └───────────▲────────────┘      └─────┬──────┘  │
  │         │                          │                         │         │
  └─────────┼──────────────────────────┼─────────────────────────┼─────────┘
            │ (FID1/2-831)             │ (Kody ACK statusu)      │ (IGM/GLSK/CB)
            ▼                          │                         ▼
  ┌────────────────────────────────────┴───────────────────────────────────┐
  │                         Szyna Transportowa CN2                         │
  └─────────┬────────────────────────────────────────────────────▲─────────┘
            │                                                    │
            │ (Transfer ZIP PERUN)                               │ (Raporty DQC)
            ▼                                                    │
  ┌──────────────────────────────────────────────────────────────┴─────────┐
  │                         SYSTEMY CENTRALNE CORE                         │
  │                                                                        │
  │  ┌──────────────────────┐   sFTP    ┌───────────────────────────────┐  │
  │  │  MinIO Repozytorium  ├──────────►│ Perun4V (Walidacja FBA)       │  │
  │  │  (perun/, cca/)      │◄──────────┤ https://lccv.tscnet.eu        │  │
  │  └──────────────────────┘           └───────────────────────────────┘  │
  │                                                                        │
  │  ┌──────────────────────────────────────────────────────────────────┐  │
  │  │  Core CC Tool GUI (Message Viewer / Manual Upload)               │  │
  │  └──────────────────────────────────────────────────────────────────┘  │
  └────────────────────────────────────────────────────────────────────────┘
</pre>

<h3>Iteracje procesu</h3>
<table class="ref"><thead><tr><th>Iteracja</th><th>Charakter</th><th>Zakres</th></tr></thead><tbody>
<tr><td><b>IDCC(a)</b></td><td>Pełny przebieg centralny + wyznaczanie ATC</td><td>AC, ATC Based Validation, Final NTC</td></tr>
<tr><td><b>IDCC(b)–(d)</b></td><td>Kolejne iteracje śróddzienne (ID2/ID3C/ID3)</td><td>GLSK, CGM, RefProg, CB, IVA, NTC, paczki PERUN</td></tr>
</tbody></table>

<h3>Wejścia PSE i bramki czasowe</h3>
<p>Każdy plik ma <b>TET</b> (Target End Time — cel) i <b>CET</b> (Critical End Time — twardy deadline). Statusy i działania
zależą od relacji do tych bramek — patrz <a href="#sec-legenda">legenda</a> i <a href="#sec-katalog">katalog plików</a>.</p>
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
    if not p.exists(): return f'<!-- brak {name} -->'
    h = p.read_text(encoding='utf-8')
    for en, pl in TH_PL.items():   # ujednolić nagłówki tabel na polski
        h = re.sub(r'(<th[^>]*>)\s*' + re.escape(en) + r'\s*(</th>)', r'\1' + pl + r'\2', h)
    h = h.replace(' ⚑ dotyczy granic PSE</h4>',
                  ' <span class="psemark">⚑ dotyczy granic PSE</span></h4>')
    # Normalizacja rejestru inżynierskiego
    h = re.sub(r'Happy\s+Day', 'Stan poprawny / nominalny', h)
    h = re.sub(r'(?i)bra\s+diostepu', 'brak dostępu', h)
    return h

# ══════════════════════════ MONTAŻ DOKUMENTU v7 ══════════════════════════════
NAV = [('Start','#top'),
 ('1 · Cel i definicje','#sec-cel'),('2 · Proces IDCC','#sec-proces'),
 ('3 · Harmonogram operacyjny','#sec-harmonogram'),('4 · Narzędzia','#sec-narzedzia'),
 ('5 · Legenda statusów','#sec-legenda'),('6 · Katalog plików','#sec-katalog'),
 ('7 · Przebieg nominalny','#sec-happyday'),('8 · Czynności w CCM','#sec-ccm'),
 ('9 · IGM / TSO DG / CB / GLSK','#sec-igm'),('10 · Walidacja FBA','#sec-walidacja'),
 ('11 · MinIO/Perun/CCCt','#sec-ops'),('12 · Kreator i AC w ZP','#sec-kreator'),
 ('13 · Procedury P01–P06','#sec-procedury'),('14 · Ryzyka R01–R29','#sec-ryzyka'),
 ('15 · Szablony maili','#sec-mail'),('16 · Buckety i kontakty','#sec-minio'),
 ('17 · Checklisty dyżurowe','#sec-checklisty'),('⭐ STICKERY','#sec-stickery')]
nav_html = ''.join(f'<a href="{h}">{esc(t)}</a>' for t,h in NAV)

cel_body = ('<p class="lead">Procedura operacyjna dyspozytora PSE dla procesu Intraday Capacity '
 'Calculation (IDCC) w regionie Core. Dokument obejmuje pełny zakres czynności TSO: dostarczanie '
 'danych wejściowych, monitorowanie na pulpicie CCM, walidację indywidualną (IVA), działania '
 'backupowe i eskalację. Wszystkie obowiązujące w tym zakresie instrukcje, scenariusze, kontakty '
 'i materiały ekranowe zostały włączone bezpośrednio do niniejszego dokumentu. Obowiązuje '
 'całodobowo, 7 dni w tygodniu.</p>'
 '<div class="callout"><b>Zasada generalna:</b> przy zdarzeniu wykraczającym poza normalny przebieg '
 'wykonuj kolejne czynności opisane w tej procedurze; przy prawdopodobnym niedotrzymaniu Target '
 'End Time powiadom CCC i przejdź do odpowiedniego scenariusza backupowego.</div>'
 + load_frag('process2_glos.html'))

proces_body2 = proces_body + load_frag('process2_a.html') + load_frag('process2_bcd.html')

katalog_body = section_katalog() + load_frag7('frag7_maski.html')

happyday_body = (load_frag7('frag7_happyday.html')
 + '<details class="gal"><summary>Szczegółowy przebieg i użycie narzędzi (opis rozszerzony)</summary>'
 + v52_slice('s5','s6') + v52_slice('s6','s7') + '</details>')

def _inject_ids(html_, mapping):
    for pref, hid in mapping:
        html_ = re.sub(r'(<h4)([^>]*>\s*' + re.escape(pref) + ')', r'\1 id="' + hid + r'"\2', html_, count=1)
    return html_

ccm_ext = v52_h3block(['7M.1.','7M.3.','7M.7.','7M.8.','7M.9.','7M.10.','7M.11.','7M.12.','7M.13.','7M.14.'])
ccm_ext = _inject_ids(ccm_ext, [('7M.1.','ccm-tryby'),('7M.3.','ccm-profile'),('7M.7.','ccm-scen'),
 ('7M.8.','ccm-ack'),('7M.9.','ccm-powiadomienia'),('7M.10.','ccm-eksport'),('7M.11.','ccm-idcf'),
 ('7M.12.','ccm-c6plus'),('7M.13.','ccm-uprawnienia'),('7M.14.','ccm-awarie')])
ccm_body = ccm_section() + '<h3 id="ccm-ext">Rozszerzenia CCM (katalog 7M)</h3>' + ccm_ext

igm_body = (v52_slice('s4a','s4b') + v52_slice('s4b','s4c') + v52_slice('s4c','s4d') + v52_slice('s4d','s5'))

walidacja_body = (load_frag7('frag7_walidacja.html')
 + '<h4>Ekrany — tryb normalny (NOR)</h4>' + gallery('nor','Walidacja NOR')
 + '<h4>Ekrany — tryb backup (BUP)</h4>' + gallery('bup','Walidacja BUP')
 + '<h4 id="wal-glsk">GLSK (FIDx-607) — katalog 32 stanów kafelka</h4>' + gallery('fid607','GLSK 607 — stany kafelka'))

ops_body = v52_slice('s8','s9')

kreator_body = kreator_section() + '<h3 id="aczp">AC w ZP (FIDx-831)</h3>' + aczp_section()

ryzyka_body = ('<p class="lead">Pełna baza 29 ryzyk operacyjnych (R01–R29). Każde ryzyko zawiera '
 'wpływ, szczegółową procedurę działania oraz skrót decyzyjny. Wymagane kanały zgłoszeń: '
 'CIZ, WPO i PSE-I; wszystkie informacje potrzebne do reakcji znajdują się w tej sekcji.</p>'
 + '<div class="ref riskbase">' + RYZ_HTML + '</div>'
 + '<details class="gal"><summary>Mapowanie U-kodów (U01–U23) i tabela kodów ACK</summary><div class="ref">'
 + inw_slice('# 3. Ryzyka', '# 4. Procedury', '# 3. Ryzyka') + '</div></details>')

kontakty_body = '''<h3 id="kontakty">Kontakty operacyjne</h3>
<p class="lead">Komplet kontaktów wymaganych przy realizacji scenariuszy opisanych w tej procedurze.</p>
<table class="ref">
  <thead><tr><th>Podmiot / narzędzie</th><th>E-mail / kanał</th><th>Telefon</th><th>Zakres</th></tr></thead>
  <tbody>
    <tr><td><strong>TSCNET (CCC)</strong></td><td>operator@tscnet.eu</td><td>+49 89 45554 201</td><td>Operator CCCt — decyzje backup/kill</td></tr>
    <tr><td><strong>Coreso (CCC)</strong></td><td>day-ahead.engineer@coreso.eu</td><td>+32 2 743 21 10</td><td>Principal contact, scalanie CGM</td></tr>
    <tr><td><strong>USY IDCC</strong></td><td>idcc.helpdesk@unicorn.com</td><td>+420 221 400 540</td><td>Helpdesk CCCt (GUI, pliki, obliczenia)</td></tr>
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
   ('Brak v2 po 14:30 → MinIO cca/… → telefon do CCC', '#hd-a'),
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
 ('📣 Komunikacja i eskalacja', [
   ('Wybierz właściwy szablon maila Core ID', '#proc-mail'),
   ('Telefony i adresy: CCC / USY / kdm6', '#kontakty'),
   ('Znajdź ryzyko i skrót działania (R01–R29)', '#sec-ryzyka'),
   ('Fallbacki iteracji (b)–(d) wg BPD', '#proc-bcd'),
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

doc = f"""<!doctype html><html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#0f3e63">
<title>Procedura IDCC TSO v7 — kompletna instrukcja z ekranami</title>
<style>{CSS}
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
.stick a{{color:var(--fg);text-decoration:none;border-bottom:1px dotted var(--acc)}}
.stick a:hover{{color:var(--acc);border-bottom-style:solid}}
</style></head><body>
<div class="wrap">
<nav><h2>Spis treści</h2>{nav_html}</nav>
<main id="top">
<header class="hero">
  <div class="eyebrow">FBA_TSO_IDCC · PSE S.A. · KDM · REGION CORE</div>
  <h1>Procedura operacyjna dyspozytora — proces IDCC</h1>
  <p class="subtitle">Kompletna, samowystarczalna instrukcja eksploatacyjna TSO: proces, terminy, czynności w narzędziach, scenariusze awaryjne, kontakty i materiały ekranowe.</p>
  <div class="hero-meta"><span>WYDANIE v7</span><span>OBOWIĄZUJE 24/7</span><span>18 SEKCJI</span><span>309 ZASOBÓW EKRANOWYCH</span><span>TRYB OFFLINE</span></div>
</header>
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
  <a class="quickcard emergency" href="#sec-ryzyka"><span class="qicon">!</span><b>Zagrożenie / awaria</b><small>Reakcja, backup i eskalacja.</small></a>
  <a class="quickcard warning" href="#sec-stickery"><span class="qicon">↗</span><b>41 szybkich działań</b><small>Skrót → pełny krok i ekran.</small></a>
</div>
<div class="semantic-key" aria-label="Znaczenie kolorów">
  <div class="key-item key-success"><span class="key-dot"></span><span><b>ZIELONY · PRAWIDŁOWO</b>monitoruj, bez interwencji</span></div>
  <div class="key-item key-warning"><span class="key-dot"></span><span><b>ŻÓŁTY · UWAGA</b>termin lub stan przejściowy</span></div>
  <div class="key-item key-danger"><span class="key-dot"></span><span><b>CZERWONY · ZAGROŻENIE</b>działaj i eskaluj</span></div>
  <div class="key-item key-action"><span class="key-dot"></span><span><b>NIEBIESKI · DZIAŁANIE</b>krok operatora</span></div>
</div>
<p class="lead"><b>Najpierw kolor i screen, potem szczegóły.</b> Galerie operacyjne są rozwinięte; kliknij ekran, aby go powiększyć. Tabele wariantów pozostają zwinięte, aby nie zasłaniały głównego przebiegu.</p>
{section('sec-cel','Cel, zakres i definicje','1',cel_body,[('#sec-proces','proces'),('#sec-harmonogram','harmonogram')])}
{section('sec-proces','Proces IDCC — kroki istotne dla PSE','2',proces_body2,[('#sec-katalog','katalog plików'),('#sec-harmonogram','harmonogram')])}
{section('sec-harmonogram','Harmonogram operacyjny (CCCt)','3',load_frag7('frag7_harmonogram.html'),[('#sec-happyday','przebieg nominalny'),('#sec-katalog','TET/CET plików')])}
{section('sec-narzedzia','Narzędzia','4','<div class="ref">'+TOOLS_HTML+'</div>',[('#sec-ops','obsługa MinIO/Perun/CCCt'),('#sec-ryzyka','ryzyka')])}
{section('sec-legenda','Legenda statusów kafelków','5',legend_section(),[('#sec-ccm','czynności w CCM'),('#sec-katalog','stany plików')])}
{section('sec-katalog','Katalog plików FIDx — opisy, stany, maski','6',katalog_body,[('#sec-legenda','legenda'),('#sec-ccm','obsługa w CCM')])}
{section('sec-happyday','Przebieg nominalny i scenariusze backupowe','7',happyday_body,[('#sec-harmonogram','harmonogram'),('#sec-walidacja','walidacja')])}
{section('sec-ccm','Czynności w CCM (C.1–C.12 + katalog 7M)','8',ccm_body,[('#sec-legenda','legenda'),('#sec-ryzyka','ryzyka')])}
{section('sec-igm','Dane wejściowe PSE — IGM, TSO Data Gathering, CB, GLSK','9',igm_body,[('#sec-kreator','Kreator IDCF'),('#sec-katalog','katalog')])}
{section('sec-walidacja','Walidacja domeny FBA (NOR / BUP / GLSK)','10',walidacja_body,[('#sec-happyday','scenariusze B1–B4'),('#sec-ops','Perun4V')])}
{section('sec-ops','Obsługa MinIO, Perun4V i Core CC Tool','11',ops_body,[('#sec-narzedzia','narzędzia'),('#sec-procedury','procedury')])}
{section('sec-kreator','Kreator IDCF i AC w ZP','12',kreator_body,[('#sec-igm','CB/GLSK'),('#sec-katalog','FID2-831')])}
{section('sec-procedury','Procedury P01–P06','13','<div class="ref">'+inw_slice('# 4. Procedury','# 5. Buckety','# 4. Procedury')+'</div>',[('#sec-ryzyka','ryzyka'),('#sec-ccm','CCM')])}
{section('sec-ryzyka','Ryzyka R01–R29, U-kody i kody ACK','14',ryzyka_body,[('#sec-procedury','procedury'),('#sec-mail','szablony maili')])}
{section('sec-mail','Szablony maili operacyjnych (Core ID)','15','<div class="proc">'+load_frag('process2_mail.html')+'</div>',[('#kontakty','kontakty'),('#sec-ryzyka','ryzyka')])}
{section('sec-minio','Buckety MinIO, mapa relacji i kontakty','16',minio_body,[('#sec-katalog','pliki'),('#sec-narzedzia','MinIO')])}
{section('sec-checklisty','Checklisty dyżurowe','17',checklisty_body,[('#sec-happyday','przebieg nominalny'),('#sec-stickery','stickery')])}
{section('sec-stickery','⭐ STICKERY — szybkie kroki działania','18',stickery_section_html(),[('#top','początek dokumentu')])}
<dialog id="screen-dialog" class="screen-dialog" aria-label="Powiększony zrzut ekranu">
  <button type="button" aria-label="Zamknij powiększenie">×</button><img alt=""><p></p>
</dialog>
<footer style="margin:3em 0 2em;color:var(--mut);font-size:13px;border-top:1px solid var(--rule);padding-top:14px">
<strong>PROCEDURA_IDCC_TSO_v7</strong> · jeden samowystarczalny dokument · {len(MAN)} zasobów ekranowych w manifeście ·
{sum(len(v) for v in HINTS.values())} wariantów stanów · {len(FILES)} opisów plików · 19 szablonów wiadomości.
Wszystkie instrukcje, kontakty i materiały ekranowe potrzebne do realizacji opisanych działań znajdują się powyżej.
Każde ryzyko zgłaszać do: <b>CIZ, WPO, PSE-I (PSE Innowacje)</b>.</footer>
<script>
const semanticPatterns = {{
  danger: /KRYTYCZNE|STOP|brak (?:ACK|pliku|wyniku)|brak dostępu|awaria|błąd procesu|negatywny ACK|plik niezwalidowany|niepoprawn[yae]|niezgodn[yae]|niedostarczon[yae]|timeout|odrzucon[yae]|Rejected|Process failed|przekroczono CET|minął CET|nie wysyłaj/giu,
  warning: /UWAGA|OSTRZEŻENIE|zbliża się (?:TET|CET)|ERR-I|po CET|tryb backupowy|IVA BACKUP|fallback/giu,
  success: /PRAWIDŁOWO|SUKCES|SUCCESSFUL|proces poprawny|stan prawidłowy|brak działań|potwierdzony ACK|Processed/giu,
  action: /ZGŁOŚ|ZADZWOŃ|SPRAWDŹ|POWIADOM|WYŚLIJ(?: PLIK)? RĘCZNIE|POBIERZ(?: POPRAWNY)? PLIK|ODCZYTAJ KOD ACK|USTAW STATUS|URUCHOM(?: PONOWNIE)? OBLICZENIA|PRZEJDŹ DO SCENARIUSZA|ESKALACJA/giu
}};
const semanticPattern = /KRYTYCZNE|STOP|brak (?:ACK|pliku|wyniku)|brak dostępu|awaria|błąd procesu|negatywny ACK|plik niezwalidowany|niepoprawn[yae]|niezgodn[yae]|niedostarczon[yae]|timeout|odrzucon[yae]|Rejected|Process failed|przekroczono CET|minął CET|nie wysyłaj|UWAGA|OSTRZEŻENIE|zbliża się (?:TET|CET)|ERR-I|po CET|tryb backupowy|IVA BACKUP|fallback|PRAWIDŁOWO|SUKCES|SUCCESSFUL|proces poprawny|stan prawidłowy|brak działań|potwierdzony ACK|Processed|ZGŁOŚ|ZADZWOŃ|SPRAWDŹ|POWIADOM|WYŚLIJ(?: PLIK)? RĘCZNIE|POBIERZ(?: POPRAWNY)? PLIK|ODCZYTAJ KOD ACK|USTAW STATUS|URUCHOM(?: PONOWNIE)? OBLICZENIA|PRZEJDŹ DO SCENARIUSZA|ESKALACJA/giu;
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
      if (!node.nodeValue.trim() || node.parentElement.closest('script,style,code,pre,.signal,.screen-dialog')) return NodeFilter.FILTER_REJECT;
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
    'FBA_TSO_NOR_03 v0.21': 'instrukcja walidacji w trybie normalnym',
    'FBA_TSO_BUP_03 v0.32': 'instrukcja walidacji w trybie backupowym',
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
    lambda _: r'<code>\\uo-data\ZUO\Pion_UOD\Wydzial_DP\MODELE\5_DYSP\FBA\Pliki wejściowe do ID FBA\rrrMMdd\PERUN\</code>',
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
doc = re.sub(r'FBA_TSO_BUP_03\s*<strong>v0\.32</strong>\s*z 05\.01\.2026',
             'instrukcja walidacji w trybie backupowym opisana poniżej', doc)
doc = doc.replace('Pełna instrukcja narzędzia: IDCF_InstrUżytk_v5',
                  'Pełna instrukcja narzędzia znajduje się w <a href="#sec-kreator">sekcji Kreator IDCF</a>')
doc = re.sub(r'<li><strong>Pełna instrukcja narzędzia:</strong>\s*<code>IDCF_InstrUżytk_v5</code>.*?</li>',
             '<li><strong>Instrukcja narzędzia:</strong> wykonaj kroki i skorzystaj z ekranów w '
             '<a href="#sec-kreator">sekcji Kreator IDCF i AC w ZP</a>.</li>', doc, flags=re.S)
doc = re.sub(r'<em>tryb backupowy Rys\. dla Ryzyka 9 \(\)</em>',
             '<a href="#sec-walidacja">Ekrany Perun4V znajdują się w sekcji Walidacja FBA</a>', doc)
doc = doc.replace('Dla pełnych kart ryzyk patrz rozdział 9.',
                  'Pełne karty ryzyk znajdują się w <a href="#sec-ryzyka">sekcji Ryzyka R01–R29</a>.')
doc = doc.replace('BUP DA', 'tryb backupowy').replace('NOR DA', 'tryb normalny')
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
doc = re.sub(r'<em>tryb backupowy Rys\. dla Ryzyka 9 \(\)</em>',
             '<a href="#sec-walidacja">Ekrany Perun4V znajdują się w sekcji Walidacja FBA</a>', doc)
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

def _restore_asset(match):
    return f'src="{_embedded_sources[int(match.group(1))]}"'
doc = re.sub(r'src="__EMBEDDED_ASSET_(\d+)__"', _restore_asset, doc)

# warstwa komentarzy recenzenta (offline, localStorage + eksport JSON/MD)
_cw = (ROOT/'_comments_widget.html')
if _cw.exists():
    doc = doc.replace('</body>', _cw.read_text(encoding='utf-8') + '\n</body>')

# ── walidacja kompletności i samowystarczalności ─────────────────────────────
ids = set(re.findall(r'id="([^"]+)"', doc))
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

visible_doc = re.sub(r'src="data:[^"]+"', 'src="[embedded]"', doc, flags=re.I)
visible_doc = re.sub(r'<(?:style|script)\b.*?</(?:style|script)>', ' ', visible_doc, flags=re.I | re.S)
visible_doc = html.unescape(re.sub(r'<[^>]+>', ' ', visible_doc))
banned_references = ['Core_Operational_Contact_List.xlsx', 'AC manuall ZP.docx',
                     'PROCEDURA_IDCC_TSO_v5_2', 'QuickRef', 'Operator Manual',
                     'Inwentarz_IDCC.md', 'Karta_ryzyk_IDCC.md', 'Confluence', 'BPD',
                     'CCM Instrukcja', 'IDCC_bcd', 'IDCF_InstrUżytk', 'Procedury skróconej',
                     'FBA_TSO_BUP', 'BUP DA', 'NOR DA', 'HTML §', 'Rys. dla Ryzyka',
                     'Procedura_KreatorIDCF_GLSK_CBCORA.html', 'Przyklady_FID1-831.md',
                     'PDF Dyspozytora', 'draft timings', 'Status: DRAFT', 'Na podstawie:']
found_references = [term for term in banned_references if term.lower() in visible_doc.lower()]
assert not found_references, f"Pozostały odwołania do dokumentów źródłowych: {found_references}"

unresolved_markers = ['❓', 'TODO', 'do uzupełnienia', 'czy dozwolone',
                      'jakie narzędzie konkretnie', 'do dopytania']
found_unresolved = [term for term in unresolved_markers if term.lower() in visible_doc.lower()]
assert not found_unresolved, f"Pozostały nierozstrzygnięte kroki: {found_unresolved}"

OUT.write_text(doc, encoding='utf-8')
print('Zapisano:', OUT)
print('Rozmiar:', OUT.stat().st_size, 'B |', doc.count('<figure'), 'figur |',
      doc.count('class="icell"'), 'ikon |', len(FILES), 'plików |',
      sum(len(v) for v in HINTS.values()), 'stanów |', len(embedded_manifest),
      'osadzonych zasobów | walidacja offline OK')

# ── STICKERY_IDCC.md (ten sam wsad) ──────────────────────────────────────────
DOCNAME = OUT.name
lines = ['# STICKERY IDCC — szybkie kroki działania', '',
         f'Każdy krok linkuje do pełnej procedury `{DOCNAME}`.', '']
for title, steps in STICKER_STEPS:
    lines.append(f'## {title}'); lines.append('')
    for t,h in steps:
        lines.append(f'1. [{t}]({DOCNAME}{h})')
    lines.append('')
ST = ROOT / 'STICKERY_IDCC.md'
ST.write_text('\n'.join(lines), encoding='utf-8')
print('Zapisano:', ST, f'({len(STICKER_STEPS)} grup, {sum(len(s) for _,s in STICKER_STEPS)} kroków)')
