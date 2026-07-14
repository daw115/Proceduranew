# Kontekst projektu Procedura IDCC

Aktualizacja: 2026-06-25

## Cel
Procedura operacyjna obsługi punktu IDCC dla TSO (PSE) + monitorowanie CCM
(Capacity Calculation Module). Dwa nurty: (1) dokument procedury HTML/DOCX/PDF,
(2) dane dla pulpitu CCM (mapowanie kafelków na statusy programu).

## Najnowsza praca (24.06)
- `_build_statichints.py` — generator słownika `staticHints` (TypeScript) dla
  WSZYSTKICH plików IDCC. Źródła:
  - `Stany_kafelkow_per_plik_IDCC.xlsx` (stany per kod: marker+fill = kafelek,
    pełne ramki: sytuacja, procedury awaryjne, opis pliku, ścieżka)
  - `CCM/staticHints-przyklad-dla-FID1-831.txt` (wzór formatu + enumy AC do walidacji)
- Wynik: `CCM/staticHints-IDCC-all.txt` (9590 linii)
  - **71 kluczy** w formacie `'NAZWA^KOD'` (np. `AC^FID1-831`, `IVA^FID2-710`,
    `Final Intraday NTC^FID3-921`)
  - **974 stany** (bloki `status:` → DashboardItemStatus)
  - **0** oznaczeń `/*?*/` — mapowanie pełne wg oficjalnej legendy enumów
- Mapowanie kafelek(marker,fill) → DashboardItemStatus: 13 kombinacji 1:1
  (UNKNOWN, FAILURE, SUCCESS, FORCEDSUCCESS, SENTMANUALLY, SENTMANUALLYAFTERCET,
  ACKNOTRECEIVED, WARNING, EXCEEDED, FILESIZEBAD, PROCESSRUNNING, CONN_AFTER_CET)
- Walidacja: skrypt sprawdza dokładność per-enum na wzorze AC 831 (ma być 100%);
  dedup identycznych stanów (IDCC(b)+IDA3 po usunięciu godzin)
- Arkusze źródłowe (7): AC 831 (2CCT), GLSK CBCORA 607-617 (2CCT),
  ATC 928 (zwrotny), IVA 710 (3COL), Paczki PERUN (2MS), Skladowe MinIO (MIN),
  sFTP-ZP NTC MD250 IGM (SFTP)

## Wcześniej (22.06 i starsze)
- `PROCEDURA_IDCC_TSO_v5_2.html` / `.pdf` / `_EDYTOR.html` / `.docx` — pełna
  procedura z monitorowaniem CCM (kafelki, 82 stany, pulpit, instrukcja dyspozytora)
- `CCM/info.pdf` (6.4 MB) + `_build_info_pdf.py`
- `CCM/mail_opis_prac.html` + `_build_mail.py` — mail z opisem prac
- `CCM/edytowalny-info.docx`
- Komplet popupów `Przyklady_FID*` (FID1/2/3/3C × 607/617/831/928)
- `img_ccm/tiles/` — ikony kafelków (13 png: kolory + markery R/W/q/!/excl)

## Nowy dokument v6 (25.06)
- `_build_procedura_v6.py` → `PROCEDURA_IDCC_TSO_v6.html` (~894 KB) — szczegółowa instrukcja
  z ekranami + karty-stickery (skrót z hiperłączem do detalu).
- Dwuwarstwowa: tablica 13 kart-stickerów (cover) + mini-stickery per sekcja → detal.
- 13 sekcji: proces, narzędzia N01–N22, legenda statusów (kafelki img_ccm/tiles),
  katalog 126 plików FIDx (z 974 stanami z staticHints), czynności CCM (C.1–C.5),
  walidacja NOR, walidacja BUP, GLSK 607 (32 stany), Kreator IDCF, AC w ZP,
  procedury P01–P06, ryzyka U01–U23, buckety MinIO + mapa relacji.
- **301 screenów wpiętych** z manifestu (audyt 309 ekranów: 234 clear, 67 cropped,
  6 dup, 2 blurred). Manifest: `screens_manifest.json` (+ części `screens_manifest_*.json`).
- Sekcje referencyjne (narzędzia/ryzyka/procedury/buckety) generowane z `Inwentarz_IDCC.md`
  (markdown→HTML, wycinki bez duplikacji).
- Zweryfikowane w przeglądarce (preview): 126 kart, 126 tabel stanów, 13 sekcji,
  0 brakujących obrazów, 0 błędów konsoli.
- DO ZROBIENIA: eksport DOCX/PDF (master = HTML); PDF wymaga paginacji (strona ~64000 px).

## v6 — rozszerzenia (26.06)
- Narzędzia BEZ numeracji Nxx: nagłówki = unikalna nazwa, kotwice #Nxx wewnętrznie; ścieżki katalogu +
  źródła = hiperłącza do definicji (304 linki). Transform: `denumber()` / `linkify_refs()` / CODE2NAME.
- Tabele stanów: kolumna „Status kafelka" = graficzne KAFELKI (img_ccm/tiles), nie opis słowny
  (2492 kafelki; ENUM2TILE, status_tile(); opis statusu w tooltipie).
- Podpisy screenów BUP naprawione (38 bez diakrytyków → poprawione); wykluczone nieczytelne/duplikaty (299 screenów).
- OPIS PROCESU (BPD) w sekcji 1 — wersja PSE-FOCUSED (finalna, zastąpiła pełne tłumaczenie):
  tylko kroki istotne dla PSE, nazwy pod-procesów PO ANGIELSKU, IDCC(a) osobno,
  IDCC(b)–(d) JAKO JEDEN opis z tabelą różnic (FID2/FID3C/FID3), kody FIDx, bardzo treściwie.
  Fragmenty: `process2_glos.html` (skróty EN, zakres PSE, 8 plików wejściowych),
  `process2_a.html` (7 kroków, 9 fallbacków PSE), `process2_bcd.html` (11 kroków, 18 FIDx),
  `process2_mail.html` (19 szablonów maili Core ID 01–20 bez 15, treść EN, „Kiedy" PL,
  znacznik „⚑ dotyczy granic PSE" → .psemark). Źródła: Core_IDCC_BPD.txt + Email_Templates_IDCC.txt
  (kopia z /Volumes/SSD/Downloads/proceduraaaaa/Email_Templates_for_Go_live_Core_IDCC.docx — to TXT).
  Pod-nawigacja: #proc-pse/#proc-a/#proc-bcd/#proc-mail. Stare `process_*.html` (pełne tłumaczenie,
  203 KB) zostają na dysku, ale NIE wchodzą do dokumentu.
- STICKERY: tablica 14 kart (dodany 📧 Szablony maili → #proc-mail). Generator tworzy też
  `STICKERY_IDCC.md` — wkład do stickerów (karty skrócone + hiperłącza do kotwic v6, z jednego
  źródła STICKERS + mini-stickery sekcji).
- staticHints zaktualizowany zewnętrznie 26.06 05:53 → 986 stanów (było 974); dokument odzwierciedla.

## v6 — kontrola jakości i przebudowa (14.07)
- Przegląd tekstowy fragmentów procesowych: poprawione niezgrabne strony bierne i kalki
  („PSE jest przypomniane" → „PSE otrzymuje mailowe przypomnienie", „PSE dotknięte" →
  „PSE monitoruje wynik na swoich granicach", „PSE informowane (TSO); UMM" → pełne zdania,
  „plik brakuje" → „brakuje pliku"); „DISCLAIMER" → „Uwaga"; „Pliki wejściowe PSE" →
  „Kluczowe pliki PSE" (tabela zawiera też pliki zwrotne). 0 słów bez diakrytyków.
- Kontrola screenów (PIL): 309/309 plików istnieje, 0 uszkodzonych. 52 mikro-wycinki ikon
  (<140×140 px) przeniesione z galerii do zwartych pasków „Elementy interfejsu" w rozmiarze
  rzeczywistym (is_micro(), .iconstrip) — nie są już rozciągane na szerokość kolumny.
- Wynik przebudowy: 253 figury + 46 ikon w paskach; 19 kart maili; 2492 kafelki stanów
  (126 wpisów katalogu → 71 unikalnych kodów → 1552 stany; 9 nowych kodów z staticHints
  nie występuje w katalogu popup_content, stąd bez zmiany liczby kafelków).
- STICKERY_IDCC.md przegenerowany (14 kart).

## v7 — KOMPLETNA procedura (14.07 wieczór)
- `_build_procedura_v7.py` → `PROCEDURA_IDCC_TSO_v7.html` (1,16 MB, 18 sekcji) — "wszystko
  istotne z perspektywy TSO, skondensowane": BPD (process2_*), harmonogram HLBP CCCt 4.2
  (frag7_harmonogram, tabela zbiorcza wg Skróconej v4.1 + 51 wierszy faz z xlsx + korekty
  v4_1_official), przebieg nominalny + ERR-I/Process failed/B1–B4 (frag7_happyday z QuickRef
  i Skróconej), maski IVA/numery MV/timestampy Perun/ścieżki MinIO (frag7_maski), walidacja
  NOR v0.21 + BUP v0.32 z F109→F308 (frag7_walidacja), slice'y v5_2 (v52_slice/v52_h3block:
  §4A–4D=#s4a–d, §5+§6 w details, 7M.1/3/7–14 z idkami ccm-*, §8=#s8, aneks=#aneks),
  pełna baza ryzyk R01–R29 (Ryzyka_pelna_baza md→HTML) + U-kody/ACK w details, kontakty
  operacyjne (CCC/USY/kdm6 z telefonami), katalog 78 plików/965 stanów, 19 maili, 253 figury.
- STICKERY: sekcja 18 NA KOŃCU dokumentu — 9 grup scenariuszy, 41 krótkich kroków w punktach,
  KAŻDY krok = hiperłącze do kotwicy w procedurze; walidacja kotwic asercją w buildzie.
  Cover board usunięty. STICKERY_IDCC.md przegenerowany w tym samym formacie.
- Poprawki w buildzie: gołe kody Nxx ze slice'ów → linki z nazwą narzędzia (denumber rozszerzony),
  balans divów slice'ów (_div_balance), normalizacja Happy Day.
- `_gen_pdf.py` sparametryzowany (argv) → output/PROCEDURA_IDCC_TSO_v7.pdf (158 KB).
- v6 nietknięta. Agenci treściowi padli na limicie sesji — fragmenty zbudowane inline
  (slice v5_2 zamiast przepisywania; autorskie tylko harmonogram/maski/happyday/walidacja).

## v7 — warstwa komentarzy recenzenta (14.07 noc)
- `_comments_widget.html` wpinany przez generator przed </body> (poza f-stringiem).
  Offline: tryb komentowania (klik w blok, opcjonalny cytat z zaznaczenia), pinezki numerowane,
  panel z listą (skok do celu + flash), edycja/usuwanie, localStorage (klucz idcc_v7_comments),
  eksport/import JSON + eksport Markdown (do przekazania zmian), ukryty w druku.
- Naprawa v52_slice: fallback końca dokumentu (v5_2 nie ma </main>, ma podwójny </body></html>) —
  aneks nie wciąga już ogona; defensywne czyszczenie </body>/</html> ze slice'ów.
- Test funkcjonalny headless Chrome: render() OK, seed 2 komentarzy → panel + pinezki OK.

## Stan
Generator staticHints zakończony (80 kodów / 965 stanów po aktualizacji 14.07 — 32 → 29; katalog używa 71).
Dokument v6 (HTML master, ~1,21 MB) FINALNY po QC tekstowo-wizualnym + feedback Maria Rutkowska:
usunięto z staticHints 3 niemożliwe stany GLSK (SUCCESS+FAILURE, SUCCESS+ACKNOTRECEIVED, SUCCESS+EXCEEDED).
Eksport DOCX/PDF — do zrobienia.

## Pliki kluczowe
- Generator: `_build_statichints.py`
- Wynik dla CCM: `CCM/staticHints-IDCC-all.txt`
- Źródło danych: `Stany_kafelkow_per_plik_IDCC.xlsx`
- Wzór formatu: `CCM/staticHints-przyklad-dla-FID1-831.txt`
- Procedura: `PROCEDURA_IDCC_TSO_v5_2.html`
## Sesja: 2026-06-25 15:12:44
Katalog: /Volumes/SSD/CLAUDE_WORK/Procedura

## Sesja: 2026-06-26 02:44:44
Katalog: /Volumes/SSD/CLAUDE_WORK/Procedura

## Sesja: 2026-06-26 02:52:32
Katalog: /Volumes/SSD/CLAUDE_WORK/Procedura

## Sesja: 2026-06-26 03:00:22
Katalog: /Volumes/SSD/CLAUDE_WORK/Procedura

## Sesja: 2026-06-26 03:02:17
Katalog: /Volumes/SSD/CLAUDE_WORK/Procedura

## Sesja: 2026-06-26 03:20:49
Katalog: /Volumes/SSD/CLAUDE_WORK/Procedura

## Sesja: 2026-07-14 12:15:36
Katalog: /Volumes/SSD/CLAUDE_WORK/Procedura

## Sesja: 2026-07-14 12:25:32
Katalog: /Volumes/SSD/CLAUDE_WORK/Procedura

## Sesja: 2026-07-14 17:07:04
Katalog: /Volumes/SSD/CLAUDE_WORK/Procedura

## Sesja: 2026-07-14 22:31:27
Katalog: /Volumes/SSD/CLAUDE_WORK/Procedura

## Sesja: 2026-07-14 22:46:26
Katalog: /Volumes/SSD/CLAUDE_WORK/Procedura

## Sesja: 2026-07-14 22:55:14
Katalog: /Volumes/SSD/CLAUDE_WORK/Procedura

