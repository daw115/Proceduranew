# Pytania do rozstrzygnięcia — Walidacja domeny FBA IDCC (v0.2)

> Dokument roboczy towarzyszący [FBA_TSO_IDCC_Walidacja_domeny_v0.2.html](FBA_TSO_IDCC_Walidacja_domeny_v0.2.html).
> Każda pozycja odpowiada znacznikowi `[DO POTWIERDZENIA #N]` w treści procedury (Załącznik C) oraz wierszowi
> tabeli w [PLAN_Walidacja_domeny_FBA_IDCC.md](PLAN_Walidacja_domeny_FBA_IDCC.md) §5.2.
> Po otrzymaniu odpowiedzi: zaktualizować treść procedury w miejscu znacznika, usunąć znacznik, odnotować
> zmianę w tabeli „Poprzednie wersje" (metryka dokumentu) i odhaczyć pozycję w PLAN §5.2.

**Stan na:** 17.07.2026 · **Wersja procedury:** v0.2 DRAFT

---

## Do PSE-I (PSE Innowacje)

### #1 — Maski nazw paczek sFTP ↔ Perun4V i skład agregatu AGR_PERUN_IDx

**Kontekst:** procedura opisuje (§3.1 pkt 3, [v0.2#r31](FBA_TSO_IDCC_Walidacja_domeny_v0.2.html#r31)) przekazanie
paczki AGR_PERUN_IDx z Connector 2.0 do sFTP pod maską czytaną przez Perun4V, analogicznie do znanej z procesu DA
maski `PSE_RRRRMMDD_DA_v*_input_validation_DACCA.zip`. Dla iteracji ID2/ID3C/ID3 maska nie została jeszcze
potwierdzona wprost w żadnym ze źródeł (BPD v5.0, Instrukcja CCM v2.6).

**Pytanie:** Jaka jest dokładna maska nazwy paczki AGR_PERUN_IDx dla każdej iteracji (ID2 / ID3C / ID3) i czy
skład agregatu (9 składowych wymienionych w §1.3/§3.2) jest identyczny dla wszystkich trzech iteracji, czy
różni się per iteracja?

**Odpowiedź / decyzja:**
_(miejsce na odpowiedź)_

---

### #6 — Minimalne oczekiwane wielkości plików paczki PERUN_IDx

**Kontekst:** §4.15 ([v0.2#b15](FBA_TSO_IDCC_Walidacja_domeny_v0.2.html#b15)) opisuje reakcję na status
„czerwony kafelek z wykrzyknikiem" (plik mniejszy niż oczekiwany), ale nie podaje progów wielkości per plik
składowy paczki.

**Pytanie:** Jakie są skonfigurowane w CCM minimalne oczekiwane wielkości (w bajtach lub jako % wielkości
referencyjnej) dla każdego z 9 plików składowych AGR_PERUN_IDx?

**Odpowiedź / decyzja:**
_(miejsce na odpowiedź)_

---

## Do właściciela procedur / WPO

### #2 — Numeracja procedury i podział na dokumenty

**Kontekst:** dokument roboczo nazwany `FBA_TSO_NOR_04` (tryb normalny) / `FBA_TSO_BUP_04` (tryb backupowy),
łączony w jeden plik HTML — wzorem po części na `FBA_TSO_NOR_03` / `FBA_TSO_BUP_03` (dwa osobne dokumenty
dla procesu DA).

**Pytanie:** Czy numeracja `NOR_04` / `BUP_04` jest właściwa (kolejny wolny numer w serii FBA_TSO), czy
istnieje inna obowiązująca konwencja numeracji dla procedur ID? Czy dokument ma zostać rozdzielony na dwa
osobne pliki (NOR + BUP), tak jak w serii `_03` dla DA, czy pozostać jako jeden dokument łączony (obecna forma)?

**Odpowiedź / decyzja:**
_(miejsce na odpowiedź)_

---

### #4 — Wykonalność ponownego przeliczenia w Perun4V z dodatkowym wyłączeniem

**Kontekst:** §4.9 ([v0.2#b9](FBA_TSO_IDCC_Walidacja_domeny_v0.2.html#b9)) opisuje procedurę dodania wyłączenia
awaryjnego i ponownego uruchomienia obliczeń w Perun4V. Okno walidacji IDCC trwa 40 minut łącznie (pierwsza
faza automatyczna + ewentualna faza ręczna z wyłączeniem).

**Pytanie:** Czy operacyjnie da się zmieścić: (a) identyfikację potrzeby dodatkowego wyłączenia, (b) konfigurację
w Perun4V (Configurations → CC Validation Region), (c) ponowne obliczenia i (d) wysyłkę wyniku przez CCM —
w pozostałym czasie okna 40-minutowego po zakończeniu pierwszej (automatycznej) fazy? Jeśli nie — jaki jest
realny czas trwania kroków (b)–(c) w Perun4V, żeby ustalić praktyczny próg decyzyjny?

**Odpowiedź / decyzja:**
_(miejsce na odpowiedź)_

---

### #5 — Ścieżki katalogów sieciowych dla plików IDCC

**Kontekst:** §4.1.1 ([v0.2#b1](FBA_TSO_IDCC_Walidacja_domeny_v0.2.html#b1)) odsyła do zapisu pobranej paczki
w katalogu sieciowym dedykowanym iteracji, przez analogię do ścieżki znanej z procesu DA:
`\\uo-data\ZUO\Pion_UOD\Wydzial_DP\MODELE\5_DYSP\FBA\...`.

**Pytanie:** Jaka jest dokładna ścieżka katalogu sieciowego dla plików roboczych procesu ID (paczki wejściowe,
wyniki Perun4V, raporty)? Czy struktura jest wspólna dla ID2/ID3C/ID3, czy każda iteracja ma osobny podkatalog?

**Odpowiedź / decyzja:**
_(miejsce na odpowiedź)_

---

## Do WPO / CORESO

### #3 — Nazwa kroku w CCCt View Results dla bulk edit IVA w procesie ID

**Kontekst:** §4.4 ([v0.2#b4](FBA_TSO_IDCC_Walidacja_domeny_v0.2.html#b4)) opisuje wprowadzenie IVA jako
20% Fmax przez zakładkę View Results → wybór kroku „Initial FB Computation" danej iteracji → Edit Bulk. Dla
procesu DA odpowiednikiem jest krok „Intermediate FB Computation V_1" — nazewnictwo kroków w View Results
dla procesu ID nie zostało jeszcze zweryfikowane.

**Pytanie:** Jaka jest dokładna nazwa kroku obliczeniowego w CCCt → View Results dla iteracji ID2 / ID3C / ID3,
odpowiadającego etapowi Initial FB Computation, do którego należy zastosować Edit Bulk (MinRAM%_Core zeroBalanced,
20%)?

**Odpowiedź / decyzja:**
_(miejsce na odpowiedź)_

---

## Do redakcji / stanowisko VI (materiał własny)

### #7 — Zrzuty ekranu dedykowane iteracjom IDx

**Kontekst:** w v0.2 osadzono 8 rysunków (Załącznik C, poz. 7 zaktualizowana). Trzy z nich — Rysunek 3
([v0.2#rys3](FBA_TSO_IDCC_Walidacja_domeny_v0.2.html#rys3), schemat wymiany danych), Rysunek 5
([v0.2#rys5](FBA_TSO_IDCC_Walidacja_domeny_v0.2.html#rys5), okno Perun4V) i Rysunek 6
([v0.2#rys6](FBA_TSO_IDCC_Walidacja_domeny_v0.2.html#rys6), e-mail CCA) — pochodzą tymczasowo z materiałów
procesu DA (brak w repozytorium dedykowanych zrzutów dla procesu ID). Rysunek 8 (formatka wysyłki backupowej
IVA BACKUP) nie ma jeszcze zrzutu samej formatki z uzasadnieniem — tylko menu kontekstowe.

**Pytanie / zadanie:** Wykonać i dostarczyć zrzuty ekranu: (a) schemat wymiany danych CN2/MinIO/sFTP/Perun4V/CCA
dedykowany procesowi ID (bucket `ID_FBCC`, bez gałęzi LTA); (b) okno Perun4V z widoczną kolumną Business Process
dla jednej z iteracji IDx; (c) przykładowy e-mail CCA dla iteracji IDx (zamiast przykładu F310/DA); (d) formatka
wysyłki backupowej IVA BACKUP w CCM z wypełnionym polem uzasadnienia.

**Status:** materiał do zebrania na stanowisku dyspozytorskim VI przy najbliższej dostępnej iteracji IDCC(b)–(d).

---

## Podsumowanie

| # | Pozycja | Adresat | Sekcja procedury |
|---|---|---|---|
| 1 | Maski paczek sFTP↔Perun4V + skład agregatu | PSE-I | [§3.1](FBA_TSO_IDCC_Walidacja_domeny_v0.2.html#r31) |
| 2 | Numeracja i podział dokumentu | WPO / właściciel procedur | metryka dokumentu |
| 3 | Nazwa kroku View Results (bulk edit) | WPO / CORESO | [§4.4](FBA_TSO_IDCC_Walidacja_domeny_v0.2.html#b4) |
| 4 | Wykonalność przeliczenia z wyłączeniem w 40 min | WPO | [§4.9](FBA_TSO_IDCC_Walidacja_domeny_v0.2.html#b9) |
| 5 | Ścieżki katalogów sieciowych | WPO | [§4.1](FBA_TSO_IDCC_Walidacja_domeny_v0.2.html#b1) |
| 6 | Minimalne wielkości plików paczki | PSE-I | [§4.15](FBA_TSO_IDCC_Walidacja_domeny_v0.2.html#b15) |
| 7 | Zrzuty ekranu dedykowane IDx (rys. 3, 5, 6, 8) | redakcja / stanowisko VI | Załącznik C |
