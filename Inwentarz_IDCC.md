# Inwentarz IDCC — Master Reference

> **Cel:** Jeden dokument referencyjny agregujący narzędzia, ryzyka, stany kafelków, procedury i buckety MinIO dla całego procesu IDCC.
> Inne dokumenty (karty FID, karty stanów) linkują tu jako master source.

> ⚠ **Każde ryzyko należy zgłosić do: CIZ, WPO, PSE-I (PSE Innowacje).**

**Źródła pierwotne:**
- HTML procedura IDCC (FBA_TSO_IDCC v1.0 FINAL DRAFT)
- FBA_TSO_BUP_03 — Walidacja domeny FBA v0.31 (BUP DA)
- FBA_TSO_NOR_03 — Walidacja domeny FBA v0.21 (NOR DA)
- CCM Instrukcja Użytkownika Dyspozytora v2.6
- Confluence „ID FB CC Zawartość opisów biznesowych do podpowiedzi na pulpicie dyspozytorskim dla pozycji IVA i IVA Backup" v.X
- AC manuall ZP.docx

---

## Spis treści

1. [Narzędzia](#tools) — N01–N22 (wewnętrzne PSE, zewnętrzne, zgłoszenie)
2. [Stany kafelków](#states) — legenda + macierze per profil (3COL, 2CCT, 2MS, MIN, SFTP)
3. [Ryzyka uniwersalne U01–U23](#risks) — definicje + mapowanie źródeł
4. [Procedury P01–P06](#procedures) — działania backupowe + procedury narzędziowe (krok po kroku)
5. [Buckety MinIO](#buckets) — pełna mapa lokalizacji plików
6. [Mapa relacji](#matrix) — narzędzie ↔ ryzyko ↔ procedura
7. [TODO — do dopytania](#todo)

---

<a id="tools"></a>
# 1. Narzędzia

## 1.A. Wewnętrzne PSE

<a id="N01"></a>
### N01 — CCM (Capacity Calculation Monitoring)
- **URL:** https://ccm.spsm.pse.pl
- **Funkcja:** główny pulpit dyspozytorski; monitoring statusów wszystkich kafelków IDCC; ręczna wysyłka plików (PPM → Wyślij); ustawianie statusu ręcznego 'R'; opcja „Wyślij po CET"
- **Pulpity:** *„IDCC FB Pulpit dyspozytorski"*, *„IDCC (do 3C) z ATC i SFTP Pulpit dyspozytorski"*
- **Tryby odświeżania:** ultraszybki (10s) / szybki (30s) / wolny (5 min)
- **Powiązane ryzyko:** [U01](#U01) (brak dostępu)
- **Procedury:** ustawianie statusu ręcznego — patrz [Logowanie i nawigacja w CCM](#proc-ccm)

<a id="N02"></a>
### N02 — Core CC Tool (CCCt)
- **URL:** (zewnętrzny URL CCCt — zgodnie z aktualną konfiguracją)
- **Funkcja:** system centralny procesu; Message Viewer (status pliku, kody ACK); Manual Upload (ręczna wysyłka pliku z dysku); publikacja wyników do PuTo
- **Selektor procesu:** `ID1`, `ID2`, `ID3C`, `ID3` *(IDCC)* vs domyślny `DA` *(Day-Ahead)*
- **Powiązane ryzyko:** [U02](#U02) (brak dostępu)
- **Procedury:** [Logowanie i nawigacja w Core CC Tool](#proc-cct), [P01](#P01) Manual Upload

<a id="N03"></a>
### N03 — Perun4V
- **URL:** https://lccv.tscnet.eu
- **Funkcja:** narzędzie walidacji FBA — wykonuje obliczenia IVA dla danej doby; pokazuje status obliczeń (Successful / ERR-I / Process failed); umożliwia ręczne uruchomienie procesu
- **Logowanie:** Local Login → username/password → akceptacja TSCNET Policy
- **Powiązane ryzyko:** [U05](#U05) (brak dostępu)
- **Procedury:** [Logowanie i nawigacja w Perun4V](#proc-perun), [P03](#P03) Ręczne uruchomienie obliczeń

<a id="N04"></a>
### N04 — MinIO
- **URL:** https://minio-gui.pse.pl
- **Funkcja:** centralne repozytorium plików procesowych w sieci PSE; buckety: `perun/`, `cca/`, `mam/`
- **Powiązane ryzyko:** [U04](#U04) (brak dostępu)
- **Procedury:** [Logowanie i nawigacja w MinIO](#proc-minio), [P04](#P04) Pobranie z MinIO

<a id="N05"></a>
### N05 — Connector 2.0 (CN2)
- **Lokalizacja:** narzędzie transportowe działa w tle
- **Funkcja:** główny kanał transportu plików w PSE: CCM ↔ CCCt ↔ MinIO ↔ Perun4V
- **Stworzony przez:** PSE Innowacje
- **Powiązane ryzyko:** [U03](#U03) (awaria, obejmuje też scalone U18 — Connector nie kopiuje do bucketów)

<a id="N06"></a>
### N06 — ZP (zdolności przesyłowe)
- **Lokalizacja:** aplikacja desktop na komputerze dyspozytorskim
- **Funkcja:** źródło plików **AC (FIDx-831)** dla iteracji IDCC; bilans AC; generowanie nowych wersji
- **Powiązane ryzyko:** [U06](#U06) (brak dostępu / brak wersji)
- **Procedury:** [Logowanie i nawigacja w ZP](#proc-zp), [P02](#P02) Pobranie z ZP

<a id="N07"></a>
### N07 — KreatorDACF&2DAF_CGMES
- **Lokalizacja:** aplikacja PSE / PLANS
- **Funkcja:** generator IGM (Individual Grid Model) i plików wejściowych — **dla iteracji IDCC(b)**: FID2-607 (GLSK), FID2-617 (CBCORA)
- **Powiązane ryzyko:** [U06](#U06) (brak dostępu / błąd generowania)

<a id="N08"></a>
### N08 — KreatorIDCF_CGMES
- **Lokalizacja:** aplikacja PSE / PLANS
- **Funkcja:** dla iteracji **IDCC(c), IDCC(d), IDCC(e)** generuje **modele IGM/CGM** oraz pliki **GLSK (FIDx-607)**, **CBCORA (FIDx-617)** i **RA (FIDx_RA — środki zaradcze)**; publikacja przez **Publikuj Connector**
- **Procedura ręczna (backup) ze screenami:** [Generowanie GLSK + CBCORA + RA w KreatorIDCF](Procedura_KreatorIDCF_GLSK_CBCORA.html) — uruchamiana, gdy auto-skrypt Monitora zgłosi BŁĄD
- **Pełna instrukcja narzędzia:** `IDCF_InstrUżytk_v5` (rozdz. „Tworzenie plików GLSK, CBCORA oraz RA"; też tworzenie modeli IDCF/IGM, CGMES, weryfikacja N-1)
- **Powiązane ryzyko:** [U06](#U06)

<a id="N09"></a>
### N09 — CCA (Capacity Calculation Application)
- **Lokalizacja:** aplikacja wewnętrzna PSE
- **Funkcja:** generowanie raportów walidacyjnych, **IVA BACKUP** (publikacja do `cca/ID_FBCC/out/[BD]/`), automatyczne wysyłki backupowe do CCCt
- **Powiązane ryzyko:** [U19](#U19) (niezgodność wersji IVA/Backup), [U23](#U23) (brak raportu CCA), [U18 scalone z U03](#U03) (Connector nie kopiuje IVA do bucketów CCA)
- **Zgłoszenie:** [Zespół utrzymania CCA N21](#N21)

<a id="N10"></a>
### N10 — PuTo (Platforma Udostępniania Transmisyjnych)
- **Lokalizacja:** wewnętrzny system PSE
- **Funkcja:** docelowy odbiorca pliku **AC (FIDx-831)** po publikacji przez Core CC Tool jako wynik IDCC(a)/IDCC(b)/(c)/(d)

<a id="N11"></a>
### N11 — kdm6@pse.pl
- **Lokalizacja:** skrzynka mailowa PSE
- **Funkcja:** kanał pasywny dla raportów: CCA (raporty walidacyjne, LTA_CURTAILMENT, IVA na CNECach), Perun4V (raporty po obliczeniach z informacją o policzonych godzinach i max IVA)
- **Powiązane ryzyko:** [U07](#U07) (brak dostępu)

<a id="N12"></a>
### N12 — sFTP@pse.pl
- **Lokalizacja:** protokół transportowy
- **Funkcja:** transport paczek ZIP z MinIO do Perun4V (i wyniki zwrotnie do MinIO/Connector 2.0)
- **Powiązane ryzyko:** wpisuje się w [U03](#U03) (jeśli sFTP nie działa, paczki nie dotrą do Perun4V)

## 1.B. Zewnętrzne (CCC / RCC / TSO)

<a id="N13"></a>
### N13 — RCC / TSCNET
- **Kontakt:** operator@tscnet.eu (lista operacyjna do telefonu)
- **Funkcja:** Regional Coordination Centre — koordynacja procesu IDCC; sterowanie fazami centralnymi (CGM merging, Domain calculation, NTC publication)

<a id="N14"></a>
### N14 — CORESO
- **Kontakt:** day-ahead.engineer@coreso.eu
- **Funkcja:** koordynacja po stronie operatora procesu

<a id="N15"></a>
### N15 — Core CC Tool (centralne procesy)
- **Funkcja:** publikacja wyników centralnych (FIDx-928 walidacja ATC, FID1-921 NTC, ID1-373 AAC); dyspozytor PSE wyłącznie monitoruje — nie wykonuje czynności wykonawczych

<a id="N16"></a>
### N16 — ECP/EDX (Energy Communication Platforms)
- **Funkcja:** protokół wymiany TSO ↔ CCCt — automatyczna wysyłka CB/GLSK/EC; ręczny upload przez CCCt GUI; dostarczenie Shadow Auction (MD250)
- **Powiązane ryzyko:** wpisuje się w [U21](#U21) (Decoupling SDAC — MD250)

<a id="N17"></a>
### N17 — XBID
- **Funkcja:** system aukcyjny intraday — odbiorca AAC (ID1-373-XX), NTC (FIDx-921)
- **Powiązane ryzyko:** [U20](#U20) (AAC Fallback), [U22](#U22) (Late NTC)

## 1.C. Zgłoszenie / wsparcie

<a id="N18"></a>
### N18 — WPO (Wydział Wsparcia Procesów Operatorskich)
- **Skład:** Słabicki, Jarzęcka, Krzysztoszek, Łukaszewski, Rodo
- **Funkcja:** zgłoszenie operacyjna; decyzje w sytuacjach niestandardowych

<a id="N19"></a>
### N19 — CIZ (Centrum Zgłaszania Incydentów PSE)
- **Lokalizacja:** wewnętrzny system PSE
- **Funkcja:** rejestracja incydentów (awarie narzędzi, problemy procesowe); priorytet zależny od fazy procesu

<a id="N20"></a>
### N20 — PSE Innowacje
- **Kanał:** wewnętrzny PSE
- **Funkcja:** utrzymanie narzędzi PSE — CCM, Connector 2.0, MinIO, sFTP
- **Zgłoszenie przy:** [U01](#U01), [U03](#U03), [U04](#U04)

<a id="N21"></a>
### N21 — Zespół utrzymania CCA
- **Kanał:** wewnętrzny PSE Innowacje (zespół CCA)
- **Funkcja:** utrzymanie aplikacji CCA, raportów walidacyjnych, IVA BACKUP, FID1-928
- **Zgłoszenie przy:** [U19](#U19), [U23](#U23)

<a id="N22"></a>
### N22 — Zespół utrzymania ZP
- **Kanał:** wewnętrzny PSE
- **Funkcja:** utrzymanie aplikacji ZP (zdolności przesyłowe) — źródła AC FIDx-831
- **Zgłoszenie przy:** [U06](#U06) (awaria ZP, brak generowania)

---

<a id="states"></a>
# 2. Stany kafelków

<a id="states-legend"></a>
## 2.A. Legenda kolorów + ikon

Źródło: PDF Dyspozytora s. 11–15, Confluence v.X

| Kolor / Symbol | Znaczenie | Typowy moment |
|---|---|---|
| `szary` | Plik nie wymagany (>30 min do TET) | Przed startem procesu |
| `pomarańczowy` | 30 min przed TET do 30 min przed CET — dokumentu nie ma | TET zbliża się |
| `czerwony` | Plik niedostarczony przed CET lub wysyłka zakończyła się błędem | CET zbliża się |
| `czerwony !` | Plik dostarczony, ale rozmiar < minimum | Po dostarczeniu |
| `czerwony ?` | Brak ACK / proces nie skończył się w czasie | Po wysyłce |
| `zielony` | Plik dostarczony, ACK pozytywny (Processed) | Happy Day |
| `ciemnozielony 'W'` | Dostarczone ręcznie z CCM przed CET | Po C.4 |
| `ciemnozielony 'W po CET'` | Dostarczone ręcznie z CCM po CET | Po C.5 |
| `zielony 'R'` | Status ręczny nadany przez Dyspozytora | Po ręcznej decyzji |
| `fioletowy` | Dostarczone i zwalidowane po CET, ACK pozytywny | Opóźnienie automatyczne |
| `czarny` | Plik nie dostarczony, minął CET | Krytyczne |
| `spinner` (kółko) | Operacja w toku — wysyłka backupowa do CCCt | IVA Backup automat |
| `red_pulse` (zielony z pulsującą czerwoną obwódką) | Nowa wersja IVA Backup wymaga monitoringu | Scenariusz 4 |

<a id="states-3col"></a>
## 2.B. Profil 3COL — CCTool wyśl. + CCTool zwalid. + MinIO

Stosowany dla **IVA (FIDx-710)**. Źródło: Confluence PDF, opis dla pozycji IVA.

| # | CCTool wyśl. | CCTool zwalid. | MinIO | Co oznacza | Ryzyka | Procedura |
|---|---|---|---|---|---|---|
| 1 | szary | szary | szary | Plik jeszcze nie wysłany ani do CCCt ani na MinIO. Brak ACK. | — | monitoring |
| 2 | pomarańczowy | pomarańczowy | pomarańczowy | Zbliża się TET, dokument nie obsłużony. | [U02](#U02), [U03](#U03) | sprawdź CCCt MV / MinIO |
| 3 | czerwony | czerwony | czerwony | Zbliża się CET, dokument nie obsłużony. Możliwa ręczna wysyłka IVA Backup. | [U03](#U03), [U08](#U08) | [P01](#P01) lub [P02](#P02) |
| 4 | czarny | czarny | czarny | Dokument niedostarczony ani do CCCt ani na MinIO, minął CET. | [U03](#U03), [U08](#U08), [U16](#U16) | zgłoś + telefon CCC; [P03](#P03) Perun4V |
| 5 | fioletowy | fioletowy | fioletowy | Dokument dostarczony do CCCt i na MinIO po CET, ACK pozytywny. | [U13](#U13) | [P06](#P06) wpis A.4 |
| 6 | zielony R | zielony R | zielony R | Dokument IVA oznaczony ręcznie jako wysłany OK. | [U13](#U13) | [P06](#P06) |
| 7 | zielony | zielony | zielony | **Happy Day** — Processed w CCCt, IVA na MinIO. | — | brak |
| 8 | czerwony ? | (puste) | zielony | Wysyłka do CCCt trwa, ACK oczekuje. Dokument dostarczony na MinIO. | [U11](#U11) | po 5 min CCCt MV |
| 9 | zielony | (puste) | zielony | Plik wysłany OK, oczekiwanie ACK (<3 min). | [U11](#U11) | monitoring |
| 10 | zielony | czerwony ? | zielony | Brak ACK w żądanym czasie. Po najechaniu — czas oczekiwania. | [U11](#U11) | po 3 min CCCt MV |
| 11 | zielony | czerwony | zielony | ACK negatywny: kod 20/21/22/30 lub Błąd procesu. | [U10](#U10) | per kod ACK; [P01](#P01) |
| 12 | zielony | fioletowy | zielony | ACK pozytywny po CET. | [U13](#U13) | [P06](#P06) |
| 13 | zielony | czarny | zielony | ACK nie napłynął do CET. | [U03](#U03), [U11](#U11) | zgłoś; sprawdź CN2 |
| 14 | zielony | zielony R | zielony | Brak automatycznego ACK, Dyspozytor ustawił 'R' po weryfikacji. | [U13](#U13) | [P06](#P06) |
| 15 | czerwony ? | (puste) | czerwony ! | Wysyłka trwa; plik na MinIO ma za mały rozmiar. | [U09](#U09), [U11](#U11) | sprawdź rozmiar; [P02](#P02) |
| 16 | czerwony ! | (puste) | czerwony ! | Wysłany dokument za mały, ACK oczekuje. | [U09](#U09) | [P02](#P02) → [P01](#P01) |
| 17 | czerwony ! | czerwony ? | czerwony ! | Za mały rozmiar + brak ACK. | [U09](#U09), [U11](#U11) | [P02](#P02) → [P01](#P01) |
| 18 | czerwony ! | czerwony | czerwony ! | Za mały rozmiar + ACK negatywny. | [U09](#U09), [U10](#U10) | [P02](#P02) → [P01](#P01) z v+1 |
| 19 | czerwony ! | fioletowy | czerwony ! | Za mały rozmiar + ACK pozytywny po CET. Sprzeczność. | [U09](#U09), [U13](#U13) | weryfikuj zawartość |
| 20 | czerwony ! | czarny | czerwony ! | Za mały rozmiar + brak ACK do CET. | [U03](#U03), [U09](#U09) | zgłoś + telefon CCC |
| 21 | czerwony ! | zielony R | czerwony ! | Za mały rozmiar + Dyspozytor ustawił 'R'. | [U09](#U09), [U13](#U13) | [P06](#P06) |
| 22 | ciemnozielony W | zielony | ciemnozielony W | Ręczna wysyłka z CCM, ACK OK. | [U03](#U03) | [P06](#P06) |
| 23 | ciemnozielony W | (puste) | ciemnozielony W | Ręczna wysyłka, ACK oczekuje. | [U11](#U11) | po 3 min CCCt MV |
| 24 | ciemnozielony W | czerwony ? | ciemnozielony W | Ręczna wysyłka, ACK nie napłynął, zbliża się CET. | [U11](#U11) | [P01](#P01) z v+1 |
| 25 | ciemnozielony W | czerwony | ciemnozielony W | Ręczna wysyłka, ACK negatywny. | [U10](#U10) | per kod ACK |
| 26 | ciemnozielony W | fioletowy | ciemnozielony W | Ręczna wysyłka, ACK po CET OK. | [U13](#U13) | [P06](#P06) |
| 27 | ciemnozielony W | czarny | ciemnozielony W | Ręczna wysyłka, brak ACK do CET. | [U03](#U03), [U11](#U11) | zgłoś + CN2 |
| 28 | ciemnozielony W | zielony R | ciemnozielony W | Ręczna wysyłka, Dyspozytor ustawił 'R'. | [U13](#U13) | [P06](#P06) |
| 29 | ciemnozielony W po CET | (puste) | ciemnozielony W po CET | Ręczna wysyłka po CET, ACK oczekuje. | [U13](#U13) | po 2 min status 'R' |
| 30 | ciemnozielony W po CET | czerwony ? | ciemnozielony W po CET | Ręczna po CET, brak ACK (>2 min). | [U11](#U11), [U13](#U13) | [P06](#P06) z 'R' |
| 31 | ciemnozielony W po CET | czerwony | ciemnozielony W po CET | Ręczna po CET, ACK negatywny. | [U10](#U10) | zgłoś |
| 32 | ciemnozielony W po CET | fioletowy | ciemnozielony W po CET | Ręczna po CET, ACK pozytywny. | [U13](#U13) | [P06](#P06) |
| 33 | ciemnozielony W po CET | czarny | ciemnozielony W po CET | Ręczna po CET, brak ACK do końca doby. | [U03](#U03) | zgłoś + telefon CCC |
| 34 | zielony R | (puste) | zielony R | Status ręczny 'R', ACK oczekuje. | [U11](#U11), [U13](#U13) | po 2 min CCCt MV |
| 35 | zielony R | czerwony ? | zielony R | Status ręczny, brak ACK (>2 min). | [U11](#U11) | [P06](#P06) |
| 36 | zielony R | czarny | zielony R | Status ręczny, brak ACK do CET. | [U11](#U11) | zgłoś |
| 37 | fioletowy | czerwony | fioletowy | Dostarczone po CET, ACK negatywny. | [U10](#U10), [U13](#U13) | zgłoś |
| 38 | fioletowy | czarny | fioletowy | Dostarczone po CET, ACK nie napłynął. | [U03](#U03), [U13](#U13) | zgłoś + CN2 |

<a id="states-2cct"></a>
## 2.C. Profil 2CCT — CCTool wyśl. + CCTool zwalid.

Stosowany dla: **AC (FIDx-831), GLSK (FIDx-607), CBCORA (FIDx-617), ATC Based Validation (FIDx-928), MD250 (FID1-250)**.
**Pełny katalog 28 stanów** dla FID1-831 — patrz [Przyklady_FID1-831.md](Przyklady_FID1-831.md). Wzór ogólny:

| # | CCTool wyśl. | CCTool zwalid. | Co oznacza | Ryzyka | Procedura |
|---|---|---|---|---|---|
| 1 | szary | szary | Plik nie wymagany | — | monitoring |
| 2 | pomarańczowy | pomarańczowy | TET zbliża się, brak pliku | [U03](#U03), [U06](#U06), [U08](#U08) | CCCt MV → MinIO → źródło |
| 3 | pomarańczowy | czerwony | TET + ACK negatywny | [U10](#U10), [U12](#U12) | per kod ACK |
| 4 | czerwony | czerwony | CET zbliża się, brak / błąd | [U03](#U03), [U08](#U08), [U10](#U10) | [P02](#P02)/[P04](#P04) → [P01](#P01) |
| 5 | czerwony ? | (puste) | Wysyłka trwa | [U11](#U11) | po 5 min CCCt MV |
| 6 | czarny | czarny | Niedostarczone, minął CET | [U03](#U03), [U08](#U08) | KRYTYCZNE — zgłoś + telefon CCC |
| 7 | zielony | czarny | Plik wysłany, brak ACK do CET | [U03](#U03), [U11](#U11) | CCCt MV → status 'R' lub [P01](#P01) |
| 8 | zielony | zielony | **Happy Day** | — | brak |
| 9 | zielony | czerwony | ACK negatywny | [U10](#U10) | per kod ACK (20/21/30) |
| 10 | zielony | czerwony ? | ACK timeout | [U11](#U11) | po 10 min [P01](#P01) |
| 11 | zielony | fioletowy | ACK pozytywny po CET | [U13](#U13) | [P06](#P06) |
| 12 | zielony | zielony R | ACK ręczny | [U13](#U13) | [P06](#P06) |
| 13 | ciemnozielony W | zielony | Ręczna OK | [U03](#U03) | [P06](#P06) |
| 14 | ciemnozielony W | czerwony | Ręczna, ACK negatywny | [U10](#U10), [U12](#U12) | per kod ACK |
| 15 | ciemnozielony W | czerwony ? | Ręczna, timeout | [U11](#U11) | po 5 min [P01](#P01) v+1 |
| 16 | ciemnozielony W | czarny | Ręczna, brak ACK do CET | [U03](#U03), [U11](#U11) | zgłoś + CN2 |
| 17 | ciemnozielony W po CET | zielony | Ręczna po CET, ACK OK | [U03](#U03), [U13](#U13) | [P06](#P06) |
| 18 | ciemnozielony W po CET | czerwony | Ręczna po CET, ACK negatywny | [U10](#U10), [U12](#U12) | zgłoś |
| 19 | ciemnozielony W po CET | czerwony ? | Ręczna po CET, timeout | [U11](#U11) | status 'R' |
| 20 | ciemnozielony W po CET | czarny | Ręczna po CET, brak ACK do końca doby | [U03](#U03), [U11](#U11) | zgłoś + telefon CCC |
| 21 | zielony R | zielony R | Status ręczny w obu | [U13](#U13) | [P06](#P06) |
| 22 | fioletowy | fioletowy | Wszystko po CET, OK | [U13](#U13) | [P06](#P06) |
| 23 | czerwony ! | czerwony ! | Za mały rozmiar | [U09](#U09) | weryfikuj zawartość; [P02](#P02) |
| 24 | czerwony ! | czerwony ? | Za mały + timeout | [U09](#U09), [U11](#U11) | [P02](#P02); CCCt MV |
| 25 | czerwony ! | czerwony | Za mały + ACK negatywny | [U09](#U09), [U10](#U10), [U12](#U12) | [P02](#P02) → [P01](#P01) v+1 |
| 26 | czerwony ! | czarny | Za mały + brak ACK do CET | [U03](#U03), [U09](#U09), [U11](#U11) | KRYTYCZNE — zgłoś + telefon CCC |
| 27 | czerwony ! | fioletowy | Za mały + ACK po CET pozytywny | [U09](#U09), [U13](#U13) | weryfikuj; zgłoś jeśli niepoprawny |
| 28 | czerwony ! | zielony R | Za mały + status ręczny | [U09](#U09), [U13](#U13) | [P06](#P06) |

<a id="states-2ms"></a>
## 2.D. Profil 2MS — MinIO + sFTP/ZP wyśl.

Stosowany dla **AGR Paczka ZIP (top-level)**: PERUN_ID2, PERUN_ID3C, PERUN_ID3 oraz analogiczne paczki ATC.

| # | MinIO | sFTP/ZP wyśl. | Co oznacza | Ryzyka | Procedura |
|---|---|---|---|---|---|
| 1 | szary | szary | Paczka jeszcze nie wygenerowana | — | monitoring |
| 2 | pomarańczowy | pomarańczowy | Zbliża się TET, paczka nie powstała | [U08](#U08) | sprawdź składowe |
| 3 | czerwony | czerwony | CET zbliża się, paczka nieobsłużona | [U08](#U08) | uzupełnij składowe |
| 4 | czarny | czarny | Niedostarczona, minął CET | [U03](#U03), [U08](#U08) | zgłoś + telefon CCC; składowe → S.13 |
| 5 | zielony | zielony | **Happy Day** — paczka wysłana do Perun4V | [U14](#U14) (potencjalne) | brak interwencji |
| 6 | zielony | szary | Paczka na MinIO, brak transportu sFTP | [U03](#U03) | sprawdź CN2 |
| 7 | zielony | czerwony | Paczka na MinIO, błąd sFTP | [U03](#U03) | [P05](#P05); zgłoś |
| 8 | zielony | czarny | Paczka na MinIO, brak sFTP do CET | [U03](#U03) | zgłoś + CN2 |
| 9 | ciemnozielony W | zielony | Paczka uzupełniona ręcznie | [U08](#U08) | [P06](#P06) |
| 10 | ciemnozielony W | czerwony | Uzupełniona, błąd sFTP | [U03](#U03), [U08](#U08) | CN2 + [P06](#P06) |
| 11 | fioletowy | fioletowy | Dostarczona po CET, OK | [U13](#U13) | [P06](#P06) |
| 12 | czerwony ! | czerwony ! | Składowa za mała → cała paczka błędna | [U09](#U09) | rozwiń agregat → [P05](#P05) |
| 13 | ciemnozielony W po CET | zielony | Uzupełniona po CET | [U13](#U13) | [P06](#P06) |
| 14 | zielony R | zielony R | Status ręczny | [U13](#U13) | [P06](#P06) |
| 15 | czarny | szary | Składowe nie dotarły, paczka nigdy się nie pojawiła | [U03](#U03), [U08](#U08) | KRYTYCZNE — zgłoś + telefon CCC |

<a id="states-min"></a>
## 2.E. Profil MIN — tylko MinIO

Stosowany dla: **IVA Backup (FIDx-710 wariant MIN), IVA_ATC (FIDx-710_ATC), składowe paczek ZIP (FIDx-610/-620/-632/-645/-657/-659/-665/-701/-701_ATC/-882, XID_RA)**.

| # | MinIO | Co oznacza | Ryzyka | Procedura |
|---|---|---|---|---|
| 1 | szary | Plik nie dostarczony jeszcze na MinIO | — | monitoring |
| 2 | spinner (kółko) | Trwa wysyłka backupowa CCA → CCCt (IVA Backup) | — | monitoring |
| 3 | pomarańczowy | TET zbliża się, plik nie obsłużony | [U03](#U03) | sprawdź źródło |
| 4 | czerwony | CET zbliża się — możliwa ręczna wysyłka backupowa | [U03](#U03), [U08](#U08) | menu boczne → Wyślij; sprawdź „Błąd procesu" |
| 5 | czerwony ! | Plik dostarczony, niepoprawny rozmiar | [U09](#U09) | LPM → Informacje; zgłoś jeśli błędny |
| 6 | zielony | Plik dostarczony OK | — | monitoring (IVA Backup: porównaj wersję z IVA) |
| 7 | ciemnozielony W | Wysłany ręcznie z CCM przed CET (Wyślij) | — | [P06](#P06) |
| 8 | ciemnozielony W po CET | Wysłany ręcznie z CCM po CET | [U13](#U13) | [P06](#P06) |
| 9 | zielony R | Status ręczny | [U13](#U13) | [P06](#P06) |
| 10 | zielony (z notką CCA, v+1) | Plik z CCA z wersją o 1 wyższą niż IVA | [U19](#U19) | wysłać ręcznie do CCCt (IVA Backup); zgłoś (R16) |
| 11 | ciemnozielony W (CCA, v+1) | Wysłany ręcznie przed CET z CCA, v+1 | [U19](#U19) | [P01](#P01) do CCCt; zgłoś |
| 12 | ciemnozielony W po CET (CCA, v+1) | Wysłany ręcznie po CET z CCA, v+1 | [U19](#U19), [U13](#U13) | [P01](#P01) do CCCt; zgłoś |
| 13 | fioletowy | Dostarczone po CET | [U13](#U13) | [P06](#P06) |
| 14 | czarny | Niedostarczone, minął CET | [U03](#U03), [U23](#U23) | zgłoś |
| 15 | red_pulse | Nowa wersja IVA Backup z wyższym numerem niż IVA — Scenariusz 4 | [U19](#U19) | porównaj wersje IVA vs Backup; NIE wysyłać ręcznie (HTML §5.3 dla standardowego modelu IDCC) |

<a id="states-sftp"></a>
## 2.F. Profil SFTP — tylko sFTP/ZP wyśl.

Stosowany dla: **24 modele IGM (DACF_IGM_UCT), Raporty z Perun (RAP_PERUN_*), Final Intraday NTC (FIDx-921), MD250 (FID1-250)**.

| # | sFTP/ZP wyśl. | Co oznacza | Ryzyka | Procedura |
|---|---|---|---|---|
| 1 | szary | Plik nie wymagany | — | monitoring |
| 2 | pomarańczowy | TET zbliża się, brak transportu | [U03](#U03) | sprawdź CN2 / sFTP |
| 3 | czerwony | CET zbliża się, brak / błąd | [U03](#U03), [U08](#U08) | [P05](#P05) z CCCt MV |
| 4 | czarny | Niedostarczone, minął CET | [U03](#U03), [U08](#U08), [U22](#U22) | zgłoś + telefon CCC (dla NTC: [U22](#U22)) |
| 5 | zielony | **Happy Day** | — | brak |
| 6 | ciemnozielony W | Ręczna wysyłka | [U03](#U03) | [P06](#P06) |
| 7 | fioletowy | Dostarczone po CET | [U13](#U13) | [P06](#P06) |
| 8 | zielony R | Status ręczny | [U13](#U13) | [P06](#P06) |
| 9 | czerwony ? | Wysyłka trwa, timeout | [U11](#U11) | po 5 min CCCt MV |
| 10 | czerwony ! | Plik za mały | [U09](#U09) | sprawdź zawartość; [P05](#P05) |
| 11 | ciemnozielony W po CET | Ręczna po CET | [U13](#U13) | [P06](#P06) |
| 12 | czerwony + zgłoś + telefon CCC | (dla FID1-250 MD250 / FID1-921 NTC) | [U21](#U21) / [U22](#U22) | natychmiastowa zgłoszenie |

---

<a id="risks"></a>
# 3. Ryzyka uniwersalne U01–U23

> Pełne karty ryzyk z opisami, objawami, działaniami i zgłoszeniem: patrz [Karta_ryzyk_IDCC.md](Karta_ryzyk_IDCC.md). Poniżej **skrót + mapowanie do dokumentów źródłowych**.

## 3.A. Grupa I — Dostępność narzędzi

<a id="U01"></a>**U01 — Brak dostępu do CCM** *([N01](#N01))*
- HTML §9: R06 | BUP DA: #27 (str. 69) | NOR DA: #27

<a id="U02"></a>**U02 — Brak dostępu do Core CC Tool** *([N02](#N02))*
- HTML §9: R07 | BUP DA: #11 (str. 47) | NOR DA: #11

<a id="U03"></a>**U03 — Brak dostępu / awaria Connector 2.0** *([N05](#N05))* — *obejmuje też scalone U18 (CN2 nie kopiuje do bucketów)*
- HTML §9: R09 + R16 | BUP DA: #1 (str. 9), #2 (str. 17), #10 (str. 46), #16 (str. 54), #24 | NOR DA: #2, #10, #16, #24

<a id="U04"></a>**U04 — Brak dostępu do MinIO** *([N04](#N04))*
- BUP DA: #2 (częściowo), #24, #25 (str. 67) | NOR DA: #24, #25

<a id="U05"></a>**U05 — Brak dostępu do Perun4V** *([N03](#N03))*
- BUP DA: #4 (str. 26), #17 | NOR DA: #4, #17

<a id="U06"></a>**U06 — Brak dostępu do źródła pliku** *([N06](#N06), [N07](#N07), [N08](#N08), [N09](#N09))*
- Nowe (zidentyfikowane w trakcie pracy); pokrywa ZP, Kreatory, CCA

<a id="U07"></a>**U07 — Brak dostępu do poczty kdm6** *([N11](#N11))*
- BUP DA: #25 (częściowo)

## 3.B. Grupa II — Plik i dostarczenie

<a id="U08"></a>**U08 — Plik niedostarczony w czasie**
- HTML §9: R04 | BUP DA: #3 (str. 22), #28 | Stany: czarny, czerwony, pomarańczowy

<a id="U09"></a>**U09 — Plik dostarczony, ale błędny (rozmiar / struktura)**
- HTML §9: R04 (rozszerzony) | ACK kod 30 (file size mismatch); „Message has some invalid timeSeries…"

<a id="U10"></a>**U10 — ACK negatywny (odrzucenie)**
- HTML §9: R05 | BUP DA: #13 (str. 49) | Kody ACK: 20 (gateClosed), 21 (duplicatedVersion), 22 (Negative — historyczny), 30 (size)

<a id="U11"></a>**U11 — Brak ACK (timeout)**
- HTML §9: R05 (zawężenie) | BUP DA: #12 (str. 48)

<a id="U12"></a>**U12 — Niezgodność wersji pliku**
- ACK kod 21 (duplicatedVersion), kod 40 (Backup version lower)

<a id="U13"></a>**U13 — Plik dostarczony po CET (informacyjne)**
- Stan: fioletowy; bez działań naprawczych poza [P06](#P06)

## 3.C. Grupa III — Proces obliczeniowy (Perun4V / IVA)

<a id="U14"></a>**U14 — Brak uruchomienia obliczeń w Perun4V**
- HTML §9: R01 | BUP DA: #1 (str. 9)

<a id="U15"></a>**U15 — ERR-I (część TS niepoliczona)**
- HTML §9: R02 | BUP DA: #6 (str. 29), #20

<a id="U16"></a>**U16 — Process failed (wszystkie TS niepoliczone)**
- HTML §9: R03 | BUP DA: #7 (str. 39), #21

## 3.D. Grupa IV — Strumień ATC

<a id="U17"></a>**U17 — Niezakończenie walidacji ATC w czasie**
- HTML §9: R11 | Dotyczy: FIDx-928

## 3.E. Grupa V — Transport zwrotny

<a id="U18"></a>**~~U18~~** → scalone z [U03](#U03)

<a id="U19"></a>**U19 — Niezgodność wersji IVA / IVA BACKUP**
- HTML §9: R12 | Dotyczy: FIDx-710 (3COL) vs FIDx-710 (MIN — IVA Backup)

## 3.F. Grupa VI — Zgłoszenie zewnętrzna

<a id="U20"></a>**U20 — AAC Fallback** *([N17](#N17))*
- HTML §9: R13 | Deadliny: 20:00 D-1 (IDCC(b)), 02:00 D (IDCC(c)), 07:00 D (IDCC(d))

<a id="U21"></a>**U21 — Decoupling SDAC — konieczność MD250** *([N16](#N16))*
- HTML §9: R14 | Plik: FID1-250 (Shadow Auction)

<a id="U22"></a>**U22 — Late NTC delivery po IDA2** *([N17](#N17))*
- HTML §9: R15 | Plik: FIDx-921

<a id="U23"></a>**U23 — Brak raportu CCA** *([N09](#N09))*
- HTML §9: R20 | BUP DA: #26 (str. 69) | Bucket: `cca/ID_FBCC/out/[BD]/`

## 3.G. Tabela kodów ACK (CCCt)

| Kod | Treść | Działanie |
|---|---|---|
| 0 | Message fully accepted | OK |
| 20 | Gate for provided message definition is not opened | Bramka zamknięta — sprawdź TET/CET; CCCt `IDx-AC-FORWARDING` → admin CCCt + zgłoś |
| 21 | Provided version is not higher than already stored data (duplicatedVersion) | Podbić wersję; ponów [P01](#P01) |
| 22 | ~~Delivered constraint value is negative~~ | ❌ Nieaktualny (CCCt akceptuje wartości ujemne) |
| 30 | File size mismatch | [P04](#P04) lub [P02](#P02); weryfikuj zawartość → [P01](#P01) |
| 40 | Backup version lower | NIE wysyłać backup z niższą wersją |
| 41 | Backup not available | → [U23](#U23) |
| 42 | Backup validation failed | Raport CCA; zgłoś |
| — | Message has some invalid timeSeries that does not meet primary MTU rules | Poprawić strukturę pliku → [P01](#P01) |
| — | Błąd procesu | Proces CCCt zakończony błędem; zgłoś |

---

<a id="procedures"></a>
# 4. Procedury

## 4.A. Procedury reagujące na ryzyka (P01–P06)

> Pełne opisy: [Karta_ryzyk_IDCC.md](Karta_ryzyk_IDCC.md). Skrót poniżej.

<a id="P01"></a>**P01 — GUI CCCt Manual Upload** — w odpowiedzi na [U03](#U03), [U09](#U09), [U10](#U10), [U11](#U11). Procedura: [4.B Logowanie i nawigacja w CCCt](#proc-cct).

<a id="P02"></a>**P02 — Pobranie z ZP → GUI CCCt** — w odpowiedzi na [U03](#U03), [U06](#U06). Dotyczy FIDx-831. Procedura: [4.B Logowanie i nawigacja w ZP](#proc-zp).

<a id="P03"></a>**P03 — Ręczne uruchomienie obliczeń w Perun4V** — w odpowiedzi na [U14](#U14). Procedura: [4.B Logowanie i nawigacja w Perun4V](#proc-perun).

<a id="P04"></a>**P04 — Pobranie z MinIO → CCM Wyślij** — w odpowiedzi na [U08](#U08), [U09](#U09). Procedura: [4.B Logowanie i nawigacja w MinIO](#proc-minio).

<a id="P05"></a>**P05 — Pobranie z CCCt Message Viewer → CCM Wyślij** — dla składowych paczki (FIDx-610 Merged GLSK ≠ FIDx-607 raw GLSK).

<a id="P06"></a>**P06 — Wpis w karcie A.4** — przy każdym ręcznym działaniu. Pola: data, iteracja, FID, stan przed/po, procedura, ryzyko, wersja, zgłoszenie, uwagi.

## 4.B. Procedury narzędziowe (krok po kroku)

<a id="proc-ccm"></a>
### Logowanie i nawigacja w CCM
1. Otwórz przeglądarkę → https://ccm.spsm.pse.pl
2. Zaloguj (na środowisku produkcyjnym proces automatyczny dla stanowiska dyspozytorskiego)
3. Lista pulpitów → kliknij ikonę oka 👁 obok wybranego pulpitu
4. Wybierz dobę biznesową (strzałki ← →) lub kliknij kalendarz 📅
5. Tryby odświeżania: ultraszybki (10s) / szybki (30s) / wolny (5 min, domyślny)

**Wysyłka pliku (przed CET):** najedź na wiersz → **PPM → Wyślij** → wskaż plik z dysku → potwierdź → kafelek → `ciemnozielony W` → `zielony` po ACK

**Wysyłka po CET:** najedź → **PPM → Wyślij po CET** → wskaż plik → potwierdź

**Ustaw status ręcznie 'R':** PPM na wierszu → **Ustaw status ręcznie** → wybierz 'R' → zatwierdź
*(❓ dokładna ścieżka — do weryfikacji w CCM Instrukcji Dyspozytora v2.6, rozdz. „Zmiana statusu dokumentu na wysłany ręcznie")*

**Informacje o pliku:** LPM na kolumnie statusu → menu → **Informacje** → rozmiar, lokalizacja MinIO, data dostarczenia

<a id="proc-cct"></a>
### Logowanie i nawigacja w Core CC Tool
> 📖 BUP DA Ryzyko 2 (str. 17), Rys. 11–13

1. Otwórz przeglądarkę → URL CCCt (wewn.)
2. Zaloguj danymi dyspozytorskimi
3. **Selektor procesu** (obok niebieskiego pola u góry) → wybierz `ID1` / `ID2` / `ID3C` / `ID3` (zamiast domyślnego `DA`)
4. Na niebieskim tle → wybierz **Business Day**
5. **Process Instance** (lewe menu) → wybierz dla daty (lub wyczyść filtry)
6. **Message Viewer** → pole **Message Definition** → wpisz np. `FID1-831` → **Apply**
7. Sprawdź **kolumnę Status**: `Processed` / `Rejected` / brak wpisu
8. **Pobranie pliku:** strzałka w dół po prawej stronie wiersza
9. **Manual Upload:** przycisk **Manual Upload** → wskaż plik z dysku → **Upload file** → odśwież → Message Viewer

<a id="proc-minio"></a>
### Logowanie i nawigacja w MinIO
> 📖 BUP DA Ryzyko 3 (str. 22)

1. Otwórz przeglądarkę → https://minio-gui.pse.pl
2. Zaloguj danymi dyspozytorskimi
3. Lewy panel → **Buckets** → wybierz bucket (`perun`, `cca`, `mam`)
4. Nawiguj do podfolderu (np. `cca/ID_FBCC/in/yyyymmdd/`)
5. **Pobierz plik:** ikona **Download** po prawej stronie wiersza pliku
6. **Alternatywnie** (z poziomu CCM): kafelek `MinIO` → LPM → **Pobierz** → wskaż katalog lokalny

<a id="proc-zp"></a>
### Logowanie i nawigacja w ZP
> 📖 AC manuall ZP.docx

1. Otwórz aplikację **ZP** (zdolności przesyłowe) — desktop
2. Zaloguj danymi dyspozytorskimi
3. **Główne okno** → zakładka **`bilans AC`**
4. Górna część listy dokumentów → wybierz **FID1-831** (lub odpowiedni FIDx-831 dla iteracji)
5. **Pobranie pliku:** kliknij **`Pobierz XML`** → plik zapisany lokalnie
6. **Generowanie nowej wersji** (gdy brak):
   - Wróć do okna `bilans AC`
   - Wybierz wersję
   - Kliknij niebieski przycisk **`Nowa wersja`**
   - Po wygenerowaniu wróć do kroku 5 (Pobierz XML)

<a id="proc-perun"></a>
### Logowanie i nawigacja w Perun4V
> 📖 BUP DA Ryzyko 1 (str. 9), NOR DA §2.3.2.2

1. Otwórz przeglądarkę → https://lccv.tscnet.eu
2. Kliknij **Local Login**
3. Wpisz `Username` i `Password` → zaznacz **Read and accept the TSCNET Policy** → **Login**
4. **Główne okno** — lista obliczeń per data
5. Sprawdź dostarczającego (typowo `sFTP@pse.pl`)
6. Sprawdź status obliczeń: `Calculating` / `Successful` / `ERR-I` / `Process failed`
7. **Wczytanie paczki:** sekcja **Select timestamp date** → wybierz BD → przeciągnij plik ZIP na pole (lub kliknij i wybierz z dysku)
8. **Uruchomienie obliczeń:** kliknij przycisk uruchamiania
9. **Status → Details** — szczegóły per godzina, kolumna `[Result]`
10. **Pobranie wyniku** (F310/IVA): po zakończeniu obliczeń kliknij download

---

<a id="buckets"></a>
# 5. Buckety MinIO

| Bucket | Pełna ścieżka | Zawartość | Źródło |
|---|---|---|---|
| `perun/` | `perun/DA_FBCC/in/yyyy-mm-dd/` | Paczki wejściowe DA do Perun4V | BUP DA §6, NOR DA |
| `perun/` | `perun/ID_FBCC/in/yyyy-mm-dd/` | Paczki wejściowe IDCC do Perun4V | HTML §6 |
| `perun/` | `perun/DA_FBCC/out/yyyy-mm-dd/` | Wyniki DA z Perun4V (IVA F310, raporty) | BUP DA |
| `perun/` | `perun/ID_FBCC/out/yyyy-mm-dd/` | Wyniki IDCC z Perun4V (IVA FIDx-710, raporty) | HTML §6 |
| `cca/` | `cca/DA_FBCC/out/[BD]/` | IVA BACKUP + raporty CCA (DA) | BUP DA §6, HTML §6 |
| `cca/` | `cca/ID_FBCC/out/[BD]/` | IVA BACKUP + raporty CCA (IDCC) | HTML §6, Aneks A.3 |
| `cca/` | `cca/ID_FBCC/in/yyyymmdd/yyyymmdd-FIDx-831-v*` | Pliki AC (FIDx-831) — wejście CCA | uzgodnienie z użytkownikiem |
| `mam/` | (do uzupełnienia) | ❓ — nieznana zawartość, do dopytania PSE Innowacje ([TODO-5](#todo)) | — |

**Katalog sieciowy zapisu plików ręcznie pobranych z CCCt:**
`\\uo-data\ZUO\Pion_UOD\Wydzial_DP\MODELE\5_DYSP\FBA\Pliki wejściowe do DA FBA\rrrMMdd\PERUN\` *(BUP DA)*
*(❓ analogiczna ścieżka dla IDCC — do weryfikacji)*

---

<a id="matrix"></a>
# 6. Mapa relacji

## 6.A. Macierz narzędzie × ryzyko

| Narzędzie | Ryzyko gdy niedostępne | Ryzyko transportowe / procesowe | Zespół utrzymania |
|---|---|---|---|
| [CCM (N01)](#N01) | [U01](#U01) | — | zgłoś |
| [Core CC Tool (N02)](#N02) | [U02](#U02) | [U10](#U10), [U11](#U11), [U12](#U12) | [CCC/TSCNET (N13)](#N13) |
| [Perun4V (N03)](#N03) | [U05](#U05) | [U14](#U14), [U15](#U15), [U16](#U16) | [TSCNET (N13)](#N13) |
| [MinIO (N04)](#N04) | [U04](#U04) | — | zgłoś |
| [Connector 2.0 (N05)](#N05) | [U03](#U03) | obejmuje też scalone U18 | zgłoś |
| [ZP (N06)](#N06) | [U06](#U06) | — | zgłoś |
| [Kreator2DAF/IDCF (N07/N08)](#N07) | [U06](#U06) | — | PLANS |
| [CCA (N09)](#N09) | — | [U19](#U19), [U23](#U23) | zgłoś |
| [PuTo (N10)](#N10) | (pośrednio przez CCCt) | — | wewn. PSE |
| [kdm6 (N11)](#N11) | [U07](#U07) | — | utrzymanie poczty PSE |
| [sFTP (N12)](#N12) | (część [U03](#U03)) | — | zgłoś |
| [ECP/EDX (N16)](#N16) | — | [U21](#U21) | TSCNET |
| [XBID (N17)](#N17) | — | [U20](#U20), [U22](#U22) | zewn. |

## 6.B. Macierz stan kafelka × procedura backupowa (skrót)

| Stan kafelka (uniwersalny) | Typowe ryzyka | Sugerowana ścieżka |
|---|---|---|
| szary/szary (przed TET) | — | monitoring |
| pomarańczowy/* (TET zbliża się) | [U03](#U03), [U06](#U06), [U08](#U08) | CCCt MV → MinIO → źródło ([N06](#N06)) |
| czerwony/* (CET zbliża się) | [U03](#U03), [U08](#U08), [U10](#U10) | [P02](#P02)/[P04](#P04) → [P01](#P01) |
| czarny/czarny (po CET) | [U03](#U03), [U08](#U08) | KRYTYCZNE — zgłoś + telefon [CCC (N13)](#N13) |
| zielony/czerwony (ACK Rejected) | [U10](#U10) | per kod ACK (20/21/30) |
| zielony/czerwony ? (timeout) | [U11](#U11) | CCCt MV → [P01](#P01) |
| zielony/zielony (Happy Day) | — | brak |
| czerwony ! / * (size mismatch) | [U09](#U09) | [P04](#P04) / [P02](#P02) → [P01](#P01) |
| ciemnozielony W / zielony | [U03](#U03) | [P06](#P06) wpis A.4 |
| fioletowy / fioletowy | [U13](#U13) | [P06](#P06) |
| zielony R / zielony R | [U13](#U13) | [P06](#P06) |
| red_pulse (IVA Backup) | [U19](#U19) | porównaj wersje IVA vs Backup |

---

<a id="todo"></a>
# 7. TODO — do dopytania zespołu CCA / PSE Innowacje

| # | Pytanie | Skierowane do | Status |
|---|---|---|---|
| TODO-1 | Czym dokładnie jest **R08** (HTML §9)? Hipoteza: „Brak dostępu do Perun4V" — czy potwierdzone? | Zespół CCA | otwarte | -> bra diostepu do perun i nalezy uzyc narzedzia standalone jak w DA.
| TODO-2 | Czy **R10** istnieje? Brak opisu w HTML §9 — czy to numer archiwalny? | Zespół CCA / WPO | otwarte | - nie istnieje
| TODO-3 | Opisy **R17, R18, R19** — wzmiankowane w kontaktach CCA („Zgłoszenie przy ryzykach R12, R16, R17, R18, R19, R20"), brak definicji w §9 | Zespół CCA | otwarte | -
| TODO-4 | Czy istnieje dedykowany **email** zespołu CCA, czy zawsze przez PSE Innowacje? | Zespół CCA | otwarte |
| TODO-5 | Bucket MinIO **`mam/`** — co zawiera i kiedy używany? | PSE Innowacje | otwarte | 
| TODO-6 | Dokładna ścieżka **„Ustaw status ręcznie 'R'"** w CCM — czy zgodnie z CCM Instrukcją v2.6 (rozdz. „Zmiana statusu dokumentu na wysłany ręcznie")? | PSE Innowacje | otwarte |
| TODO-7 | Katalog sieciowy zapisu plików **dla IDCC** — czy `…\Pliki wejściowe do ID FBA\rrrMMdd\` czy ten sam co DA? | Dyspozytor IDCC | otwarte |
| TODO-8 | Wzorzec wysyłek automatycznych z ZP **v+1** — czy 14:20 to dla doby D+1 czy backup dla D? | Dyspozytor / ZP | otwarte |

---

**Wersja Inwentarza:** 1.0 — utworzony zgodnie z planem `/Users/dawidslabicki/.claude/plans/potrzebuje-dla-kazdego-jednego-snoopy-sprout.md`
**Data:** 2026-05-20
