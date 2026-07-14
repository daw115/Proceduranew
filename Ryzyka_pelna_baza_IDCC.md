# Pełna baza ryzyk IDCC — Master Reference

> **Cel:** Pełna baza wszystkich możliwych ryzyk w procesie IDCC, zagregowanych z wszystkich instrukcji (HTML procedura, BUP DA, NOR DA, CCM Instrukcja, AC manuall ZP, Confluence). Numeracja **nowa sekwencyjna R01–R32**.
>
> **Każde ryzyko ma dwie formy:**
> - **A. Rozbudowany opis + procedura ze screenami** — pełna instrukcja krok po kroku z odniesieniami do rysunków w dokumentach źródłowych
> - **B. Skrót strzałkami** — 1-2 linijki gotowe do wklejenia w opisach stanów kafelków
>
> **Źródła:**
> - HTML procedura IDCC (FBA_TSO_IDCC v1.0 FINAL DRAFT) — §9 R01-R20
> - FBA_TSO_BUP_03 (BUP DA v0.31) — Ryzyka #1-#14, #25-#28 *(LTA pominięte)*
> - FBA_TSO_NOR_03 (NOR DA v0.21)
> - CCM Instrukcja Użytkownika Dyspozytora v2.6
> - Confluence „IVA i IVA Backup"
> - AC manuall ZP.docx

> ⚠ **Każde ryzyko należy zgłosić do: CIZ, WPO, PSE-I (PSE Innowacje).** Poniższe procedury podają tylko działania operacyjne — nie powtarzają odbiorców zgłoszenia.

---

## Spis treści

### Grupa I — Narzędzia dyspozytorskie (CCM)
1. [R01 — Brak dostępu do CCM](#R01)
2. [R02 — Błędna paczka do Perun4V (weryfikacja CCM)](#R02)

### Grupa II — Core CC Tool (CCCt)
3. [R03 — Brak dostępu do Core CC Tool](#R03)
4. [R04 — Brak dostarczonego pliku do CCCt](#R04)
5. [R05 — Plik odrzucony przez CCCt (ACK negatywny)](#R05)
6. [R06 — Brak ACK / timeout](#R06)
7. [R07 — Niezakończenie walidacji ATC w czasie](#R07)

### Grupa III — Perun4V
8. [R08 — Brak działania sFTP / brak uruchomienia FBA](#R08)
9. [R09 — ERR-I (część TS niepoliczona)](#R09)
10. [R10 — Process failed (wszystkie TS niepoliczone)](#R10)
11. [R11 — Brak dostępu do Perun4V](#R11)
12. [R12 — Brak wyników IVA i raportów z sFTP](#R12)
13. [R13 — Brak możliwości pobrania F310 z Perun4V](#R13)
14. [R14 — Dodanie wyłączenia awaryjnego w Perun4V](#R14)

### Grupa IV — MinIO
15. [R15 — Brak dostępu do MinIO / Awaria Connector 2.0](#R15)
16. [R16 — Brak paczki plików na MinIO](#R16)
17. [R17 — Brak dostępu do MinIO dla raportu CCA](#R17)

### Grupa V — Connector 2.0
18. [R18 — Awaria Connector 2.0](#R18)
19. [R19 — CN2 nie kopiuje IVA i raportów do bucketów CCA](#R19)

### Grupa VI — Aplikacje wewnętrzne (ZP, Kreatory, CCA)
20. [R20 — Brak dostępu do ZP / brak wersji FIDx-831](#R20)
21. [R21 — Brak generowania IGM/GLSK/CBCORA (Kreator)](#R21)
22. [R22 — Brak F320_CCA / Vertices_MAP_CCA](#R22)
23. [R23 — Brak dostępnego raportu CCA](#R23)
24. [R24 — Niezgodność logiki IVA BACKUP z Perun4V](#R24)

### Grupa VII — Pomocnicze narzędzia (kdm6, sFTP)
25. [R25 — Brak dostępu do poczty kdm6](#R25)
26. [R26 — Brak działania sFTP (uniwersalne)](#R26)

### Grupa VIII — Zgłoszenie zewnętrzna (ECP/EDX, XBID)
27. [R27 — Decoupling SDAC — konieczność MD250](#R27)
28. [R28 — AAC Fallback (IDCC(a) nie dostarczył AACs)](#R28)
29. [R29 — Late NTC delivery po IDA2](#R29)

---

<a id="R01"></a>
# R01 — Brak dostępu do CCM

**Aplikacja:** CCM ([N01](Inwentarz_IDCC.md#N01))
**Źródło:** HTML §9 R06, BUP DA §Ryzyko 27 (str. 69)
**U-kod:** [U01](Karta_ryzyk_IDCC.md#U01) | **Stary kod:** CCM-R01
**Wpływ na IDCC:** brak monitoringu wszystkich kafelków; brak ręcznej wysyłki przez PPM → Wyślij; brak funkcji „Informacje" o pliku; utrata wglądu w fazę procesu.

## A. Procedura szczegółowa

1. **Diagnoza dostępności:**
   - Sprawdź czy strona https://ccm.spsm.pse.pl ładuje się w przeglądarce
   - 📷 *CCM Instrukcja v2.6, Rys. 1 — Okno logowania do aplikacji*
   - Spróbuj w innej przeglądarce / trybie incognito
   - Sprawdź połączenie VPN/sieci PSE
2. **Zgłoszenie incydentu:**
   - **Zgłoś** (CIZ, WPO, PSE-I — patrz nagłówek dokumentu)
3. **Tymczasowa praca bez CCM** — monitoruj bezpośrednio w narzędziach docelowych:
   - **Core CC Tool — Message Viewer** dla statusów plików (📷 *BUP DA Rys. 12, str. 17*)
   - **MinIO GUI** dla plików w bucketach (https://minio-gui.pse.pl)
   - **Perun4V** dla wyników FBA
   - **kdm6@pse.pl** dla raportów CCA
4. **Ręczna wysyłka plików** (gdy brak CCM):
   - Wykorzystaj **[P01 — GUI CCCt Manual Upload](Karta_ryzyk_IDCC.md#P01)** bezpośrednio z dysku
   - 📷 *BUP DA Rys. 15 — Core CC Tool manual file upload, str. 47*
5. **Po przywróceniu CCM:** [P06 — Wpis A.4](Karta_ryzyk_IDCC.md#P06).

## B. Skrót strzałkami

CCM niedostępne → sprawdź VPN/przeglądarkę → zgłoś → tymczasowo: CCCt MV / MinIO GUI / Perun4V / kdm6 → wysyłka przez [P01](Karta_ryzyk_IDCC.md#P01) → [P06](Karta_ryzyk_IDCC.md#P06)

## Powiązania
- **Współwystępowanie:** [R03](#R03) (brak CCCt) — krytyczne; pozostają tylko telefon CCC + MinIO
- **Procedury:** [P01](Karta_ryzyk_IDCC.md#P01), [P04](Karta_ryzyk_IDCC.md#P04)

---

<a id="R02"></a>
# R02 — Błędna paczka do Perun4V (weryfikacja CCM)

**Aplikacja:** CCM ([N01](Inwentarz_IDCC.md#N01)), Perun4V ([N03](Inwentarz_IDCC.md#N03))
**Źródło:** BUP DA §Ryzyko 28 (str. 69)
**U-kod:** [U08](Karta_ryzyk_IDCC.md#U08), [U09](Karta_ryzyk_IDCC.md#U09) | **Stary kod:** CCM-R02
**Wpływ na IDCC:** paczka ZIP (PERUN_IDx) niekompletna lub błędna → niemożliwa konstrukcja paczki do Perun4V → brak obliczeń FBA dla iteracji.

## A. Procedura szczegółowa

1. **Identyfikacja problemu w CCM:**
   - W CCM rozwiń agregat **PERUN_IDx** (kliknięcie ▼ obok wiersza)
   - 📷 *CCM Instrukcja v2.6, sekcja „Grupowanie pozycji"*
   - Zidentyfikuj problematyczną składową — kolor czerwony !, czarny, czerwony
2. **Sprawdzenie szczegółów składowej:**
   - LPM na ikonę statusu składowej → wybierz **„Informacje"**
   - 📷 *CCM Instrukcja v2.6, Rys. 11 — Monitorowanie wielkości plików*
   - Odczytaj rozmiar (rzeczywisty vs oczekiwany), lokalizację MinIO, datę dostarczenia
3. **Pobranie poprawnego pliku** ([P05 — CCCt Message Viewer](Karta_ryzyk_IDCC.md#P05)):
   - CCCt → Message Viewer → filtr po FID składowej (np. `FID2-610` dla Merged GLSK)
   - 📷 *BUP DA Rys. 12, str. 17 — CC Tool Message Viewer*
   - Pobierz plik (strzałka w dół po prawej)
   - ⚠ **Uwaga:** FIDx-610 (Merged GLSK z CCCt) ≠ FIDx-607 (raw GLSK od PSE)
4. **Wysyłka przez CCM:**
   - CCM → PPM na wierszu składowej → **Wyślij** → wskaż pobrany plik
   - 📷 *CCM Instrukcja v2.6, Rys. 19 — Rozwijane menu opcja Wyślij*
5. Po wysłaniu: składowa → zielony 'R'; agregat PERUN_IDx → zielony 'W'; kolumna sFTP/ZP wysł. → zielona.

## B. Skrót strzałkami

CCM rozwiń agregat → zidentyfikuj składową (czerwony!/czarny) → LPM Informacje → [P05](Karta_ryzyk_IDCC.md#P05) pobierz z CCCt MV → CCM PPM Wyślij → zweryfikuj zielony W

## Powiązania
- **Wpływa na:** [R08](#R08) (jeśli paczka błędna, Perun4V odrzuci)
- **Procedury:** [P05](Karta_ryzyk_IDCC.md#P05)

---

<a id="R03"></a>
# R03 — Brak dostępu do Core CC Tool

**Aplikacja:** Core CC Tool ([N02](Inwentarz_IDCC.md#N02))
**Źródło:** HTML §9 R07, BUP DA §Ryzyko 11 (str. 47)
**U-kod:** [U02](Karta_ryzyk_IDCC.md#U02) | **Stary kod:** CCCt-R01
**Wpływ na IDCC:** brak weryfikacji ACK, brak [P01 Manual Upload](Karta_ryzyk_IDCC.md#P01), brak publikacji AC do PuTo, brak monitoringu wyników centralnych CCCt.

## A. Procedura szczegółowa

1. **Diagnoza dostępności:**
   - Sprawdź czy strona CCCt ładuje się
   - 📷 *BUP DA Rys. 11 — Core CC Tool okno główne, str. 47*
   - Spróbuj zalogować ponownie
2. **Tymczasowa praca bez CCCt:**
   - Monitoruj statusy w **CCM** (kafelki) — jedyne źródło dla TSO PSE
   - Monitoruj **kdm6@pse.pl** dla raportów zwrotnych
3. **Zgłoszenie telefoniczna:**
   - **CCC ([N13](Inwentarz_IDCC.md#N13))** — operator@tscnet.eu + telefon (lista operacyjna)
4. **Alternatywny kanał** (tylko po uzgodnieniu z CCC):
   - ECP/EDX bezpośrednio (dla CB/GLSK/EC)
5. **Zgłoszenie incydentu:**
   - **Zgłoś** (CIZ, WPO, PSE-I — patrz nagłówek dokumentu) — incydent krytyczny przy braku CCCt
6. Po przywróceniu CCCt: [P06 — Wpis A.4](Karta_ryzyk_IDCC.md#P06).

## B. Skrót strzałkami

CCCt niedostępne → monitoruj w CCM/kdm6 → telefon CCC → alternatywny kanał (ECP/EDX) tylko po uzgodnieniu → zgłoś → po przywróceniu [P06](Karta_ryzyk_IDCC.md#P06)

## Powiązania
- **Współwystępowanie z [R01](#R01) (brak CCM)** = krytyczne — pozostaje tylko telefon CCC + MinIO bezpośrednio

---

<a id="R04"></a>
# R04 — Brak dostarczonego pliku do CCCt

**Aplikacja:** Core CC Tool ([N02](Inwentarz_IDCC.md#N02))
**Źródło:** HTML §9 R04 (pośrednio) + R09, BUP DA §Ryzyko 12 (str. 48)
**U-kod:** [U08](Karta_ryzyk_IDCC.md#U08), [U11](Karta_ryzyk_IDCC.md#U11) | **Stary kod:** CCCt-R02
**Wpływ na IDCC:** plik nie pojawił się w CCCt mimo upływu czasu wysyłki; proces nie kontynuuje; brak publikacji do PuTo (AC) lub XBID (NTC).

## A. Procedura szczegółowa

1. **Sprawdzenie w CCCt Message Viewer:**
   - CCCt → logowanie → **selektor procesu** obok niebieskiego pola → wybierz **`ID1` / `ID2` / `ID3C` / `ID3`** (zamiast `DA`)
   - 📷 *BUP DA Rys. 11 — CC Tool okno główne*
   - Wybierz Business Day → **Message Viewer**
   - 📷 *BUP DA Rys. 12 — CC Tool Message Viewer*
   - W polu **Message Definition** wpisz np. `FID1-831` → **Apply**
   - 📷 *BUP DA Rys. 13 — szczegóły pobieranego pliku*
2. **Analiza wyniku:**
   - **Brak wpisu** → plik faktycznie nie dotarł
3. **Diagnostyka transportu:**
   - Sprawdź [R18](#R18) (CN2)
   - Sprawdź [R15](#R15) (MinIO — czy plik jest w bucketcie)
4. **Pobranie ze źródła:**
   - **AC (FIDx-831):** [P02 — Pobranie z ZP](Karta_ryzyk_IDCC.md#P02)
   - **IVA / paczki:** [P04 — Pobranie z MinIO](Karta_ryzyk_IDCC.md#P04)
   - **Składowe paczki:** [P05 — z CCCt MV](Karta_ryzyk_IDCC.md#P05) (z innej iteracji jeśli możliwe)
5. **Manual Upload:** [P01 — GUI CCCt Manual Upload](Karta_ryzyk_IDCC.md#P01) — 📷 *BUP DA Rys. 15, str. 47*
6. Po wysłaniu: zweryfikuj status **Processed** w Message Viewer → [P06](Karta_ryzyk_IDCC.md#P06).

## B. Skrót strzałkami

CCCt MV → selektor procesu `ID1...ID3` → Message Definition `FID` → Apply → brak wpisu → sprawdź [R15](#R15)/[R18](#R18) → [P02](Karta_ryzyk_IDCC.md#P02)/[P04](Karta_ryzyk_IDCC.md#P04) → [P01](Karta_ryzyk_IDCC.md#P01) → status Processed → [P06](Karta_ryzyk_IDCC.md#P06)

---

<a id="R05"></a>
# R05 — Plik odrzucony przez CCCt (ACK negatywny)

**Aplikacja:** Core CC Tool ([N02](Inwentarz_IDCC.md#N02))
**Źródło:** HTML §9 R05, BUP DA §Ryzyko 13 (str. 49)
**U-kod:** [U10](Karta_ryzyk_IDCC.md#U10), [U12](Karta_ryzyk_IDCC.md#U12) | **Stary kod:** CCCt-R03
**Wpływ na IDCC:** plik dotarł do CCCt, ale ACK negatywny — proces zatrzymany, konieczne ponowienie z poprawionym plikiem / wyższą wersją.

## A. Procedura szczegółowa

1. **Odczyt kodu ACK w CCM:**
   - Najedź kursorem na czerwony status w kolumnie **CCTool zwalid.**
   - 📷 *PDF Dyspozytora v2.6, s. 13 — komunikat ACK po najechaniu*
   - Odczytaj komunikat błędu
2. **Weryfikacja w CCCt Message Viewer:**
   - CCCt → ID# process → MV → filtr po FID → wybierz wpis
   - 📷 *BUP DA Rys. 12 — Message Viewer*
   - Sprawdź szczegóły rejekcji
3. **Reakcja per kod ACK:**

| Kod | Komunikat | Działanie |
|---|---|---|
| 20 | Gate for provided message definition is not opened | Bramka zamknięta — sprawdź TET/CET; w CCCt sprawdź proces `IDx-AC-FORWARDING`; zgłoś (admin CCCt otwiera bramkę) |
| 21 | Provided version is not higher than already stored data | **duplicatedVersion** — podbij wersję; [P02](Karta_ryzyk_IDCC.md#P02) / [P04](Karta_ryzyk_IDCC.md#P04) → [P01](Karta_ryzyk_IDCC.md#P01) z v+1 |
| 22 | ~~Delivered constraint value is negative~~ | ❌ Nieaktualne (CCCt akceptuje wartości ujemne) |
| 30 | File size mismatch | [P04 MinIO](Karta_ryzyk_IDCC.md#P04) lub [P02 ZP](Karta_ryzyk_IDCC.md#P02) z poprawnym plikiem → weryfikacja zawartości → [P01](Karta_ryzyk_IDCC.md#P01) |
| 40 | Backup version lower | NIE wysyłać backupu (dotyczy IVA BACKUP) |
| 41 | Backup not available | → [R23](#R23) |
| 42 | Backup validation failed | Sprawdź raport CCA → zgłoś |
| — | Message has some invalid timeSeries… | Poprawa struktury XML (MTU) → ponowić |
| — | Błąd procesu | Proces w CCCt zakończony błędem → zgłoś |

4. Po poprawie i ponownej wysyłce → zweryfikuj **Processed** → [P06](Karta_ryzyk_IDCC.md#P06).

## B. Skrót strzałkami

Najedź na czerwony status → odczytaj kod ACK → reakcja per kod (20: zgłoś — admin CCCt otwiera bramkę; 21: podbicie wersji + [P01](Karta_ryzyk_IDCC.md#P01); 30: [P04](Karta_ryzyk_IDCC.md#P04)/[P02](Karta_ryzyk_IDCC.md#P02) → [P01](Karta_ryzyk_IDCC.md#P01)) → status Processed → [P06](Karta_ryzyk_IDCC.md#P06)

---

<a id="R06"></a>
# R06 — Brak ACK / timeout

**Aplikacja:** Core CC Tool ([N02](Inwentarz_IDCC.md#N02))
**Źródło:** HTML §9 R05 (zawężenie), BUP DA §Ryzyko 12 (str. 48)
**U-kod:** [U11](Karta_ryzyk_IDCC.md#U11) | **Stary kod:** CCCt-R04
**Wpływ na IDCC:** plik wysłany do CCCt (CCTool wyśl. zielony), ale ACK nie napłynął w czasie (>2-3 min); niepewność statusu; ryzyko duplikatu jeśli Dyspozytor ponawia.

## A. Procedura szczegółowa

1. **Najedź na status z '?'** (czerwony ?) → odczytaj **czas oczekiwania**
   - 📷 *PDF Dyspozytora v2.6, s. 12 — Brak ACK*
2. **Czekaj 5 min od wysyłki** — przeciążenie / opóźnienie transportu może być normalne
3. **Po 5 min — weryfikacja w CCCt Message Viewer:**
   - CCCt → ID# process → MV → filtr po FID
   - Sprawdź **kolumnę Status**:

| Status w CCCt | Działanie |
|---|---|
| `Processed` | CCM się nie odświeżył; ustaw status ręcznie 'R' w CCM; zgłoś |
| `Rejected` | Odczytaj kod ACK → przejdź do [R05](#R05) |
| **Brak wpisu** | Plik nie dotarł → [R18](#R18) Connector 2.0 |

4. **Brak wpisu >10 min:**
   - Zgłoś (Connector 2.0)
   - Ponowna wysyłka tylko z podbiciem wersji → [P01](Karta_ryzyk_IDCC.md#P01) z v+1
5. ⚠ **NIE wysyłać ponownie bez weryfikacji** — kod 21 duplicatedVersion

## B. Skrót strzałkami

Najedź na '?' → odczytaj czas oczekiwania → czekaj 5 min → CCCt MV (`Processed` = ustaw R w CCM; `Rejected` = patrz [R05](#R05); brak = [R18](#R18)) → >10 min: zgłoś + [P01](Karta_ryzyk_IDCC.md#P01) z v+1

---

<a id="R07"></a>
# R07 — Niezakończenie walidacji ATC w czasie

**Aplikacja:** Core CC Tool ([N02](Inwentarz_IDCC.md#N02)) — proces walidacji ATC
**Źródło:** HTML §9 R11
**U-kod:** [U17](Karta_ryzyk_IDCC.md#U17) | **Stary kod:** CCCt-R06
**Dotyczy:** FIDx-928 (ATC Based Validation)
**Wpływ na IDCC:** **brak lokalnego fallbacku** (HTML §5.4). Po CET dyspozytor nie wykonuje dalszych czynności. Brak wyniku walidacji ATC dla iteracji.

## A. Procedura szczegółowa

1. **PRZED CET — uzupełnienie składowych paczki ATC:**
   - W CCM rozwiń agregat **PERUN_IDx_ATC**
   - Zidentyfikuj brakujące/błędne składowe (kolor czarny/czerwony/czerwony !)
   - [P05 — pobierz z CCCt MV](Karta_ryzyk_IDCC.md#P05) → wyślij przez CCM
2. **Monitoring walidacji ATC:**
   - 📷 *HTML §5.4 — Zasady szczególne dla ATC*
   - CCM kafelek FIDx-928 — monitoring statusu
   - CCCt → ID# process → MV → filtr `FID1-928`
3. **PO CET:**
   - ⛔ **STOP — żadnych działań ręcznych**
   - HTML §5.4 cyt.: *„Brak wyniku ATC w czasie → dyspozytor nie wykonuje dalszych czynności. Brak lokalnego fallbacku."*
4. **Zgłoszenie natychmiast:**
   - **Zgłoś** (CIZ, WPO, PSE-I — patrz nagłówek dokumentu)
   - **CCC ([N13](Inwentarz_IDCC.md#N13))** — telefonicznie
5. [P06 — Wpis A.4](Karta_ryzyk_IDCC.md#P06).

## B. Skrót strzałkami

**Przed CET:** uzupełnij składowe PERUN_IDx_ATC → [P05](Karta_ryzyk_IDCC.md#P05) → CCM Wyślij → monitoruj FIDx-928
**Po CET:** ⛔ STOP — zgłoś + telefon CCC; [P06](Karta_ryzyk_IDCC.md#P06)

---

<a id="R08"></a>
# R08 — Brak działania sFTP / brak uruchomienia FBA

**Aplikacja:** Perun4V ([N03](Inwentarz_IDCC.md#N03)), sFTP ([N12](Inwentarz_IDCC.md#N12))
**Źródło:** HTML §9 R01, BUP DA §Ryzyko 1 (str. 9-16)
**U-kod:** [U03](Karta_ryzyk_IDCC.md#U03), [U14](Karta_ryzyk_IDCC.md#U14) | **Stary kod:** Perun-R01
**Wpływ na IDCC:** paczka PERUN_IDx wysłana z CCM (sFTP/ZP zielony), ale Perun4V nie rozpoczął obliczeń. Brak wyniku IVA dla iteracji.

## A. Procedura szczegółowa

1. **Diagnoza w Perun4V GUI:**
   - Otwórz https://lccv.tscnet.eu → Local Login
   - 📷 *NOR DA Rys. 7-8 — okna logowania Perun4V*
   - 📷 *NOR DA Rys. 9 — Główne okno Perun4V*
   - Sprawdź czy obliczenie dla danej doby pojawia się na liście
2. **Analiza komunikatów błędu:**

| Komunikat | Przyczyna | Działanie |
|---|---|---|
| Błędny BD | Próba uruchomienia ze złą datą | W sekcji **Select timestamp date** ustaw poprawny BD → ponów |
| Brak pliku w paczce | Brakuje jednej ze składowych ZIP | 📷 *BUP DA Rys. 29 — Perun4V brak pliku, str. 9-10*. Sprawdź zawartość ZIP; uzupełnij składową ([R02](#R02), [P05](Karta_ryzyk_IDCC.md#P05)); przepakuj |
| Błędny plik w paczce | Plik niepoprawny w ZIP | 📷 *BUP DA Rys. 30 — błąd przeliczania, str. 10-11*. Pobierz wszystkie pliki ręcznie z CCCt MV → przepakuj zgodnie z [R16](#R16) |

3. **Ręczne uruchomienie obliczeń:**
   - [P03 — Ręczne uruchomienie obliczeń w Perun4V](Karta_ryzyk_IDCC.md#P03)
   - Pobierz paczkę z MinIO `perun/ID_FBCC/in/yyyy-mm-dd/` → przeciągnij na pole w Perun4V (lub LPM → wybierz z dysku)
   - 📷 *NOR DA, sekcja Wczytanie danych do Peruna*
4. **Pobranie wyniku F310 po obliczeniach:**
   - Perun4V → pobierz F310 (download)
   - Lokalizacja zapisu: `\\uo-data\ZUO\Pion_UOD\Wydzial_DP\MODELE\5_DYSP\FBA\Pliki wejściowe do ID FBA\rrrMMdd\PERUN\` *(❓ do weryfikacji dla IDCC — patrz TODO)*
5. **Wysyłka F310/IVA do CCCt:**
   - CCM → PPM na wierszu IVA → Wyślij; lub [P01](Karta_ryzyk_IDCC.md#P01) Manual Upload
6. Jeśli mimo wszystko nie rusza → oczekuj **IVA BACKUP** od CCA (patrz [R10](#R10)).

## B. Skrót strzałkami

Perun4V GUI → sprawdź komunikat → [Błędny BD: poprawny BD] / [Brak pliku: uzupełnij + [R02](#R02)] / [Błędny plik: pobierz z CCCt MV + [R16](#R16)] → [P03](Karta_ryzyk_IDCC.md#P03) ręczne uruchomienie → pobierz F310 → CCM Wyślij lub [P01](Karta_ryzyk_IDCC.md#P01)

---

<a id="R09"></a>
# R09 — ERR-I (część TS niepoliczona)

**Aplikacja:** Perun4V ([N03](Inwentarz_IDCC.md#N03))
**Źródło:** HTML §9 R02, BUP DA §Ryzyko 6 (str. 29-38)
**U-kod:** [U15](Karta_ryzyk_IDCC.md#U15) | **Stary kod:** Perun-R02
**Wpływ na IDCC:** publikacja **wyższej wersji IVA** = wyniki Perun4V + dane CCA dla brakujących TS. Konieczne porównanie wersji.

## A. Procedura szczegółowa

1. **Identyfikacja w Perun4V GUI:**
   - Główne okno → status obliczeń z dopiskiem **`ERR-I`**
   - 📷 *BUP DA Rys. 31 — Perun4V ERR-I, str. 29*
   - Kolumna `Timestamps (Failed/Success/Running/Total)` — liczba niepoliczonych godzin
   - ⚠ Uwaga: 25 Timestamps = 24 godziny + 1 raporty
2. **Szczegóły per godzina:**
   - `Status → Details` — rozbicie obliczeń na godziny
   - 📷 *BUP DA Rys. 32 — Perun4V niepoliczona godzina, str. 30*
   - Kolumna `[Result]` — która godzina jest niepoliczona
3. **Weryfikacja w Core CC Tool:**
   - Czy zastosowano **DFP (Default Flow Parameters)** lub **Spanning hours** dla problematycznych godzin
   - CCCt → Process Detail → klik w datę BD → klik w okno BD → rozwiń szczegóły procesu
4. **Email z informacją:** sprawdź **kdm6@pse.pl** — CCC wysyła informację o zastosowaniu DFP/Spanning
5. **Monitoring IVA BACKUP:**
   - Kafelek IVA Backup powinien pokazać wyższą wersję (Backup > IVA z Perun4V)
   - Jeśli stan **red_pulse** (zielony z pulsującą czerwoną obwódką) → Scenariusz 4 HTML §8.8
6. **Brak publikacji Backup w czasie:**
   - **Zgłoś + telefon CCC**
7. ⚠ **Zakaz** stosowania fallbacku 20% Fmax z DA.

## B. Skrót strzałkami

Perun4V `ERR-I` → Status → Details → zidentyfikuj niepoliczone godziny → sprawdź DFP/Spanning w CCCt → kdm6 (email) → monitoruj IVA Backup (wyższa wersja) → brak publikacji = zgłoś + telefon CCC

---

<a id="R10"></a>
# R10 — Process failed (wszystkie TS niepoliczone)

**Aplikacja:** Perun4V ([N03](Inwentarz_IDCC.md#N03))
**Źródło:** HTML §9 R03, BUP DA §Ryzyko 7 (str. 39)
**U-kod:** [U16](Karta_ryzyk_IDCC.md#U16) | **Stary kod:** Perun-R03
**Wpływ na IDCC:** publikowana **IVA BACKUP v1** jako wynik wyłącznie z CCA. Brak wartości IVA z obliczeń Perun4V.

## A. Procedura szczegółowa

1. **Identyfikacja w Perun4V GUI:**
   - Status obliczenia: **`Process failed`**
   - Kolumna Timestamps: wszystkie godziny w **`Failed`**
2. **Oczekiwanie na IVA BACKUP v1:**
   - CCA wygeneruje IVA Backup automatycznie
   - Kafelek IVA Backup → zielony lub `red_pulse` (Scenariusz 4)
3. **Brak publikacji Backup w czasie:**
   - **Zgłoś + telefon CCC** — natychmiast
4. ⚠ **Zakaz** stosowania fallbacku 20% Fmax z DA (HTML §7).
5. **Wpis A.4:** [P06](Karta_ryzyk_IDCC.md#P06) — pełny opis zdarzenia.

## B. Skrót strzałkami

Perun4V `Process failed` → oczekuj IVA Backup v1 z CCA → brak = zgłoś + telefon CCC; ⛔ zakaz fallbacku 20% Fmax; [P06](Karta_ryzyk_IDCC.md#P06)

---

<a id="R11"></a>
# R11 — Brak dostępu do Perun4V

**Aplikacja:** Perun4V ([N03](Inwentarz_IDCC.md#N03))
**Źródło:** BUP DA §Ryzyko 4 (str. 26)
**U-kod:** [U05](Karta_ryzyk_IDCC.md#U05) | **Stary kod:** Perun-R04
**Wpływ na IDCC:** brak monitoringu stanu obliczeń (Successful/ERR-I/Process failed); brak [P03 Ręczne uruchomienie](Karta_ryzyk_IDCC.md#P03).

## A. Procedura szczegółowa

1. **Diagnoza:**
   - Sprawdź https://lccv.tscnet.eu w innej przeglądarce
   - Sprawdź sieć / TSCNET status
2. **Tymczasowy monitoring (gdy brak Perun4V):**
   - **CCM** — statusy IVA / Raporty z Perun (kafelki MinIO)
   - **kdm6@pse.pl** — raporty Perun4V po obliczeniach (email z informacją o policzonych godzinach i max IVA)
3. **Zgłoszenie telefoniczna:**
   - **TSCNET** — operator@tscnet.eu + telefon
4. **Zgłoszenie:**
   - **Zgłoś** (CIZ, WPO, PSE-I — patrz nagłówek dokumentu)

## B. Skrót strzałkami

Perun4V niedostępny → tymczasowo CCM + kdm6 → telefon TSCNET → zgłoś

---

<a id="R12"></a>
# R12 — Brak wyników IVA i raportów z sFTP

**Aplikacja:** Perun4V ([N03](Inwentarz_IDCC.md#N03)), sFTP ([N12](Inwentarz_IDCC.md#N12))
**Źródło:** HTML §9 R01 (pośrednio), BUP DA §Ryzyko 5 (str. 28)
**U-kod:** [U03](Karta_ryzyk_IDCC.md#U03), [U14](Karta_ryzyk_IDCC.md#U14) | **Stary kod:** Perun-R05
**Wpływ na IDCC:** Perun4V wykonał obliczenia, ale wyniki (IVA + raporty) nie trafiły przez sFTP do Connector 2.0. Brak IVA w CCM/CCCt mimo obliczonego procesu.

## A. Procedura szczegółowa

1. **Weryfikacja w Perun4V:** obliczenia zakończone (status `Successful` / `ERR-I`)
2. **Pobranie F310 ręcznie z Perun4V GUI:**
   - W liście obliczeń → klik na zakończone obliczenie → download F310/IVA
3. **Wysyłka:**
   - **CCM** → PPM → Wyślij; lub
   - [P01 — Manual Upload do CCCt](Karta_ryzyk_IDCC.md#P01)
4. **Zgłoszenie sFTP:**
   - **Zgłoś**
5. **Sprawdzenie raportów:** czy raporty są na MinIO `perun/ID_FBCC/out/yyyy-mm-dd/`

## B. Skrót strzałkami

Perun4V Successful, brak IVA w CCM → pobierz F310 ręcznie z Perun4V → CCM Wyślij / [P01](Karta_ryzyk_IDCC.md#P01) → zgłoś

---

<a id="R13"></a>
# R13 — Brak możliwości pobrania F310 z Perun4V

**Aplikacja:** Perun4V ([N03](Inwentarz_IDCC.md#N03))
**Źródło:** BUP DA §Ryzyko 8 (str. 39)
**U-kod:** [U05](Karta_ryzyk_IDCC.md#U05), [U14](Karta_ryzyk_IDCC.md#U14) | **Stary kod:** Perun-R06
**Wpływ na IDCC:** brak możliwości ręcznego dostarczenia wyniku, gdy obliczenia zakończone ale download nie działa.

## A. Procedura szczegółowa

1. **Sprawdź dostęp do Perun4V** ([R11](#R11))
2. **Alternatywne pobranie F310 z MinIO:**
   - Wyniki Perun4V są kopiowane na MinIO `perun/ID_FBCC/out/yyyy-mm-dd/`
   - MinIO GUI → bucket → pobierz F310
3. **Wysyłka:** [P01](Karta_ryzyk_IDCC.md#P01) Manual Upload
4. **Zgłoszenie:**
   - **Zgłoś**

## B. Skrót strzałkami

Perun4V brak download F310 → MinIO `perun/ID_FBCC/out/yyyy-mm-dd/` → pobierz → [P01](Karta_ryzyk_IDCC.md#P01) → zgłoś

---

<a id="R14"></a>
# R14 — Dodanie wyłączenia awaryjnego w Perun4V

**Aplikacja:** Perun4V ([N03](Inwentarz_IDCC.md#N03))
**Źródło:** BUP DA §Ryzyko 9 (str. 44)
**U-kod:** — | **Stary kod:** Perun-R07
**Wpływ na IDCC:** scenariusz specyficzny dla operacyjnych wyłączeń awaryjnych; rzadkie w IDCC.

## A. Procedura szczegółowa

1. **Decyzja operacyjna** — wykonywana wyłącznie po uzgodnieniu z przełożonym dyżurnym (zgłoś).
2. **Perun4V GUI → Outage management:**
   - Procedura dodawania wyłączenia awaryjnego
   - 📷 *BUP DA Rys. dla Ryzyka 9 (str. 44)*
3. **Po dodaniu wyłączenia:** [P03 — ponowne uruchomienie obliczeń](Karta_ryzyk_IDCC.md#P03)

## B. Skrót strzałkami

Decyzja operacyjna → uzgodnienie (zgłoś) → Perun4V GUI → Outage management → [P03](Karta_ryzyk_IDCC.md#P03)

---

<a id="R15"></a>
# R15 — Brak dostępu do MinIO / Awaria Connector 2.0 dotykająca MinIO

**Aplikacja:** MinIO ([N04](Inwentarz_IDCC.md#N04))
**Źródło:** BUP DA §Ryzyko 2 (str. 17)
**U-kod:** [U04](Karta_ryzyk_IDCC.md#U04) | **Stary kod:** MinIO-R01
**Wpływ na IDCC:** brak pobierania backupowej kopii pliku; brak [P04](Karta_ryzyk_IDCC.md#P04); raporty CCA niedostępne.

## A. Procedura szczegółowa

1. **Diagnoza:**
   - Sprawdź https://minio-gui.pse.pl
   - Sprawdź funkcję „Pobierz" w CCM (LPM na kolumnie MinIO)
2. **Alternatywne źródła plików:**

| Plik | Alternatywne źródło |
|---|---|
| AC (FIDx-831) | [P02 ZP](Karta_ryzyk_IDCC.md#P02) |
| IVA / wyniki Perun4V | Perun4V GUI bezpośrednio |
| Raporty CCA | kdm6@pse.pl ([R25](#R25)) |
| Składowe paczek | [P05 CCCt MV](Karta_ryzyk_IDCC.md#P05) |

3. **Zgłoszenie:**
   - **Zgłoś** (CIZ, WPO, PSE-I — patrz nagłówek dokumentu)

## B. Skrót strzałkami

MinIO niedostępne → alternatywne źródła per plik (AC: [P02](Karta_ryzyk_IDCC.md#P02) / IVA: Perun4V GUI / Raporty: kdm6 / Składowe: [P05](Karta_ryzyk_IDCC.md#P05)) → zgłoś

---

<a id="R16"></a>
# R16 — Brak paczki plików na MinIO

**Aplikacja:** MinIO ([N04](Inwentarz_IDCC.md#N04))
**Źródło:** BUP DA §Ryzyko 3 (str. 22-25)
**U-kod:** [U08](Karta_ryzyk_IDCC.md#U08) | **Stary kod:** MinIO-R02
**Wpływ na IDCC:** mimo dostarczenia składowych do CCM, paczka ZIP nie pojawia się w MinIO `perun/ID_FBCC/in/yyyy-mm-dd/`. Perun4V nie otrzyma paczki → brak obliczeń.

## A. Procedura szczegółowa

1. **Sprawdzenie MinIO:**
   - MinIO GUI → bucket `perun/ID_FBCC/in/yyyy-mm-dd/`
   - Brak paczki ZIP mimo upływu czasu transportu
2. **Diagnostyka Connector 2.0** ([R18](#R18))
3. **Ręczne stworzenie paczki:**
   - Pobierz wszystkie składowe z **CCCt Message Viewer**:

| Plik | FID dla IDCC(b) | Działanie |
|---|---|---|
| Merged D-2CF CGM | F109/F308 | CCCt MV → filtr |
| Reference Program | FID2-632 (RefProg) | CCCt MV → filtr |
| Merged GLSK | FID2-610 | CCCt MV → filtr |
| MergingLog | F515 | CCCt MV → filtr |
| Intermediate FB Domain (Virgin) | FID2-645 | CCCt MV → filtr |
| Real GLSK | FID2-657 | CCCt MV → filtr |
| Configuration for RAO | F327 | CCCt MV → filtr |
| Individual Filtered CB | FID2-665 | CCCt MV → filtr |

  - ⚠ Przy F312/CB **odbiorca = PSE**
  - 📷 *BUP DA Rys. 11-13, str. 17-19*

4. **Zapisanie składowych:**
   - Lokalizacja: `\\uo-data\ZUO\Pion_UOD\Wydzial_DP\MODELE\5_DYSP\FBA\Pliki wejściowe do ID FBA\rrrMMdd\PERUN\` *(❓ do weryfikacji dla IDCC)*
5. **Spakowanie do ZIP:**
   - Zaznacz wszystkie pliki → PPM → **7-Zip → Dodaj do archiwum...**
   - Format archiwum: **zip**
   - Przykładowa nazwa: `rrrrMMddPerun1.zip`
   - **Bez hasła**
6. **Wczytanie do Perun4V** → [P03](Karta_ryzyk_IDCC.md#P03)
7. **Dodatkowe pliki F320_CCA / Vertices_MAP_CCA** → patrz [R22](#R22)

## B. Skrót strzałkami

MinIO brak paczki → sprawdź CN2 ([R18](#R18)) → pobierz składowe z CCCt MV → zapisz lokalnie → 7-Zip → zip → [P03](Karta_ryzyk_IDCC.md#P03) Perun4V; dodatkowo [R22](#R22) F320_CCA/Vertices_MAP_CCA

---

<a id="R17"></a>
# R17 — Brak dostępu do MinIO dla raportu CCA

**Aplikacja:** MinIO ([N04](Inwentarz_IDCC.md#N04)), CCA ([N09](Inwentarz_IDCC.md#N09))
**Źródło:** BUP DA §Ryzyko 25 (str. 67)
**U-kod:** [U04](Karta_ryzyk_IDCC.md#U04), [U23](Karta_ryzyk_IDCC.md#U23) | **Stary kod:** MinIO-R03
**Wpływ na IDCC:** raport CCA w `cca/ID_FBCC/out/[BD]/` niedostępny → brak weryfikacji analizy IVA na CNECach.

## A. Procedura szczegółowa

1. **Sprawdź [R15](#R15)** (czy to ogólna awaria MinIO czy tylko bucket CCA)
2. **Alternatywne pobranie raportu CCA** ze skrzynki **kdm6@pse.pl**:
   - 📷 *BUP DA Rys. 98 — Raport CCA wiadomość mailowa, str. 67*
   - CCA wysyła raport również mailem
3. **Zapisanie raportu lokalnie**
4. **Zgłoszenie:**
   - **Zgłoś** — niski priorytet (raporty mają charakter informacyjny)

## B. Skrót strzałkami

MinIO bucket CCA niedostępny → pobierz raport z kdm6@pse.pl (CCA wysyła mailem) → zapisz lokalnie → zgłoś (niski priorytet)

---

<a id="R18"></a>
# R18 — Awaria Connector 2.0

**Aplikacja:** Connector 2.0 ([N05](Inwentarz_IDCC.md#N05))
**Źródło:** HTML §9 R09 + R16, BUP DA §Ryzyko 2 (str. 17)
**U-kod:** [U03](Karta_ryzyk_IDCC.md#U03) | **Stary kod:** CN2-R01
**Wpływ na IDCC:** wszystkie wysyłki automatyczne wstrzymane; konieczne ręczne wysyłki przez Manual Upload.

## A. Procedura szczegółowa

1. **Diagnoza:**
   - HTML §8.9 — Connector 2.0 narzędzie diagnostyczne
   - Sprawdź czy procesy CN2 się zakończyły
   - Logi błędów
2. **Identyfikacja zakresu awarii:**

| Stan plików | Diagnoza | Działanie |
|---|---|---|
| Plik w źródle, brak w CCM | Pełna awaria CN2 | [P02](Karta_ryzyk_IDCC.md#P02) / [P04](Karta_ryzyk_IDCC.md#P04) → [P01](Karta_ryzyk_IDCC.md#P01) |
| Plik na MinIO `perun/`, brak w `cca/` | Selektywna — kopia do CCA zerwana | [R19](#R19); zgłoś |
| Brak ACK po wysłaniu | CN2 zwrotny zerwany | [R06](#R06) timeout |

3. **Ręczne wysyłki per plik:**
   - **AC FIDx-831:** [P02 — pobranie z ZP](Karta_ryzyk_IDCC.md#P02) → [P01](Karta_ryzyk_IDCC.md#P01)
   - **IVA FIDx-710:** [P04 — pobranie z MinIO](Karta_ryzyk_IDCC.md#P04) → [P01](Karta_ryzyk_IDCC.md#P01) lub Perun4V GUI download
   - **Składowe paczek:** [P05 — pobranie z CCCt MV](Karta_ryzyk_IDCC.md#P05) → CCM Wyślij
4. **Zgłoszenie:**
   - **Zgłoś** (CIZ, WPO, PSE-I — patrz nagłówek dokumentu)

## B. Skrót strzałkami

CN2 awaria → identyfikuj zakres (pełna/selektywna) → per plik ([P02](Karta_ryzyk_IDCC.md#P02) AC / [P04](Karta_ryzyk_IDCC.md#P04) IVA / [P05](Karta_ryzyk_IDCC.md#P05) składowe) → [P01](Karta_ryzyk_IDCC.md#P01) Manual Upload → zgłoś

---

<a id="R19"></a>
# R19 — CN2 nie kopiuje IVA i raportów do bucketów CCA

**Aplikacja:** Connector 2.0 ([N05](Inwentarz_IDCC.md#N05)), CCA ([N09](Inwentarz_IDCC.md#N09))
**Źródło:** HTML §9 R16, BUP DA §Ryzyko 10 (str. 46)
**U-kod:** [U03](Karta_ryzyk_IDCC.md#U03), [U19](Karta_ryzyk_IDCC.md#U19) | **Stary kod:** CN2-R02
**Wpływ na IDCC:** CN2 selektywnie nie kopiuje IVA do `cca/`. CCA nie otrzymała pliku → brak IVA BACKUP, brak raportów. Kafelek IVA Backup czarny/szary.

## A. Procedura szczegółowa

1. **Identyfikacja zakresu:**
   - MinIO `perun/ID_FBCC/out/yyyy-mm-dd/` — jest IVA?
   - MinIO `cca/ID_FBCC/in/yyyymmdd/` — jest IVA?
2. **Decyzja:**

| Sytuacja | Zgłoszenie |
|---|---|
| Plik w `perun/`, brak w `cca/` | **Zgłoś** |
| Brak w obu | **Zgłoś** |

3. **Tymczasowe rozwiązanie:**
   - Pobierz IVA z `perun/` → ręcznie skopiuj/wgraj do `cca/` *(❓ czy dozwolone — do weryfikacji)*
   - Alternatywnie: wyślij IVA ręcznie przez CCM jako Backup
4. **Zgłoszenie pilne** — wpływa na IVA BACKUP i [R23](#R23).

## B. Skrót strzałkami

Sprawdź MinIO `perun/` vs `cca/` → plik w `perun/` brak w `cca/` = zgłoś; brak w obu = zgłoś → tymczasowo ręczne kopiowanie *(❓)*

---

<a id="R20"></a>
# R20 — Brak dostępu do ZP / brak wersji FIDx-831

**Aplikacja:** ZP ([N06](Inwentarz_IDCC.md#N06))
**Źródło:** AC manuall ZP.docx (procedura ZP); nie ma odpowiednika w BUP DA (DA używa CCCt jako źródła F118)
**U-kod:** [U06](Karta_ryzyk_IDCC.md#U06) | **Stary kod:** ZP-R01
**Wpływ na IDCC:** brak źródła pliku AC FIDx-831 dla iteracji. Bez ZP nie można wykonać [P02](Karta_ryzyk_IDCC.md#P02).

## A. Procedura szczegółowa

1. **Diagnoza ZP:**
   - Otwórz aplikację ZP (desktop)
   - Sprawdź czy startuje, czy logowanie działa
2. **Sprawdzenie wersji:**
   - ZP → Główne okno → **`bilans AC`**
   - Wyszukaj FIDx-831 dla bieżącej doby handlowej
3. **Decyzja:**

| Stan w ZP | Działanie |
|---|---|
| Wersja jest wygenerowana | Kliknij **`Pobierz XML`** → [P01](Karta_ryzyk_IDCC.md#P01) |
| Brak wersji | Wygeneruj: `bilans AC` → wybierz wersję → niebieski przycisk **`Nowa wersja`** → po wygenerowaniu Pobierz XML |
| Awaria ZP / nie startuje | Zgłoś |

4. **Generowanie się nie powiodło:**
   - Zgłoś
   - Ryzyko niedostarczenia AC w terminie

## B. Skrót strzałkami

ZP → bilans AC → wyszukaj FIDx-831 → [wersja jest: Pobierz XML → [P01](Karta_ryzyk_IDCC.md#P01)] / [brak wersji: `Nowa wersja` → Pobierz XML] / [awaria: zgłoś]

---

<a id="R21"></a>
# R21 — Brak generowania IGM/GLSK/CBCORA (Kreator)

**Aplikacja:** KreatorDACF&2DAF_CGMES ([N07](Inwentarz_IDCC.md#N07)) dla IDCC(b); KreatorIDCF_CGMES ([N08](Inwentarz_IDCC.md#N08)) dla IDCC(c)/(d)/(e)
**Źródło:** dla IDCC(c)/(d)/(e) — [Procedura ręczna: Generowanie GLSK + CBCORA w KreatorIDCF (ze screenami)](Procedura_KreatorIDCF_GLSK_CBCORA.html); dla IDCC(b) analogia BUP DA — KreatorDACF&2DAF_CGMES (NOR DA §1.3)
**U-kod:** [U06](Karta_ryzyk_IDCC.md#U06) | **Stary kod:** Kreator-R01
**Normalnie vs backup:** GLSK/CBCORA są wysyłane **automatycznie skryptem Monitora** (np. 00:05 v2, 00:50 v3); ręczna generacja w KreatorIDCF (GSK/CBCORA → Publikuj Connector) to **procedura backupowa** uruchamiana, gdy Monitor pokaże status BŁĄD.
**Wpływ na IDCC:** brak GLSK (FIDx-607) / CBCORA (FIDx-617) → niemożliwa konstrukcja paczki PERUN_IDx → brak obliczeń FBA.

## A. Procedura szczegółowa

1. **Diagnoza Kreatora:**
   - Sprawdź czy aplikacja Kreator (PLANS) startuje
   - Sprawdź czy generowanie pliku dla bieżącej doby działa
2. **Zgłoszenie:**
   - **PLANS** — zespół utrzymania Kreatora *(❓ kanał kontaktu — patrz TODO)*
3. **Alternatywne pobranie GLSK/CBCORA:**
   - **GLSK (FIDx-607):** z CCCt Message Viewer ([P05](Karta_ryzyk_IDCC.md#P05))
   - **CBCORA (FIDx-617):** z CCCt Message Viewer ([P05](Karta_ryzyk_IDCC.md#P05))
   - ⚠ FIDx-610 (Merged GLSK z CCCt) ≠ FIDx-607 (raw GLSK od PSE)
4. **Wysyłka:** CCM → PPM → Wyślij → [P06](Karta_ryzyk_IDCC.md#P06)

## B. Skrót strzałkami

Kreator nie generuje → PLANS (kontakt) → tymczasowo pobierz GLSK/CBCORA z CCCt MV ([P05](Karta_ryzyk_IDCC.md#P05)) → CCM Wyślij → [P06](Karta_ryzyk_IDCC.md#P06)

---

<a id="R22"></a>
# R22 — Brak F320_CCA / Vertices_MAP_CCA

**Aplikacja:** CCA ([N09](Inwentarz_IDCC.md#N09))
**Źródło:** BUP DA §Ryzyko 14 (str. 50)
**U-kod:** [U06](Karta_ryzyk_IDCC.md#U06), [U08](Karta_ryzyk_IDCC.md#U08) | **Stary kod:** CCA-R01
**Wpływ na IDCC:** brak F320_CCA (Vertices of Initial FB Domain) lub Vertices_MAP_CCA → paczka PERUN_IDx niekompletna → brak obliczeń FBA.

## A. Procedura szczegółowa

1. **Diagnoza:**
   - MinIO `cca/ID_FBCC/in/` — czy CCA wygenerowała pliki F320 i Vertices_MAP
2. **Ręczne generowanie narzędziem `fbc_lta_vertices.exe`** (analogicznie do BUP DA):
   - Lokalizacja: pulpit komputera dyspozytorskiego, katalog `F320_backup`
   - 📷 *BUP DA Rys. 67 — fbc_lta_vertices folder*
   - Pobierz z CCCt MV: F110, F114 LTA, F118 AC, F320, F330 — patrz [R16](#R16) lista plików
   - Uruchom `fbc_lta_vertices.exe` → wskaż pobrane pliki → wygeneruj F320_CCA i Vertices_MAP_CCA
3. **Dodaj wygenerowane pliki do paczki PERUN_IDx** → [R16](#R16) i [P03](Karta_ryzyk_IDCC.md#P03)
4. **Zgłoszenie:**
   - **Zgłoś** (CIZ, WPO, PSE-I — patrz nagłówek dokumentu)

## B. Skrót strzałkami

MinIO `cca/.../in/` brak F320/Vertices_MAP → fbc_lta_vertices.exe → pobierz pliki z CCCt MV → wygeneruj F320_CCA + Vertices_MAP_CCA → dodaj do paczki ([R16](#R16) + [P03](Karta_ryzyk_IDCC.md#P03)) → zgłoś

---

<a id="R23"></a>
# R23 — Brak dostępnego raportu CCA

**Aplikacja:** CCA ([N09](Inwentarz_IDCC.md#N09))
**Źródło:** HTML §9 R20, BUP DA §Ryzyko 26 (str. 69)
**U-kod:** [U23](Karta_ryzyk_IDCC.md#U23) | **Stary kod:** CCA-R02
**Wpływ na IDCC:** raport CCA nie został wygenerowany lub niedostępny → brak IVA BACKUP, brak analizy IVA na CNECach.

## A. Procedura szczegółowa

1. **Sprawdzenie statusu CCA:**
   - CCM → wiersz IVA Backup → kafelek MinIO
2. **Sprawdzenie MinIO ręcznie:**
   - Bucket: `cca/ID_FBCC/out/[BD]/`
   - 📷 *BUP DA Rys. 21 (NOR DA — Otrzymanie raportu CCA)*
3. **Sprawdzenie kdm6@pse.pl:**
   - CCA wysyła raport również mailem → patrz [R17](#R17)
4. **Diagnoza przyczyny:**
   - Plik w `cca/` istnieje ale CCM nie widzi → [R19](#R19) (CN2 zwrotny)
   - Plik nie istnieje mimo poprawnego zakończenia procesu CCA → **zgłoś**
   - Status procesu CCA nieukończony → zgłoś
5. **Wpis A.4** — [P06](Karta_ryzyk_IDCC.md#P06)

## B. Skrót strzałkami

CCM IVA Backup brak → MinIO `cca/ID_FBCC/out/[BD]/` ręcznie → kdm6 (email) → plik w `cca/` brak w CCM = [R19](#R19); brak w `cca/` = zgłoś → [P06](Karta_ryzyk_IDCC.md#P06)

---

<a id="R24"></a>
# R24 — Niezgodność logiki IVA BACKUP z Perun4V

**Aplikacja:** CCA ([N09](Inwentarz_IDCC.md#N09))
**Źródło:** HTML §9 R12
**U-kod:** [U19](Karta_ryzyk_IDCC.md#U19) | **Stary kod:** CCA-R03
**Wpływ na IDCC:** wersja IVA BACKUP (z CCA) i wersja IVA (FIDx-710, Perun4V) nie zgadzają się. Prawidłowo: Backup > IVA. Stan kafelka: `red_pulse` lub Backup z wersją nieprawidłową.

## A. Procedura szczegółowa

1. **Porównanie wersji w CCM:**
   - Wiersz IVA — wersja
   - Wiersz IVA Backup — wersja
   - Prawidłowo: Backup > IVA
2. **Weryfikacja w Perun4V:**
   - Status obliczeń (Successful/ERR-I/Process failed)
   - Wersja FIDx-710 w Perun4V
3. **Weryfikacja w MinIO:**
   - `cca/ID_FBCC/out/BD/` → raport CCA z wersją Backup
4. **Stan `red_pulse`** (zielony z pulsującą czerwoną obwódką):
   - Scenariusz 4 HTML §8.8 — nowa wersja IVA Backup wymaga monitoringu
   - 📷 *HTML §8.8 Scenariusz 4*
   - ⚠ **NIE uruchamiać ręcznej wysyłki IVA BACKUP** w standardowym modelu IDCC (HTML §5.3)
5. **Niezgodność wersji:**
   - **Zgłoś + telefon CCC** — niezwłocznie
   - ❌ **Nie zastępować automatyki ręcznym menu** (HTML §9 R12)

## B. Skrót strzałkami

Porównaj wersje: CCM IVA vs IVA Backup, Perun4V FIDx-710, MinIO `cca/` raport → red_pulse = Scenariusz 4 monitoring → niezgodność = zgłoś + telefon CCC niezwłocznie; ⛔ nie zastępować automatyki ręcznie

---

<a id="R25"></a>
# R25 — Brak dostępu do poczty kdm6

**Aplikacja:** kdm6@pse.pl ([N11](Inwentarz_IDCC.md#N11))
**Źródło:** BUP DA §Ryzyko 25 (str. 67) pośrednio
**U-kod:** [U07](Karta_ryzyk_IDCC.md#U07) | **Stary kod:** kdm6-R01
**Wpływ na IDCC:** brak weryfikacji raportów CCA (IVA na CNECach), brak informacji o liczbie policzonych godzin w Perun4V.

## A. Procedura szczegółowa

1. **Diagnoza:**
   - Outlook nie ładuje skrzynki kdm6
   - Brak nowych wiadomości mimo upływu czasu
2. **Alternatywne źródła:**
   - **Raporty CCA** → MinIO `cca/ID_FBCC/out/[BD]/` ([R17](#R17))
   - **Raporty Perun4V** → Perun4V GUI bezpośrednio
3. **Zgłoszenie:**
   - **Zgłoś**

## B. Skrót strzałkami

kdm6 niedostępne → raporty z MinIO `cca/ID_FBCC/out/[BD]/` lub Perun4V GUI bezpośrednio → zgłoś

---

<a id="R26"></a>
# R26 — Brak działania sFTP (uniwersalne)

**Aplikacja:** sFTP@pse.pl ([N12](Inwentarz_IDCC.md#N12))
**Źródło:** HTML §9 R01 (pośrednio), BUP DA §Ryzyko 1 (str. 9)
**U-kod:** [U03](Karta_ryzyk_IDCC.md#U03) | **Stary kod:** sFTP-R01
**Wpływ na IDCC:** brak transportu paczek ZIP z MinIO do Perun4V; lub brak wyników IVA z powrotem.

## A. Procedura szczegółowa

1. **Diagnoza:**
   - patrz [R08](#R08) (sFTP jest częścią ścieżki Connector 2.0 → MinIO → Perun4V)
2. **Ręczne wczytanie paczki do Perun4V:**
   - [P03 — Ręczne uruchomienie obliczeń](Karta_ryzyk_IDCC.md#P03)
3. **Zgłoszenie:**
   - **Zgłoś**

## B. Skrót strzałkami

sFTP brak działania → patrz [R08](#R08) → [P03](Karta_ryzyk_IDCC.md#P03) ręczne uruchomienie Perun4V → zgłoś

---

<a id="R27"></a>
# R27 — Decoupling SDAC — konieczność MD250

**Aplikacja:** ECP/EDX ([N16](Inwentarz_IDCC.md#N16))
**Źródło:** HTML §9 R14
**U-kod:** [U21](Karta_ryzyk_IDCC.md#U21) | **Stary kod:** ECP-R01
**Dotyczy:** FID1-250 (MD250 Shadow Auction Results)
**Wpływ na IDCC:** w przypadku Decoupling SDAC IDCC(a) wymaga dostarczenia MD250.

## A. Procedura szczegółowa

1. **Identyfikacja sytuacji:**
   - Komunikat o Decoupling SDAC (od CCC/SDAC)
   - Kafelek FID1-250 wymaga aktywnego monitoringu
2. **Dostarczenie MD250:**
   - Plik Shadow Auction Results → CCCt przez **ECP/EDX**
   - Deadliny:
     - **Deadline 1:** TET MCR (~15:43)
     - **Deadline 2:** ~17:24
3. **Potwierdzenie do CCC** mailowo
4. **Zgłoszenie przy opóźnieniu:**
   - **Zgłoś + telefon CCC**

## B. Skrót strzałkami

Decoupling SDAC → MD250 do CCCt przez ECP/EDX (Deadline 1: 15:43; Deadline 2: 17:24) → potwierdzenie mailem CCC → opóźnienie = zgłoś + telefon CCC

---

<a id="R28"></a>
# R28 — AAC Fallback (IDCC(a) nie dostarczył AACs)

**Aplikacja:** XBID ([N17](Inwentarz_IDCC.md#N17))
**Źródło:** HTML §9 R13
**U-kod:** [U20](Karta_ryzyk_IDCC.md#U20) | **Stary kod:** XBID-R01
**Wpływ na IDCC:** kolejne iteracje IDCC(b)/(c)/(d) wstrzymane (brak AAC dla XBID).

## A. Procedura szczegółowa

1. **Identyfikacja sytuacji:**
   - IDCC(a) nie wygenerował AACs (ID1-373-XX) na czas
2. **Dostarczenie computed AACs do XBID** przez narzędzie lokalne *(❓ jakie narzędzie konkretnie — do weryfikacji)*
3. **Deadliny:**

| Iteracja | Deadline AAC |
|---|---|
| IDCC(b) | **20:00 D-1** |
| IDCC(c) | **02:00 D** |
| IDCC(d) | **07:00 D** |

4. **Potwierdzenie do CCC** mailowo
5. **Zgłoszenie:**
   - **Zgłoś + telefon CCC**

## B. Skrót strzałkami

IDCC(a) brak AAC → dostarcz computed AACs do XBID przez narzędzie lokalne (deadliny per iteracja: b 20:00 D-1 / c 02:00 D / d 07:00 D) → potwierdzenie mailem CCC → zgłoś

---

<a id="R29"></a>
# R29 — Late NTC delivery po IDA2

**Aplikacja:** XBID ([N17](Inwentarz_IDCC.md#N17)), Core CC Tool ([N02](Inwentarz_IDCC.md#N02))
**Źródło:** HTML §9 R15
**U-kod:** [U22](Karta_ryzyk_IDCC.md#U22) | **Stary kod:** XBID-R02
**Dotyczy:** FIDx-921 (Final Intraday NTC)
**Wpływ na IDCC:** IDCC(b) wstrzymany do 22:30; brak NTC do XBID przed aukcją IDA2.

## A. Procedura szczegółowa

1. **Identyfikacja sytuacji:**
   - NTC nie dostarczono do XBID przed **21:53 D-1**
   - Checkpoint przed startem aukcji IDA2 nieosiągnięty
   - Proces IDCC(b) wstrzymany automatycznie
2. **Monitorowanie wznowienia:**
   - Po IDA2 → automatyczne wznowienie
   - Deadline publikacji NTC: **22:30**
   - CCM kafelek FIDx-921 — monitoring
3. **Brak wznowienia / publikacji NTC przed 22:30:**
   - **Zgłoś + telefon CCC**
4. **Wpis A.4** — [P06](Karta_ryzyk_IDCC.md#P06)

## B. Skrót strzałkami

NTC brak do 21:53 D-1 → IDCC(b) wstrzymane → automatyczne wznowienie po IDA2 → monitoruj NTC przed 22:30 → brak = zgłoś + telefon CCC

---

# Podsumowanie

| Grupa | Liczba ryzyk | Źródła |
|---|---|---|
| I — CCM | 2 (R01-R02) | HTML R06 + BUP #27, #28 |
| II — CCCt | 5 (R03-R07) | HTML R05, R07, R09, R11 + BUP #11, #12, #13 |
| III — Perun4V | 7 (R08-R14) | HTML R01, R02, R03 + BUP #1, #4-#9 |
| IV — MinIO | 3 (R15-R17) | BUP #2, #3, #25 |
| V — Connector 2.0 | 2 (R18-R19) | HTML R09, R16 + BUP #2, #10 |
| VI — Aplikacje wewnętrzne | 5 (R20-R24) | HTML R12, R20 + BUP #14, #26; nowe: ZP, Kreator |
| VII — Pomocnicze | 2 (R25-R26) | BUP #25, #1 |
| VIII — Zgłoszenie zewn. | 3 (R27-R29) | HTML R13, R14, R15 |

| **Razem** | **29** | — |

**Pominięte (LTA-specific z BUP DA):** Ryzyka #15-24, #29 — IDCC nie ma LTA.

**Sposób wykorzystania:**
- **Forma A (rozbudowana ze screenami)** — dla pełnego onboardingu Dyspozytora i instrukcji szkoleniowych
- **Forma B (skrót strzałkami)** — gotowy wkład do opisów stanów kafelków per FID (np. w `Przyklady_FID1-831.md`)
