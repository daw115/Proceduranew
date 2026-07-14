# Karty plików FIDx-xxx — pulpit IDCC CCM

> **Edytuj ten plik bezpośrednio.** Po każdej karcie powiedz „dalej" — odczytam aktualną treść (z Twoimi poprawkami) i dopiszę kolejną kartę. Konsolidacja do xlsx na końcu.
>
> **Pełne opisy ryzyk i procedur:** [Karta_ryzyk_IDCC.md](Karta_ryzyk_IDCC.md). W tabelach stanów używamy kodów **U-** (ryzyka) i **P-** (procedury) jako hiperłącza do szczegółów.

**Status:** IDCC(a) — 2/4 kart zaproponowane; IDCC(b) — 0/23 kart.

**Legenda statusów ryzyk:**
- ✅ — zaakceptowane przez Dyspozytora
- ✏️ — wymaga poprawki / dopisu
- ❓ — pytanie do rozstrzygnięcia
- ❌ — nie aplikuje się / usunąć

**Wspólne narzędzia (HTML §6):**
- **CCM** — https://ccm.spsm.pse.pl — monitoring statusów
- **Core CC Tool (CCCt)** — Message Viewer, Manual Upload
- **Perun4V** — https://lccv.tscnet.eu — walidacja FBA
- **MinIO** — https://minio-gui.pse.pl — repozytorium plików (buckets: `perun/`, `cca/`, `mam/`)
- **Connector 2.0** — transport między CCM ↔ CCCt ↔ MinIO ↔ Perun4V
- **KreatorDACF&2DAF_CGMES** — używany dla **FID2-607 i FID2-617** (IDCC(b) tylko); dla IDCC(c)/(d) → KreatorIDCF (inne procedury BUP)
- **KreatorIDCF_CGMES** — używany dla **FIDx-607 i FIDx-617** dla IDCC(c)/(d)/(e)
- **kdm6@pse.pl** — skrzynka pocztowa (raporty CCA)
- **CIZ** — Centrum Zgłaszania Incydentów PSE
- **WPO** — Wydział Wsparcia Procesów Operatorskich (Słabicki, Jarzęcka, Krzysztoszek, Łukaszewski, Rodo)

> ⚠ **Każde ryzyko należy zgłosić do: CIZ, WPO, PSE-I (PSE Innowacje).**

---

## Karta #1 — FID1-831 (AC, Allocation Constraints, IDCC(a))

**Faza:** IDCC(a) — Allocation Constraints
**TET:** 13:50 | **CET:** 14:45 | **Profil pulpitu:** 2CCT (CCTool wyśl. + CCTool zwalid.)

### Automatyczne wysyłki z ZP

| Wersja | Godzina wysyłki | Uwaga |
|---|---|---|

| v1 | **13:45** | Doba D-1 automatyczna najbardziej aktualnej wersji |
| v+1 | **14:20** | Doba D-1 automatyczna najbardziej aktualnej wersji |

> **Wzorzec ogólny** (dla wszystkich FIDx-831):
> - FID1: v1 13:45, v+1 14:20
> - FID2: v1 13:45 (D-1), v+1 21:40 (D-1)
> - FID3C / FID3: v1 13:45 (D-1), v+1 4:10 (D), v+1 9:40 (D)

### Czym jest FID1-831

Plik z wynikiem **Allocation Constraints** dla iteracji IDCC(a). Publikowany przez TSO do **PuTo** poprzez Core CC Tool jako wynik procesu IDCC(a) (HTML §4.3).

### Tor narzędziowy

```
ZP (źródło AC)  ─► Connector 2.0 ─► Core CC Tool ─[ACK]─► CCM (CCTool zwalid.)
                        │                 │
                        └─► MiNIO         └─► publikacja do PuTo
```

- **Generator:** ZP - zdolności przesyłowe
- **Transport:** Connector 2.0 (EDX_KAFKA_CCCTOOL-SQLNET_ZP)
- **Odbiorca:** Core CC Tool → publikacja AC do PuTo, MiNIO
- **Monitoring:** CCM, kolumny CCTool wyśl. i CCTool zwalid.

### Komunikaty ACK specyficzne dla FID1-831

(PDF Dyspozytora s. 13)

| Kod | Treść | Działanie |
|---|---|---|
| 0 | Message fully accepted | OK — publikacja AC do PuTo |
| 20 | Gate for provided message definition is not opened | **Bramka zamknięta — wysłanie pliku niemożliwe.** Sprawdź TET i CET; jeśli zgodny → sprawdź w CCCt proces `IDx-AC-FORWARDING`. Zgłoś |
| 21 | Provided version is not higher than already stored data (duplicatedVersion) | Podbić wersję i ponowić Manual Upload |
| 22 | ~~Delivered constraint value is negative~~ | ❌ **Nie występuje już** — CCCt przyjmuje wartości ujemne |
| 30 | File size mismatch | Pobrać z MinIO i wgrać przez CCM lub GUI CCCt. **Jeśli brak MinIO — tylko GUI CCCt** (procedura: pobranie z ZP, patrz niżej) |
| — | Message has some invalid timeSeries that does not meet primary MTU rules | Poprawić plik AC (struktura), ponowić |

### Ryzyka aplikujące się do FID1-831

**Narzędziowe:** [U01](Karta_ryzyk_IDCC.md#U01), [U02](Karta_ryzyk_IDCC.md#U02), [U03](Karta_ryzyk_IDCC.md#U03) (CN2 — obejmuje pełną i selektywną awarię), [U04](Karta_ryzyk_IDCC.md#U04), [U06](Karta_ryzyk_IDCC.md#U06) (ZP)
**Plikowe:** [U08](Karta_ryzyk_IDCC.md#U08), [U09](Karta_ryzyk_IDCC.md#U09), [U10](Karta_ryzyk_IDCC.md#U10), [U11](Karta_ryzyk_IDCC.md#U11), [U12](Karta_ryzyk_IDCC.md#U12), [U13](Karta_ryzyk_IDCC.md#U13)

**Procedury reagujące:** [P01 (GUI CCCt)](Karta_ryzyk_IDCC.md#P01), [P02 (ZP→CCCt)](Karta_ryzyk_IDCC.md#P02), [P04 (MinIO)](Karta_ryzyk_IDCC.md#P04), [P06 (wpis A.4)](Karta_ryzyk_IDCC.md#P06)

### Ryzyka NIE aplikujące się do FID1-831

- [U05](Karta_ryzyk_IDCC.md#U05) (Perun4V), [U07](Karta_ryzyk_IDCC.md#U07) (kdm6) — AC nie używa
- [U14](Karta_ryzyk_IDCC.md#U14)-[U17](Karta_ryzyk_IDCC.md#U17) — obliczenia FBA / ATC
- ~~U18~~ (scalone z [U03](Karta_ryzyk_IDCC.md#U03))
- [U19](Karta_ryzyk_IDCC.md#U19)-[U23](Karta_ryzyk_IDCC.md#U23) — inne strumienie (Backup, AAC, MD250, NTC, CCA)

### Tabela stanów kafelka × ryzyka × działanie

| # | CCTool wyśl. | CCTool zwalid. | Opis (krótko) | Ryzyka | Procedura | Status |
|---|---|---|---|---|---|---|
| 1 | szary | szary | Przedwczesne (>30 min do TET) | [U01](Karta_ryzyk_IDCC.md#U01), [U02](Karta_ryzyk_IDCC.md#U02) | monitoring | |
| 2 | pomarańczowy | pomarańczowy | Zbliża się TET, brak AC | [U03](Karta_ryzyk_IDCC.md#U03), [U08](Karta_ryzyk_IDCC.md#U08) | sprawdzić ZP (bilans AC); szykować [P02](Karta_ryzyk_IDCC.md#P02) | |
| 3 | czerwony | czerwony | Zbliża się CET, brak wysyłki / błąd | [U03](Karta_ryzyk_IDCC.md#U03), [U08](Karta_ryzyk_IDCC.md#U08), [U10](Karta_ryzyk_IDCC.md#U10) | CCM PPM Wyślij; brak CN2 → [P02](Karta_ryzyk_IDCC.md#P02) + [P01](Karta_ryzyk_IDCC.md#P01) | |
| 4 | czarny | czarny | Nie dostarczono, minął CET | [U03](Karta_ryzyk_IDCC.md#U03), [U08](Karta_ryzyk_IDCC.md#U08), [U03](Karta_ryzyk_IDCC.md#U03) | **KRYTYCZNE** — zgłoś + telefon CCC. **Po CET dograć już nie można** | |
| 5 | zielony | zielony | Happy Day — publikacja do PuTo | — | brak interwencji | |
| 6 | zielony | czerwony | ACK negatywny | [U10](Karta_ryzyk_IDCC.md#U10) | sprawdzić kod ACK (20/21/30) → [P01](Karta_ryzyk_IDCC.md#P01) z poprawionym plikiem ([P02](Karta_ryzyk_IDCC.md#P02) lub [P04](Karta_ryzyk_IDCC.md#P04)) | |
| 7 | zielony | czerwony z '?' | ACK nie napłynął (>2-3 min) | [U11](Karta_ryzyk_IDCC.md#U11) | CCCt Message Viewer; po 10 min → [P01](Karta_ryzyk_IDCC.md#P01) | |
| 8 | zielony | czarny | Brak ACK do CET | [U11](Karta_ryzyk_IDCC.md#U11), [U03](Karta_ryzyk_IDCC.md#U03) | sprawdzić CN2; [P01](Karta_ryzyk_IDCC.md#P01) z [P02](Karta_ryzyk_IDCC.md#P02) | |
| 9 | zielony | fioletowy | ACK pozytywne po CET — ⚠ wysyłka powinna być do TET | [U13](Karta_ryzyk_IDCC.md#U13) | [P06](Karta_ryzyk_IDCC.md#P06) wpis A.4 | |
| 10 | zielony | zielony 'R' (ręczny) | Status nadany ręcznie | [U13](Karta_ryzyk_IDCC.md#U13) | [P06](Karta_ryzyk_IDCC.md#P06) | |
| 11 | ciemnozielony 'W' | zielony | Ręczna wysyłka przed CET, ACK OK | [U03](Karta_ryzyk_IDCC.md#U03) | [P02](Karta_ryzyk_IDCC.md#P02) → [P01](Karta_ryzyk_IDCC.md#P01) → [P06](Karta_ryzyk_IDCC.md#P06) | |
| 12 | ciemnozielony 'W' | czerwony | Ręczna wysyłka, ACK negatywne | [U10](Karta_ryzyk_IDCC.md#U10), [U12](Karta_ryzyk_IDCC.md#U12) | kod ACK → ponowić z [U12](Karta_ryzyk_IDCC.md#U12) lub plik z [P02](Karta_ryzyk_IDCC.md#P02) | |
| 13 | ciemnozielony 'W' | czerwony z '?' | Ręczna, brak ACK w czasie | [U11](Karta_ryzyk_IDCC.md#U11) | CCCt MV; po 5 min ponowny [P01](Karta_ryzyk_IDCC.md#P01) | |
| 14 | ciemnozielony 'W' | czarny | Ręczna, brak ACK do CET | [U11](Karta_ryzyk_IDCC.md#U11), [U03](Karta_ryzyk_IDCC.md#U03) | CN2 diagnostyka; powtórny [P01](Karta_ryzyk_IDCC.md#P01) z [P02](Karta_ryzyk_IDCC.md#P02) | |
| 15 | ciemnozielony 'W po CET' | zielony | Ręczna po CET, ACK OK | [U03](Karta_ryzyk_IDCC.md#U03), [U13](Karta_ryzyk_IDCC.md#U13) | [P01](Karta_ryzyk_IDCC.md#P01) (z opcją Wyślij po CET) → [P06](Karta_ryzyk_IDCC.md#P06) | |
| 16 | ciemnozielony 'W po CET' | czerwony | Ręczna po CET, ACK negatywne | [U10](Karta_ryzyk_IDCC.md#U10), [U12](Karta_ryzyk_IDCC.md#U12) | sprawdzić kod ACK; zgłoś | |
| 17 | ciemnozielony 'W po CET' | czerwony z '?' | Ręczna po CET, brak ACK w czasie | [U11](Karta_ryzyk_IDCC.md#U11) | po 2 min status ręczny 'R' | |
| 18 | ciemnozielony 'W po CET' | czarny | Ręczna po CET, brak ACK do końca doby | [U11](Karta_ryzyk_IDCC.md#U11), [U03](Karta_ryzyk_IDCC.md#U03) | zgłoś + telefon CCC | |
| 19 | zielony 'R' | zielony 'R' | Status ręczny po obu stronach | [U13](Karta_ryzyk_IDCC.md#U13) | [P06](Karta_ryzyk_IDCC.md#P06) | |
| 20 | fioletowy | fioletowy | Wszystko po CET, OK | [U13](Karta_ryzyk_IDCC.md#U13) | [P06](Karta_ryzyk_IDCC.md#P06) | |
| 21 | czerwony z '!' | czerwony z '!' | Za mały rozmiar AC | [U09](Karta_ryzyk_IDCC.md#U09) | C.3 Informacje → [P02](Karta_ryzyk_IDCC.md#P02) → [P01](Karta_ryzyk_IDCC.md#P01) | |
| 22 | czerwony z '!' | czerwony z '?' | Niepoprawny rozmiar + brak ACK | [U09](Karta_ryzyk_IDCC.md#U09), [U11](Karta_ryzyk_IDCC.md#U11) | [P02](Karta_ryzyk_IDCC.md#P02); po 3 min CCCt MV | |
| 23 | czerwony z '!' | czerwony | Niepoprawny rozmiar + ACK negatywne | [U09](Karta_ryzyk_IDCC.md#U09), [U10](Karta_ryzyk_IDCC.md#U10), [U12](Karta_ryzyk_IDCC.md#U12) | [P02](Karta_ryzyk_IDCC.md#P02) → [P01](Karta_ryzyk_IDCC.md#P01) z wyższą wersją | |
| 24 | czerwony z '!' | czarny | Niepoprawny rozmiar + brak ACK do CET | [U09](Karta_ryzyk_IDCC.md#U09), [U11](Karta_ryzyk_IDCC.md#U11), [U03](Karta_ryzyk_IDCC.md#U03) | **KRYTYCZNE** [P02](Karta_ryzyk_IDCC.md#P02) → [P01](Karta_ryzyk_IDCC.md#P01); zgłoś | |
| 25 | czerwony z '!' | fioletowy | Niepoprawny rozmiar + ACK po CET pozytywne | [U09](Karta_ryzyk_IDCC.md#U09), [U13](Karta_ryzyk_IDCC.md#U13) | zweryfikować plik (może być OK); niepoprawny → zgłoś | |
| 26 | czerwony z '!' | zielony 'R' | Niepoprawny rozmiar + status ręczny | [U09](Karta_ryzyk_IDCC.md#U09), [U13](Karta_ryzyk_IDCC.md#U13) | [P06](Karta_ryzyk_IDCC.md#P06); zweryfikować plik | |
| 27 | czerwony z '?' | (brak) | Wysyłka trwa | [U11](Karta_ryzyk_IDCC.md#U11) | po 5 min CCCt MV | |

### Uwagi / pytania do rozstrzygnięcia

- ✅ Źródło: aplikacja **ZP** (zdolności przesyłowe) — bilans AC
- ✅ Kod ACK 22 (Negative constraint) — usunięty (CCCt akceptuje wartości ujemne)
- ✅ Nowe ryzyko **R_CN** (brak Connector 2.0) — dodane z procedurą pobrania z ZP
- ❓ **Harmonogram automatycznych wysyłek z ZP**: czy v+1 o 14:20 to wysyłka dla doby D+1, czy backupowa wersja dla doby D wysyłana wcześniej? Doprecyzować.
- ❓ Komunikat `Message has some invalid timeSeries…` — jakie jest praktyczne pochodzenie błędu (struktura XML, MTU)? Czy też usunąć z aktualnej listy?

### Aktualizacje do uwzględnienia w xlsx

- Nowa kolumna: **R_CN — Brak działania Connector 2.0** → procedura: pobranie z ZP → GUI CCCt Manual Upload
- Aktualizacja Generatora dla FIDx-831: **ZP (zdolności przesyłowe)**
- Usunięcie ACK 22 z opisów (nieaktualne)

---

## Karta #2 — FID1-928 (ATC Based Validation, IDCC(a))

**Faza:** IDCC(a) — ATC Based Validation
**TET:** 13:40 | **CET:** 14:20 | **Profil pulpitu:** 2CCT (CCTool wyśl. + CCTool zwalid.)

### Czym jest FID1-928

Wynik **walidacji ATC** prowadzonej centralnie po stronie Core CC Tool. Walidacja ATC jest **strumieniem odrębnym od FBA** (HTML §5.4) — uruchamiana po dostarczeniu paczki ATC. FIDx-928 jest plikiem **zwrotnym** publikowanym przez CCCt → TSO przez Connector 2.0.

### Tor narzędziowy

```
Paczka ATC (PERUN_IDx_ATC) ─► Core CC Tool ─[walidacja ATC]─► FIDx-928 ─► Connector 2.0 ─► CCM
                                                                                    │
                                                                                    └─► monitoring (TSO)
```

- **Generator:** Core CC Tool (centralnie, wynik walidacji)
- **Transport zwrotny:** Connector 2.0 (EDX_KAFKA_CCCTOOL-SQLNET)
- **Odbiorca:** CCM (monitoring statusu)
- **Zależność wejściowa:** PERUN_IDx_ATC (paczka ATC) musi być prawidłowo wysłana
- **Uwaga:** FIDx-928 NIE jest wysyłany przez TSO — Manual Upload nie ma zastosowania

### Komunikaty ACK

| Kod | Treść | Znaczenie dla FIDx-928 |
|---|---|---|
| 0 | Message fully accepted | Walidacja ATC OK, wynik opublikowany |
| 20 | Gate for provided message definition is not opened | Brama dla FIDx-928 zamknięta — admin CCCt |
| 21 | Provided version is not higher than already stored data | Błąd procesowy CCCt |
| 30 | File size mismatch | Niepoprawny rozmiar wyniku ATC |

### Procedury backupowe — analogie z FBA_TSO_BUP_03 (DA)

| HTML IDCC | NOR/BUP DA | Zastosowanie do FID1-928 |
|---|---|---|
| **R11** niezakończenie ATC w czasie | — (specyficzne dla IDCC) | **Brak lokalnego fallbacku**. Po CET — żadnych działań ręcznych |
| **R04** brak paczki/błędna składowa | BUP §Ryzyko 3 (str. 22) | Dotyczy paczki PERUN_IDx_ATC — uzupełnić w CCM |
| **R05** brak ACK | BUP §Ryzyko 12 (str. 48) | CCCt Message Viewer — odczyt statusu |
| **R06** brak CCM | BUP §Ryzyko 27 (str. 69) | zgłoś |
| **R07** brak Core CC Tool | BUP §Ryzyko 11 (str. 47) | Telefoniczne z CCC |
| **R16** Connector 2.0 | BUP §Ryzyko 10 (str. 46) | Transport zwrotny zerwany |

### Ryzyka NIE aplikujące się do FID1-928

- R01, R02, R03 (Perun4V) — ATC nie idzie przez Perun4V
- R09 (Manual Upload) — FIDx-928 to wynik z CCCt, nie wysyłany z TSO
- R12, R13, R14, R15, R20 — inne kafelki / iteracje

### Tabela stanów kafelka × ryzyka × działanie

| # | CCTool wyśl. | CCTool zwalid. | Opis | Ryzyka | Działanie backupowe + procedura BUP | Status |
|---|---|---|---|---|---|---|
| 1 | szary | szary | Przedwczesne (>30 min do TET) | R06, R07 | Monitoring; sprawdzić w CCM postęp walidacji paczki PERUN_IDx_ATC | |
| 2 | pomarańczowy | pomarańczowy | Zbliża się TET, brak FIDx-928 | R04, R06, R07, R11 | Monitoring; rozwinąć agregat PERUN_IDx_ATC → zweryfikować składowe; ew. **uzupełnić brakujące w CCM** (HTML §5.4) | |
| 3 | czerwony | czerwony | Zbliża się CET | R04, R05, R06, R07, R11 | **Ostatnia szansa**: dokończyć uzupełnienia paczki ATC w CCM przed utratą sensu; sprawdzić CCCt Message Viewer; zgłoś | |
| 4 | czarny | czarny | Minął CET, brak FIDx-928 | R04, R05, R06, R07, R11, R16 | **STOP — żadnych działań ręcznych**. HTML §5.4: *„Brak wyniku ATC w czasie → dyspozytor nie wykonuje dalszych czynności. Brak lokalnego fallbacku."* Poinformować: zgłoś + telefon CCC | |
| 5 | zielony | zielony | Happy Day — walidacja ATC OK | — | Brak interwencji (S.1) | |
| 6 | zielony | czerwony | ACK negatywny | R05, R06, R07, R11 | S.6: CCCt Message Viewer → kod 20 (gateClosed → admin CCCt) / 21 (duplicatedVersion → CCCt) / 30 (size). zgłoś | |
| 7 | zielony | czerwony z '?' | ACK nie napłynął w czasie | R05, R06, R07, R11 | S.6: po 5 min → CCCt Message Viewer; brak >10 min → zgłoszenie Connector 2.0 (R16) | |
| 8 | zielony | czarny | Brak ACK do CET | R05, R06, R07, R11, R16 | R16: sprawdzić Connector 2.0 (transport zwrotny); zgłoś | |
| 9 | zielony | fioletowy | ACK po CET pozytywne | R06, R07, R11 | Walidacja opóźniona, ale OK. Wpis A.4 | |
| 10 | zielony | zielony 'R' (ręczny) | Status nadany ręcznie | R06, R07, R11 | Wpis A.4 z uzasadnieniem (FIDx-928 ręczny — nietypowe dla wyniku zwrotnego) | |
| 11 | czerwony z '!' | czerwony z '!' | Niepoprawny rozmiar FIDx-928 | R05, R06, R07, R11, R16 | C.3 'Informacje' → sprawdzić rozmiar. Pobranie ponownie nie ma sensu (zwrotny). zgłoś + telefon CCC | |
| 12 | czerwony z '!' | czerwony z '?' | Niepoprawny rozmiar + brak ACK | R05, R06, R07, R11, R16 | CCCt Message Viewer; zgłoś + telefon CCC | |
| 13 | czerwony z '!' | czerwony | Niepoprawny rozmiar + ACK negatywny | R05, R06, R07, R11 | Komunikat ACK; zgłoszenie CCC | |
| 14 | czerwony z '!' | czarny | Niepoprawny rozmiar + brak ACK do CET | R05, R06, R07, R11, R16 | Krytyczne; zgłoś + telefon CCC | |
| 15 | fioletowy | fioletowy | FIDx-928 dostarczony po CET, OK | R06, R07 | Walidacja zakończona po terminie. Wpis A.4 | |
| 16 | szary z '?' | (puste) | Wysyłka zwrotna trwa | R05, R06, R07 | S.6: po 5 min → Connector 2.0; brak >10 min → zgłoś | |
| 17 | zielony 'R' | zielony 'R' | Status ręczny przyznany | R06, R07, R11 | Wpis A.4 (uzasadnić: zwrotny — nietypowe) | |
| 18 | pomarańczowy | czerwony | TET zbliża się, ACK błąd już teraz | R04, R05, R06, R07, R11 | CCCt Message Viewer — odczytać błąd paczki ATC; uzupełnić w CCM | |

### Stany NIE mające zastosowania dla FID1-928

- **dkgreen_W / dkgreen_W_postCET** (ręczna wysyłka z CCM) — FIDx-928 to wynik zwrotny z CCCt, nie wysyłany przez TSO; te stany teoretycznie mogą pokazać się na kafelku (jeśli Dyspozytor kliknie „Wyślij"), ale operacyjnie nie mają sensu.

### Uwagi / pytania do rozstrzygnięcia

- **❓ R11 vs HTML §5.4** — Czy stosować zasadę „STOP po CET" dla każdego stanu czarnego (#4, #8, #14), czy tylko gdy paczka ATC też była czarna?
- **❓ Stany dkgreen_W** — wykluczyć je całkowicie czy zostawić jako teoretyczne z notatką?
- **❓ Czy w IDCC(a) walidacja ATC ma swoją osobną paczkę?** — w pulpicie IDCC(a) nie ma kafelka „PERUN_ID1_ATC" (jest tylko ATC Based Validation, AC, Final NTC, MD250). Czy paczka ATC w IDCC(a) idzie inną ścieżką?

---

## (kolejne karty pojawią się po Twojej akceptacji)
