# Ryzyka per aplikacja — IDCC

> **Cel:** Agregacja wszystkich możliwych ryzyk pogrupowanych wg aplikacji/narzędzia, którego dotyczą. Najpierw ryzyka z HTML procedura IDCC (§9), potem z BUP DA (DA #1-14 + #25-28; LTA #15-24, #29 **pominięte** — IDCC nie ma LTA).
>
> Każde ryzyko ma:
> - **Nowy kod** w schemacie `<Aplikacja>-R<NN>` (np. CCM-R01, CCCt-R02, Perun-R03)
> - **Źródło:** HTML §9 (R-kod) i/lub BUP DA (#numer + strona)
> - **Powiązanie z U-kodem** z [Karta_ryzyk_IDCC.md](Karta_ryzyk_IDCC.md) dla spójności
> - **Powiązanie z narzędziem** z [Inwentarz_IDCC.md](Inwentarz_IDCC.md) (N-kod)
> - **Opis + reakcja**

> ⚠ **Każde ryzyko należy zgłosić do: CIZ, WPO, PSE-I (PSE Innowacje).**

**Źródła:**
- HTML procedura IDCC §9 *(R01–R20; R08, R10, R17-R19 — luki, patrz [TODO Inwentarza](Inwentarz_IDCC.md#todo))*
- FBA_TSO_BUP_03 (BUP DA) §2.2 — Ryzyka #1–#14, #25–#28 *(LTA #15-24, #29 pominięte)*

---

## Spis treści

1. [CCM (N01)](#ccm) — 2 ryzyka
2. [Core CC Tool / CCCt (N02)](#ccct) — 6 ryzyk
3. [Perun4V (N03)](#perun) — 8 ryzyk
4. [MinIO (N04)](#minio) — 3 ryzyka
5. [Connector 2.0 (N05)](#cn2) — 2 ryzyka
6. [ZP (N06)](#zp) — 1 ryzyko
7. [Kreatory IGM (N07/N08)](#kreator) — 1 ryzyko
8. [CCA (N09)](#cca) — 4 ryzyka
9. [kdm6 (N11)](#kdm6) — 1 ryzyko
10. [sFTP (N12)](#sftp) — 1 ryzyko
11. [ECP/EDX (N16)](#ecp) — 1 ryzyko
12. [XBID (N17)](#xbid) — 2 ryzyka

**Razem: 32 ryzyka** zagregowane z 15 ryzyk HTML §9 (R01-R20 minus R08/R10/R17-R19) + 18 ryzyk BUP DA (#1–#14, #25–#28).

**Luki do dopytania:** R08, R10, R17, R18, R19 — patrz [TODO Inwentarza](Inwentarz_IDCC.md#todo).

---

<a id="ccm"></a>
# 1. CCM (Capacity Calculation Monitoring) — [N01](Inwentarz_IDCC.md#N01)

### CCM-R01 — Brak dostępu do CCM
- **HTML §9:** R06
- **BUP DA:** Ryzyko 27 (str. 69)
- **U-kod:** [U01](Karta_ryzyk_IDCC.md#U01)
- **Opis:** Strona https://ccm.spsm.pse.pl nie ładuje się lub błąd logowania. Sesja CCM wygasła i ponowne logowanie zwraca błąd. Pulpit zawiesza się / nie odświeża >5 min.
- **Wpływ na IDCC:** brak monitoringu statusów kafelków; brak ręcznej wysyłki przez PPM → Wyślij; brak funkcji „Informacje".
- **Reakcja:** sieć/VPN PSE; inna przeglądarka; **zgłoś**. Tymczasowo: monitoring bezpośrednio w CCCt MV ([N02](Inwentarz_IDCC.md#N02)), MinIO GUI ([N04](Inwentarz_IDCC.md#N04)), Perun4V ([N03](Inwentarz_IDCC.md#N03)). Wysyłka przez [P01 Manual Upload](Karta_ryzyk_IDCC.md#P01).

### CCM-R02 — Błędna paczka do Perun4V (weryfikacja w CCM)
- **HTML §9:** R04 (pośrednio)
- **BUP DA:** Ryzyko 28 (str. 69)
- **U-kod:** [U08](Karta_ryzyk_IDCC.md#U08), [U09](Karta_ryzyk_IDCC.md#U09)
- **Opis:** CCM pokazuje, że paczka ZIP ma błędne składowe (czerwony !, czarny lub czerwony na składowej). Agregat PERUN_IDx nie może zostać wysłany.
- **Wpływ na IDCC:** paczka nie trafi do Perun4V → brak obliczeń IVA dla danej iteracji.
- **Reakcja:** rozwiń agregat → zidentyfikuj problematyczną składową → LPM → Informacje → pobierz z CCCt Message Viewer lub MinIO ([P05](Karta_ryzyk_IDCC.md#P05)) → CCM PPM → Wyślij.

---

<a id="ccct"></a>
# 2. Core CC Tool (CCCt) — [N02](Inwentarz_IDCC.md#N02)

### CCCt-R01 — Brak dostępu do Core CC Tool
- **HTML §9:** R07
- **BUP DA:** Ryzyko 11 (str. 47)
- **U-kod:** [U02](Karta_ryzyk_IDCC.md#U02)
- **Opis:** brak możliwości zalogowania / korzystania z CCCt. Message Viewer i Manual Upload niedostępne.
- **Wpływ na IDCC:** brak weryfikacji ACK, brak [P01 Manual Upload](Karta_ryzyk_IDCC.md#P01), brak publikacji AC do PuTo.
- **Reakcja:** monitoruj nadal w CCM; sprawdź kdm6@pse.pl; telefon do CCC ([N13](Inwentarz_IDCC.md#N13)); alternatywny kanał TYLKO po uzgodnieniu z CCC; **zgłoś**.

### CCCt-R02 — Brak dostarczonego pliku do CCCt
- **HTML §9:** R04 (pośrednio), R09
- **BUP DA:** Ryzyko 12 (str. 48)
- **U-kod:** [U08](Karta_ryzyk_IDCC.md#U08), [U11](Karta_ryzyk_IDCC.md#U11)
- **Opis:** plik nie pojawił się w CCCt — brak wpisu w Message Viewer mimo upływu czasu wysyłki.
- **Wpływ na IDCC:** proces nie kontynuuje (brak FID-831/710/928 do CCCt); brak publikacji do PuTo.
- **Reakcja:** sprawdź w CCCt MV (selektor procesu → `ID1/ID2/ID3C/ID3` → Message Definition); jeśli brak wpisu → diagnostyka transportu ([CN2-R01](#CN2-R01)); pobranie ze źródła ([P02 ZP](Karta_ryzyk_IDCC.md#P02) / [P04 MinIO](Karta_ryzyk_IDCC.md#P04)) → [P01 Manual Upload](Karta_ryzyk_IDCC.md#P01).

### CCCt-R03 — Plik odrzucony przez CCCt (ACK negatywny)
- **HTML §9:** R05
- **BUP DA:** Ryzyko 13 (str. 49)
- **U-kod:** [U10](Karta_ryzyk_IDCC.md#U10), [U12](Karta_ryzyk_IDCC.md#U12)
- **Opis:** plik dotarł do CCCt, ale ACK negatywny z kodem 20/21/22/30 lub „Błąd procesu".
- **Wpływ na IDCC:** plik nie został przyjęty — proces zatrzymany; konieczne ponowienie z poprawionym plikiem / wyższą wersją.
- **Reakcja:** najedź na status → odczytaj kod ACK:
  - **20 gateClosed** → admin CCCt + **zgłoś**; sprawdź proces `IDx-AC-FORWARDING`
  - **21 duplicatedVersion** → podbić wersję; [P02](Karta_ryzyk_IDCC.md#P02) → [P01](Karta_ryzyk_IDCC.md#P01)
  - **22 Negative constraint** → ❌ nieaktualne (CCCt akceptuje wartości ujemne)
  - **30 file size mismatch** → [P04 MinIO](Karta_ryzyk_IDCC.md#P04) / [P02 ZP](Karta_ryzyk_IDCC.md#P02) z poprawnym plikiem → [P01](Karta_ryzyk_IDCC.md#P01)
  - **Błąd procesu** → **zgłoś**
  - **Inne** → [Tabela kodów ACK w Inwentarzu](Inwentarz_IDCC.md#risks)

### CCCt-R04 — Brak ACK / timeout
- **HTML §9:** R05 (zawężenie)
- **BUP DA:** Ryzyko 12 (str. 48)
- **U-kod:** [U11](Karta_ryzyk_IDCC.md#U11)
- **Opis:** plik wysłany do CCCt (CCTool wyśl. zielony), ale ACK nie napłynął w przewidywanym czasie (typowo 2-3 min). Kafelek: czerwony `?`.
- **Wpływ na IDCC:** niepewność statusu; ryzyko duplikatu (kod 21) jeśli Dyspozytor ponawia bez weryfikacji.
- **Reakcja:** najedź na `?` → odczytaj czas oczekiwania. CCCt MV → filtr po kodzie przepływu → status (`Processed` = CCM nie odświeżył; `Rejected` = patrz [CCCt-R03](#CCCt-R03); brak wpisu = patrz [CCCt-R02](#CCCt-R02)). **NIE wysyłać ponownie bez weryfikacji.**

### CCCt-R05 — Konieczność ręcznego uploadu FBA
- **HTML §9:** R09 *(traktowany jako procedura, nie ryzyko)*
- **BUP DA:** Ryzyko 11-13 (str. 47-49)
- **U-kod:** patrz [P01](Karta_ryzyk_IDCC.md#P01) (procedura)
- **Opis:** sytuacja w której ręczny upload przez GUI CCCt staje się konieczny — typowo w odpowiedzi na CCM-R01, CN2-R01, CCCt-R02/R03/R04, MinIO-R01.
- **Wpływ na IDCC:** wymaga ręcznej interwencji Dyspozytora.
- **Reakcja:** [P01 — GUI CCCt Manual Upload](Karta_ryzyk_IDCC.md#P01); wpis [P06](Karta_ryzyk_IDCC.md#P06).

### CCCt-R06 — Niezakończenie walidacji ATC w czasie
- **HTML §9:** R11
- **BUP DA:** —
- **U-kod:** [U17](Karta_ryzyk_IDCC.md#U17)
- **Opis:** walidacja ATC nie zakończyła się przed CET dla kafelka FIDx-928. Kafelek czarny po CET.
- **Wpływ na IDCC:** **brak lokalnego fallbacku** (HTML §5.4). Po CET dyspozytor nie wykonuje dalszych czynności.
- **Reakcja:**
  - **PRZED CET:** uzupełnij brakujące składowe paczki ATC (PERUN_IDx_ATC) w CCM ([P05](Karta_ryzyk_IDCC.md#P05))
  - **PO CET:** **STOP** — żadnych działań ręcznych; **zgłoś** + telefon CCC

---

<a id="perun"></a>
# 3. Perun4V — [N03](Inwentarz_IDCC.md#N03)

### Perun-R01 — Brak działania sFTP (transport paczki do Perun4V)
- **HTML §9:** R01 (pośrednio — brak uruchomienia FBA)
- **BUP DA:** Ryzyko 1 (str. 9), podpunkty:
  - 1.1 pobranie paczki
  - 1.2 wczytanie danych do Peruna
  - 1.3 uruchomienie obliczeń
  - 1.4 pobranie pliku wynikowego
  - 1.5 dostarczenie wyników do MinIO i CCCt
- **U-kod:** [U03](Karta_ryzyk_IDCC.md#U03) (sFTP jako część transportu), [U14](Karta_ryzyk_IDCC.md#U14)
- **Opis:** sFTP nie transportuje paczki ZIP do Perun4V. Obliczenia nie startują automatycznie.
- **Wpływ na IDCC:** paczka PERUN_IDx wysłana z CCM (sFTP/ZP zielony), ale Perun4V nie rozpoczął obliczeń.
- **Reakcja:** w Perun4V GUI sprawdź komunikat błędu:
  - **Błędny BD** → ustaw poprawny BD w „Select timestamp date"
  - **Brak pliku w paczce** → uzupełnij składową ([P05](Karta_ryzyk_IDCC.md#P05)) i ponów
  - **Błędny plik** → pobierz ręcznie z CCCt Message Viewer → spakuj → wczytaj
  - [P03 — Ręczne uruchomienie obliczeń](Karta_ryzyk_IDCC.md#P03)

### Perun-R02 — ERR-I (część TS niepoliczona)
- **HTML §9:** R02
- **BUP DA:** Ryzyko 6 (str. 29)
- **U-kod:** [U15](Karta_ryzyk_IDCC.md#U15)
- **Opis:** w Perun4V status `ERR-I` — przynajmniej jedna godzina (TimeSlice) niepoliczona. W kolumnie `Timestamps (Failed/Success/Running/Total)` widoczna liczba niepoliczonych.
- **Wpływ na IDCC:** publikacja **wyższej wersji IVA** = wyniki Perun4V + dane CCA dla brakujących TS.
- **Reakcja:** w Perun4V `Status → Details` → kolumna `[Result]` per godzina. Sprawdź w CCCt czy zastosowano DFP (Default Flow Parameters) / Spanning hours. Email z informacją na kdm6@pse.pl. Monitoruj [IVA BACKUP](Inwentarz_IDCC.md#U19) (wyższa wersja). Brak publikacji → **zgłoś** + telefon CCC.

### Perun-R03 — Process failed (wszystkie TS niepoliczone)
- **HTML §9:** R03
- **BUP DA:** Ryzyko 7 (str. 39)
- **U-kod:** [U16](Karta_ryzyk_IDCC.md#U16)
- **Opis:** w Perun4V status `Process failed`. Żadna godzina nie została policzona.
- **Wpływ na IDCC:** publikowana **IVA BACKUP v1** jako wynik wyłącznie z CCA.
- **Reakcja:** oczekuj IVA BACKUP v1 ([N09 CCA](Inwentarz_IDCC.md#N09)); brak publikacji → **zgłoś** + telefon CCC. ❌ **Zakaz fallbacku 20% Fmax z DA** (HTML §7).

### Perun-R04 — Brak dostępu do platformy Perun4V
- **HTML §9:** — *(brak osobnego R; potencjalnie R08 — patrz [TODO](Inwentarz_IDCC.md#todo))*
- **BUP DA:** Ryzyko 4 (str. 26)
- **U-kod:** [U05](Karta_ryzyk_IDCC.md#U05)
- **Opis:** brak możliwości zalogowania / korzystania z https://lccv.tscnet.eu.
- **Wpływ na IDCC:** brak monitoringu stanu obliczeń (Successful/ERR-I/Process failed); brak [P03 Ręczne uruchomienie](Karta_ryzyk_IDCC.md#P03).
- **Reakcja:** sprawdź TSCNET / sieć; inna przeglądarka. Tymczasowo: monitoring w CCM (statusy IVA/Raporty) i kdm6@pse.pl (raporty Perun po obliczeniach). Telefon do TSCNET (operator@tscnet.eu); **zgłoś**.

### Perun-R05 — Brak wyników IVA i raportów z sFTP
- **HTML §9:** R01 (pośrednio)
- **BUP DA:** Ryzyko 5 (str. 28)
- **U-kod:** [U03](Karta_ryzyk_IDCC.md#U03) (sFTP), [U14](Karta_ryzyk_IDCC.md#U14)
- **Opis:** Perun4V wykonał obliczenia, ale wyniki (IVA F310 + raporty) nie trafiły z powrotem przez sFTP do Connectora 2.0.
- **Wpływ na IDCC:** brak IVA w CCM/CCCt mimo obliczonego procesu.
- **Reakcja:** sprawdź sFTP; w Perun4V pobierz F310 ręcznie (download) → wyślij przez CCM/Manual Upload. **Zgłoś**.

### Perun-R06 — Brak możliwości pobrania pliku F310 z Perun4V
- **HTML §9:** —
- **BUP DA:** Ryzyko 8 (str. 39)
- **U-kod:** [U05](Karta_ryzyk_IDCC.md#U05), [U14](Karta_ryzyk_IDCC.md#U14)
- **Opis:** obliczenia w Perun4V zakończone, ale GUI nie pozwala pobrać wynikowego F310.
- **Wpływ na IDCC:** brak możliwości ręcznego dostarczenia wyniku.
- **Reakcja:** sprawdź [Perun-R04](#Perun-R04) (dostęp); spróbuj pobrać z MinIO ([MinIO-R02](#MinIO-R02) — `perun/ID_FBCC/out/yyyy-mm-dd/`); **zgłoś**.

### Perun-R07 — Dodanie wyłączenia awaryjnego w Perun4V
- **HTML §9:** —
- **BUP DA:** Ryzyko 9 (str. 44)
- **U-kod:** —
- **Opis:** konieczność dodania wyłączenia (outage) awaryjnego w Perun4V dla obliczeń.
- **Wpływ na IDCC:** specyficzne dla scenariuszy operacyjnych; rzadkie w IDCC.
- **Reakcja:** procedura w Perun4V GUI (Outage management); **zgłoś** przed wykonaniem.

### Perun-R08 — Błędna paczka do Perun4V / nieprawidłowe dane
- **HTML §9:** R04 (pośrednio)
- **BUP DA:** Ryzyko 28 (str. 69) *(częściowo Perun4V, częściowo CCM)*
- **U-kod:** [U08](Karta_ryzyk_IDCC.md#U08), [U09](Karta_ryzyk_IDCC.md#U09)
- **Opis:** paczka ZIP dotarła do Perun4V, ale obliczenia nie startują z powodu błędnej zawartości (brakujące pliki, błędna data, błędny format).
- **Wpływ na IDCC:** brak obliczeń mimo dostarczenia paczki.
- **Reakcja:** Perun4V GUI → komunikat błędu („brak pliku", „błędny BD", „błędny plik"); → [Perun-R01](#Perun-R01) i [CCM-R02](#CCM-R02).

---

<a id="minio"></a>
# 4. MinIO — [N04](Inwentarz_IDCC.md#N04)

### MinIO-R01 — Brak dostępu do MinIO / Awaria Connector 2.0 dotykająca MinIO
- **HTML §9:** R09 (pośrednio przez CN2)
- **BUP DA:** Ryzyko 2 (str. 17)
- **U-kod:** [U04](Karta_ryzyk_IDCC.md#U04)
- **Opis:** https://minio-gui.pse.pl niedostępne; funkcja „Pobierz" w CCM zwraca błąd; buckety `perun/`, `cca/`, `mam/` niedostępne.
- **Wpływ na IDCC:** brak pobierania backupowej kopii pliku; brak [P04](Karta_ryzyk_IDCC.md#P04); raporty CCA niedostępne → [CCA-R02](#CCA-R02).
- **Reakcja:** sieć/VPN PSE. Alternatywne źródła:
  - **AC FIDx-831** → [P02 ZP](Karta_ryzyk_IDCC.md#P02)
  - **IVA / wyniki Perun4V** → Perun4V GUI (download)
  - **Raporty CCA** → kdm6@pse.pl ([kdm6-R01](#kdm6-R01))
  - **Składowe paczek** → [P05 CCCt MV](Karta_ryzyk_IDCC.md#P05)
  
  **Zgłoś.**

### MinIO-R02 — Brak paczki plików na MinIO
- **HTML §9:** R04 (pośrednio)
- **BUP DA:** Ryzyko 3 (str. 22)
- **U-kod:** [U08](Karta_ryzyk_IDCC.md#U08)
- **Opis:** mimo dostarczenia składowych do CCM, paczka ZIP nie pojawia się w MinIO `perun/ID_FBCC/in/yyyy-mm-dd/`.
- **Wpływ na IDCC:** Perun4V nie otrzyma paczki → brak obliczeń.
- **Reakcja:** sprawdź CN2 ([CN2-R01](#CN2-R01)). Ręczne stworzenie paczki: pobierz składowe z CCCt Message Viewer → spakuj 7-Zip do `.zip` → ręcznie wczytaj do Perun4V ([P03](Karta_ryzyk_IDCC.md#P03)). Lokalizacja zapisu: `\\uo-data\ZUO\Pion_UOD\Wydzial_DP\MODELE\5_DYSP\FBA\Pliki wejściowe do ID FBA\rrrMMdd\PERUN\` *(❓ do weryfikacji ścieżki IDCC — patrz [TODO](Inwentarz_IDCC.md#todo))*.

### MinIO-R03 — Brak dostępu do MinIO dla raportu CCA
- **HTML §9:** —
- **BUP DA:** Ryzyko 25 (str. 67)
- **U-kod:** [U04](Karta_ryzyk_IDCC.md#U04), [U23](Karta_ryzyk_IDCC.md#U23)
- **Opis:** raport CCA w `cca/ID_FBCC/out/[BD]/` niedostępny z powodu awarii MinIO.
- **Wpływ na IDCC:** brak weryfikacji raportu CCA (analiza IVA na CNECach).
- **Reakcja:** pobierz raport ze skrzynki **kdm6@pse.pl** (CCA wysyła go również mailem); **zgłoś**.

---

<a id="cn2"></a>
# 5. Connector 2.0 (CN2) — [N05](Inwentarz_IDCC.md#N05)

### CN2-R01 — Brak działania / awaria Connector 2.0
- **HTML §9:** R09 + R16
- **BUP DA:** Ryzyko 2 (str. 17), Ryzyko 16 (LTA — pominięte)
- **U-kod:** [U03](Karta_ryzyk_IDCC.md#U03)
- **Opis:** Connector 2.0 nie transportuje plików między CCM ↔ CCCt ↔ MinIO ↔ Perun4V. Plik widoczny w źródle, ale nie pojawia się w docelowym narzędziu.
- **Wpływ na IDCC:** wszystkie wysyłki automatyczne wstrzymane; konieczne ręczne wysyłki.
- **Reakcja:** sprawdź procesy CN2 (HTML §8.9); logi błędów. **Dla AC FIDx-831:** [P02 ZP → P01 CCCt](Karta_ryzyk_IDCC.md#P02). **Dla IVA / paczek:** [P01](Karta_ryzyk_IDCC.md#P01) z plikiem z [P04 MinIO](Karta_ryzyk_IDCC.md#P04). **Zgłoś.**

### CN2-R02 — Connector 2.0 nie kopiuje IVA i raportów do bucketów CCA
- **HTML §9:** R16
- **BUP DA:** Ryzyko 10 (str. 46)
- **U-kod:** [U03](Karta_ryzyk_IDCC.md#U03) (scalone U18), [U19](Karta_ryzyk_IDCC.md#U19)
- **Opis:** transport CN2 działa selektywnie — plik w `perun/` jest, ale brak w `cca/`. CCA nie otrzymała IVA → brak IVA BACKUP.
- **Wpływ na IDCC:** brak IVA BACKUP w CCM (kafelek IVA Backup czarny lub szary mimo upływu czasu); CCA nie wygeneruje raportów.
- **Reakcja:** sprawdź MinIO ręcznie — w którym bucketcie plik jest. Pliki w `perun/`, brak w `cca/` → **zgłoś**. Brak w obu → **zgłoś**.

---

<a id="zp"></a>
# 6. ZP (zdolności przesyłowe) — [N06](Inwentarz_IDCC.md#N06)

### ZP-R01 — Brak dostępu do ZP / brak wersji pliku AC
- **HTML §9:** — *(brak; specyficzne dla IDCC)*
- **BUP DA:** — *(DA nie używa ZP — F118 pobierane bezpośrednio z CCCt)*
- **U-kod:** [U06](Karta_ryzyk_IDCC.md#U06)
- **Opis:** aplikacja ZP nie startuje / brak dostępu / brak wygenerowanej wersji FIDx-831 dla bieżącej doby.
- **Wpływ na IDCC:** brak źródła pliku AC dla iteracji IDCC; bez ZP nie ma backupowej kopii dla [P02](Karta_ryzyk_IDCC.md#P02).
- **Reakcja:**
  1. Sprawdź w ZP → bilans AC → FIDx-831 dla bieżącej doby
  2. **Brak wersji** → wygeneruj: `bilans AC` → wybierz wersję → niebieski przycisk **Nowa wersja** → po wygenerowaniu Pobierz XML
  3. **Awaria ZP** → **zgłoś**

---

<a id="kreator"></a>
# 7. Kreatory IGM — [N07](Inwentarz_IDCC.md#N07) / [N08](Inwentarz_IDCC.md#N08)

### Kreator-R01 — Brak generowania IGM / GLSK / CBCORA
- **HTML §9:** — *(brak)*
- **BUP DA:** — *(analogia: KreatorDACF&2DAF_CGMES dla DA, źródło CORE_FB_DA_RA_country.xlsx)*
- **U-kod:** [U06](Karta_ryzyk_IDCC.md#U06)
- **Opis:** Kreator nie generuje plików wejściowych:
  - **IDCC(b)** → [Kreator2DAF&DACF_CGMES (N07)](Inwentarz_IDCC.md#N07) → FID2-607 (GLSK), FID2-617 (CBCORA)
  - **IDCC(c)/(d)** → [KreatorIDCF_CGMES (N08)](Inwentarz_IDCC.md#N08) → FIDx-607, FIDx-617
- **Wpływ na IDCC:** brak GLSK/CBCORA → niemożliwa konstrukcja paczki PERUN_IDx → brak obliczeń FBA.
- **Reakcja:** zgłoszenie PLANS (zespół utrzymania Kreatora); alternatywne pobranie GLSK/CBCORA z CCCt Message Viewer ([P05](Karta_ryzyk_IDCC.md#P05)); **zgłoś**.

---

<a id="cca"></a>
# 8. CCA (Capacity Calculation Application) — [N09](Inwentarz_IDCC.md#N09)

### CCA-R01 — Brak przygotowanych danych F320_CCA / Vertices_MAP_CCA
- **HTML §9:** —
- **BUP DA:** Ryzyko 14 (str. 50)
- **U-kod:** [U06](Karta_ryzyk_IDCC.md#U06), [U08](Karta_ryzyk_IDCC.md#U08)
- **Opis:** CCA nie wygenerowała F320_CCA (Vertices of Initial FB Domain) lub Vertices_MAP_CCA — wejścia do paczki Perun4V.
- **Wpływ na IDCC:** paczka PERUN_IDx niekompletna → obliczenia FBA niemożliwe.
- **Reakcja:** sprawdź MinIO `cca/ID_FBCC/in/` → czy CCA wygenerowała pliki; brak → ręczne generowanie narzędziem `fbc_lta_vertices.exe` *(analogicznie do BUP DA)*; **zgłoś**.

### CCA-R02 — Brak dostępnego raportu CCA
- **HTML §9:** R20
- **BUP DA:** Ryzyko 26 (str. 69)
- **U-kod:** [U23](Karta_ryzyk_IDCC.md#U23)
- **Opis:** raport CCA nie został wygenerowany lub nie jest dostępny w MinIO `cca/ID_FBCC/out/[BD]/`.
- **Wpływ na IDCC:** brak IVA BACKUP, brak analizy IVA na CNECach.
- **Reakcja:** sprawdź status procesu CCA w CCM. Sprawdź bucket MinIO ręcznie. Brak w MinIO ale wiadomość mailowa → pobierz raport z kdm6@pse.pl ([kdm6-R01](#kdm6-R01)). Brak mimo poprawnego zakończenia procesu CCA → **zgłoś**.

### CCA-R03 — Niezgodność logiki IVA BACKUP z Perun4V
- **HTML §9:** R12
- **BUP DA:** —
- **U-kod:** [U19](Karta_ryzyk_IDCC.md#U19)
- **Opis:** wersja IVA BACKUP (z CCA) i wersja IVA (FIDx-710, z Perun4V) nie zgadzają się logicznie. Prawidłowo: Backup > IVA. Stan kafelka: `red_pulse` lub kafelek IVA Backup z wersją nieprawidłową.
- **Wpływ na IDCC:** niejasny stan publikacji; ryzyko niepoprawnych wyników FBA do XBID.
- **Reakcja:** porównaj wersje:
  - CCM: wiersz IVA vs IVA Backup
  - Perun4V: wersja FIDx-710
  - MinIO `cca/ID_FBCC/out/BD/` → raport CCA
  
  Niezgodność → **zgłoś** + telefon CCC niezwłocznie. ❌ **Nie zastępować automatyki ręcznym menu.**

### CCA-R04 — CN2 nie kopiuje IVA do bucketów CCA *(referencja krzyżowa)*
- Patrz [CN2-R02](#CN2-R02). Przyczyna w CN2, ale skutek dla CCA (brak IVA Backup) — **zgłoś**.

---

<a id="kdm6"></a>
# 9. kdm6@pse.pl — [N11](Inwentarz_IDCC.md#N11)

### kdm6-R01 — Brak dostępu do skrzynki kdm6 / brak raportów
- **HTML §9:** —
- **BUP DA:** Ryzyko 25 (str. 67) *(pośrednio)*, Ryzyko 26 (str. 69) *(brak raportu CCA mailem)*
- **U-kod:** [U07](Karta_ryzyk_IDCC.md#U07)
- **Opis:** Outlook nie ładuje skrzynki kdm6@pse.pl; brak nowych wiadomości od CCA / Perun4V mimo upływu czasu obliczeń.
- **Wpływ na IDCC:** brak weryfikacji raportów CCA (IVA na CNECach), brak informacji o liczbie policzonych godzin w Perun4V, brak alertów.
- **Reakcja:** sprawdź Outlook / połączenie sieciowe. Alternatywnie pobierz raporty z MinIO `cca/ID_FBCC/out/[BD]/` ([MinIO-R03](#MinIO-R03)). Sprawdź w Perun4V GUI status obliczeń bezpośrednio. **Zgłoś** (utrzymanie poczty PSE).

---

<a id="sftp"></a>
# 10. sFTP — [N12](Inwentarz_IDCC.md#N12)

### sFTP-R01 — Brak działania sFTP
- **HTML §9:** R01 (pośrednio)
- **BUP DA:** Ryzyko 1 (str. 9)
- **U-kod:** [U03](Karta_ryzyk_IDCC.md#U03) *(sFTP jako część transportu)*
- **Opis:** protokół sFTP nie transportuje paczek ZIP z MinIO do Perun4V; wyniki z Perun4V nie wracają przez sFTP.
- **Wpływ na IDCC:** brak obliczeń mimo dostarczenia paczki na MinIO; lub brak wyników IVA mimo zakończonych obliczeń.
- **Reakcja:** patrz [Perun-R01](#Perun-R01) — sFTP jest częścią ścieżki Connector 2.0 → MinIO → Perun4V. Ręczne wczytanie paczki do Perun4V przez GUI ([P03](Karta_ryzyk_IDCC.md#P03)). **Zgłoś.**

---

<a id="ecp"></a>
# 11. ECP/EDX — [N16](Inwentarz_IDCC.md#N16)

### ECP-R01 — Decoupling SDAC — konieczność MD250
- **HTML §9:** R14
- **BUP DA:** —
- **U-kod:** [U21](Karta_ryzyk_IDCC.md#U21)
- **Opis:** Decoupling SDAC — wymaga dostarczenia Shadow Auction Results (MD250) do CCCt przez ECP/EDX. Plik FID1-250 monitorowany w pulpicie IDCC(a).
- **Wpływ na IDCC:** specyficzne dla scenariusza decouplingu; bez MD250 IDCC(a) nie kontynuuje.
- **Reakcja:** dostarcz MD250 przez ECP/EDX. Deadliny:
  - **Deadline 1:** TET MCR (~15:43)
  - **Deadline 2:** ~17:24
  
  Telefon CCC; **zgłoś**.

---

<a id="xbid"></a>
# 12. XBID — [N17](Inwentarz_IDCC.md#N17)

### XBID-R01 — AAC Fallback (IDCC(a) nie dostarczył AACs)
- **HTML §9:** R13
- **BUP DA:** —
- **U-kod:** [U20](Karta_ryzyk_IDCC.md#U20)
- **Opis:** IDCC(a) nie wytworzył Allocation Available Capacities (AACs, ID1-373-XX) dla XBID w wymaganym czasie.
- **Wpływ na IDCC:** kolejne iteracje IDCC(b)/(c)/(d) wstrzymane (brak AAC dla XBID).
- **Reakcja:** dostarcz **computed AACs do XBID przez narzędzie lokalne**. Deadliny:
  - **20:00 D-1** dla IDCC(b)
  - **02:00 D** dla IDCC(c)
  - **07:00 D** dla IDCC(d)
  
  Potwierdzenie mailowe do CCC.

### XBID-R02 — Late NTC delivery po IDA2
- **HTML §9:** R15
- **BUP DA:** —
- **U-kod:** [U22](Karta_ryzyk_IDCC.md#U22)
- **Opis:** NTC (FIDx-921) nie dostarczone do XBID przed 21:53 D-1 — checkpoint dostarczenia NTC do XBID przed startem aukcji IDA2 nieosiągnięty. Proces IDCC(b) wstrzymany automatycznie.
- **Wpływ na IDCC:** IDCC(b) opóźnione.
- **Reakcja:** automatyczne wznowienie po IDA2; monitoruj wznowienie i publikację NTC **przed 22:30**. Brak publikacji → **zgłoś** + telefon CCC.

---

# Podsumowanie agregacji

| Aplikacja | Ryzyk | Z HTML §9 | Z BUP DA | Nowe (specyficzne IDCC) |
|---|---|---|---|---|
| [CCM (N01)](#ccm) | 2 | R06 (R04 pośrednio) | #27, #28 | — |
| [CCCt (N02)](#ccct) | 6 | R05, R07, R09, R11 | #11, #12, #13 | — |
| [Perun4V (N03)](#perun) | 8 | R01, R02, R03 | #1, #4, #5, #6, #7, #8, #9 | — |
| [MinIO (N04)](#minio) | 3 | — | #2, #3, #25 | — |
| [Connector 2.0 (N05)](#cn2) | 2 | R09, R16 | #2, #10 | — |
| [ZP (N06)](#zp) | 1 | — | — | ZP-R01 |
| [Kreator (N07/N08)](#kreator) | 1 | — | analogicznie BUP DA Kreator | Kreator-R01 |
| [CCA (N09)](#cca) | 4 | R12, R20 | #14, #26, #10 | — |
| [kdm6 (N11)](#kdm6) | 1 | — | #25, #26 | — |
| [sFTP (N12)](#sftp) | 1 | R01 (pośrednio) | #1 | — |
| [ECP/EDX (N16)](#ecp) | 1 | R14 | — | — |
| [XBID (N17)](#xbid) | 2 | R13, R15 | — | — |
| **Razem** | **32** | **15** | **18** | **2** |

**Pominięte (LTA-specific z BUP DA):** #15-24, #29 — IDCC nie ma LTA.
**Luki (HTML §9):** R08, R10, R17, R18, R19 — patrz [TODO Inwentarza](Inwentarz_IDCC.md#todo).
