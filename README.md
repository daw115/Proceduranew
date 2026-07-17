# Proceduranew — generator dokumentacji procedury IDCC (TSO)

Repozytorium zawiera źródła i skrypty budujące operacyjną procedurę IDCC dla TSO
(PSE) w formatach HTML/PDF/DOCX oraz dane `staticHints` dla pulpitu CCM.

## Aktualny pipeline (v7 / final)

| Krok | Skrypt | Wynik |
|---|---|---|
| 1 | `_build_procedura_v7.py` | `PROCEDURA_IDCC_TSO_v7.html` (samowystarczalny, ~23 MB) + `STICKERY_IDCC.md` |
| 2 | `_build_procedura_final.py` | `PROCEDURA_IDCC_TSO_v7-final.html` + `STICKERY_IDCC-final.md` (layout `measured-flow`; uruchamia też `_build_design_canvas.py`) |
| 3 | `_gen_pdf.py PROCEDURA_IDCC_TSO_v7` | `output/PROCEDURA_IDCC_TSO_v7.pdf` |

```bash
pip install -r requirements-final.txt   # dokładnie Markdown==3.10.2 + Pillow==12.3.0
python3 _build_procedura_v7.py
python3 _build_procedura_final.py       # wymaga pinowanego fontu Noto Sans (patrz niżej)
python3 _gen_pdf.py PROCEDURA_IDCC_TSO_v7
```

Podgląd: `python3 -m http.server 8770` i otwarcie wygenerowanego HTML
(konfiguracja `procedura` w `.claude/launch.json`).

Uwagi:

- Wygenerowane artefakty (`PROCEDURA_IDCC_TSO_v7*.html`, `output/`, itd.) **nie są
  wersjonowane** — buduje się je lokalnie.
- `_build_design_canvas.py` renderuje okładkę `IDCC_DESIGN_CANVAS_FINAL.png`
  deterministycznie: wymaga Pillow 12.3.0, FreeType 2.14.3 i pliku
  `NotoSans[wght].ttf` o pinowanym sha256. Ścieżkę do fontu wskazuje zmienna
  `PROCEDURA_FONT_PATH` (domyślnie ścieżka linuksowa). Gotowy PNG jest w repo,
  więc przebudowa okładki zwykle nie jest potrzebna.
- Build v7 ma wbudowane asercje QA (struktura dokumentu, ankory, zakazane frazy) —
  build, który przechodzi bez wyjątków, jest zweryfikowany.

## Kluczowe pliki źródłowe (wejścia buildu v7)

- `screens_manifest.json` — manifest zrzutów ekranu (dokładnie 309 pozycji)
- `popup_content_IDCC.json`, `CCM/staticHints-IDCC-all.txt` — treści popupów / hinty CCM
- `Inwentarz_IDCC.md`, `Ryzyka_pelna_baza_IDCC.md`, `Karta_ryzyk_IDCC.md`, `STICKERY_IDCC.md`
- `PROCEDURA_IDCC_TSO_v5_2.html` — **wejście** (v7 wycina z niego sekcje); nie usuwać
- fragmenty `process2_*.html`, `frag7_*.html`, `_comments_widget.html`
- katalogi obrazów: `screens/`, `screens_fid607/`, `screens_kreatoridcf/`, `img_ccm/`, `CCM/`
- `PROCEDURA_IDCC_TSO_v6 copy.html` — wejście `generate_full.py` (mimo nazwy „copy")

## Skrypty legacy (poprzednie wersje dokumentu)

`_build_procedure.py` (v5.2; baza v5.1 spoza repo — ścieżka przez env
`PROCEDURA_V51_SRC`), `_build_docx.py` (v5.2→DOCX, wymaga `pandoc`),
`_build_procedure_pdf.py` (v5.2→PDF), `_build_procedura_v6.py` (v6),
`generate_full.py` (ekstrakcja z v6). Pozostawione dla
odtwarzalności historycznych wersji; pełne zależności: `pip install -r requirements.txt`.

## Narzędzia pomocnicze

- `_build_statichints.py` — `Stany_kafelkow_per_plik_IDCC.xlsx` → `CCM/staticHints-IDCC-all.txt`
- `_build_naklejki.py` / `_build_info_pdf.py` — naklejki i `CCM/info.pdf`
  (oba skrypty nadpisują ten sam `CCM/info.pdf`; wersją nadrzędną jest
  `_build_info_pdf.py` — uruchamiać go jako ostatni)
- `_build_mail.py` — `CCM/mail_opis_prac.html`

## Bieżąca praca merytoryczna

Procedura walidacji domeny FBA dla IDCC — patrz `PLAN_Walidacja_domeny_FBA_IDCC.md`
(roadmapa v0.1 → 1.0) i draft `FBA_TSO_IDCC_Walidacja_domeny_v0.2.html`. Otwarte pytania
do PSE-I/WPO/CORESO zebrane w `TODO_Pytania_FBA_IDCC_v0.2.md`.
Filozofia wizualna dokumentu: `IDCC_DESIGN_PHILOSOPHY.md` („Mierzony Przepływ").
