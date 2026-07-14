# FID1-921 (Final Intraday NTC, IDCC(a))

**TET:** 14:45 | **CET:** 14:55 | **Profil pulpitu:** SFTP (tylko kolumna sFTP/ZP wyśl.)
**Źródło:** Core CC Tool (centralny wynik CCCt — ID1-921 ID NTCs)
**Cel:** publikacja **ID NTCs do XBID** jako wynik procesu IDCC(a)

> ⚠ **Każde ryzyko należy zgłosić do: CIZ, WPO, PSE-I (PSE Innowacje).**

---

## Stan 1: `szary`

### 1. Kafelki
| sFTP/ZP wyśl. |
|---|
| szary |

### 2. Co oznaczają kafelki
Plik nie wymagany — pozostało >30 min do TET (14:45). Stan normalny.

### 3. Działania backupowe
Brak — monitoring.

---

## Stan 2: `pomarańczowy`

### 1. Kafelki
| sFTP/ZP wyśl. |
|---|
| pomarańczowy |

### 2. Co oznaczają kafelki
Zbliża się TET (14:45). NTC z procesu IDCC(a) nie zostało jeszcze opublikowane do XBID.

### 3. Działania backupowe

#### 3.1 [Sprawdzenie w Core CC Tool — czy NTC wygenerowane](Inwentarz_IDCC.md#N02)

CCCt → logowanie → selektor procesu → **`ID1`** → **`Message Viewer`** → **`Message Definition`** → wpisz **`FID1-921`** lub **`ID1-921`** → **`Apply`**

**Decyzja:**

| Status w CCCt | Działanie |
|---|---|
| **`Processed`** lub plik widoczny | NTC wygenerowane — czekać na transport sFTP/ZP (monitoring) |
| **Brak wpisu** | Proces centralny CCCt nie zakończony → kontakt **CCC ([N13](Inwentarz_IDCC.md#N13))** |

#### 3.2 [Diagnostyka Connector 2.0](Inwentarz_IDCC.md#N05)
- Sprawdź procesy CN2 (HTML §8.9)
- Awaria → **Zgłoś** (CIZ, WPO, PSE-I)

---

## Stan 3: `czerwony`

### 1. Kafelki
| sFTP/ZP wyśl. |
|---|
| czerwony |

### 2. Co oznaczają kafelki
Zbliża się CET (14:55) — NTC niedostarczone lub błąd transportu sFTP/ZP. Stan alarmowy.

### 3. Działania backupowe

#### 3.1 [Weryfikacja w Core CC Tool](Inwentarz_IDCC.md#N02)
- CCCt → `ID1 process` → Message Viewer → `FID1-921`
- Status `Processed` → NTC istnieje, problem w transporcie sFTP/ZP → 3.2
- Brak wpisu → centralny proces CCCt nie zakończony → CCC pilnie

#### 3.2 [Diagnostyka Connector 2.0 / sFTP](Inwentarz_IDCC.md#N05)
- Sprawdź CN2 i sFTP
- Awaria → zgłoś pilnie

#### 3.3 Zgłoszenie
- **CCC ([N13](Inwentarz_IDCC.md#N13))** — telefonicznie
- **Zgłoś** (CIZ, WPO, PSE-I)

---

## Stan 4: `czarny`

### 1. Kafelki
| sFTP/ZP wyśl. |
|---|
| czarny |

### 2. Co oznaczają kafelki
**KRYTYCZNE** — minął CET (14:55), NTC niedostarczone do XBID. Brak lokalnego fallbacku. W IDCC(b) może aktywować się **[XBID-R02 Late NTC delivery](Ryzyka_per_aplikacja_IDCC.md#xbid)** (proces IDCC(b) wstrzymany do 22:30).

### 3. Działania backupowe

#### 3.1 Zgłoszenie natychmiastowa
- Telefon **CCC ([N13](Inwentarz_IDCC.md#N13))**
- **Zgłoś** (CIZ, WPO, PSE-I)

#### 3.2 Monitoring odzyskania
- Sprawdź czy CCCt zakończył proces centralny ([N15](Inwentarz_IDCC.md#N15))
- Jeśli NTC pojawi się po CET → fioletowy (Stan 7); akceptowalne z opóźnieniem
- Brak wznowienia przed 22:30 → IDCC(b) wstrzymane → zgłoszenie XBID-R02

#### 3.3 [P06 — Wpis A.4](Karta_ryzyk_IDCC.md#P06)
- Pełny opis zdarzenia z przyczyną

---

## Stan 5: `zielony`

### 1. Kafelki
| sFTP/ZP wyśl. |
|---|
| zielony |

### 2. Co oznaczają kafelki
**Happy Day** — NTC z IDCC(a) prawidłowo opublikowane do XBID przez sFTP/ZP.

### 3. Działania backupowe
Brak — proces przebiegł poprawnie.

---

## Stan 6: `ciemnozielony W`

### 1. Kafelki
| sFTP/ZP wyśl. |
|---|
| ciemnozielony W |

### 2. Co oznaczają kafelki
NTC wysłane ręcznie z poziomu CCM przed CET (PPM → Wyślij). Stan backupowy.

### 3. Działania backupowe

#### 3.1 [P06 — Wpis A.4](Karta_ryzyk_IDCC.md#P06)
- Uzasadnij przyczynę ręcznej wysyłki (typowo awaria CN2/sFTP)

---

## Stan 7: `fioletowy`

### 1. Kafelki
| sFTP/ZP wyśl. |
|---|
| fioletowy |

### 2. Co oznaczają kafelki
NTC dostarczone do XBID po CET, ale OK. Proces zakończony z opóźnieniem.

### 3. Działania backupowe

#### 3.1 [P06 — Wpis A.4](Karta_ryzyk_IDCC.md#P06)
- Najedź na fioletowy → odczytaj czas dostarczenia
- Wpis z uzasadnieniem opóźnienia

---

## Stan 8: `ciemnozielony W po CET`

### 1. Kafelki
| sFTP/ZP wyśl. |
|---|
| ciemnozielony W po CET |

### 2. Co oznaczają kafelki
Ręczna wysyłka NTC po CET (opcja „Wyślij po CET" w CCM). Proces zakończony po terminie.

### 3. Działania backupowe

#### 3.1 [P06 — Wpis A.4](Karta_ryzyk_IDCC.md#P06)
- Pełne uzasadnienie opóźnienia
- Zgłoś (informacyjnie)

---

## Stan 9: `zielony R`

### 1. Kafelki
| sFTP/ZP wyśl. |
|---|
| zielony R |

### 2. Co oznaczają kafelki
Status ręczny 'R' nadany przez Dyspozytora po weryfikacji w CCCt.

### 3. Działania backupowe

#### 3.1 [P06 — Wpis A.4](Karta_ryzyk_IDCC.md#P06)
- Uzasadnij dlaczego status ręczny

---

## Stan 10: `czerwony ?`

### 1. Kafelki
| sFTP/ZP wyśl. |
|---|
| czerwony ? |

### 2. Co oznaczają kafelki
Wysyłka trwa — sFTP/ZP w trakcie transportu, brak potwierdzenia w wyznaczonym czasie (>2-3 min).

### 3. Działania backupowe

#### 3.1 Oczekiwanie
- Czekaj 5 min od TET

#### 3.2 [Weryfikacja w CCCt](Inwentarz_IDCC.md#N02) (po 5 min)
- Message Viewer → FID1-921 → status
- Processed → CCM nie odświeżył; zgłoś
- Brak wpisu → awaria CN2 → zgłoś

---

## Stan 11: `czerwony !`

### 1. Kafelki
| sFTP/ZP wyśl. |
|---|
| czerwony ! |

### 2. Co oznaczają kafelki
Plik dostarczony, ale rozmiar < minimum. Prawdopodobnie niekompletne dane NTC.

### 3. Działania backupowe

#### 3.1 Weryfikacja rozmiaru
- CCM → LPM → **Informacje**
- Odczytaj rzeczywisty rozmiar vs oczekiwany

#### 3.2 [P04 — Pobranie z MinIO + weryfikacja](Karta_ryzyk_IDCC.md#P04)
- Sprawdź zawartość pliku NTC
- Niepoprawne dane → zgłoszenie **CCC ([N13](Inwentarz_IDCC.md#N13))**: centralny proces CCCt mógł zwrócić niepoprawny wynik

#### 3.3 Zawartość OK pomimo rozmiaru
- Zgłoś (zmiana konfiguracji minimum rozmiaru pliku)

---

## Definicja pliku

**Plik:** FID1-921 (Final Intraday NTC, IDCC(a))

**Plik przychodzący z:** **Core CC Tool (centralny proces)** — [N15](Inwentarz_IDCC.md#N15). Kod centralny CCCt: **ID1-921** (ID NTCs).
**Plik wychodzący do:** **XBID** — system aukcyjny intraday ([N17](Inwentarz_IDCC.md#N17)).
**Transport:** Connector 2.0 → MinIO → sFTP/ZP (kolumna sFTP/ZP wyśl. w CCM).

**Budowa pliku:**
- **Format:** XML
- **Maska nazwy:** `rrrrMMdd-FID1-921-v*-<sender>-to-<receiver>.xml`
- **Zawartość:** Final Intraday Net Transfer Capacities (NTC) — finalne wartości zdolności przesyłowych intraday dla iteracji IDCC(a), dla wszystkich kierunków transgranicznych w obszarze Core
- **Struktura logiczna:** TimeSeries per kierunek, wartości NTC per godzina (MTU = 60 min)
- **Wersjonowanie:** v1 (typowo); kolejne wersje gdy poprawki centralne
- **Charakter:** wynik **centralny CCCt** (nie generowany przez TSO PSE); TSO PSE wyłącznie monitoruje publikację

**Uwagi specyficzne dla FID1-921:**
- Brak lokalnego fallbacku — TSO nie generuje NTC samodzielnie
- W przypadku Late delivery — automatyczne wznowienie po IDA2 (deadline 22:30 dla IDCC(b))
- HTML §10.1.1: *„Kody ID1-NNN są generowane przez CCCt centralnie; dyspozytor PSE wyłącznie monitoruje ich publikację, nie wykonuje czynności wykonawczych"*
