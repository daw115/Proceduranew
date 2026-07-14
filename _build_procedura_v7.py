#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator PROCEDURA_IDCC_TSO_v6.html — szczegółowa instrukcja z ekranami + karty-stickery.

Warstwy:
  • STICKER  — karty skrócone (cover + na górze każdej sekcji), hiperłącze do detalu.
  • DETAL    — szczegółowe kroki wszystkich możliwości + właściwe screeny (z manifestu).

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
    """Osadza obraz jako <img> ze ścieżką względną + podpis."""
    m = BYFILE.get(file, {})
    cap = cap or m.get('caption') or m.get('shows') or ''
    return (f'<figure class="{cls}"><img loading="lazy" src="{esc(file)}" alt="{esc(cap)}">'
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
            f'<img src="{esc(m["file"])}" alt="{esc(m.get("caption") or "")}">'
            f'<small>{esc((m.get("caption") or "")[:60])}</small></span>' for m in icons)
        strip = (f'<p class="iconshead">Elementy interfejsu (ikony i przyciski, rozmiar rzeczywisty):</p>'
                 f'<div class="iconstrip">{cells}</div>')
    return (f'<details class="gal"><summary>{esc(title)} — pełna galeria '
            f'({len(shots)} ekranów{f" + {len(icons)} ikon" if icons else ""})</summary>'
            f'{("<p>"+esc(intro)+"</p>") if intro else ""}<div class="grid">{figs}</div>{strip}</details>')

def featured(file):
    """Pojedynczy wyróżniony screen w kroku (jeśli istnieje)."""
    return img(file) if file in BYFILE else ''

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
            f'<img class="tile" src="img_ccm/tiles/{tile}" alt="{esc(lab)}">'
            f'<span class="tlab">{esc(cn)}</span></span>')

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
        if j == -1: j = V52.find('</main>', i)
        body = V52[i:j]
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
            rows += (f'<tr><td class="stcol">{tiles}</td><td>{esc(s["sit"])}</td>'
                     f'<td>{s["proc"]}</td></tr>')
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
:root{--bg:#fff;--fg:#1a1f29;--mut:#5b6473;--bd:#dfe3ea;--acc:#0a4d8c;--accbg:#eaf2fb;
--ok:#1b8a3a;--okb:#e7f6ec;--warn:#b06f00;--warnb:#fff4e0;--err:#c0271f;--errb:#fdeceb;
--run:#6a3fb0;--runb:#f0eafb;--idle:#6b7280;--idleb:#eef0f3;}
*{box-sizing:border-box}
body{margin:0;font:15px/1.6 -apple-system,Segoe UI,Roboto,Arial,sans-serif;color:var(--fg);background:#f5f6f8}
.wrap{display:flex;max-width:1500px;margin:0 auto;background:var(--bg)}
nav{position:sticky;top:0;align-self:flex-start;width:265px;height:100vh;overflow:auto;
border-right:1px solid var(--bd);padding:18px 14px;font-size:13px;background:#fbfcfe}
nav h2{font-size:13px;text-transform:uppercase;letter-spacing:.05em;color:var(--mut);margin:14px 0 6px}
nav a{display:block;color:var(--fg);text-decoration:none;padding:3px 6px;border-radius:5px}
nav a:hover{background:var(--accbg);color:var(--acc)}
main{flex:1;min-width:0;padding:28px 34px;max-width:1180px}
h1{font-size:27px;margin:.2em 0}
h2{font-size:22px;border-bottom:2px solid var(--acc);padding-bottom:5px;margin-top:2.2em;color:var(--acc)}
h3{font-size:18px;margin-top:1.6em}
h4{margin:.2em 0}
.lead{color:var(--mut);font-size:15px}
.tag{display:inline-block;background:var(--accbg);color:var(--acc);border-radius:20px;
padding:2px 11px;font-size:12px;font-weight:600;margin-right:6px}
/* sticker board */
.board{display:grid;grid-template-columns:repeat(auto-fill,minmax(215px,1fr));gap:12px;margin:18px 0}
.sticker{display:flex;flex-direction:column;gap:4px;background:linear-gradient(160deg,#fffef4,#fff7d9);
border:1px solid #ecd98a;border-left:5px solid #e0b400;border-radius:10px;padding:12px 13px;
text-decoration:none;color:var(--fg);box-shadow:0 1px 3px rgba(0,0,0,.07);transition:.15s}
.sticker:hover{transform:translateY(-2px);box-shadow:0 5px 14px rgba(0,0,0,.13)}
.sticker .ic{font-size:22px}.sticker .ti{font-weight:700;font-size:14px}
.sticker .de{font-size:12px;color:var(--mut);line-height:1.4}
.sticker .go{font-size:11px;color:var(--acc);font-weight:600;margin-top:2px}
.mini{display:inline-block;background:var(--accbg);color:var(--acc);font-size:12px;font-weight:600;
text-decoration:none;border-radius:6px;padding:2px 9px;margin:0 6px 6px 0;border:1px solid #cfe0f3}
.stickerbar{display:flex;flex-wrap:wrap;gap:0;margin:.4em 0 1.2em;padding:10px 12px;
background:#fffdf3;border:1px dashed #e0b400;border-radius:9px}
.stickerbar b{width:100%;font-size:12px;color:var(--warn);text-transform:uppercase;letter-spacing:.04em;margin-bottom:6px}
/* status badges */
.st{display:inline-block;border-radius:5px;padding:1px 8px;font-size:12px;font-weight:600;white-space:nowrap}
.st-ok{background:var(--okb);color:var(--ok)}.st-warn{background:var(--warnb);color:var(--warn)}
.st-err{background:var(--errb);color:var(--err)}.st-run{background:var(--runb);color:var(--run)}
.st-idle{background:var(--idleb);color:var(--idle)}
/* file catalog */
.fgrid{display:grid;grid-template-columns:1fr;gap:12px}
.fcard{border:1px solid var(--bd);border-radius:9px;padding:13px 15px;background:#fff}
.fcard h4 .code{font-size:12px;background:var(--idleb);color:var(--idle);border-radius:5px;padding:1px 7px;font-weight:600}
.fcard .meta{display:flex;flex-wrap:wrap;gap:5px 16px;font-size:12.5px;color:var(--mut);margin:6px 0}
.fcard .opis{margin:6px 0}.fcard .path{font-size:13px;color:var(--mut)}
.sttab{width:100%;border-collapse:collapse;font-size:13px;margin-top:6px}
.sttab th,.sttab td{border:1px solid var(--bd);padding:6px 8px;text-align:left;vertical-align:top}
.sttab th{background:var(--accbg);color:var(--acc)}
.stcol{white-space:normal}
.tcell{display:inline-flex;flex-direction:column;align-items:center;gap:3px;margin:2px 10px 2px 0;vertical-align:top}
.tcell .tile{width:30px;height:30px;border:1px solid var(--bd);border-radius:6px;display:block;background:#fafbfc}
.tcell .tlab{font-size:10.5px;color:var(--mut);max-width:80px;text-align:center;line-height:1.15}
details{margin:8px 0}summary{cursor:pointer;font-weight:600;color:var(--acc)}
details.states>summary{font-size:13px}
/* screenshots */
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;margin-top:10px}
figure.shot{margin:0;border:1px solid var(--bd);border-radius:8px;overflow:hidden;background:#fff}
figure.shot img{width:100%;display:block;background:#fafbfc}
figure.shot figcaption{font-size:12px;color:var(--mut);padding:6px 9px;border-top:1px solid var(--bd)}
.iconshead{font-size:13px;color:var(--mut);margin:14px 0 6px}
.iconstrip{display:flex;flex-wrap:wrap;gap:10px;align-items:flex-start}
.iconstrip .icell{display:inline-flex;flex-direction:column;align-items:center;gap:4px;
border:1px solid var(--bd);border-radius:8px;padding:8px 10px;background:#fff;max-width:150px}
.iconstrip img{width:auto;height:auto;max-width:130px;max-height:80px}
.iconstrip small{font-size:10.5px;color:var(--mut);text-align:center;line-height:1.2}
.step{border-left:3px solid var(--acc);background:var(--accbg);border-radius:0 8px 8px 0;padding:10px 14px;margin:12px 0}
.step .n{font-weight:700;color:var(--acc)}
.feat{max-width:560px;margin:10px 0}
details.gal>summary{margin:6px 0}
.callout{background:var(--warnb);border:1px solid #e8c97a;border-radius:8px;padding:10px 14px;margin:12px 0;font-size:14px}
.ref table,table.ref{border-collapse:collapse;width:100%;font-size:13px;margin:8px 0}
.ref th,.ref td,table.ref th,table.ref td{border:1px solid var(--bd);padding:5px 8px;text-align:left;vertical-align:top}
.ref th,table.ref th{background:var(--accbg);color:var(--acc)}
.proc h3{font-size:18px;border-bottom:1px solid var(--bd);padding-bottom:4px;margin-top:1.8em}
.proc h4{font-size:15px;color:var(--acc);margin:1.1em 0 .3em}
.proc h5{font-size:13.5px;margin:.8em 0 .2em}
.proc table{display:block;overflow-x:auto;white-space:normal}
/* karty szablonów maili */
.mailtpl{border:1px solid var(--bd);border-left:4px solid var(--acc);border-radius:9px;
padding:12px 15px;margin:14px 0;background:#fff}
.mailtpl h4{margin:.1em 0 .4em}
.mailtpl .when{font-size:13px;color:var(--mut);margin:.2em 0 .6em}
.mailtpl table{margin:6px 0}
.mailbody{background:#f7f8fa;border:1px solid var(--bd);border-radius:7px;padding:10px 13px;
font-size:13px;margin-top:8px}
.psemark{display:inline-block;background:var(--errb);color:var(--err);font-size:11.5px;
font-weight:700;border-radius:5px;padding:1px 8px;margin-left:8px;vertical-align:middle}
.ref h1{font-size:22px;color:var(--acc);border-bottom:2px solid var(--acc)}
.ref h2{font-size:18px}.ref h3{font-size:15px;margin-top:1.2em}
@media print{nav{display:none}.wrap{display:block}main{max-width:none;padding:0}
.sticker:hover{transform:none}details{display:block}details>summary{display:none}
.grid{grid-template-columns:repeat(2,1fr)}}
.arch{background:#fafbfc;border:1px solid var(--bd);border-radius:8px;padding:14px 16px;
font-family:'Courier New',Consolas,monospace;font-size:11.5px;line-height:1.25;overflow-x:auto;
margin:10px 0;white-space:pre;color:var(--fg)}
@media(max-width:860px){nav{display:none}main{padding:16px}}
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
    for fn,lab,desc in tiles:
        p = f'img_ccm/tiles/{fn}'
        cells += (f'<div class="fcard" style="display:flex;gap:12px;align-items:center">'
                  f'<img src="{esc(p)}" alt="{esc(lab)}" style="width:42px;height:42px;flex:none;border:1px solid var(--bd);border-radius:6px">'
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
    s.append('<div class="callout"><b>Najczęstsze błędy walidacji:</b> „Za mały rozmiar pliku!” (rozmiar poniżej progu MinIO), '
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
 ('1 · Cel i definicje','#sec-cel'),('2 · Proces IDCC (BPD)','#sec-proces'),
 ('3 · Harmonogram HLBP','#sec-harmonogram'),('4 · Narzędzia','#sec-narzedzia'),
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
 'backupowe i eskalację. Podstawy: Core IDCC Flow-Based BPD v5.0, HLBP CCCt 4.2, instrukcje '
 'FBA_TSO_NOR_03 v0.21 / FBA_TSO_BUP_03 v0.32, CCM Instrukcja Użytkownika, Core CC Tool Operator '
 'Manual 4.1. Obowiązuje całodobowo, 7 dni w tygodniu.</p>'
 '<div class="callout">Zasada generalna: przy zdarzeniu wykraczającym poza normalny przebieg '
 'wykonuj kolejne czynności wg niniejszej procedury; przy prawdopodobnym niedotrzymaniu Target '
 'End Time — powiadom CCC i postępuj wg działań backupowych.</div>'
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

ryzyka_body = ('<p class="lead">Pełna baza 29 ryzyk operacyjnych (R01–R29) zagregowana ze źródeł: '
 'procedura HTML §9, BUP DA, NOR, CCM Instrukcja v2.6, Confluence, AC manuall ZP. Każde ryzyko: '
 'wpływ, procedura szczegółowa (A) i skrót strzałkowy (B). Zgłoszenia: CIZ, WPO, PSE-I.</p>'
 + '<div class="ref riskbase">' + RYZ_HTML + '</div>'
 + '<details class="gal"><summary>Mapowanie U-kodów (U01–U23) i tabela kodów ACK</summary><div class="ref">'
 + inw_slice('# 3. Ryzyka', '# 4. Procedury', '# 3. Ryzyka') + '</div></details>')

kontakty_body = '''<h3 id="kontakty">Kontakty operacyjne</h3>
<table class="ref">
  <thead><tr><th>Podmiot / narzędzie</th><th>E-mail / URL</th><th>Telefon</th><th>Zakres</th></tr></thead>
  <tbody>
    <tr><td><strong>TSCNET (CCC)</strong></td><td>operator@tscnet.eu</td><td>+49 89 45554 201</td><td>Operator CCCt — decyzje backup/kill</td></tr>
    <tr><td><strong>Coreso (CCC)</strong></td><td>day-ahead.engineer@coreso.eu</td><td>+32 2 743 21 10</td><td>Principal contact, scalanie CGM</td></tr>
    <tr><td><strong>USY IDCC</strong></td><td>idcc.helpdesk@unicorn.com</td><td>+420 221 400 540</td><td>Helpdesk CCCt (GUI, pliki, obliczenia)</td></tr>
    <tr><td><strong>USY ECP/EDX</strong></td><td>global-ecp@unicorn.com</td><td>+420 221 400 902</td><td>Kanał ECP/EDX</td></tr>
    <tr><td><strong>Raport CCA</strong></td><td>kdm6@pse.pl</td><td>—</td><td>Skrzynka raportów walidacji</td></tr>
    <tr><td><strong>PSE Innowacje</strong></td><td>zgłoszenie przez CIZ/WPO</td><td>—</td><td>Connector 2.0, SFTP, MinIO</td></tr>
  </tbody>
</table>
<p class="note">Pełna lista kontaktów Core (114 pozycji, per TSO): <i>Core_Operational_Contact_List.xlsx</i>, arkusz „IDCC (TSO only)".</p>'''
minio_body = ('<div class="ref">' + inw_slice('# 5. Buckety','# 7. TODO','# 5. Buckety') + '</div>' + kontakty_body)

checklisty_body = v52_slice('aneks')

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
<title>Procedura IDCC TSO v7 — kompletna instrukcja z ekranami</title><style>{CSS}
/* v5_2 compat */
.tbl-wrap{{overflow-x:auto}} .subhead{{font-weight:700;color:var(--acc);margin:.8em 0 .3em}}
.branch{{border-left:3px solid var(--bd);padding:6px 12px;margin:8px 0;background:#fafbfc;border-radius:0 6px 6px 0}}
.sdot{{display:inline-block;width:12px;height:12px;border-radius:3px;vertical-align:middle;margin-right:4px}}
.tile-state img{{vertical-align:middle}}
.risk-h{{border-top:2px solid var(--bd);padding-top:12px;margin-top:1.6em}}
.riskbase h5{{color:var(--acc)}}
/* stickery */
.stickgrid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px;margin:16px 0}}
.stick{{background:linear-gradient(160deg,#fffef4,#fff7d9);border:1px solid #ecd98a;border-left:5px solid #e0b400;
border-radius:10px;padding:12px 15px;box-shadow:0 1px 3px rgba(0,0,0,.07);break-inside:avoid}}
.stick h4{{margin:.1em 0 .5em}}
.stick ol{{margin:0;padding-left:20px}}
.stick li{{margin:4px 0;font-size:13.5px;line-height:1.35}}
.stick a{{color:var(--fg);text-decoration:none;border-bottom:1px dotted var(--acc)}}
.stick a:hover{{color:var(--acc)}}
</style></head><body>
<div class="wrap">
<nav><h2>Spis treści</h2>{nav_html}</nav>
<main id="top">
<span class="tag">FBA_TSO_IDCC · v7</span>
<h1>Procedura operacyjna dyspozytora PSE — proces IDCC</h1>
<h2 style="border:none;margin-top:.2em">Kompletna instrukcja eksploatacyjna TSO (region Core)</h2>
<p class="lead">Jeden dokument: proces wg BPD, harmonogram HLBP, katalog plików i stanów,
czynności w narzędziach ze zrzutami ekranu, walidacja FBA, ryzyka i procedury backupowe,
szablony maili, kontakty i checklisty. Na końcu <a href="#sec-stickery"><b>STICKERY</b></a> —
krótkie kroki z hiperłączami do pełnych opisów.</p>
{section('sec-cel','Cel, zakres i definicje','1',cel_body,[('#sec-proces','proces'),('#sec-harmonogram','harmonogram')])}
{section('sec-proces','Proces IDCC — kroki istotne dla PSE (BPD)','2',proces_body2,[('#sec-katalog','katalog plików'),('#sec-harmonogram','harmonogram')])}
{section('sec-harmonogram','Harmonogram HLBP (CCCt 4.2)','3',load_frag7('frag7_harmonogram.html'),[('#sec-happyday','przebieg nominalny'),('#sec-katalog','TET/CET plików')])}
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
<footer style="margin:3em 0 2em;color:var(--mut);font-size:13px;border-top:1px solid var(--bd);padding-top:14px">
PROCEDURA_IDCC_TSO_v7 — wygenerowano automatycznie ze źródeł: Core IDCC BPD v5.0, HLBP CCCt 4.2 v1,
PROCEDURA_IDCC_TSO_v5_2, FBA_TSO_NOR_03 v0.21, FBA_TSO_BUP_03 v0.32, QuickRef/Skrócona v4.1,
Inwentarz_IDCC, Ryzyka_pelna_baza (R01–R29), staticHints ({sum(len(v) for v in HINTS.values())} stanów),
popup_content ({len(FILES)} plików), screens_manifest (309 ekranów), Email_Templates (19 szablonów).
Każde ryzyko zgłaszać do: <b>CIZ, WPO, PSE-I (PSE Innowacje)</b>.</footer>
</main></div></body></html>"""

doc = denumber(doc)
doc = re.sub(r'Happy\s+Day', 'Stan poprawny / nominalny', doc)
doc = re.sub(r'(?i)bra\s+diostepu', 'brak dostępu', doc)

# ── walidacja kotwic stickerów ────────────────────────────────────────────────
ids = set(re.findall(r'id="([^"]+)"', doc))
missing = [h for _,steps in STICKER_STEPS for _,h in steps if h.lstrip('#') not in ids]
assert not missing, f"Brakujące kotwice stickerów: {missing}"

OUT.write_text(doc, encoding='utf-8')
print('Zapisano:', OUT)
print('Rozmiar:', OUT.stat().st_size, 'B |', doc.count('<figure'), 'figur |',
      doc.count('class="icell"'), 'ikon |', len(FILES), 'plików |',
      sum(len(v) for v in HINTS.values()), 'stanów | kotwice stickerów OK')

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
