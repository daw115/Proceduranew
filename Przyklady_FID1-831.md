# FID1-831 (AC, IDCC(a))

**TET:** 14:00 *(dla XBID)* | **CET:** 17:36 | **Profil pulpitu:** 2CCT (CCTool wyśl. + CCTool zwalid.)
**Wysyłki automatyczne z ZP:**
- **v1** — 13:46 *(pierwsza wersja przed TET)*
- **14:41** — automat publikujący najbardziej aktualną wersję

**Legenda kategorii (zweryfikowane z Confluence i z Dyspozytorem):**
- 🟢 **Kategoria A — STAN OK / Dyspozytor zatwierdził** (zielony / fioletowy / ciemnozielony W / W po CET / zielony R w którejkolwiek kolumnie) → brak procedur backupowych; ewentualnie [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4
- ⚪ **Kategoria B — MONITORING** (szary / pomarańczowy + szary / wysyłka trwa) → bez akcji, czujność
- 🟡 **Kategoria C — BACKUP WYMAGANY** (czerwony / czerwony ? / czerwony ! bez ręcznego znacznika) → procedury z [Ryzyka_pelna_baza_IDCC.html](Ryzyka_pelna_baza_IDCC.html)
- 🔴 **Kategoria D — KRYTYCZNY** (czarny / czarny) → zgłoszenie, brak możliwości naprawy

**Zasada główna:** ręczny znacznik (`W`, `W po CET`, `R`) w którejkolwiek kolumnie = Dyspozytor już wykonał interwencję / zatwierdził status = brak procedur backupowych.

> ⚠ **Każde ryzyko należy zgłosić do: CIZ, WPO, PSE-I (PSE Innowacje).**

---

# Kategoria 🟢 A — STANY OK + Z RĘCZNYM ZNACZNIKIEM (24 stany, bez procedur backupowych)

## A.1. Stany Happy Day i pozytywne automatyczne (14 stanów)

### Stan 1: `zielony` / `zielony` 🟢 A — **Happy Day**

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| zielony | zielony |

**Co oznacza:** Plik dostarczony z ZP automatycznie, ACK pozytywny, publikacja AC do PuTo zaakceptowana.
**Działania:** Brak — proces przebiegł poprawnie.

---

### Stan 2: `zielony` / `zielony R` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| zielony | zielony R |

**Co oznacza:** Plik dotarł, ACK oznaczono ręcznie statusem 'R' przez Dyspozytora po weryfikacji w CCCt.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4 z uzasadnieniem statusu 'R'.

---

### Stan 3: `zielony` / `fioletowy` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| zielony | fioletowy |

**Co oznacza:** ACK pozytywny, ale dotarł po CET. Plik zaakceptowany z opóźnieniem.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4 z czasem dostarczenia.

---

### Stan 4: `ciemnozielony W` / `zielony` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| ciemnozielony W | zielony |

**Co oznacza:** Plik wysłany ręcznie z CCM (PPM → Wyślij) lub przez GUI CCCt (Manual Upload) przed CET. ACK pozytywny.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4 z uzasadnieniem ręcznej wysyłki.

---

### Stan 5: `ciemnozielony W` / `zielony R` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| ciemnozielony W | zielony R |

**Co oznacza:** Ręczna wysyłka przed CET + ACK ręczny ('R') po weryfikacji w CCCt.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4 z pełnym uzasadnieniem.

---

### Stan 6: `ciemnozielony W` / `fioletowy` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| ciemnozielony W | fioletowy |

**Co oznacza:** Ręczna wysyłka przed CET, ale ACK napłynął po CET. Proces zakończony.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4.

---

### Stan 7: `ciemnozielony W po CET` / `zielony` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| ciemnozielony W po CET | zielony |

**Co oznacza:** Ręczna wysyłka po CET (opcja „Wyślij po CET"), ACK pozytywny. Proces zakończony po terminie.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4 z pełnym uzasadnieniem opóźnienia + zgłoś (informacyjnie).

---

### Stan 8: `ciemnozielony W po CET` / `zielony R` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| ciemnozielony W po CET | zielony R |

**Co oznacza:** Ręczna wysyłka po CET + status ACK 'R' nadany ręcznie.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4.

---

### Stan 9: `ciemnozielony W po CET` / `fioletowy` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| ciemnozielony W po CET | fioletowy |

**Co oznacza:** Wszystko po CET — ręczna wysyłka po CET + ACK po CET pozytywny.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4.

---

### Stan 10: `zielony R` / `zielony` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| zielony R | zielony |

**Co oznacza:** Status wysyłki nadany ręcznie 'R' + ACK automatyczny pozytywny.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4.

---

### Stan 11: `zielony R` / `zielony R` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| zielony R | zielony R |

**Co oznacza:** Status ręczny 'R' w obu kolumnach — proces w pełni oznaczony ręcznie po weryfikacji w CCCt.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4 z pełnym uzasadnieniem.

---

### Stan 12: `zielony R` / `fioletowy` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| zielony R | fioletowy |

**Co oznacza:** Status wysyłki nadany ręcznie 'R' + ACK pozytywny po CET.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4.

---

### Stan 13: `fioletowy` / `zielony` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| fioletowy | zielony |

**Co oznacza:** Plik dostarczony do CCCt po CET, ale ACK wcześniejszy pozytywny.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4.

---

### Stan 14: `fioletowy` / `fioletowy` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| fioletowy | fioletowy |

**Co oznacza:** AC dostarczone i zwalidowane automatycznie po CET. Proces zakończony z opóźnieniem.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4 z czasem dostarczenia.

---

## A.2. Stany z ręcznym znacznikiem — Dyspozytor podjął decyzję (10 stanów)

> Z perspektywy Dyspozytora ręczny znacznik (W / W po CET / R) oznacza świadomą interwencję. Pomimo problematycznych stanów w drugiej kolumnie — sytuacja została obsłużona ręcznie. Wymagany wpis A.4 z uzasadnieniem.

### Stan 15: `ciemnozielony W` / `czerwony` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| ciemnozielony W | czerwony |

**Co oznacza:** Ręczna wysyłka przed CET, ACK negatywny — Dyspozytor wysłał, CCCt odrzucił z kodem (typowo 20/21/30).
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4 — odczytaj kod ACK, opisz przyczynę. Jeśli krytyczne (proces nie domknięty) — Dyspozytor sam decyduje o kolejnej iteracji (ponowna ręczna z v+1).

---

### Stan 16: `ciemnozielony W` / `czerwony ?` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| ciemnozielony W | czerwony ? |

**Co oznacza:** Ręczna wysyłka przed CET, ACK nie napłynął w czasie — opóźnienie potwierdzenia z CCCt.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4. Monitoring (CCCt MV); jeśli sytuacja długotrwała — decyzja Dyspozytora (zgłoś jeśli CN2 zwrotny).

---

### Stan 17: `ciemnozielony W` / `czarny` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| ciemnozielony W | czarny |

**Co oznacza:** Ręczna wysyłka przed CET, ACK nie napłynął do CET — możliwa awaria transportu zwrotnego CN2 lub plik został przyjęty bez ACK.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4. Weryfikacja w CCCt MV; jeśli Processed → ustaw ręczny 'R' i zgłoś na CCM. Jeśli rzeczywista awaria CN2 zwrotny → zgłoś.

---

### Stan 18: `ciemnozielony W po CET` / `czerwony` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| ciemnozielony W po CET | czerwony |

**Co oznacza:** Ręczna wysyłka po CET, ACK negatywny (typowo 20 gateClosed — bramka zamknięta po CET).
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4 z kodem ACK. Zgłoś (informacyjnie).

---

### Stan 19: `ciemnozielony W po CET` / `czerwony ?` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| ciemnozielony W po CET | czerwony ? |

**Co oznacza:** Ręczna wysyłka po CET, ACK nie napłynął w czasie (>2 min).
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4. Monitoring CCCt MV; po 2 min → status ręczny 'R' jeśli zasadne.

---

### Stan 20: `ciemnozielony W po CET` / `czarny` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| ciemnozielony W po CET | czarny |

**Co oznacza:** Ręczna wysyłka po CET, brak ACK do końca doby.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4 z pełnym opisem. Zgłoś (informacyjnie) + telefon CCC; diagnostyka CN2 → zgłoś.

---

### Stan 21: `zielony R` / `czerwony` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| zielony R | czerwony |

**Co oznacza:** Status wysyłki nadany ręcznie 'R' + ACK negatywny — Dyspozytor zaznaczył jako wysłane, ale CCCt zwrócił błąd ACK.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4 z kodem ACK i uzasadnieniem statusu 'R'. Weryfikacja w CCCt MV; ewentualna decyzja o nowej iteracji.

---

### Stan 22: `zielony R` / `czerwony ?` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| zielony R | czerwony ? |

**Co oznacza:** Status wysyłki ręczny 'R' + ACK nie napłynął.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4. CCCt MV → weryfikacja; po 5 min → ustaw 'R' w obu kolumnach jeśli proces OK.

---

### Stan 23: `zielony R` / `czarny` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| zielony R | czarny |

**Co oznacza:** Status wysyłki ręczny 'R' + brak ACK do CET.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4. CCCt MV → weryfikacja statusu; diagnostyka CN2 zwrotny przy konieczności → zgłoś.

---

### Stan 24: `czerwony !` / `zielony R` 🟢 A

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| czerwony ! | zielony R |

**Co oznacza:** Plik o niepoprawnym rozmiarze, ale status ACK ręczny 'R' przyznany przez Dyspozytora po weryfikacji w CCCt — zawartość pliku została potwierdzona jako poprawna mimo małego rozmiaru.
**Działania:** [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4 z uzasadnieniem (zawartość zweryfikowana mimo ostrzeżenia o rozmiarze). Zgłoś (informacyjnie — zmiana konfiguracji minimalnego rozmiaru jeśli problem powtarza się).

---

# Kategoria ⚪ B — MONITORING (3 stany, bez procedur)

## Stan 25: `szary` / `szary` ⚪ B

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| szary | szary |

**Co oznacza:** Plik nie wymagany — pozostało >30 min do TET. Stan normalny przed startem procesu.
**Działania:** Brak — monitoring.

---

## Stan 26: `pomarańczowy` / `szary` ⚪ B

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| pomarańczowy | szary |

**Co oznacza:** Zbliża się TET (14:00) — TET dla XBID. ZP miało wysłać v1 o 13:46 — plik nie dotarł do CCM. **Czujność.**
**Działania:** Brak. **Czujność i przygotowanie** — sprawdź [R20](Ryzyka_pelna_baza_IDCC.html#R20) (ZP gotowość), [R18](Ryzyka_pelna_baza_IDCC.html#R18) (CN2). Jeśli sytuacja się utrzyma do CET → Kategoria C (Stan 28-29).

---

## Stan 27: `czerwony ?` / `szary` ⚪ B

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| czerwony ? | szary |

**Co oznacza:** Wysyłka trwa — plik oddany do Connector 2.0, oczekiwanie na potwierdzenie. Stan przejściowy (~1-2 min).
**Działania:** Brak. **Czekaj 5 min**; jeśli nadal `czerwony ?` → sprawdź [R18](Ryzyka_pelna_baza_IDCC.html#R18) CN2.

---

# Kategoria 🟡 C — BACKUP WYMAGANY (10 stanów)

## Stan 28: `pomarańczowy` / `czerwony` 🟡 C

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| pomarańczowy | czerwony |

**Co oznacza:** TET zbliża się + ACK negatywny z poprzedniej próby wysyłki. Sytuacja nietypowa.
**Procedura:** [R05](Ryzyka_pelna_baza_IDCC.html#R05) — odczytaj kod ACK; przygotuj nową wersję.
**Kroki:** odczytaj kod ACK (20 gateClosed → zgłoś (admin CCCt otwiera bramkę); 21 duplicatedVersion → [R20](Ryzyka_pelna_baza_IDCC.html#R20) ZP → [P01](Karta_ryzyk_IDCC.md#P01) z v+1; 30 file size → patrz Stan 32).

---

## Stan 29: `czerwony` / `czerwony` 🟡 C

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| czerwony | czerwony |

**Co oznacza:** Zbliża się CET (17:36) — plik niedostarczony lub wysyłka zakończona błędem. **Stan alarmowy.**
**Procedury:** [R04](Ryzyka_pelna_baza_IDCC.html#R04), [R18](Ryzyka_pelna_baza_IDCC.html#R18).
**Kroki:** CCCt MV → sprawdź czy plik jest; brak CN2 → [R20 ZP](Ryzyka_pelna_baza_IDCC.html#R20) → [P02](Karta_ryzyk_IDCC.md#P02) → [P01](Karta_ryzyk_IDCC.md#P01). Brak ACK >5 min → ponów z wyższą wersją.

---

## Stan 30: `czerwony` / `czerwony ?` 🟡 C

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| czerwony | czerwony ? |

**Co oznacza:** CET zbliża się + ACK w trakcie próby. **Ostatnia szansa.**
**Procedury:** [R04](Ryzyka_pelna_baza_IDCC.html#R04), [R06](Ryzyka_pelna_baza_IDCC.html#R06).
**Kroki:** CCCt MV → po 2 min weryfikacja; → [P02](Karta_ryzyk_IDCC.md#P02) + [P01](Karta_ryzyk_IDCC.md#P01); zgłoś + telefon CCC.

---

## Stan 31: `czerwony !` / `czerwony ?` 🟡 C

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| czerwony ! | czerwony ? |

**Co oznacza:** Niepoprawny rozmiar pliku + brak ACK w czasie.
**Procedury:** [R05](Ryzyka_pelna_baza_IDCC.html#R05), [R06](Ryzyka_pelna_baza_IDCC.html#R06).
**Kroki:** weryfikacja rozmiaru (CCM LPM → Informacje); [R20 ZP](Ryzyka_pelna_baza_IDCC.html#R20) → [P02](Karta_ryzyk_IDCC.md#P02) → [P01](Karta_ryzyk_IDCC.md#P01) z v+1; po 3 min CCCt MV.

---

## Stan 32: `czerwony !` / `czerwony` 🟡 C

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| czerwony ! | czerwony |

**Co oznacza:** Niepoprawny rozmiar + ACK negatywny (typowo kod 30 file size mismatch).
**Procedura:** [R05](Ryzyka_pelna_baza_IDCC.html#R05) (kod 30).
**Kroki:** CCM LPM → Informacje → potwierdź rozmiar; [R20 ZP](Ryzyka_pelna_baza_IDCC.html#R20) → [P02](Karta_ryzyk_IDCC.md#P02) → [P01](Karta_ryzyk_IDCC.md#P01) z v+1. Nadal za mały → zgłoś.

---

## Stan 33: `czerwony !` / `fioletowy` 🟡 C *(sprzeczność)*

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| czerwony ! | fioletowy |

**Co oznacza:** Niepoprawny rozmiar + ACK po CET pozytywny. **Sprzeczność** — wymaga weryfikacji.
**Działania:** [P04](Karta_ryzyk_IDCC.md#P04) — pobierz z MinIO, sprawdź zawartość; zawartość OK → zgłoś (zmiana konfiguracji rozmiaru); niepoprawna → zgłoś; sprawdź czy AC w PuTo jest aktualne. Po weryfikacji można nadać `zielony R` → Stan 24 (Kategoria A).

---

## Stan 34: `zielony` / `czerwony` 🟡 C

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| zielony | czerwony |

**Co oznacza:** Plik dotarł do CCCt, ale ACK negatywny (Rejected). Kody najczęstsze: 20 / 21 / 30.
**Procedura:** [R05](Ryzyka_pelna_baza_IDCC.html#R05) — reakcja per kod ACK.
**Kroki:** odczytaj kod ACK (najedź na czerwony status); reakcja:
- **20 gateClosed** → zgłoś (admin CCCt otwiera bramkę); sprawdź `IDx-AC-FORWARDING`
- **21 duplicatedVersion** → [R20 ZP](Ryzyka_pelna_baza_IDCC.html#R20) → [P01](Karta_ryzyk_IDCC.md#P01) z v+1
- **30 file size** → [P04 MinIO](Karta_ryzyk_IDCC.md#P04) / [P02 ZP](Karta_ryzyk_IDCC.md#P02) → weryfikacja → [P01](Karta_ryzyk_IDCC.md#P01)

---

## Stan 35: `zielony` / `czerwony ?` 🟡 C

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| zielony | czerwony ? |

**Co oznacza:** Plik wysłany, ACK nie napłynął w przewidywanym czasie (>2-3 min). Stan oczekiwania.
**Procedura:** [R06](Ryzyka_pelna_baza_IDCC.html#R06).
**Kroki:** czekaj do 5 min od wysyłki; po 5 min → CCCt MV (Processed → zgłoś; Rejected → patrz Stan 34; brak wpisu → [R18 CN2](Ryzyka_pelna_baza_IDCC.html#R18)). ⚠ NIE wysyłać ponownie bez weryfikacji.

---

## Stan 36: `zielony` / `czarny` 🟡 C

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| zielony | czarny |

**Co oznacza:** Plik wysłany, ale ACK nie napłynął do CET. Niejasny status w CCCt.
**Procedury:** [R06](Ryzyka_pelna_baza_IDCC.html#R06), [R18](Ryzyka_pelna_baza_IDCC.html#R18).
**Kroki:** CCCt MV → status; `Processed` → status ręczny 'R' w CCM + zgłoś → przechodzi do Stan 2 (Kategoria A); `Rejected` → [P01](Karta_ryzyk_IDCC.md#P01) z opcją „Wyślij po CET"; brak wpisu → [R18 CN2 awaria zwrotna](Ryzyka_pelna_baza_IDCC.html#R18) → zgłoś. Zgłoś + telefon CCC.

---

## Stan 37: `czerwony !` / `czarny` 🟡 C

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| czerwony ! | czarny |

**Co oznacza:** **KRYTYCZNE w obrębie Kategorii C** — niepoprawny rozmiar + brak ACK do CET. Plik nieprzyjęty, proces zatrzymany.
**Procedury:** [R05](Ryzyka_pelna_baza_IDCC.html#R05), [R18](Ryzyka_pelna_baza_IDCC.html#R18).
**Kroki:** [R20 ZP](Ryzyka_pelna_baza_IDCC.html#R20) → [P02](Karta_ryzyk_IDCC.md#P02) → [P01](Karta_ryzyk_IDCC.md#P01) „Wyślij po CET" (jeśli bramka jeszcze otwarta); natychmiast zgłoś + telefon CCC.

---

# Kategoria 🔴 D — KRYTYCZNY (1 stan)

## Stan 38: `czarny` / `czarny` 🔴 D

| CCTool wyśl. | CCTool zwalid. |
|---|---|
| czarny | czarny |

**Co oznacza:** **KRYTYCZNE** — minął CET (17:36), AC niedostarczone. Publikacja do PuTo nie nastąpiła. **Po CET dograć już nie można** — bramka zamknięta.
**Działania:** **Brak możliwości naprawy.** Natychmiast:
- Telefon **CCC ([N13](Inwentarz_IDCC.md#N13))** — uprzedzić o braku publikacji AC dla doby D
- **Zgłoś** (CIZ, WPO, PSE-I) — incydent krytyczny
- [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4 z pełnym opisem zdarzenia i analizą przyczyn

---

# Definicja pliku

**Plik:** FID1-831 (AC — Allocation Constraints)

**Plik przychodzący z:** aplikacja **ZP** (zdolności przesyłowe) — system wewnętrzny PSE
**Plik wychodzący do:** Core CC Tool → publikacja **AC do PuTo** (Platforma Udostępniania Transmisyjnych)
**Transport:** Connector 2.0 (kanał `EDX_KAFKA_CCCTOOL-SQLNET_ZP`); kopia na MinIO `cca/ID_FBCC/in/yyyymmdd/`

**Budowa pliku:**
- **Format:** XML
- **Maska nazwy:** `rrrrMMdd-FID1-831-v*-<sender>-to-<receiver>.xml`
- **Zawartość:** wartości Allocation Constraints (ograniczenia alokacyjne) dla iteracji IDCC(a), per godzina doby handlowej
- **Struktura logiczna:** TimeSeries per kierunek (np. PL→DE, DE→PL), wartość ograniczenia mocowego per godzina (MTU = 60 min)
- **Wersjonowanie:** v1, v2, … (kolejna wersja musi być wyższa — sprawdzane przez CCCt, kod ACK 21 jeśli nie)

---

# Statystyki

| Kategoria | Liczba stanów | Stany |
|---|---|---|
| 🟢 A.1 — OK pozytywne automatyczne | 14 | #1-14 |
| 🟢 A.2 — Ręczne znaczniki (W/W po CET/R) | 10 | #15-24 |
| ⚪ B — Monitoring | 3 | #25-27 |
| 🟡 C — Backup wymagany | 10 | #28-37 |
| 🔴 D — Krytyczny | 1 | #38 |
| **Razem** | **38** | |

**Zasada:** każdy stan z ręcznym znacznikiem (`W`, `W po CET`, `R`) w którejkolwiek kolumnie = Kategoria A (Dyspozytor już podjął decyzję / wykonał interwencję) = bez procedur backupowych; wymagany [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4.

**Weryfikacja z Confluence (PDF s. 4-7):** opisy IVA dla stanów z ręcznymi znacznikami **nie mają sekcji „propozycja działania"** → potwierdzono brak procedur backupowych.
