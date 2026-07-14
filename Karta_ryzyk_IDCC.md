# Karta ryzyk i procedur backupowych — IDCC

> Dokument szczegółowy — odnośnik z [Karty_plikow_FIDx.md](Karty_plikow_FIDx.md) oraz z xlsx Pulpit_IDCC_CCM_opisy_kafelkow.xlsx.
> Każde ryzyko ma unikalny anchor (`#U01`…`#U23`, `#P01`…`#P06`) do bezpośredniego linkowania.

> ⚠ **Każde ryzyko należy zgłosić do: CIZ, WPO, PSE-I (PSE Innowacje).** Procedury poniżej podają tylko działania operacyjne — nie powtarzają odbiorców zgłoszenia.

**Źródła:**
- HTML procedura IDCC (FBA_TSO_IDCC v1.0 FINAL DRAFT)
- FBA_TSO_BUP_03 — Walidacja domeny FBA v0.31 (procedury backupowe DA)
- CCM Instrukcja Użytkownika Dyspozytora v2.6
- AC manuall ZP.docx (procedura pobrania AC z ZP)

---

## Spis treści

### Grupa I — Dostępność narzędzi
- [U01 — Brak dostępu do CCM](#U01)
- [U02 — Brak dostępu do Core CC Tool](#U02)
- [U03 — Brak dostępu / awaria Connector 2.0](#U03)
- [U04 — Brak dostępu do MinIO](#U04)
- [U05 — Brak dostępu do Perun4V](#U05)
- [U06 — Brak dostępu do źródła pliku (ZP / Kreator / CCA)](#U06)
- [U07 — Brak dostępu do poczty kdm6](#U07)

### Grupa II — Plik i dostarczenie
- [U08 — Plik niedostarczony w czasie](#U08)
- [U09 — Plik dostarczony, ale błędny (rozmiar / struktura)](#U09)
- [U10 — ACK negatywny (odrzucenie)](#U10)
- [U11 — Brak ACK (timeout)](#U11)
- [U12 — Niezgodność wersji pliku](#U12)
- [U13 — Plik dostarczony po CET (informacyjne)](#U13)

### Grupa III — Proces obliczeniowy (Perun4V / IVA)
- [U14 — Brak uruchomienia obliczeń w Perun4V](#U14)
- [U15 — ERR-I — część TS niepoliczona](#U15)
- [U16 — Process failed — wszystkie TS niepoliczone](#U16)

### Grupa IV — Strumień ATC
- [U17 — Niezakończenie walidacji ATC w czasie](#U17)

### Grupa V — Transport zwrotny / kopiowanie
- ~~U18~~ → scalone z [U03](#U03)
- [U19 — Niezgodność wersji IVA / IVA BACKUP](#U19)

### Grupa VI — Zgłoszenie zewnętrzna / fallbacki
- [U20 — AAC Fallback (IDCC(a) nie dostarczył AACs)](#U20)
- [U21 — Decoupling SDAC — konieczność MD250](#U21)
- [U22 — Late NTC delivery po IDA2](#U22)
- [U23 — Brak raportu CCA](#U23)

### Procedury (działania w odpowiedzi na ryzyka)
- [P01 — GUI CCCt — Manual Upload](#P01)
- [P02 — Pobranie pliku z ZP → GUI CCCt](#P02)
- [P03 — Ręczne uruchomienie obliczeń w Perun4V](#P03)
- [P04 — Pobranie pliku z MinIO → CCM Wyślij](#P04)
- [P05 — Pobranie z CCCt Message Viewer → CCM Wyślij](#P05)
- [P06 — Wpis w karcie A.4 (status ręczny)](#P06)

### Kontakty do zgłoszeń
- [Kontakty](#kontakty)

---

# Grupa I — Dostępność narzędzi

<a id="U01"></a>
## U01 — Brak dostępu do CCM

**Kategoria:** Dostępność narzędzi
**Źródło:** HTML R06, BUP §Ryzyko 27 (str. 69)

### Opis
Brak możliwości otwarcia / zalogowania do https://ccm.spsm.pse.pl. Dyspozytor traci główne narzędzie monitorowania statusów pulpitu.

### Objawy
- Strona CCM nie ładuje się / błąd logowania
- Sesja CCM wygasła i ponowne logowanie zwraca błąd
- Pulpit CCM zawiesza się / nie odświeża po >5 min

### Skutki
- Brak monitoringu statusów kafelków
- Brak możliwości wysyłki plików przez CCM (PPM → Wyślij)
- Brak możliwości użycia funkcji „Informacje" o pliku

### Działanie
1. Sprawdzić sieć / VPN PSE
2. Spróbować w innej przeglądarce / trybie prywatnym
3. Zgłoś (priorytet zależny od fazy procesu)
4. **Tymczasowo:** monitorować bezpośrednio w narzędziach docelowych:
   - Core CC Tool — Message Viewer (dla plików do CCCt)
   - MinIO GUI — bezpośredni podgląd bucketów
   - Perun4V — dla wyników FBA
5. Pliki do wysłania ręcznie: [P01 — GUI CCCt Manual Upload](#P01) bezpośrednio z dysku
6. Wpis w karcie po przywróceniu CCM ([P06](#P06))

### Zgłoszenie
- **Zgłoś** (CIZ, WPO, PSE-I — patrz sekcja Kontakty do zgłoszeń)

### Powiązane
- [U02](#U02) — gdy współwystępuje brak CCCt → poważne (jedyny kanał: MinIO + telefon)
- [P01](#P01) — alternatywna wysyłka przez GUI CCCt
- [P04](#P04) — pobranie pliku bezpośrednio z MinIO

---

<a id="U02"></a>
## U02 — Brak dostępu do Core CC Tool

**Kategoria:** Dostępność narzędzi
**Źródło:** HTML R07, BUP §Ryzyko 11 (str. 47)

### Opis
Brak możliwości zalogowania / korzystania z Core CC Tool (CCCt). Główny kanał wymiany TSO ↔ CCCt zerwany.

### Objawy
- Strona CCCt nie ładuje się / błąd uwierzytelnienia
- Message Viewer niedostępny
- Manual Upload zwraca błąd

### Skutki
- Brak weryfikacji ACK
- Brak możliwości [P01 (Manual Upload)](#P01)
- Brak publikacji wyników do PuTo (dla AC, NTC)

### Działanie
1. Monitorować nadal w **CCM** — kafelki, statusy
2. Monitorować na **skrzynce kdm6@pse.pl** — raporty zwrotne
3. Telefoniczny kontakt z **CCC** (operator@tscnet.eu / lista operacyjna)
4. **Alternatywny kanał** wyłącznie po uzgodnieniu z CCC (np. ECP/EDX bezpośrednio)
5. Zgłoś

### Zgłoszenie
- **CCC / TSCNET** — natychmiast (telefon)
- **Zgłoś** (CIZ, WPO, PSE-I — patrz sekcja Kontakty do zgłoszeń)
- **CORESO** (day-ahead.engineer@coreso.eu) — przy potrzebie koordynacji

### Powiązane
- [U01](#U01) — współwystępowanie pogarsza sytuację
- [U03](#U03) — brak Connector 2.0 + brak CCCt = krytyczne

---

<a id="U03"></a>
## U03 — Brak dostępu / awaria Connector 2.0

**Kategoria:** Dostępność narzędzi
**Źródło:** BUP §Ryzyko 2 (str. 17), §Ryzyko 10 (str. 46), §Ryzyko 16 (str. 54), §Ryzyko 1 (str. 9), HTML R16

### Opis
Connector 2.0 (CN2) — główne narzędzie transportu plików w infrastrukturze PSE. Awaria powoduje, że pliki nie są przekazywane między CCM ↔ CCCt ↔ MinIO ↔ Perun4V.

**Obejmuje wszystkie warianty:**
- **Pełna awaria** — żadne pliki nie są transportowane
- **Selektywna awaria** — plik dostarczony do jednego kanału, ale nie skopiowany do drugiego (np. plik na MinIO `perun/`, brak w `cca/`)
- **Brak kopiowania zwrotnego** — brak ACK / FID-928 / kopiowania IVA do bucketów CCA

### Objawy
- Plik widoczny w źródle (np. ZP, KreatorDACF), ale nie pojawia się w CCM
- CCM kolumna „CCTool wyśl." pozostaje szara mimo upływu TET
- Procesy „pending" w Connector 2.0
- Brak ACK po wysyłce automatycznej
- W MinIO plik widoczny w jednym bucketcie, brak w drugim (np. brak kopii do CCA → wpływa na IVA Backup)

### Skutki
- Wysyłki automatyczne wstrzymane (pełne lub selektywne)
- Konieczne przejście na **ręczną wysyłkę** plików
- Brak IVA Backup / raportów CCA (przy selektywnej awarii kopii do `cca/`)

### Działanie
1. Sprawdzić **Connector 2.0** — czy proces transportu się zakończył (BUP §8.9)
2. Logi błędów Connector 2.0 — diagnostyka przyczyny
3. Identyfikacja zakresu awarii (pełna / selektywna):
   - Pliki w `perun/`, brak w `cca/` → zgłoś
   - Brak w obu → zgłoś
4. **Dla pliku FIDx-831 (AC):** [P02 — Pobranie z ZP → GUI CCCt](#P02)
5. **Dla pliku IVA / paczek:** [P01 — GUI CCCt Manual Upload](#P01) z plikiem pobranym z [P04 — MinIO](#P04) lub źródła
6. Zgłoś
7. Wpis w karcie A.4 — [P06](#P06)

### Zgłoszenie
- **Zgłoś** (CIZ, WPO, PSE-I — patrz sekcja Kontakty do zgłoszeń)

### Powiązane
- [P01](#P01), [P02](#P02), [P04](#P04), [P05](#P05) — procedury ręcznej wysyłki
- [U19](#U19) — niezgodność wersji IVA / IVA Backup jako konsekwencja braku kopii do `cca/`

---

<a id="U04"></a>
## U04 — Brak dostępu do MinIO

**Kategoria:** Dostępność narzędzi
**Źródło:** BUP §Ryzyko 2/16/24/25

### Opis
Brak dostępu do https://minio-gui.pse.pl — centralnego repozytorium plików procesowych.

### Objawy
- GUI MinIO nie ładuje się
- CCM funkcja „Pobierz" zwraca błąd
- Buckety `perun/`, `cca/`, `mam/` niedostępne

### Skutki
- Brak możliwości pobrania backupowej kopii pliku
- Brak [P04](#P04)
- Raporty CCA niedostępne → [U23](#U23)

### Działanie
1. Sprawdzić sieć / VPN PSE
2. Alternatywne źródła pliku:
   - **Dla AC (FIDx-831):** [P02 — pobranie z ZP](#P02)
   - **Dla IVA / wyników Perun4V:** pobrać z **Perun4V** (poprzez GUI)
   - **Dla raportów CCA:** [U07 — sprawdzić kdm6@pse.pl](#U07) → kopia mailem
   - **Dla składowych paczek:** [P05 — CCCt Message Viewer](#P05)
3. Zgłoś (priorytet wg fazy procesu)

### Zgłoszenie
- **Zgłoś** (CIZ, WPO, PSE-I — patrz sekcja Kontakty do zgłoszeń)

### Powiązane
- [P04](#P04) — niedostępne
- [P02](#P02), [P05](#P05) — alternatywne źródła pobrania
- [U07](#U07) — alternatywa dla raportów CCA

---

<a id="U05"></a>
## U05 — Brak dostępu do Perun4V

**Kategoria:** Dostępność narzędzi
**Źródło:** BUP §Ryzyko 4 (str. 26), §Ryzyko 17

### Opis
Brak możliwości zalogowania / korzystania z Perun4V (https://lccv.tscnet.eu). Brak monitoringu i wglądu w stan obliczeń FBA.

### Objawy
- Strona Perun4V nie ładuje się / błąd logowania
- Brak komunikatu o uruchomieniu obliczeń (zazwyczaj sFTP@pse.pl)
- Sesja Perun4V wygasła

### Skutki
- Brak monitoringu stanu obliczeń (Successful / ERR-I / Process failed)
- Brak [P03 — ręcznego uruchomienia obliczeń](#P03)
- Brak weryfikacji statusu poszczególnych godzin

### Dotyczy plików
- **IVA (FIDx-710)** — główny
- **Pośrednio** wszystkie składowe paczki PERUN_IDx (monitorowanie wynikowe)

### Działanie
1. Sprawdzić TSCNET status / sieć
2. Spróbować w innej przeglądarce
3. **Tymczasowo:** monitorować przez **CCM** (statusy kafelków IVA/Raporty) oraz **kdm6@pse.pl** (raporty Perun4V po obliczeniach)
4. Telefoniczny kontakt z **TSCNET** (operator@tscnet.eu)
5. Zgłoś

### Zgłoszenie
- **TSCNET** — telefon
- **Zgłoś** (CIZ, WPO, PSE-I — patrz sekcja Kontakty do zgłoszeń)

### Powiązane
- [U14](#U14), [U15](#U15), [U16](#U16) — bez Perun4V niemożliwe rozróżnienie tych ryzyk

---

<a id="U06"></a>
## U06 — Brak dostępu do źródła pliku

**Kategoria:** Dostępność narzędzi
**Źródło:** Nowe (zidentyfikowane w trakcie pracy)

### Opis
Brak dostępu do narzędzia będącego **źródłem** pliku (zależnie od FID):
- **ZP (zdolności przesyłowe)** — dla FIDx-831 (AC)
- **KreatorDACF&2DAF_CGMES** — dla GLSK/CBCORA (FID2-607, FID2-617 w IDCC(b))
- **KreatorIDCF** — dla GLSK/CBCORA w IDCC(c)/(d)
- **CCA** — dla F320, VERTICES_MAP, IVA Backup
- **Perun4V** — dla F310 (IVA)

### Objawy
- Aplikacja źródłowa nie startuje
- Brak pliku w katalogu źródłowym
- Procedura generowania pliku zakończona błędem

### Skutki
- Brak możliwości manualnej wysyłki danego pliku
- Konieczne pobranie z innego kanału (jeśli istnieje) lub zgłoszenie

### Działanie
1. Identyfikacja źródła pliku per FID (patrz nagłówek karty pliku)
2. Sprawdzenie czy plik istnieje w katalogu sieciowym `\\uo-data\ZUO\Pion_UOD\Wydzial_DP\MODELE\5_DYSP\FBA\Pliki wejściowe do ID FBA\YYYYMMDD\Perun\`
3. Alternatywne źródło (zależnie od FID): MinIO, kdm6, CCCt Message Viewer
4. Zgłoszenie zespołu utrzymania danego narzędzia (np. PLANS dla Kreatora)
5. Zgłoś

### Zgłoszenie
- Zespół utrzymania źródłowego narzędzia (np. PLANS dla Kreatora)
- **Zgłoś** (CIZ, WPO, PSE-I — patrz sekcja Kontakty do zgłoszeń)

### Powiązane
- [P02](#P02) — gdy źródło to ZP (dla FIDx-831)
- [P04](#P04), [P05](#P05) — alternatywne pobrania

---

<a id="U07"></a>
## U07 — Brak dostępu do poczty kdm6

**Kategoria:** Dostępność narzędzi
**Źródło:** BUP §Ryzyko 25/26 (str. 67-69)

### Opis
Brak dostępu do skrzynki kdm6@pse.pl — kanału pasywnego, na który CCA wysyła raporty walidacyjne, raporty Perun4V i potwierdzenia.

### Objawy
- Outlook nie ładuje skrzynki kdm6
- Brak nowych wiadomości od CCA / Perun4V mimo upływu czasu obliczeń

### Skutki
- Brak weryfikacji raportów CCA (IVA na CNECach)
- Brak informacji o ilości policzonych godzin w Perun4V
- Potencjalna utrata informacji o błędach obliczeniowych

### Działanie
1. Sprawdzić Outlook / połączenie sieciowe
2. Alternatywnie pobrać raporty z **MinIO** bucket `cca/DA_FBCC/out/[YYYY-MM-DD]/` (dla DA) lub `cca/ID_FBCC/out/[BD]/` (dla IDCC)
3. Sprawdzenie w **Perun4V** GUI — status obliczeń bezpośrednio
4. Zgłoś

### Zgłoszenie
- **PSE** — zespół utrzymania poczty
- **Zgłoś** (CIZ, WPO, PSE-I — patrz sekcja Kontakty do zgłoszeń)

### Powiązane
- [U23](#U23) — brak raportu CCA jako konsekwencja
- [P04](#P04) — pobranie raportu bezpośrednio z MinIO

---

# Grupa II — Plik i dostarczenie

<a id="U08"></a>
## U08 — Plik niedostarczony w czasie

**Kategoria:** Plik i dostarczenie
**Źródło:** HTML R04, BUP §Ryzyko 3 (str. 22)

### Opis
Plik nie pojawił się w CCM / na MinIO / w CCCt w czasie wymaganym przez harmonogram (TET → CET).

### Objawy
- Kafelek **szary** po 30 min przed TET (przedwczesne) → **pomarańczowy** (30 min przed TET-CET) → **czerwony** (CET zbliża się) → **czarny** (po CET)
- W przypadku składowych paczki: błędna składowa blokuje wysyłkę całego agregatu

### Skutki
- Opóźnienie procesu IDCC
- Zgłoszenie kolejnych iteracji (np. IDCC(b) wstrzymane przez Late NTC → [U22](#U22))
- W przypadku składowej: paczka ZIP nie powstanie → [U16](#U16) (Process failed)

### Działanie
1. Identyfikacja źródła pliku (per FID)
2. Rozwinąć agregat (jeśli to składowa) — sprawdzić wszystkie składowe (HTML §8.8 Scenariusz 2)
3. Pobrać plik z alternatywnego źródła:
   - **AC (FIDx-831):** [P02 — z ZP](#P02)
   - **GLSK/CBCORA (FID2-607/-617):** Kreator2DAF&DACF lub CCCt MV
   - **Składowe paczki:** [P05 — CCCt Message Viewer](#P05)
   - **IVA / FIDx-710:** [P04 — MinIO](#P04) (`perun/ID_FBCC/out/BD/`)
4. Wysłać ręcznie przez CCM (PPM → Wyślij) lub [P01](#P01)
5. Zgłoś jeśli zbliża się CET bez sukcesu

### Zgłoszenie
- Czas > 5 min przed CET: zgłoś
- Po CET: zgłoś + telefon CCC

### Powiązane
- [P02](#P02), [P04](#P04), [P05](#P05) — alternatywne pobrania
- [U16](#U16) — brak paczki → Process failed
- [U22](#U22) — Late NTC

---

<a id="U09"></a>
## U09 — Plik dostarczony, ale błędny (rozmiar / struktura)

**Kategoria:** Plik i dostarczenie
**Źródło:** ACK 30 (File size mismatch), ACK „Message has some invalid timeSeries", HTML R04

### Opis
Plik dotarł do CCM/CCCt, ale jego zawartość jest nieprawidłowa:
- **Rozmiar** — za mały w porównaniu do minimalnej skonfigurowanej (ACK 30)
- **Struktura** — nie spełnia reguł MTU dla danej definicji wiadomości

### Objawy
- Kafelek **czerwony z '!'** — niepoprawny rozmiar
- ACK negatywny z kodem 30 lub treścią „Message has some invalid timeSeries…"
- W menu bocznym statusu: informacja o rozmiarze pliku (faktyczny vs oczekiwany)

### Skutki
- Plik nie przyjęty przez CCCt — proces zatrzymany
- Konieczna podmiana na poprawiony plik

### Działanie
1. Najechać kursorem → odczytać komunikat (LPM → „Informacje" w CCM)
2. Sprawdzić rozmiar pliku w MinIO (link w „Informacje")
3. **Zweryfikować plik manualnie** — pobrać z MinIO/źródła, rozpakować, sprawdzić zawartość. Mimo małego rozmiaru może być OK
4. Jeśli niepoprawny:
   - **AC:** [P02 — z ZP](#P02) → [P01 GUI CCCt](#P01) z podbitą wersją
   - **IVA:** pobranie z Perun4V → [P01](#P01) z wyższą wersją
   - **Składowa paczki:** [P05 — CCCt MV](#P05) → CCM Wyślij
5. Wpis w karcie A.4 — [P06](#P06)

### Zgłoszenie
- Plik niepoprawny: zgłoś
- Brak możliwości regeneracji: zgłoś + zespół utrzymania źródła

### Powiązane
- [U12](#U12) — wymóg podbicia wersji (kod 21 duplicatedVersion)
- [P01](#P01), [P02](#P02), [P05](#P05)

---

<a id="U10"></a>
## U10 — ACK negatywny (odrzucenie)

**Kategoria:** Plik i dostarczenie
**Źródło:** HTML R05, BUP §Ryzyko 13 (str. 49), kody ACK 20/21/22/30

### Opis
Plik dotarł do CCCt, ale został odrzucony — ACK zawiera komunikat błędu lub „Błąd procesu".

### Objawy
- Kolumna „CCTool zwalid." **czerwona** (z kodem) lub **czerwona z ikoną błędu procesu**
- Po najechaniu na status — komunikat błędu z CCCt

### Kody ACK (najczęstsze)

| Kod | Treść | Działanie |
|---|---|---|
| 20 | Gate for provided message definition is not opened | Bramka zamknięta — sprawdź TET/CET; jeśli zgodny → CCCt proces `IDx-AC-FORWARDING` → zgłoś |
| 21 | Provided version is not higher than already stored data (duplicatedVersion) | [U12](#U12) — podbić wersję i ponowić |
| 22 | ~~Delivered constraint value is negative~~ | ❌ Nie występuje już (CCCt akceptuje wartości ujemne) |
| 30 | File size mismatch | → [U09](#U09) |
| — | Message has some invalid timeSeries… | Poprawić strukturę pliku (MTU), ponowić |
| — | Błąd procesu | Proces w CCCt zakończył się błędem — sprawdzić CCCt Message Viewer; zgłoś |

### Działanie
1. Najechać na status → odczytać kod ACK
2. **CCCt Message Viewer** → filtr po kodzie przepływu → szczegóły błędu
3. Reakcja zależna od kodu (patrz tabela powyżej)
4. W razie potrzeby [P01 — Manual Upload](#P01) z poprawionym plikiem / wyższą wersją

### Zgłoszenie
- Kod 20 (gateClosed) → zgłoś (administrator CCCt otwiera bramkę)
- Kod 22 (Negative constraint) → zgłoś *(historycznie; obecnie nie występuje)*
- Błąd procesu → zgłoś
- Brak rozwiązania w 10 min → zgłoś + telefon CCC

### Powiązane
- [U09](#U09), [U11](#U11), [U12](#U12)
- [P01](#P01)

---

<a id="U11"></a>
## U11 — Brak ACK (timeout)

**Kategoria:** Plik i dostarczenie
**Źródło:** HTML R05, BUP §Ryzyko 12 (str. 48)

### Opis
Plik wysłany do CCCt (CCTool wyśl. zielony), ale ACK nie napłynął w przewidywanym czasie (typowo 2-3 min).

### Objawy
- Kafelek **„CCTool zwalid." z '?'** (czerwony znak zapytania)
- Po najechaniu — informacja o czasie oczekiwania

### Skutki
- Niepewność statusu wysyłki
- Możliwe podwójne wysłanie (duplicatedVersion) jeśli Dyspozytor ponawia bez weryfikacji

### Działanie
1. Najechać na '?' → odczytać czas oczekiwania
2. **CCCt Message Viewer** → filtr po kodzie przepływu
   - Status `Processed` → CCM się nie odświeżył; czekać lub odświeżyć ręcznie
   - Status `Rejected` → odczytać kod → [U10](#U10)
   - **Brak wpisu** → problem transportu → [U03](#U03), [U18](#U18)
3. **Po 10 min braku wpisu:** zgłoś (problem transportu Connector 2.0)
4. **⚠ NIE wysyłać pliku ponownie bez sprawdzenia** — kod 21 duplicatedVersion

### Zgłoszenie
- Po 5 min: sprawdzić Message Viewer
- Po 10 min bez wpisu: zgłoś (problem transportu Connector 2.0)

### Powiązane
- [U03](#U03), [U10](#U10), [U18](#U18)

---

<a id="U12"></a>
## U12 — Niezgodność wersji pliku

**Kategoria:** Plik i dostarczenie
**Źródło:** ACK 21 (duplicatedVersion), ACK 40 (Backup version lower)

### Opis
- **Kod 21:** wysłana wersja nie jest wyższa niż już zapisana w CCCt
- **Kod 40:** wersja backupowa niższa niż wersja główna (dot. IVA Backup)

### Objawy
- ACK negatywny z komunikatem `Provided version is not higher than already stored data` lub `Backup version lower`

### Działanie
1. Sprawdzić aktualną wersję w CCCt Message Viewer / w pliku Backup w MinIO
2. **Kod 21:** podbić wersję w nagłówku pliku (lub w nazwie pliku) → [P01](#P01) ponowić
3. **Kod 40:** **NIE wysyłać** backup z niższą wersją; oczekiwać aktualizacji od CCA
4. Wpis w karcie A.4 — [P06](#P06)

### Zgłoszenie
- Brak rozwiązania → zgłoś
- Niezgodność wersji IVA / IVA Backup → [U19](#U19)

### Powiązane
- [U10](#U10), [U19](#U19), [P01](#P01)

---

<a id="U13"></a>
## U13 — Plik dostarczony po CET (informacyjne)

**Kategoria:** Plik i dostarczenie

### Opis
Plik dostarczony i zwalidowany **po upłynięciu CET** — operacyjnie OK, ale wymaga wpisu monitoringu.

### Objawy
- Kafelek **fioletowy** (purple) — dostarczone po CET, ACK pozytywny
- Czas wysyłki widoczny w menu bocznym statusu

### Skutki
- Proces zakończony, brak konsekwencji operacyjnych
- Wymaga **wpisu w karcie A.4**

### Działanie
1. Brak interwencji backupowej
2. [P06 — Wpis w karcie A.4](#P06): kod przepływu, godzina dostarczenia, uzasadnienie opóźnienia

### Powiązane
- [P06](#P06)

---

# Grupa III — Proces obliczeniowy (Perun4V / IVA)

<a id="U14"></a>
## U14 — Brak uruchomienia obliczeń w Perun4V

**Kategoria:** Proces obliczeniowy
**Źródło:** HTML R01, BUP §Ryzyko 1 (str. 9)

### Opis
Paczka ZIP wysłana (sFTP/ZP zielona), ale obliczenia w Perun4V nie wystartowały.

### Objawy
- W Perun4V GUI — brak obliczenia dla danej doby
- Komunikat w Perun4V „brak pliku" / „błędny BD"
- Brak emaila z raportem na kdm6@pse.pl

### Skutki
- Brak wyniku IVA (FIDx-710)
- Opóźnienie procesu IDCC

### Działanie
1. Sprawdzić w Perun4V GUI komunikat błędu:
   - **Błędny BD** → ustawić poprawny BD w sekcji „Select timestamp date"
   - **Brak pliku w paczce** → uzupełnić brakującą składową ([U08](#U08))
   - **Błędny plik w paczce** → ręcznie pobrać z CCCt Message Viewer, spakować, wczytać
2. [P03 — Ręczne uruchomienie obliczeń w Perun4V](#P03)
3. Jeśli niemożliwe → zgłoś + oczekiwać [IVA BACKUP](#U19) v1

### Zgłoszenie
- **Zgłoś** (CIZ, WPO, PSE-I — patrz sekcja Kontakty do zgłoszeń) — przy braku możliwości uruchomienia
- **CCC** — koordynacja czasu procesu

### Powiązane
- [P03](#P03), [U15](#U15), [U16](#U16), [U19](#U19)

---

<a id="U15"></a>
## U15 — ERR-I — część TS niepoliczona

**Kategoria:** Proces obliczeniowy
**Źródło:** HTML R02, BUP §Ryzyko 6 (str. 29), §Ryzyko 20

### Opis
W Perun4V status obliczenia: **ERR-I** — przynajmniej jedna godzina (TimeSlice) nie została policzona. W kolumnie `Timestamps (Failed/Success/Running/Total)` widoczna jest liczba niepoliczonych godzin.

### Objawy
- Perun4V GUI — dopisek `ERR-I` w głównym oknie
- W `Status → Details` — kolumna `[Result]` pokazuje niepoliczone godziny

### Skutki
- Publikacja **wyższej wersji IVA** = wyniki Perun4V + dane CCA dla brakujących TS
- Konieczne porównanie wersji [U19](#U19)

### Działanie
1. W Perun4V → `Status → Details` — zidentyfikować niepoliczone godziny
2. Sprawdzić w **Core CC Tool** czy zastosowano DFP (Default Flow Parameters) lub Spanning hours
3. Email z informacją o DFP/Spanning — sprawdzić kdm6@pse.pl
4. **Monitorować [IVA BACKUP](#U19)** — wyższa wersja powinna być opublikowana automatycznie przez CCA
5. Brak publikacji Backup w czasie → zgłoś + telefon CCC

### Zgłoszenie
- zgłoś + telefon CCC — przy braku publikacji IVA Backup

### Powiązane
- [U16](#U16), [U19](#U19), [P03](#P03)

---

<a id="U16"></a>
## U16 — Process failed — wszystkie TS niepoliczone

**Kategoria:** Proces obliczeniowy
**Źródło:** HTML R03, BUP §Ryzyko 7 (str. 39), §Ryzyko 21

### Opis
W Perun4V status obliczenia: **Process failed** — żadna godzina (TimeSlice) nie została policzona.

### Objawy
- Perun4V GUI — status `Process failed`
- W kolumnie Timestamps: wszystkie godziny w `Failed`

### Skutki
- **Publikowana IVA BACKUP v1** jako wynik wyłącznie z CCA
- Krytyczne dla procesu IDCC

### Działanie
1. **Oczekiwać IVA BACKUP v1** — automatyczna publikacja przez CCA
2. Brak publikacji Backup → zgłoś + telefon CCC
3. **Zakaz** stosowania fallbacku 20% Fmax z DA (HTML §7)

### Zgłoszenie
- zgłoś + telefon CCC — natychmiast

### Powiązane
- [U15](#U15), [U19](#U19), [U23](#U23)

---

# Grupa IV — Strumień ATC

<a id="U17"></a>
## U17 — Niezakończenie walidacji ATC w czasie

**Kategoria:** Strumień ATC
**Źródło:** HTML R11

### Opis
Walidacja ATC nie zakończyła się przed CET kafelka **FIDx-928 (ATC Based Validation)**.

### Objawy
- Kafelek FIDx-928 **czarny** po CET
- Brak publikacji wyniku walidacji ATC

### Skutki
- HTML §5.4: *„Brak wyniku ATC w czasie → dyspozytor nie wykonuje dalszych czynności. **Brak lokalnego fallbacku.**"*

### Działanie
1. **PRZED CET:** uzupełnić brakujące składowe paczki ATC (PERUN_IDx_ATC) w CCM → [U08](#U08)
2. **PO CET:** **STOP — żadnych działań ręcznych.** Brak lokalnego fallbacku
3. Zgłoś + telefon CCC

### Zgłoszenie
- zgłoś + telefon CCC — natychmiast po przekroczeniu CET

### Powiązane
- [U08](#U08) — składowe paczki ATC

---

# Grupa V — Transport zwrotny / kopiowanie

<a id="U18"></a>
## ~~U18 — Connector 2.0 nie kopiuje do docelowych bucketów~~ → scalone z [U03](#U03)

> ⚠ **U18 zostało scalone z [U03](#U03)** — z punktu widzenia Dyspozytora reakcja na pełną i selektywną awarię Connector 2.0 jest identyczna (zgłoś).
> Wszystkie odwołania `[U18]` w innych dokumentach należy traktować jako równoważne `[U03]`.

---

<a id="U19"></a>
## U19 — Niezgodność wersji IVA / IVA BACKUP

**Kategoria:** Transport zwrotny
**Źródło:** HTML R12

### Opis
Wersja **IVA BACKUP** (z CCA) i **IVA** (FIDx-710, z Perun4V) nie zgadzają się logicznie. Prawidłowo: Backup > IVA = OK.

### Objawy
- W CCM kafelek IVA Backup z wersją niższą lub równą FIDx-710
- W Perun4V status `ERR-I` lub `Process failed` ale brak Backup w wyższej wersji
- Status Backup: zielony / fioletowy ale wersja nieprawidłowa

### Działanie
1. Porównać wersje:
   - **W CCM:** wiersz IVA vs wiersz IVA Backup
   - **W Perun4V:** wersja FIDx-710
   - **W MinIO:** `cca/ID_FBCC/out/BD/` → raport CCA z wersją Backup
2. Wersje **niezgodne** → zgłoś + telefon CCC niezwłocznie
3. **Nie zastępować automatyki ręcznym menu** (HTML R12)

### Zgłoszenie
- zgłoś + telefon CCC — niezwłocznie

### Powiązane
- [U15](#U15), [U16](#U16), [U18](#U18), [U23](#U23)

---

# Grupa VI — Zgłoszenie zewnętrzna / fallbacki

<a id="U20"></a>
## U20 — AAC Fallback (IDCC(a) nie dostarczył AACs)

**Kategoria:** Zgłoszenie zewnętrzna
**Źródło:** HTML R13

### Opis
IDCC(a) nie wytworzył Allocation Available Capacities (AACs, ID1-373-XX) dla XBID w wymaganym czasie.

### Działanie
1. Dostarczyć **computed AACs do XBID** przez narzędzie lokalne
2. Deadliny:
   - **20:00 D-1** dla IDCC(b)
   - **02:00 D** dla IDCC(c)
   - **07:00 D** dla IDCC(d)
3. **Potwierdzenie mailowe do CCC**

### Zgłoszenie
- **CCC** — potwierdzenie mailem
- **Zgłoś** (CIZ, WPO, PSE-I — patrz sekcja Kontakty do zgłoszeń)

### Powiązane
- (nie dotyczy FIDx-831 ani innych plików pulpitu — to procedura zewnętrzna)

---

<a id="U21"></a>
## U21 — Decoupling SDAC — konieczność MD250

**Kategoria:** Zgłoszenie zewnętrzna
**Źródło:** HTML R14

### Opis
Decoupling SDAC — wymaga dostarczenia Shadow Auction Results (MD250).

### Działanie
1. Dostarczyć **Shadow Auction Results (MD250)** do CCCt przez **ECP/EDX**
2. Deadliny:
   - **Deadline 1:** TET MCR (~15:43)
   - **Deadline 2:** ~17:24
3. Plik MD250 (FID1-250) monitorowany w pulpicie IDCC(a)

### Zgłoszenie
- **CCC** — koordynacja
- **Zgłoś** (CIZ, WPO, PSE-I — patrz sekcja Kontakty do zgłoszeń)

### Dotyczy plików
- **FID1-250** (MD250, Shadow Auction)

---

<a id="U22"></a>
## U22 — Late NTC delivery po IDA2

**Kategoria:** Zgłoszenie zewnętrzna
**Źródło:** HTML R15

### Opis
NTC nie dostarczone do XBID przed 21:53 D-1 — proces IDCC(b) wstrzymany automatycznie.

### Objawy
- Checkpoint dostarczenia NTC do XBID przed startem aukcji IDA2 nie został osiągnięty
- Pulpit IDCC(b) — Final Intraday NTC (FIDx-921) — kafelek czerwony / czarny

### Działanie
1. **Automatyczne wznowienie po IDA2**
2. Monitorować wznowienie i publikację NTC **przed 22:30**
3. Brak publikacji → zgłoś + telefon CCC

### Zgłoszenie
- zgłoś + telefon CCC — przy braku wznowienia

### Dotyczy plików
- **FID2-921** (Final Intraday NTC IDCC(b))

---

<a id="U23"></a>
## U23 — Brak raportu CCA

**Kategoria:** Zgłoszenie zewnętrzna
**Źródło:** HTML R20, BUP §Ryzyko 26 (str. 69)

### Opis
Raport CCA nie został wygenerowany lub nie jest dostępny w MinIO `cca/ID_FBCC/out/BD/`.

### Objawy
- Brak raportu w bucketcie MinIO
- Brak emaila z raportem CCA na kdm6@pse.pl
- Kafelek IVA Backup czarny po CET → [U18](#U18) jako możliwa przyczyna

### Działanie
1. Sprawdzić status procesu CCA w CCM
2. Sprawdzić bucket MinIO `cca/ID_FBCC/out/BD/` ręcznie
3. Sprawdzić skrzynkę **kdm6@pse.pl** — kopia mailowa raportu
4. Jeśli plik istnieje w `cca/`, a CCM nie widzi → [U18](#U18) (CN2 nie kopiuje)
5. Brak mimo poprawnego zakończenia procesu → zgłoś

### Zgłoszenie
- **Zgłoś** (CIZ, WPO, PSE-I — patrz sekcja Kontakty do zgłoszeń)

### Powiązane
- [U07](#U07), [U18](#U18), [U19](#U19)

---

# Procedury (P01-P06)

<a id="P01"></a>
## P01 — GUI CCCt — Manual Upload

**W odpowiedzi na:** [U03](#U03), [U09](#U09), [U10](#U10), [U11](#U11)
**Źródło:** BUP §Ryzyko 11-13 (str. 47-49)

### Cel
Ręczne wgranie pliku do Core CC Tool przez interfejs graficzny — alternatywa dla automatycznej wysyłki przez Connector 2.0.

### Kroki

1. Zalogować się do **Core CC Tool** (GUI)
2. Wybrać **dzień handlowy** (niebieskie tło, kalendarz)
3. Kliknąć **Manual Upload** (przycisk w panelu głównym)
4. W oknie dialogowym kliknąć ikonę wyboru pliku → wskazać plik z dysku
5. Kliknąć **Upload file**
6. Odświeżyć stronę i wejść w **Message Viewer**
7. Zweryfikować status pliku: **Processed** = OK
8. Jeśli status `Rejected` → odczytać kod błędu → [U10](#U10)
9. Wpis w karcie A.4 — [P06](#P06)

### Uwagi
- Wersja pliku **musi być wyższa** niż dotychczas wgrana — patrz [U12](#U12)
- W razie błędu `gateClosed` → zgłoś (administrator CCCt otwiera bramkę)

### Powiązane
- [P02](#P02) — pobranie pliku z ZP przed P01
- [P04](#P04) — pobranie z MinIO przed P01
- [P05](#P05) — pobranie z CCCt MV przed P01

---

<a id="P02"></a>
## P02 — Pobranie pliku z ZP → GUI CCCt

**W odpowiedzi na:** [U03](#U03), [U06](#U06) (dla FIDx-831)
**Źródło:** AC manuall ZP.docx

### Cel
Pobranie pliku AC (FIDx-831) z aplikacji **ZP (zdolności przesyłowe)** i wgranie przez GUI CCCt, gdy Connector 2.0 nie działa.

### Kroki

1. Otworzyć aplikację **ZP** → **Główne okno**
2. Przejść do zakładki **bilans AC**
3. W górze okna wybrać odpowiedni dokument **FIDx-831** dla bieżącej doby
4. Kliknąć **Pobierz XML** — plik zapisany lokalnie
5. → [P01 — GUI CCCt Manual Upload](#P01) z pobranym plikiem
6. Wpis w karcie A.4 — [P06](#P06): uzasadnienie *„brak Connector 2.0"*

### Dotyczy plików
- **FID1-831** (AC IDCC(a))
- **FID2-831** (AC IDCC(b))
- **FID3C-831, FID3-831** (AC IDCC(c), IDCC(d))

### Powiązane
- [P01](#P01)

---

<a id="P03"></a>
## P03 — Ręczne uruchomienie obliczeń w Perun4V

**W odpowiedzi na:** [U14](#U14)
**Źródło:** BUP §Ryzyko 1 (str. 9-16)

### Cel
Ręczne uruchomienie obliczeń FBA w Perun4V, gdy automatyczna ścieżka przez sFTP/Connector 2.0 zawodzi.

### Kroki

1. Zalogować się do **Perun4V** (https://lccv.tscnet.eu → Local Login)
2. Pobrać paczkę ZIP z **MinIO** (`perun/ID_FBCC/in/yyyy-mm-dd`) lub z CCM (PPM → Pobierz) → [P04](#P04)
3. Zapisać paczkę w katalogu sieciowym `\\uo-data\…\YYYYMMDD\Perun\`
4. W GUI Perun4V wybrać **„Select timestamp date"** → ustawić poprawny BD
5. Wgrać paczkę przez GUI (Upload)
6. Uruchomić obliczenia
7. Monitorować w sekcji `Status → Details` — kolumna `[Result]` per godzina
8. Po zakończeniu pobrać wynikowy plik **FIDx-710 (IVA)** z Perun4V (download)
9. Wynik wysłać przez CCM (PPM → Wyślij) lub [P01](#P01)
10. Wpis w karcie A.4 — [P06](#P06)

### Komunikaty błędu Perun4V

| Komunikat | Działanie |
|---|---|
| Błędny BD | Ustawić poprawny BD |
| Brak pliku w paczce | Uzupełnić składową, przepakować |
| Błędny plik w paczce | Pobrać z CCCt MV → spakować → wczytać |

### Powiązane
- [P04](#P04), [U14](#U14), [U15](#U15), [U16](#U16)

---

<a id="P04"></a>
## P04 — Pobranie pliku z MinIO → CCM Wyślij

**W odpowiedzi na:** [U08](#U08), [U09](#U09)
**Źródło:** BUP §Ryzyko 3 (str. 22), CCM Instrukcja Użytkownika

### Cel
Pobranie pliku backupowego z MinIO i wysyłka przez CCM.

### Kroki

1. W CCM kliknąć **LPM** na zielony kwadrat w kolumnie **„MinIO"** wiersza pliku → **Pobierz**
2. Wskazać katalog sieciowy:
   - DA: `\\uo-data\…\YYYYMMDD\Perun\`
   - IDCC: zgodnie z fazą procesu
3. Alternatywnie: zalogować się do **MinIO GUI** (https://minio-gui.pse.pl) → wybrać bucket → pobrać plik bezpośrednio
4. W CCM kliknąć **PPM** na wierszu pliku → **Wyślij** → wskazać pobrany plik
5. Zweryfikować zmianę kolumny:
   - CCTool wyśl. → **zielony 'W'**
   - CCTool zwalid. → **zielony (Processed)** po ACK
6. Wpis w karcie A.4 — [P06](#P06)

### Buckety MinIO

| Bucket | Zawartość |
|---|---|
| `perun/DA_FBCC/in/yyyy-mm-dd/` | Paczki wejściowe DA do Perun4V |
| `perun/ID_FBCC/in/yyyy-mm-dd/` | Paczki wejściowe IDCC do Perun4V |
| `perun/DA_FBCC/out/yyyy-mm-dd/` | Wyniki DA z Perun4V (IVA, raporty) |
| `perun/ID_FBCC/out/yyyy-mm-dd/` | Wyniki IDCC z Perun4V |
| `cca/DA_FBCC/out/[BD]/` | IVA BACKUP i raporty CCA (DA) |
| `cca/ID_FBCC/out/[BD]/` | IVA BACKUP i raporty CCA (IDCC) |
| `cca/ID_FBCC/yyyymmdd-FIDx-831-*` | **Pliki AC (FIDx-831)** dla iteracji IDCC |

### Powiązane
- [P01](#P01), [P05](#P05)

---

<a id="P05"></a>
## P05 — Pobranie z CCCt Message Viewer → CCM Wyślij

**W odpowiedzi na:** [U08](#U08) (dla składowych paczki, plików zwrotnych z CCCt)
**Źródło:** BUP (Manual Upload, str. 47), HTML Scenariusz 2

### Cel
Pobranie pliku z Core CC Tool (zwrotny lub zewnętrzny) i wysyłka przez CCM — typowo dla **Merged GLSK (FIDx-610)**, **Merged DACF/IDCF CGM (FIDx-620)** i innych składowych paczki PERUN_IDx.

### Kroki

1. Zalogować się do **Core CC Tool**
2. Przejść do **Message Viewer**
3. Filtr po **kodzie przepływu** (np. `FID2-610`, `FID2-620`)
4. Wybrać aktualny dla bieżącego BD
5. **Download** — pobrać plik
6. Zapisać lokalnie
7. W CCM kliknąć **PPM** na wierszu danej składowej → **Wyślij** → wskazać pobrany plik
8. Zweryfikować zmianę statusu kafelka:
   - Składowa → **zielony 'R'** (ręczny)
   - Agregat PERUN_IDx → **zielony 'W'**
   - Kolumna sFTP/ZP wysł. → **zielona** (paczka wysłana do Perun4V)
9. Wpis w karcie A.4 — [P06](#P06)

### Uwaga (HTML §8.8 Scenariusz 2)
- **FIDx-610 (Merged GLSK z CCCt)** ≠ **FIDx-607 (raw GLSK od PSE)**. Pomyłka źródła = błąd procesowy

### Powiązane
- [P01](#P01), [P04](#P04)

---

<a id="P06"></a>
## P06 — Wpis w karcie A.4 (status ręczny)

**W odpowiedzi na:** każde ręczne działanie
**Źródło:** HTML Aneks A.4 (checklista IDCC(b)–(d))

### Cel
Udokumentowanie każdej ręcznej interwencji Dyspozytora w trakcie procesu IDCC.

### Treść wpisu

| Pole | Treść |
|---|---|
| Data / godzina | YYYY-MM-DD HH:MM |
| Iteracja | IDCC(a) / (b) / (c) / (d) |
| Kafelek / FID | np. FID1-831 |
| Stan kafelka przed interwencją | np. czerwony/czerwony |
| Zastosowana procedura | np. P02 + P01 |
| Powiązane ryzyko | np. U03 (brak Connector 2.0) |
| Wersja pliku | v1, v2, … |
| Stan kafelka po interwencji | np. ciemnozielony 'W'/zielony |
| Zgłoszenie | komu zgłoszono (zgłoś — CIZ/WPO/PSE-I — i/lub CCC) |
| Uwagi | dowolne |

### Powiązane
- Każda procedura P01-P05

---

<a id="kontakty"></a>
## Kontakty do zgłoszeń

| Podmiot | Zakres | Kontakt | Uwagi |
|---|---|---|---|
| **CCC / TSCNET** | Sterowanie procesem, potwierdzenie stanu | operator@tscnet.eu | Kontakt telefoniczny wg listy operacyjnej |
| **CORESO** | Koordynacja po stronie operatora procesu | day-ahead.engineer@coreso.eu | Zgodnie z uzgodnionym kanałem |
| **PSE Innowacje** | CCM, Connector 2.0, MinIO, SFTP | Kanał wewnętrzny PSE | Zgłoszenie przy awariach narzędzi |
| **CCA — zespół utrzymania** | CCA, raporty walidacyjne, IVA BACKUP, FID1-928 | Kanał wewnętrzny PSE Innowacje | Ryzyka U18, U19, U23 |
| **WPO PSE** | Zgłoszenie operacyjna | Słabicki, Jarzęcka, Krzysztoszek, Łukaszewski, Rodo | Wszystkie błędy procesowe |
| **kdm6@pse.pl** | Potwierdzenia raportowe i korespondencja | skrzynka mailowa | Raporty CCA, Perun4V |
| **CIZ** | Centrum Zgłaszania Incydentów PSE | wewnętrzny | Awarie narzędzi (priorytet zależny od fazy) |
