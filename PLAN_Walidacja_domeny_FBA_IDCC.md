# PLAN — Walidacja domeny FBA dla procesu IDCC

> **Cel dokumentu:** konspekt nowej procedury walidacji domeny FBA dla procesu IDCC (odpowiednik pary FBA_TSO_NOR_03 / FBA_TSO_BUP_03 z procesu Day-Ahead) oraz plan wpisania jej w strukturę dokumentu *Core IDCC Flow Based Business Process Documentation*.
>
> **Źródła analizy:**
> - FBA_TSO_NOR_03 — Walidacja domeny FBA v0.21 (01.08.2025)
> - FBA_TSO_BUP_03 — Walidacja domeny FBA v0.31 (01.08.2025)
> - Core IDCC Flow-Based Business Process Documentation v5.0 (02-03-2026) — treści wyekstrahowane w repo (`process_intro.html`, `process2_glos.html`, `process2_a.html`, `process2_bcd.html`, `process_d.html`, `process2_mail.html`)
> - Inwentarz_IDCC.md, Karta_ryzyk_IDCC.md, Ryzyka_pelna_baza_IDCC.html, frag7_walidacja.html
>
> ⚠ **Zastrzeżenie źródła:** mapowanie do BPD oparto na wersji v5.0 (ekstrakty w repo). Po dostarczeniu pliku „Core IDCC Flow Based Business Process Documentation (3).docx" należy wykonać weryfikację opisaną w [części B, pkt B.5](#b5-punkt-weryfikacji-z-3docx).

---

## Spis treści

1. [Analiza — co przenosi się z DA na IDCC](#analiza)
2. [Część A — konspekt nowej procedury (NOR + BUP)](#czesc-a)
   - [A.1. FBA_TSO_NOR_04 — tryb normalny](#a1-nor)
   - [A.2. FBA_TSO_BUP_04 — tryb backupowy](#a2-bup)
   - [A.3. Mapowanie ryzyk BUP_03 → BUP_04 (los każdego ryzyka)](#a3-ryzyka)
3. [Część B — wpisanie w Core IDCC FB BPD](#czesc-b)
4. [Lista TODO / do potwierdzenia](#todo)

---

<a id="analiza"></a>
## 1. Analiza — co przenosi się z DA na IDCC

Procedury DA opisują jeden dobowy przebieg walidacji (domena DA + domena LTA + redukcja LTA). Proces IDCC powtarza krok *Individual Validation* w kilku iteracjach w ciągu doby i nie ma gałęzi LTA — zamiast niej istnieje strumień ATC/NTC. Architektura transportu (Connector 2.0 → MinIO → sFTP → Perun4V → CCCt/CCA) jest wspólna.

| Element | DA (NOR_03 / BUP_03) | IDCC (nowa procedura) |
|---|---|---|
| Iteracje | 1 przebieg dobowy (+ LTA) | IDCC(a)=ID1 · IDCC(b)=ID2 (24 TS) · IDCC(c)=ID3C (18 TS) · IDCC(d)=ID3 (12 TS) · IDCC(e) — placeholder (proces nieuruchomiony; HLBP „IDCCe Option A/B") |
| Krok walidacji | Perun4V — domena DA i LTA | IDCC(b)/(c)/(d): Individual Validation w Perun4V (CNEC-based + ATC-based); IDCC(a): wyłącznie walidacja ATC (FID1-928) + dostarczenie AC (FID1-831 z ZP) |
| Plik wynikowy | IVA **F310** | IVA **FIDx-710** (+ wariant IVA BACKUP generowany przez CCA); raport RAP_PERUN_IDx |
| Skład paczki do Perun4V | F109/F308 (CGM), F110 (RefProg), F112 (Merged GLSK), F515 (MergingLog), F212 (Intermediate FB Domain), F226 (Real GLSK), F312 (Individual Filtered CB), F327 (konfiguracja RAO), F320_CCA/F320_LTA, CORE_FB_DA_RA_PL.xlsx, VERTICES_MAP_CCA/LTA | paczka **PERUN_IDx**: Merged GLSK (FIDx-610), CGM (FIDx-620), RefProg (FIDx-632), Initial FB Domain (FIDx-645), Real GLSK (FIDx-657), CB (FIDx-665), Vertices (FIDx-701), Initial Intraday ATC (FIDx-882), RA |
| Terminy IVA (TET / CET) | DA: 07:15 / 08:50; LTA: 07:15 / 08:00 | ID2: 21:30 / 22:06 · ID3C: 04:00 / 04:36 · ID3: 09:30 / 10:06; okno IVA 40 min, gwarantowane min. **25 min** (pauza/wznowienie wyłącznie po stronie operatora procesu — PSE nie przedłuża okna samodzielnie) |
| Terminy plików wejściowych PSE | — | GLSK (FIDx-607) i CBCORA (FIDx-617): ID2 20:00/20:19 · ID3C 00:00/00:56 · ID3 06:20/07:30; AC (FIDx-831): ID2 21:45/21:55 · ID3C 04:15/04:25 · ID3 08:40/09:25; AC dla IDCC(a): 13:50/14:45 |
| Buckety MinIO | perun/DA_FBCC/in·out, cca/DA_FBCC/in·out | perun/**ID_FBCC**/in·out, cca/**ID_FBCC**/in·out (per BD) |
| Pulpit CCM | „DACC FB Pulpit dyspozytorski" | „**IDCC FB Pulpit dyspozytorski**" / „IDCC (do 3C) z ATC i SFTP Pulpit dyspozytorski" |
| Część LTA i redukcja LTA | Część 2 i 3 NOR_03, ryzyka 15–26, 29 BUP_03 | **nie występuje** — zastępuje ją strumień ATC/NTC (FIDx-882 / 921 / 922 / 928) i związane z nim zdarzenia procesowe |
| Rejestr ryzyk | 29 ryzyk BUP_03 | istniejący rejestr **U01–U23 + P01–P06** (Karta_ryzyk_IDCC.md / Inwentarz_IDCC.md) — mapowanie w [A.3](#a3-ryzyka) |
| Narzędzia | CCCt, CN2, CCM, KreatorDACF&2DAF_CGMES, MinIO, Perun4V, Outlook | jak DA **+ ZP** (źródło AC FIDx-831) **+ KreatorIDCF_CGMES** (GLSK/CBCORA/RA dla IDCC(c)–(e)); selektor procesu w CCCt: **ID1 / ID2 / ID3C / ID3** (nie domyślny DA!) |

---

<a id="czesc-a"></a>
## 2. Część A — konspekt nowej procedury

Proponowane nazwy (numeracja do potwierdzenia z właścicielem procedur):
- **FBA_TSO_NOR_04 — Walidacja domeny FBA IDCC** (tryb normalny),
- **FBA_TSO_BUP_04 — Walidacja domeny FBA IDCC** (tryb backupowy).

Układ obu dokumentów lustrzany wobec pary DA — te same sekcje, tabele i konwencje.

<a id="a1-nor"></a>
### A.1. FBA_TSO_NOR_04 — tryb normalny

**Rozdział 0 — Metryka.** Tabele: wersja/data/status, „Zatwierdzono", „Poprzednie wersje" — układ 1:1 z NOR_03.

**Uwaga ogólna.** Zdarzenie wykraczające poza normalny przebieg → użytkownik postępuje zgodnie z FBA_TSO_BUP_04.

**Rozdział 1 — Wstęp.**
- Cel: walidacja domeny FBA po kroku *Initial FB Computation* każdej iteracji IDCC przy pomocy Perun4V; wynik: IVA (FIDx-710) na przeciążonych CNEC.
- Definicja i przesłanki IVA — przeniesione 1:1 z NOR_03 (redukcja RAM do wartości bezpiecznej, tylko wartości dodatnie, nieujemny RAM; przesłanki wg CCM Core art. 20(5) itd.).
- Dane wejściowe: skład paczki PERUN_IDx (tabela z FIDx-610/620/632/645/657/665/701/882 + RA).
- Obowiązywanie: codziennie, 7 dni w tygodniu, 365(366) dni w roku; wielokrotnie w ciągu doby (per iteracja).
- Zasada TET/CET: przy zagrożeniu TET niezwłoczna informacja do operatora procesu (CORESO/TSCNET); maksymalne opóźnienie wyznacza CET.

**Rozdział 1.1 — Podsumowanie – cel.** Opis postępowania po kroku Initial FB Computation każdej iteracji; czynności użytkownika: przygotowanie, weryfikacja i udostępnienie danych na Perun4V, MinIO (buckety ID_FBCC), CCCt.

**Rozdział 1.2 — Zarządzane / Regulowane przez.** HLBP + *Core IDCC Flow Based Business Process Documentation* (dokładną wersję wpisać po weryfikacji pliku (3).docx).

**Rozdział 1.3 — Narzędzia i protokoły komunikacyjne.** Opisy narzędzi z NOR_03 + ZP + KreatorIDCF_CGMES; protokoły: e-mail, ECP/EDX, sFTP. Uwaga o selektorze procesu ID1/ID2/ID3C/ID3 w CCCt.

**Rozdział 2 — Dostarczenie i weryfikacja danych wejściowych procesu.**

*2.1 Warunki wstępne:* dostępne dane z kroku Initial FB Computation danej iteracji (wejście do Perun4V do wyliczenia IVA).

*2.2 Przegląd ogólny — tabela procesów i etapów* (odpowiednik Tabeli 1 NOR_03):

| Część | Zakres | TET / CET | Narzędzia |
|---|---|---|---|
| 1 | IDCC(b)/ID2 — walidacja domeny w Perun4V + monitorowanie (CCM / Perun4V / e-mail) | 21:30 / 22:06 | Perun4V, MinIO, CN2, CCM |
| 2 | IDCC(c)/ID3C — j.w. | 04:00 / 04:36 | j.w. |
| 3 | IDCC(d)/ID3 — j.w. | 09:30 / 10:06 | j.w. |
| 4 | IDCC(a)/ID1 — monitorowanie walidacji ATC (FID1-928) + dostarczenie AC (FID1-831) | AC: 13:50 / 14:45; FID1-928: 13:40 / 14:20 | ZP, CN2, CCCt, CCM |
| 5 | IDCC(e) — placeholder | — | proces nieuruchomiony operacyjnie |

*2.3 Szczegółowy opis procesu — wspólny przebieg IDCC(b)–(d)* (jedna sekwencja, różnice per iteracja w tabeli — wzorzec `process2_bcd.html`):

Tabela „Zestawienie danych w paczce PERUN_IDx" (odpowiednik Tabeli 2 NOR_03) — kolumny: nazwa pliku (maska FIDx), opis przygotowania (dostarczone przez CONNECTOR 2.0 / CCCt / Kreator).

Kolejne kroki procesu (automatyczne; kontrola i nadzór dyspozytora):
1. CN2 odbiera dane z CCCt/Kreatora na potrzeby paczki do weryfikacji domeny IDx.
2. CN2 tworzy paczkę PERUN_IDx i przesyła ją na MinIO do bucket `perun/ID_FBCC/in/rrrr-mm-dd`.
3. Równolegle paczka przekazywana jest do sFTP z maską czytaną przez Perun4V *(maska do potwierdzenia u PSE-I — odpowiednik `PSE_RRRRMMDD_DA_v*_input_validation_DACCA.zip` dla IDx)*.
4. Z sFTP paczka trafia do Perun4V; obliczenia startują automatycznie (użytkownik: sFTP@pse.pl).
5. Po obliczeniach raporty RAP_PERUN_IDx oraz plik IVA (FIDx-710) wracają przez sFTP do CN2.
6. CN2 wysyła IVA do CCCt oraz IVA + raporty do CCA (bucket `cca/ID_FBCC/in/BD`).
7. CCA przygotowuje IVA BACKUP i raporty, publikuje do `cca/ID_FBCC/out/BD` i wysyła na kdm6@pse.pl.

*2.4 Monitorowanie procesu* (trzy podrozdziały, jak NOR_03):
- **CCM** — pulpit „IDCC FB Pulpit dyspozytorski": kafelek „Paczka ZIP do Perun" (zielony = paczka utworzona), kolumna „sFTP/ZP wysł." (przekazanie przez CN2; ~2 min do startu obliczeń), kafelki „IVA" i „Raporty z Perun" (dostarczenie wyników do CCCt/CCA).
- **Perun4V** — https://lccv.tscnet.eu (Local Login): weryfikacja czy obliczenia dla danej iteracji wystartowały (wybór procesu IDx), status TS: 24/18/12 + 1 (raporty).
- **E-mail kdm6@pse.pl** — raport CCA po zakończeniu walidacji: czy wszystkie TS policzone, maksymalna wielkość IVA.

Po każdym etapie tabela ryzyk z odwołaniami do FBA_TSO_BUP_04 (numeracja wg [A.3](#a3-ryzyka)).

*2.5 IDCC(a) — sekcja odrębna (bez Perun4V):*
- monitorowanie wyniku walidacji ATC: FID1-928 (CCCt → CN2 → CCM), TET 13:40 / CET 14:20;
- dostarczenie AC (FID1-831) z ZP: przebieg ZP → CN2 → CCCt, TET 13:50 / CET 14:45 (procedura narzędziowa: P02 / „AC manuall ZP");
- monitorowanie FID1-921 (high-negative NTC test komunikacji + Final Intraday NTC);
- zdarzenia ID1_x — wyłącznie odwołania do BUP_04.

<a id="a2-bup"></a>
### A.2. FBA_TSO_BUP_04 — tryb backupowy

**Rozdział 0 — Metryka + uwaga ogólna** (lustrzane wobec BUP_03).

**Rozdział 1 — Wstęp.** Terminy dostarczenia FIDx-710 per iteracja (z naciskiem na CET), dane wejściowe = paczka PERUN_IDx, definicja IVA (1:1 z BUP_03).

**Rozdział 2 — Proces weryfikacji domeny IDCC.**

*2.1 Przegląd ogólny* — tabela wszystkich ryzyk zidentyfikowanych w FBA_TSO_NOR_04 (struktura Tabeli 1 BUP_03; pełne mapowanie w [A.3](#a3-ryzyka)).

*2.2 Ryzyka — szczegółowe rozwiązania.* Zasady redakcji:
- każde ryzyko = sekcje **Objawy / Działanie (kroki) / Zgłoszenie** — treści operacyjne przenieść z `Karta_ryzyk_IDCC.md` (U01–U23) i `Ryzyka_pelna_baza_IDCC.html` (R01–R21), nie pisać od zera;
- wszystkie zrzuty ekranu CCCt wykonywać z ustawionym selektorem procesu IDx;
- ścieżki sieciowe: odpowiednik `\\uo-data\...\FBA\Pliki wejściowe do DA FBA\rrrrMMdd\PERUN\` dla IDCC — *do potwierdzenia z WPO* (czy istnieje analogiczny katalog per iteracja);
- w ryzykach czasowych uwzględnić krótkie okno IVA (40 min, min. 25 min) — reakcje muszą być wykonalne w tym oknie; jeżeli nie są, domyślną reakcją jest IVA BACKUP.

<a id="a3-ryzyka"></a>
### A.3. Mapowanie ryzyk BUP_03 → BUP_04

| # BUP_03 | Ryzyko DA | Los w BUP_04 (IDCC) | Rejestr U |
|---|---|---|---|
| 1 (1.1–1.5) | Brak działania sFTP (pobranie paczki → wczytanie → obliczenia → pobranie wyniku → dostarczenie) | **Przeniesione** — identyczna sekwencja ręczna dla paczki PERUN_IDx; pobranie z `perun/ID_FBCC/in/BD` przez CCM, wynik FIDx-710 | U14, P03, P04 |
| 2 | Brak dostępu do MinIO / awaria CN2 | **Przemapowane** — ręczne pobranie plików 610/620/632/645/657/665/701/882/RA z CCCt (Message Viewer + selektor IDx), paczka 7-Zip (zip, bez hasła) | U03, U04, P01, P05 |
| 3 | Brak paczki plików na MinIO | **Przeniesione** — brakujące pliki z CCCt; podgląd braków w CCM (siwy/czerwony kafelek; czerwony także gdy do CET < 30 min) | U08, U09, P05 |
| 4 | Brak dostępu do Perun4V | **Przeniesione** — wysyłka IVA BACKUP z CCM (przepływ „IVA BACKUP"; v1 = pełny backup, v2+ = uzupełnienie godzin); gdy niedostępna → bulk edit w CCCt View Results: MinRAM%_Core zeroBalanced = 20%, justification „Individual Validation Tool failed. Applying bulk reductions", TSO fallback = true; *nazwa kroku w View Results dla ID do potwierdzenia* | U05, U19 |
| 5 | Brak wyników IVA i raportów z sFTP | **Przeniesione** — >30 min bez wyników → ręczne przeliczenie (jak ryzyko 1); diagnostyka GUI: błędny BD / brak pliku w paczce / błędny plik | U12, U14 |
| 6 | ERR-I — pojedyncze godziny niepoliczone | **Przeniesione** — najpierw sprawdzić DFP/Spanning w CCCt (żółte pole = zachowanie normalne, bez IVA na te TS); inaczej: CCA uzupełni godziny IVA BACKUP → dyspozytor wysyła IVA BACKUP v2+ z CCM (dopiero gdy wersja BACKUP > wersja IVA); konwencja godzin Perun4V vs CCCt (01:30 = godz. 2) | U15 |
| 7 | Process failed — cały dzień | **Przeniesione** — DFP/Spanning na wszystkie TS = normalne; inaczej IVA BACKUP v1 | U16 |
| 8 | Brak możliwości pobrania F310 | **Przeniesione** — „Download output files" ze statusu obliczenia; wysyłka F710 przez CCM (status ręczny „R" po ręcznym wgraniu) lub Manual Upload w CCCt | U13→P01 |
| 9 | Dodanie wyłączenia awaryjnego | **Przeniesione warunkowo** — Configurations → CC Validation Region (Additional NEC or outage); ponowne obliczenie + pobranie IVA w wyższej wersji; ⚠ wykonalność w oknie 40/25 min *do potwierdzenia z WPO* — jeżeli niewykonalne, opisać wyłącznie wariant „przyjmij wynik automatyczny" | — |
| 10 | CN2 nie kopiuje IVA/raportów do bucketów cca | **Przeniesione** — mail CCA o brakach; ręczne pobranie przez CCM i wgranie na MinIO `cca/ID_FBCC/in/BD` | U03 |
| 11 | Brak dostępu do CCCt | **Przeniesione** — weryfikacja statusów w CCM; telefon do CORESO/TSCNET; kanał awaryjny e-mail (operator@tscnet.eu, day-ahead.engineer@coreso.eu; zip <20 MB); przy dużym wolumenie od razu IVA BACKUP v1 mailem; = kod BPD ID*_24 (EDX/ECP → Helpdesk CCC) | U02 |
| 12 | F310 niedostarczone do CCCt | **Przeniesione** — Manual Upload FIDx-710; weryfikacja „710 – Individual CB Validation" → status Processed | U10, U11, P01 |
| 13 | F310 odrzucone | **Przeniesione** — podbicie wersji pliku (w Perun4V przy pobieraniu albo ręcznie w nazwie i wewnątrz pliku) i ponowny upload | U10, U12 |
| 14 | Brak F320_CCA / Vertices_MAP_CCA | **Usunięte** — plik F320/VERTICES_MAP nie wchodzi w skład paczki PERUN_IDx (vertices = FIDx-701 z CCCt); *do potwierdzenia u PSE-I, czy narzędzie fbc_lta_vertices ma odpowiednik w ID* | — |
| 15–26, 29 | Cała gałąź LTA (F320_LTA, raport CCA/RLTA, LTA_CURTAILMENT, redukcja LTA) | **Usunięte z uzasadnieniem** — w IDCC nie ma domeny LTA ani redukcji LTA. Zastępują je ryzyka strumienia ATC/NTC: U17 (niezakończenie walidacji ATC w czasie), ID*_4 / U20 (brak AAC z IDCC(a) — wysyłka AAC do XBID przez ZP przed 20:00/02:00/07:00), ID1_7 / U21 (decoupling SDAC — MD250), U22 (Late NTC po IDA2/IDA3), U23 (brak raportu CCA) | U17, U20–U23 |
| 27 | Brak dostępu do CCM | **Przeniesione** — monitoring bezpośrednio: MinIO `perun/ID_FBCC/in/BD` (paczki), Perun4V (obliczenia per iteracja od sFTP@pse.pl), kdm6 (raporty) | U01 |
| 28 | Błędna paczka / nieprawidłowe dane (CCM) | **Przeniesione** — czerwony kafelek z wykrzyknikiem = błędna wielkość pliku; podmiana z CCCt przez CCM „Wyślij"; *spodziewane wielkości plików IDx do ustalenia* | U09 |

**Nowe ryzyka (bez odpowiednika w BUP_03):**
- skrócone/przesunięte okno IVA (ID*_16 / ID2_15–16) — działanie procesowe: operator procesu pauzuje i wznawia etap, PSE wykonuje walidację w udostępnionym oknie;
- braki plików wejściowych PSE w TSO Data Merging (ID*_6/7/8/9 — GLSK/EC/CB, pliki MANDATORY) — dostarczenie/korekta przed CET na instrukcję operatora procesu, opcjonalnie replacement strategy;
- fallback automatyczny części TS w Initial/Final FB Computation (ID*_11/13) — wyłącznie przyjęcie maila do wiadomości (mail #5).

---

<a id="czesc-b"></a>
## 3. Część B — wpisanie w Core IDCC Flow Based Business Process Documentation

Struktura BPD: rozdziały per iteracja (IDCC(a); IDCC(b); IDCC(c)/(d) przez odwołanie do (b) z tabelą różnic), słownik i encje, harmonogram HLBP, szare tabele backup na końcu każdego rozdziału, numerowane szablony maili (#1–#33).

**B.1. Punkt zaczepienia = krok „Individual Validation".** W opisie kroku każdego rozdziału iteracyjnego BPD dodać odwołanie: *„TSO PSE wykonuje Individual Validation zgodnie z procedurą lokalną FBA_TSO_NOR_04; w sytuacjach awaryjnych FBA_TSO_BUP_04"* — analogicznie do istniejącego zapisu BPD „own tool, e.g. Perun". Dla IDCC(a) punktem zaczepienia jest krok „Individual CB and ATC Validation".

**B.2. Tabela krzyżowa kodów zdarzeń BPD → ryzyka procedury.** Nowa procedura zawiera tabelę mapującą każdy kod istotny dla PSE na numer własnego ryzyka i klasyfikację (słownik przyjęty w repo):

| Kod BPD | Klasyfikacja | Ryzyko BUP_04 |
|---|---|---|
| ID1_1, ID1_16, ID1_23 | DZIAŁANIE PROCESOWE | monitoring / potwierdzenia (NOR_04 §IDCC(a)) |
| ID1_7 | DZIAŁANIE BACKUPOWE | decoupling SDAC — MD250 (U21) |
| ID1_8 / ID1_9 / ID1_12 / ID1_26 | DZIAŁANIE BACKUPOWE | AAC → XBID przez ZP (U20) |
| ID1_27, ID2_24 / ID3C_22 / ID3_24 | DZIAŁANIE BACKUPOWE | problem EDX/ECP → Helpdesk CCC; upload przez Message Viewer / mail (odpowiednik ryzyka 11) |
| ID2_4 / ID3C_4 / ID3_4 | DZIAŁANIE BACKUPOWE | brak AAC z IDCC(a) — wysyłka przed 20:00 / 02:00 / 07:00 (U20) |
| ID2_6–9 / ID3C_6–9 / ID3_6–9 | DZIAŁANIE BACKUPOWE | brak/błąd plików PSE (GLSK/EC/CB — MANDATORY) w TSO Data Merging |
| ID2_11, ID2_13 (i odpowiedniki ID3C/ID3) | FALLBACK AUTOMATYCZNY | brak działań PSE; mail #5 do wiadomości |
| ID2_15–17, ID3_15–17, ID3C_15 | DZIAŁANIE PROCESOWE | strumień NTC/ATC — monitoring, UMM po stronie operatora procesu |
| ID2_19 / ID3C_17 / ID3_19 | DZIAŁANIE PROCESOWE | weryfikacja NTC (FIDx-921) po obu stronach granicy |
| ID2_23 / ID3C_21 / ID3_23 | DZIAŁANIE PROCESOWE | CCCt niedostępny w CET — UMM |
| ID3_1–ID3_3 | działania CCC (poza PSE) | tylko kontekst — bez ryzyka po stronie PSE |

**B.3. Szablony maili.** Procedura odwołuje się do numerów wiadomości BPD (mail #1–#33; treści w `process2_mail.html`) — nie kopiuje treści, żeby uniknąć rozjazdu wersji.

**B.4. Terminy — jedno źródło prawdy.** Tabele TET/CET procedury (FIDx-607/617/710/831 per iteracja) muszą być 1:1 z harmonogramem HLBP; BPD pełni rolę referencji. Przy każdej aktualizacji HLBP aktualizować tabelę w procedurze.

<a id="b5-punkt-weryfikacji-z-3docx"></a>
**B.5. Punkt weryfikacji z plikiem (3).docx.** Po uzyskaniu dostępu do „Core IDCC Flow Based Business Process Documentation (3).docx" porównać z konspektem:
1. numerację rozdziałów i nazwy kroków (m.in. czy krok nazywa się „Initial FB Computation" — w DA odpowiednik to „Intermediate FB Computation"),
2. kody zdarzeń ID1_x / ID2_x / ID3C_x / ID3_x (kompletność i numeracja),
3. numery szablonów maili,
4. czasy TET/CET wszystkich plików PSE,
5. czy wersja (3) różni się od v5.0 w zakresie okna IVA (40/25 min) i listy plików paczki PERUN_IDx.

---

<a id="todo"></a>
## 4. Lista TODO / do potwierdzenia przed redakcją dokumentów

| # | Pytanie | Adresat |
|---|---|---|
| 1 | Maski nazw paczek i raportów sFTP↔Perun4V dla IDx (odpowiedniki `PSE_RRRRMMDD_DA_v*_input_validation_DACCA.zip` / `..._validation_Reports_DACCA.zip`) | PSE-I (PSE Innowacje) |
| 2 | Numeracja nowych procedur (NOR_04/BUP_04 czy inna konwencja, np. FBA_TSO_NOR_ID_01) | właściciel procedur / WPO |
| 3 | Nazwa kroku w CCCt View Results dla bulk edit IVA w procesie ID (odpowiednik „Intermediate FB Computation V_1") | WPO / CORESO |
| 4 | Realność ponownego przeliczenia w Perun4V (dodatkowe wyłączenie awaryjne) w oknie 40/25 min | WPO |
| 5 | Ścieżki katalogów sieciowych dla plików IDCC (odpowiednik `\\uo-data\...\Pliki wejściowe do DA FBA\rrrrMMdd\PERUN\`) — czy per iteracja | WPO |
| 6 | Czy narzędzie stand-alone (odpowiednik fbc_lta_vertices.exe) występuje w procesie ID; jeżeli nie — potwierdzić usunięcie ryzyka 14 | PSE-I |
| 7 | Spodziewane prawidłowe wielkości plików paczki PERUN_IDx na MinIO (do ryzyka „błędna paczka") | PSE-I |
| 8 | Dostarczenie pliku „Core IDCC Flow Based Business Process Documentation (3).docx" → wykonać weryfikację B.5 | autor zlecenia |
