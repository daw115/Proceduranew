# Procedura IDCC TSO v6

*Instrukcja operacyjna dyspozytora PSE — proces IDCC*

## Procedura operacyjna dyspozytora PSE — proces IDCC

Szczegółowa instrukcja krok-po-kroku z właściwymi zrzutami ekranu. Dwie warstwy:

**karty skrócone**

(szybki dostęp, hiperłącza) oraz

**pełny detal**

wszystkich możliwości i stanów.

TablicaKarty skrócone (kliknij → szczegóły)

1Proces IDCC — kroki istotne dla PSE (BPD)

IDCC (Intraday Capacity Calculation) — cykliczne, śróddzienne wyznaczanie zdolności przesyłowych w regionie Core. PSE jako TSO dostarcza dane wejściowe, monitoruje strumienie plików i interweniuje przy awariach.

Iteracje procesu

IteracjaCharakterZakres
IDCC(a)Pełny przebieg centralny + wyznaczanie ATCAC, ATC Based Validation, Final NTC
IDCC(b)–(d)Kolejne iteracje śróddzienne (ID2/ID3C/ID3)GLSK, CGM, RefProg, CB, IVA, NTC, paczki PERUN

Wejścia PSE i bramki czasowe

Każdy plik ma

(Target End Time — cel) i

(Critical End Time — twardy deadline). Statusy i działania zależą od relacji do tych bramek — patrz

i

.

Opis procesu — kroki istotne dla PSE

Na podstawie

(02-03-2026). Tylko kroki, w których PSE działa lub jest adresatem; nazwy pod-procesów pozostawione po angielsku, IDCC(b)–(d) opisane wspólnie (różnice w tabeli). Kody plików w notacji FIDx.

2Narzędzia

3Legenda statusów kafelków

Pełna legenda na pulpicie

Legenda kolorów statusów plików w CCM — pełny opis znaczenia każdego koloru i oznaczenia (R, W, !, ?).

4Katalog plików FIDx — opisy i warianty stanów

IDCC(a) — 4 plików

IDCC(b) — 41 plików

IDCC(c) — 40 plików

IDCC(d) — 40 plików

IDA3 — 1 plików

5Czynności w CCM (C.1–C.5)

Pulpit dyspozytorski CCM (

) — główne miejsce monitorowania statusów wszystkich plików IDCC i ręcznej interwencji.

Główny pulpit IDCC — pełna lista plików FIDx procesu z czasami granicznymi i kolumnami statusów wysyłki/walidacji.

Zaloguj się do CCM. Wybierz pulpit „IDCC FB Pulpit dyspozytorski” lub „IDCC (do 3C) z ATC i SFTP”. Z kalendarza ustaw dobę monitorowaną. Ustaw tryb odświeżania (ultraszybki 10 s / szybki 30 s / wolny 5 min).

Odszukaj wiersz pliku (FIDx-…) i kolumnę kanału (CCTool wysł. / CCTool zwalid. / MinIO / sFTP/ZP). Kolor i znacznik kafelka = aktualny status (patrz legenda).

PPM na kafelku → „Informacje”. Popup pokazuje opis pliku, ścieżkę, TET/CET, kod ACK i ewentualny błąd walidacji.

PPM na kafelku → „Wyślij” (lub „Wyślij do CCTool”). Wskaż plik, potwierdź. Obserwuj postęp do komunikatu „Plik wysłany”.

Po CET użyj „Wyślij po CET”. Status ręczny: PPM → „Status ręczny” → wybór (Nowa wersja / Tylko zmiana statusu); cofnięcie przez „Przywróć poprzedni status”.

„Za mały rozmiar pliku!” (rozmiar poniżej progu MinIO), kod 39 (zły FID w nazwie), kod 40 (zła data w nazwie), blokada wersji backup („wersja musi być wyższa od docelowej”).

Pulpit CCM — pełna galeria (89 ekranów + 42 ikon)Logowanie do aplikacji CCM pod adresem ccm.spsm.pse.pl.Otwarcie pulpitu przez kliknięcie ikony 'oko' przy wybranej pozycji listy.Nagłówek pulpitu z polem doby handlowej (Business Day) i strzałkami zmiany dnia.Licznik czasu do najbliższego automatycznego odświeżenia.Dymek kafelka: brak dokumentu w oknie od 30 min przed TET do 30 min przed CET.Dymek błędu kafelka: dostarczona wersja nie jest wyższa od już zapisanej.Dymek kafelka z nazwą i wersją pliku (FID1-250, wersja 5).Dymek kafelka (FID1-831): dostarczona wartość ograniczenia jest ujemna.Dymek kafelka (FID2-831): dostarczona wartość ograniczenia jest ujemna.Dymek kafelka (FID1-831 wersja 2): brama dla definicji komunikatu nie jest otwarta.Dymek kafelka (FID1-921/FID1-250): brama dla definicji komunikatu nie jest otwarta.Dymek kafelka (FID1-831): komunikat zawiera nieprawidłowe szeregi czasowe niezgodne z regułami MTU.Dymek kafelka (FID2-831): komunikat zawiera nieprawidłowe szeregi czasowe niezgodne z regułami MTU.Dymek kafelka: komunikat w pełni zaakceptowany (FID2-607/FID2-617).Dymek kafelka (FID2-620, wersja 4): plik dostarczony po CET.Popup informacyjny FID2-665: plik za mały (49.858 KB przy wymaganych 50.000 KB), dostarczony po CET.Dymek kafelka: oczekiwanie na potwierdzenie ACK — minęło 5 minut.Wiersz GLSK (FID2-607): plik prawidłowo wysłany i zwalidowany (kafelki zielone).Wiersz CBCORA (FID2-617): plik wysłany, lecz walidacja bez potwierdzenia (czerwone '?').Wiersz '24 modele IGM' (DACF_IGM_UCT): brak dokumentu w kolumnie sFTP/ZP (kafelek czerwony).Wiersz IVA_ATC (FID2-710_ATC) ze statusem szarymNagłówek tabeli i wiersz MD 250 ze statusem R (ręczny)Wiersz GLSK (FID2-607) z czerwonymi kafelkami błęduWiersz GLSK (FID2-657) ze statusem WWiersz CGM Data Quality Check (FID2-659) ze statusem WWiersz Merged CGM (FID2-620) ze statusem fioletowymWiersz AC (FID1-831) ze statusami W i fioletowymPulpit IDCC(d) Individual Validation z potwierdzeniem zmiany statusuTooltip: plik wysłany ręcznie kanałami EDX/KAFKA/CCCTOOL/MINIO/PERUNPulpit z obszarami walidacji domen FBA/LTA i ekstrakcji ATCMenu PPM: przywróć status, wyślij (status ręczny aktywny)Pulpit IDCC(d) z wyborem doby i potwierdzeniem przywrócenia statusuGrupa AGR Paczka ZIP ID2 - błąd na nagłówku i FID2-620Grupa AGR Paczka ZIP ID2 - czerwony błąd na nagłówku i FID2-645Grupa AGR Paczka ZIP ID2 - statusy szare (oczekiwanie)Grupa AGR Paczka ZIP ID2 - wszystkie pliki ze statusem WGrupa Paczka ZIP do Perun - nagłówek fioletowy, pozycje WGrupa Paczka ZIP do Perun - nagłówek zielony, pozycje WPowiadomienie Chrome: konieczna weryfikacja statusu FID3-710 (IVA)Nagłówek pulpitu IDCC z trybami odświeżania i ostrzeżeniem o powiadomieniachUstawienie powiadomień: DozwolonePanel uprawnień witryny: zmiana powiadomień na DozwolonePowiadomienia włączone (przełącznik)Panel uprawnień Chrome: powiadomienia wyłączoneNagłówek pulpitu z zaznaczonym przyciskiem Test powiadomieńPulpit z powiadomieniem: powiadomienia poprawnie skonfigurowaneWycinek nagłówka tabeli pulpituZmiana szerokości kolumny w nagłówku tabeliPDF: Instrukcja Użytkownika obsługującego proces IDMenu PPM z podświetloną opcją informacje (FID2-928)Popup Informacje FID2-610 - plik dostarczony po CETPopup Informacje FID2-710 - rozmiar w bajtachNagłówek pulpitu IDCC (do 3C) z ATC i SFTPWiersz paczki ZIP do Perun w walidacji IVARozwinięta lista plików paczki ATC ID2Pasek wyboru trybu odświeżaniaMenu PPM - wyślij plik FID2-657Wybór pliku XML z eksploratora (Edge)Systemowe okno Otwórz - wskazanie plikuTrwa wysyłanie pliku FID2-657 (3%)Wiersz FID2-657 z wersją 1 po wysyłceMenu PPM - wyślij po CETOkno wysyłki po CET - FID1-250 (puste)Wiersz FID2-659 z wersją i statusemBłąd nazwy pliku (kod 39) - zła nazwa FIDBłąd nazwy pliku (kod 40) - zła dataPlik FID2-710_ATC wysłanyPlik FID3C-710_ATC wysłanyRaport RAP_PERUN_ID2 wysłanyRaport RAP_PERUN_ID2_ATC wysłanyRaport RAP_PERUN_ID3C wysłanyRaport RAP_PERUN_ID3C_ATC wysłanyMenu PPM - pobierz plik FID2-701Menu PPM na paczce ZIP/IVAUstawienia pobierania w ChromeUstawienia pobierania w FirefoxPulpit podczas pobierania pliku (8.7 MB)Powiadomienie o pobraniu pliku FID2-645Legenda - status zły rozmiar plikuMenu PPM na FID2-665 (status błędu)Informacja o zbyt małym rozmiarze pliku FID2-645Wiersz CBCORA ze statusem oczekiwania (?)Tooltip - oczekiwanie na ACK (CBCORA)Kanały statusu IVA/IVA Backup ID3CMenu PPM - Wyślij do CCTool (IVA Backup)Potwierdzenie wysyłki IVA Backup do CCToolToast - Wysłano prośbęStatusy kanałów IVA po wysyłce (ID3C)Pulpit - blokada wysyłki backup (zła wersja)Elementy interfejsu (ikony i przyciski, rozmiar rzeczywisty):Ikona 'oko' — otwiera wybrany pulpit dyspozytorski.Strzałka przejścia do następnej doby handlowej.Strzałka przejścia do poprzedniej doby handlowej.Strzałka zmiany doby (stan wyróżniony) — przejście do następStrzałka zmiany doby (stan wyróżniony) — przejście do poprzeIkona kalendarza — otwiera wybór doby handlowej.Przycisk ręcznego odświeżenia pulpitu.Przycisk 'Legenda' — rozwija opis kolorów statusów.Kafelek statusu 'oczekujący na obsługę' (biały).Kafelek statusu 'zbliża się Target End Time — brak dokumentuKafelek statusu 'brak dokumentu / błąd' (czerwony).Dymek kafelka 'Błąd procesu' (czerwony).Dymek błędu kafelka: brama dla podanej definicji komunikatu Kafelek statusu 'dokument prawidłowo obsłużony' (zielony).Kafelek statusu 'R' — dokument/składowa agregatu wysłana ręcKafelek statusu 'W' — dokument/składowa agregatu wysłana po Kafelek statusu 'dostarczony po CET' (fioletowy).Kafelek statusu 'dokument niedostarczony' (szary).Dymek kafelka 'Dokument niedostarczony (D-1)' (szary).Oznaczenie '!' — niepoprawny rozmiar pliku.Oznaczenie '?' — proces nieskończony / brak potwierdzenia ACKafelek statusu '?' (szary) — proces w trakcie wykonywania.Ikonka kłódki (zabezpieczenia)Ikonka przełączników (suwaki)Przycisk Test powiadomieńIkona ustawień (koło zębate)Ikony zoom minus/plusIkony statusu: OK (zielony) i błąd (czerwony)Ikona statusu OK (zielony)Przycisk PomocIkona rozwijania grupy (strzałka w dół)Ikona zwijania grupy (strzałka w górę)Ikona rozwijania grupy (strzałka w dół)Ikona zwijania (strzałka w górę)Ikona rozwijania (strzałka w dół)Ikona kłódki otwartej (odblokowane)Ikona kłódki zamkniętej (zablokowane)Przycisk WyślijIkona statusu - dokument WordOpcja menu - wyślij po CETIkona statusu OK (zielona)Przycisk Tak (potwierdzenie)

6Walidacja domeny FBA — tryb normalny (NOR)

Tryb normalny Day-Ahead: schemat decyzyjny walidacji domeny DA/LTA, obliczenia w Perun4V, raporty CNEC i redukcji LTA.

Walidacja NOR — pełna galeria (18 ekranów)Mapa etapów procesu FBA z zaznaczonym krokiem walidacji domeny (NOR_03)Definicja IVA i parametrów elementu CNEC (RAM, Fmax, FRM, F0,CORE)Schemat decyzyjny walidacji domeny DA z punktami kontrolnymi i ryzykamiSchemat decyzyjny walidacji domeny LTA z gałęzią redukcji LTADiagram przepływu danych między systemami (CN2, Perun, MinIO, SFTP) — kroki 1-11Lista pulpitów w aplikacji CCM z wyborem pulpitu DACC FBTabela statusów przepływów FBA — wiersz Paczka ZIP_CCA do PerunTabela statusów FBA — wiersze IVA (F310) i Raporty z PerunEkran startowy logowania do platformy LCCV (TSCNET)Formularz logowania lokalnego LCCV (Username/Password)Logi obliczeń (Calculation Logs) — zakończone obliczenie DA Estimate security reserve 25/25E-mail z raportem VALIDATION_OVERVIEW dla domeny FB (maks. IVA = 0.00)Tabela statusów FBA — sekcja Walidacja domeny LTATabela statusów LTA — wyróżnione wiersze Paczka ZIP_LTA i IVA LTAArkusz lta_curtailment bez redukcji — wszystkie wartości zeroweArkusz lta_curtailment z faktycznymi redukcjami LTA i wartościami RDPArkusz przeciążeń CNEC (Polaniec-Klikowa) — OVERLOAD, F_MAX, F_0 per godzinaE-mail z raportem lta_curtailment (RLTA) z CCA o redukcji LTA

7Walidacja domeny FBA — tryb backup (BUP)

Tryb backup Day-Ahead: generowanie wierzchołków zapasowym narzędziem CCA (F320), paczki ZIP_CCA/ZIP_LTA, estymacja rezerwy w Perun, redukcja IVA, import RLTA do ZP.

Walidacja BUP — pełna galeria (90 ekranów + 4 ikon)Mapa etapów procesu FBA - zaznaczony krok BUP_03 walidacja domenyDiagram składowych CNEC - co to jest IVA, RAM, FRM, FmaxTabela przepływów FBA - status sFTP paczki PERUN_DA_CCA podświetlonyTabela przepływów FBA - status MinIO paczki PERUN_DA_CCA zaznaczonyTabela przepływów FBA - status MinIO paczki PERUN_DA_LTA zaznaczonyMenu kontekstowe paczki PERUN_DA_CCA - opcja 'pobierz'Menu kontekstowe paczki PERUN_DA_LTA - opcja 'pobierz'TSCNET Validation - wybór procesu DA CCV i parametrów walidacjiPole wgrywania paczki ZIP z danymi TSO (TSCNET)Pole wyboru daty walidacji (TSCNET)Przycisk 'Estimate security reserve' (TSCNET)Komunikat 'Calculation started' (TSCNET)Lista obliczeń TSCNET - zadanie 8636 w trakcie liczeniaLista obliczeń TSCNET - zadanie 8636 zakończone, wyniki F310/F427Link pobrania wyniku F310 (TSCNET)Wiersz listy obliczeń TSCNET (1935) z linkami pobrania F310/F427TSCNET - podzadania: szacowanie rezerwy i tworzenie raportów (ukończone)Menu kontekstowe IVA BACKUP F310 - opcja 'wyślij'Wybór pliku F310 z folderu Pobrane do wysłania (dialog Wyślij F310)Pulpit DACC FB - plik F310 załadowany do wysłaniaPotwierdzenie 'Plik wysłany' dla F310 (pulpit DACC FB)Pulpit DACC FB - tooltip statusu wysyłki IVA F310 (kanały dystrybucji)Diagram architektury przepływu danych walidacji (CN2, Minio, CCM, Perun)Core CC Tool - dashboard procesu D-9 (Validation of Market Coupling Results)Core CC Tool Message Viewer - lista komunikatów (102, 437)Message Viewer - komunikat 312 Individual Filtered Critical BranchesIkona pola uploadu XML/ZipCore CC Tool - ręczne wgrywanie pliku F310 (Manual file upload)Message Viewer - komunikat 310 Individual CB validation (Processed/Accepted)Rozwinięta paczka AGR_PERUN_DA - lista plików składowych (F109-X427)Pulpit Day-Ahead - menu kontekstowe 'wyślij' na pliku paczkiCCM v1.8.2 - dialog wysylania pliku F333 (pulpit Day-Ahead)CCM - wysylanie F515, wybór pliku z eksploratoraEksplorator plików - wybór pliku paczki (F109-F315) do wysłaniaDialog 'Wyślij F109' z załadowanym plikiem zipKomunikat 'Plik wysłany'Menu IVA BACKUP - opcja 'backup' (ścieżka backup BUP_03)Core CC Tool View Results - filtr godzin i wyniki domeny FBCore CC Tool View Results - wartości CB (IVA, Max PTDF PL>SK)Core CC Tool Bulk edit - zbiorcza redukcja IVA 20% (fallback gdy walidacja zawiodła)Błąd TSCNET: niezgodne daty paczki ZIP i obliczeniaTSCNET - błąd niezgodności dat paczki ZIP (data 2022-05-03)Błąd TSCNET: brak plików F100/F109/F308 w paczceTSCNET - błąd brakujących plików F100/F109/F308 (2022-05-06)TSCNET - obliczenie zakończone błędem ERR-I (24 z 25 timestampów failed)Perun: status obliczeńń estymacji rezerwy – 1 godzina nieudana z 24, plus tworzenie raportów.Perun: lista zadań per godzina – jedna godzina Failed, reszta Success, dostęp do konsoli.CC Tool: wybór instancji procesu DA1 dla wybranej doby (04.10.2023).CC Tool: nagłówek Process Detail DA1 – etapy odbioru danych i status godzinowy.CC Tool: instancja oznaczona ostrzeżeniem o kandydacie fallback (przesłanka backup).Pulpit DA: menu kontekstowe na wierszu IVA BACKUP – opcja backup walidacji domeny FBA.Diagram architektury przepływu danych w procedurze IVA Backup (kroki 1–12).Pulpit DA: okno potwierdzenia wysłania dokumentu IVA Backup.Pulpit DA: pełna tabela przepływów walidacji domeny FBA i LTA ze statusami kolumnowymi.Pulpit DA: błąd – backup wymaga wersji dokumentu wyższej niż docelowa.MinIO/CCA: katalog wyjściowy backup z plikami F310-v2, RLTA, F320_LTA do pobrania.Narzędzie walidacji: Bulk edit – zbiorcza redukcja 20% po awarii Individual Validation Tool.Perun Study/Validation: logi obliczeńń, jedno zadanie estymacji rezerwy zakończone błędem.Perun: komunikat o nieudanym pobraniu pliku – wycinek samego przycisku.Perun Study/Validation: pełny ekran z komunikatem błędu pobierania pliku.Perun: wiersz obliczenia estymacji rezerwy DA z akcją Status (sFTP, 4 timestampy).Perun: estymacja rezerwy zakończona pomyślnie (24/24), pobieranie plików wyjściowych.Perun Configurations: sekcja dodatkowych NEC/wyłączeń i parametry RAO dla obliczeńń backup.Perun: formularz dodatkowego wyłączenia – elementy sieci 380 kV i wybór godzin.Perun: podgląd zapisanego dodatkowego wyłączenia H001 dla wielu godzin.Perun: wycinek wiersza obliczenia z akcją Download F310.Pulpit DA: menu kontekstowe IVA BACKUP z opcjami pobierz/wyślij.E-mail FB Core Team: brak plików IVA (F310/F310_LTA/raporty) dla doby 2024-03-21.Message Viewer: komunikat IVA 310 (PSE→CORE) odrzucony mimo ACK Accepted.Perun: lista obliczeńń z wybraną wersją 2 dokumentu F310.Wycinek nazwy pliku F310 w wersji v1.Wycinek nazwy pliku F310 w wersji v2 (porównanie wersji).XML F310: DocumentVersion = 1 w treści dokumentu Flow-Based.XML F310: DocumentVersion = 2 – wersja podwyższona do wysyłki backup.Eksplorator: folder F320_backup z plikami narzędzia fbc_lta_vertices.Konsola backup CCA: pomyślne wygenerowanie F320_CCA z plików F110/F320/F118.Eksplorator: pliki wyjściowe backup CCA dla domeny FBA (F320_CCA + mapa wierzchołków).Pulpit DA: rozwinięta paczka ZIP_CCA do Perun (pliki składowe domeny FBA).Konsola backup CCA: wygenerowano F320_LTA, ale brak danych do F320_CCA.Eksplorator: pliki wyjściowe backup CCA dla domeny LTA (F320_LTA + mapa wierzchołków).Pulpit DA: rozwinięta paczka ZIP_LTA do Perun (pliki składowe domeny LTA).E-mail: raport lta_curtailment (RLTA) z CCA z załącznikami xlsx/xml.ZP: ekran redukcji alokacji LT z błędem braku dokumentu RLTA (LTA bis) z CCA.ZP: panel importu dokumentu LTA bis – przed wyborem pliku.Eksplorator: wybór pliku 20250801-RLTA-v1-CCA-to-ZP.xml do importu w ZP.ZP: panel importu z wybranym plikiem LTA bis gotowym do zaimportowania.ZP: tabela redukcji alokacji LT wypełniona danymi godzinowymi po imporcie RLTA.Pulpit DA: błędy MinIO na paczce CCA i menu kontekstowe z opcją wyślij (ponowna wysyłka).Pulpit DA: nagłówek z trybami odświeżania i menu wysyłki paczki ZIP do Perun.E-mail FB Core Team: brak pliku F212 dla doby 2024-03-26.Elementy interfejsu (ikony i przyciski, rozmiar rzeczywisty):Status 'Processed' (Message Viewer)Przycisk 'Wyślij'Menu edycji wyników: Edit Cells / Edit BulkWycinek samego przycisku zamknięcia (X) – brak kontekstu ekr

8GLSK (FIDx-607) — katalog stanów

Plik GLSK (Generation Load Shift Keys, FIDx-607) — 32 udokumentowane stany kafelka (para lewy×prawy kanał): sukces, przetwarzanie, oczekiwanie, błędy oraz wysyłka ręczna.

GLSK 607 — stany kafelka — pełna galeria (32 ekranów)Stan bazowy - oba kafelki zielone, plik GLSK poprawny.Zielony kafelek z oznaczeniem B - sukces ze znacznikiem stanu.Oba kafelki fioletowe - przetwarzanie w toku.Oba zielone kafelki ze znacznikiem B - sukces.Ciemnozielony kafelek W (wysłany) obok jasnozielonego.Kafelek W (wysłany) obok pustego - brak statusu po prawej.Wysłany (W) po lewej, czerwony ze znakiem zapytania po prawej - problem/oczekiwanie.Wysłany (W) po lewej, błąd czerwony po prawej.Wysłany (W) po lewej, przetwarzanie (fioletowy) po prawej.Wysłany (W) po lewej, oczekujący w kolejce (granatowy) po prawej.Wysłany (W) po lewej, zielony ze znacznikiem B po prawej.Wysłany i zmodyfikowany (W*) po lewej, pusty po prawej.Zmodyfikowany wysłany (W*) po lewej, czerwony ze znakiem zapytania po prawej.Zmodyfikowany wysłany (W*) po lewej, błąd czerwony po prawej.Zmodyfikowany wysłany (W*) po lewej, przetwarzanie (fioletowy) po prawej.Zmodyfikowany wysłany (W*) po lewej, oczekujący (granatowy) po prawej.Zielony ze znacznikiem B po lewej, pusty po prawej.Zielony B po lewej, czerwony ze znakiem zapytania po prawej.Zielony B po lewej, oczekujący (granatowy) po prawej.Błąd/alert (czerwony !) po lewej, zielony B po prawej.Oba kafelki szare - stan nieaktywny/wyłączony.Oba kafelki czerwone - błąd/awaria po obu stronach.Czerwony alert (!) po lewej, czerwony ze znakiem zapytania po prawej.Czerwony alert (!) po lewej, błąd czerwony po prawej.Czerwony alert (!) po lewej, przetwarzanie (fioletowy) po prawej.Zielony po lewej, błąd czerwony po prawej.Zielony po lewej, czerwony ze znakiem zapytania po prawej.Zielony po lewej, oczekujący (granatowy) po prawej.Czerwony alert (!) po lewej, oczekujący (granatowy) po prawej.Przetwarzanie (fioletowy) po lewej, błąd czerwony po prawej.Przetwarzanie (fioletowy) po lewej, oczekujący (granatowy) po prawej.Oba kafelki granatowe - oczekiwanie/zakolejkowanie po obu stronach.

9Kreator IDCF — publikacja RA / GLSK / CBCORA

KreatorIDCF_CGMES — publikacja środków zaradczych RA oraz plików GLSK/CBCORA przez Connector → MinIO, z weryfikacją w CCM.

10AC w ZP (FIDx-831)

Plik AC (Allocation Constraints, FIDx-831) — ręczna obsługa w aplikacji ZP: tabela ograniczeń NTC/ATC, wersjonowanie, zatwierdzanie.

11Procedury P01–P06

Pełne procedury reagujące na ryzyka oraz procedury narzędziowe krok po kroku.

12Ryzyka U01–U23 i kody ACK

13Buckety MinIO i mapa relacji

Wygenerowano automatycznie z: Inwentarz_IDCC.md, popup_content_IDCC.json (126 plików), staticHints-IDCC-all.txt (986 stanów), screens_manifest.json (309 ekranów). Każde ryzyko zgłaszać do:

**CIZ, WPO, PSE-I (PSE Innowacje)**

.


![Legenda kolorów statusów plików w CCM — pełny opis znaczenia każdego koloru i oznaczenia (R, W, !, ?).](screens/ccm/ccm-017.png)


![Główny pulpit IDCC — pełna lista plików FIDx procesu z czasami granicznymi i kolumnami statusów wysyłki/walidacji.](screens/ccm/ccm-004.png)


![Lista dostępnych pulpitów dyspozytorskich w CCM — wybór pulpitu DACC FB lub IDCC.](screens/ccm/ccm-001.png)


![Wybór doby handlowej z kalendarza (przykład: 9 września 2025).](screens/ccm/ccm-011.png)


![Wybór trybu automatycznego odświeżania pulpitu (10 s / 30 s / 5 min).](screens/ccm/ccm-012.png)


![Pulpit 'IDCC (do 3C) z ATC i SFTP' z trzema kartami przeglądarki i kafelkami statusów plików FIDx.](screens/ccm/ccm-015.png)


![Menu kontekstowe PPM: status ręczny, informacje, pobierz, wyślij](screens/ccm/ccm-057.png)


![Popup Informacje FID2-665 - błąd: za mały rozmiar pliku](screens/ccm/ccm-093.png)


![Okno wysyłania pliku FID2-657 (puste)](screens/ccm/ccm-110.png)


![Okno wysyłania z wybranym plikiem FID2-657](screens/ccm/ccm-113.png)


![Plik FID2-657 wysłany pomyślnie](screens/ccm/ccm-116.png)


![Popup statusu ręcznego - wariant Nowa wersja](screens/ccm/ccm-058.png)


![Popup statusu ręcznego - wariant Tylko zmiana statusu](screens/ccm/ccm-061.png)


![Popup przywrócenia poprzedniego statusu](screens/ccm/ccm-064.png)


![Logowanie do aplikacji CCM pod adresem ccm.spsm.pse.pl.](screens/ccm/ccm-000.png)


![Otwarcie pulpitu przez kliknięcie ikony 'oko' przy wybranej pozycji listy.](screens/ccm/ccm-003.png)


![Nagłówek pulpitu z polem doby handlowej (Business Day) i strzałkami zmiany dnia.](screens/ccm/ccm-005.png)


![Licznik czasu do najbliższego automatycznego odświeżenia.](screens/ccm/ccm-014.png)


![Dymek kafelka: brak dokumentu w oknie od 30 min przed TET do 30 min przed CET.](screens/ccm/ccm-020.png)


![Dymek błędu kafelka: dostarczona wersja nie jest wyższa od już zapisanej.](screens/ccm/ccm-024.png)


![Dymek kafelka z nazwą i wersją pliku (FID1-250, wersja 5).](screens/ccm/ccm-026.png)


![Dymek kafelka (FID1-831): dostarczona wartość ograniczenia jest ujemna.](screens/ccm/ccm-027.png)


![Dymek kafelka (FID2-831): dostarczona wartość ograniczenia jest ujemna.](screens/ccm/ccm-028.png)


![Dymek kafelka (FID1-831 wersja 2): brama dla definicji komunikatu nie jest otwarta.](screens/ccm/ccm-029.png)


![Dymek kafelka (FID1-921/FID1-250): brama dla definicji komunikatu nie jest otwarta.](screens/ccm/ccm-030.png)


![Dymek kafelka (FID1-831): komunikat zawiera nieprawidłowe szeregi czasowe niezgodne z regułami MTU.](screens/ccm/ccm-031.png)


![Dymek kafelka (FID2-831): komunikat zawiera nieprawidłowe szeregi czasowe niezgodne z regułami MTU.](screens/ccm/ccm-032.png)


![Dymek kafelka: komunikat w pełni zaakceptowany (FID2-607/FID2-617).](screens/ccm/ccm-033.png)


![Dymek kafelka (FID2-620, wersja 4): plik dostarczony po CET.](screens/ccm/ccm-039.png)


![Popup informacyjny FID2-665: plik za mały (49.858 KB przy wymaganych 50.000 KB), dostarczony po CET.](screens/ccm/ccm-043.png)


![Dymek kafelka: oczekiwanie na potwierdzenie ACK — minęło 5 minut.](screens/ccm/ccm-045.png)


![Wiersz GLSK (FID2-607): plik prawidłowo wysłany i zwalidowany (kafelki zielone).](screens/ccm/ccm-047.png)


![Wiersz CBCORA (FID2-617): plik wysłany, lecz walidacja bez potwierdzenia (czerwone '?').](screens/ccm/ccm-048.png)


![Wiersz '24 modele IGM' (DACF_IGM_UCT): brak dokumentu w kolumnie sFTP/ZP (kafelek czerwony).](screens/ccm/ccm-049.png)


![Wiersz IVA_ATC (FID2-710_ATC) ze statusem szarym](screens/ccm/ccm-050.png)


![Nagłówek tabeli i wiersz MD 250 ze statusem R (ręczny)](screens/ccm/ccm-051.png)


![Wiersz GLSK (FID2-607) z czerwonymi kafelkami błędu](screens/ccm/ccm-052.png)


![Wiersz GLSK (FID2-657) ze statusem W](screens/ccm/ccm-053.png)


![Wiersz CGM Data Quality Check (FID2-659) ze statusem W](screens/ccm/ccm-054.png)


![Wiersz Merged CGM (FID2-620) ze statusem fioletowym](screens/ccm/ccm-055.png)


![Wiersz AC (FID1-831) ze statusami W i fioletowym](screens/ccm/ccm-056.png)


![Pulpit IDCC(d) Individual Validation z potwierdzeniem zmiany statusu](screens/ccm/ccm-059.png)


![Tooltip: plik wysłany ręcznie kanałami EDX/KAFKA/CCCTOOL/MINIO/PERUN](screens/ccm/ccm-060.png)


![Pulpit z obszarami walidacji domen FBA/LTA i ekstrakcji ATC](screens/ccm/ccm-062.png)


![Menu PPM: przywróć status, wyślij (status ręczny aktywny)](screens/ccm/ccm-063.png)


![Pulpit IDCC(d) z wyborem doby i potwierdzeniem przywrócenia statusu](screens/ccm/ccm-065.png)


![Grupa AGR Paczka ZIP ID2 - błąd na nagłówku i FID2-620](screens/ccm/ccm-066.png)


![Grupa AGR Paczka ZIP ID2 - czerwony błąd na nagłówku i FID2-645](screens/ccm/ccm-067.png)


![Grupa AGR Paczka ZIP ID2 - statusy szare (oczekiwanie)](screens/ccm/ccm-068.png)


![Grupa AGR Paczka ZIP ID2 - wszystkie pliki ze statusem W](screens/ccm/ccm-069.png)


![Grupa Paczka ZIP do Perun - nagłówek fioletowy, pozycje W](screens/ccm/ccm-070.png)


![Grupa Paczka ZIP do Perun - nagłówek zielony, pozycje W](screens/ccm/ccm-071.png)


![Powiadomienie Chrome: konieczna weryfikacja statusu FID3-710 (IVA)](screens/ccm/ccm-072.png)


![Nagłówek pulpitu IDCC z trybami odświeżania i ostrzeżeniem o powiadomieniach](screens/ccm/ccm-073.png)


![Ustawienie powiadomień: Dozwolone](screens/ccm/ccm-075.png)


![Panel uprawnień witryny: zmiana powiadomień na Dozwolone](screens/ccm/ccm-076.png)


![Powiadomienia włączone (przełącznik)](screens/ccm/ccm-078.png)


![Panel uprawnień Chrome: powiadomienia wyłączone](screens/ccm/ccm-079.png)


![Nagłówek pulpitu z zaznaczonym przyciskiem Test powiadomień](screens/ccm/ccm-081.png)


![Pulpit z powiadomieniem: powiadomienia poprawnie skonfigurowane](screens/ccm/ccm-082.png)


![Wycinek nagłówka tabeli pulpitu](screens/ccm/ccm-086.png)


![Zmiana szerokości kolumny w nagłówku tabeli](screens/ccm/ccm-087.png)


![PDF: Instrukcja Użytkownika obsługującego proces ID](screens/ccm/ccm-090.png)


![Menu PPM z podświetloną opcją informacje (FID2-928)](screens/ccm/ccm-091.png)


![Popup Informacje FID2-610 - plik dostarczony po CET](screens/ccm/ccm-092.png)


![Popup Informacje FID2-710 - rozmiar w bajtach](screens/ccm/ccm-094.png)


![Nagłówek pulpitu IDCC (do 3C) z ATC i SFTP](screens/ccm/ccm-098.png)


![Wiersz paczki ZIP do Perun w walidacji IVA](screens/ccm/ccm-102.png)


![Rozwinięta lista plików paczki ATC ID2](screens/ccm/ccm-104.png)


![Pasek wyboru trybu odświeżania](screens/ccm/ccm-106.png)


![Menu PPM - wyślij plik FID2-657](screens/ccm/ccm-109.png)


![Wybór pliku XML z eksploratora (Edge)](screens/ccm/ccm-111.png)


![Systemowe okno Otwórz - wskazanie pliku](screens/ccm/ccm-112.png)


![Trwa wysyłanie pliku FID2-657 (3%)](screens/ccm/ccm-115.png)


![Wiersz FID2-657 z wersją 1 po wysyłce](screens/ccm/ccm-118.png)


![Menu PPM - wyślij po CET](screens/ccm/ccm-120.png)


![Okno wysyłki po CET - FID1-250 (puste)](screens/ccm/ccm-121.png)


![Wiersz FID2-659 z wersją i statusem](screens/ccm/ccm-122.png)


![Błąd nazwy pliku (kod 39) - zła nazwa FID](screens/ccm/ccm-123.png)


![Błąd nazwy pliku (kod 40) - zła data](screens/ccm/ccm-124.png)


![Plik FID2-710_ATC wysłany](screens/ccm/ccm-125.png)


![Plik FID3C-710_ATC wysłany](screens/ccm/ccm-126.png)


![Raport RAP_PERUN_ID2 wysłany](screens/ccm/ccm-127.png)


![Raport RAP_PERUN_ID2_ATC wysłany](screens/ccm/ccm-128.png)


![Raport RAP_PERUN_ID3C wysłany](screens/ccm/ccm-129.png)


![Raport RAP_PERUN_ID3C_ATC wysłany](screens/ccm/ccm-130.png)


![Menu PPM - pobierz plik FID2-701](screens/ccm/ccm-131.png)


![Menu PPM na paczce ZIP/IVA](screens/ccm/ccm-132.png)


![Ustawienia pobierania w Chrome](screens/ccm/ccm-133.png)


![Ustawienia pobierania w Firefox](screens/ccm/ccm-134.png)


![Pulpit podczas pobierania pliku (8.7 MB)](screens/ccm/ccm-135.png)


![Powiadomienie o pobraniu pliku FID2-645](screens/ccm/ccm-136.png)


![Legenda - status zły rozmiar pliku](screens/ccm/ccm-137.png)


![Menu PPM na FID2-665 (status błędu)](screens/ccm/ccm-138.png)


![Informacja o zbyt małym rozmiarze pliku FID2-645](screens/ccm/ccm-139.png)


![Wiersz CBCORA ze statusem oczekiwania (?)](screens/ccm/ccm-140.png)


![Tooltip - oczekiwanie na ACK (CBCORA)](screens/ccm/ccm-141.png)


![Kanały statusu IVA/IVA Backup ID3C](screens/ccm/ccm-143.png)


![Menu PPM - Wyślij do CCTool (IVA Backup)](screens/ccm/ccm-144.png)


![Potwierdzenie wysyłki IVA Backup do CCTool](screens/ccm/ccm-145.png)


![Toast - Wysłano prośbę](screens/ccm/ccm-147.png)


![Statusy kanałów IVA po wysyłce (ID3C)](screens/ccm/ccm-148.png)


![Pulpit - blokada wysyłki backup (zła wersja)](screens/ccm/ccm-149.png)


![Ikona 'oko' — otwiera wybrany pulpit dyspozytorski.](screens/ccm/ccm-002.png)


![Strzałka przejścia do następnej doby handlowej.](screens/ccm/ccm-006.png)


![Strzałka przejścia do poprzedniej doby handlowej.](screens/ccm/ccm-007.png)


![Strzałka zmiany doby (stan wyróżniony) — przejście do następnego dnia.](screens/ccm/ccm-008.png)


![Strzałka zmiany doby (stan wyróżniony) — przejście do poprzedniego dnia.](screens/ccm/ccm-009.png)


![Ikona kalendarza — otwiera wybór doby handlowej.](screens/ccm/ccm-010.png)


![Przycisk ręcznego odświeżenia pulpitu.](screens/ccm/ccm-013.png)


![Przycisk 'Legenda' — rozwija opis kolorów statusów.](screens/ccm/ccm-016.png)


![Kafelek statusu 'oczekujący na obsługę' (biały).](screens/ccm/ccm-018.png)


![Kafelek statusu 'zbliża się Target End Time — brak dokumentu' (czerwono-żółty).](screens/ccm/ccm-019.png)


![Kafelek statusu 'brak dokumentu / błąd' (czerwony).](screens/ccm/ccm-021.png)


![Dymek kafelka 'Błąd procesu' (czerwony).](screens/ccm/ccm-022.png)


![Dymek błędu kafelka: brama dla podanej definicji komunikatu nie jest otwarta.](screens/ccm/ccm-023.png)


![Kafelek statusu 'dokument prawidłowo obsłużony' (zielony).](screens/ccm/ccm-025.png)


![Kafelek statusu 'R' — dokument/składowa agregatu wysłana ręcznie.](screens/ccm/ccm-035.png)


![Kafelek statusu 'W' — dokument/składowa agregatu wysłana po CET.](screens/ccm/ccm-036.png)


![Kafelek statusu 'dostarczony po CET' (fioletowy).](screens/ccm/ccm-038.png)


![Kafelek statusu 'dokument niedostarczony' (szary).](screens/ccm/ccm-040.png)


![Dymek kafelka 'Dokument niedostarczony (D-1)' (szary).](screens/ccm/ccm-041.png)


![Oznaczenie '!' — niepoprawny rozmiar pliku.](screens/ccm/ccm-042.png)


![Oznaczenie '?' — proces nieskończony / brak potwierdzenia ACK.](screens/ccm/ccm-044.png)


![Kafelek statusu '?' (szary) — proces w trakcie wykonywania.](screens/ccm/ccm-046.png)


![Ikonka kłódki (zabezpieczenia)](screens/ccm/ccm-074.png)


![Ikonka przełączników (suwaki)](screens/ccm/ccm-077.png)


![Przycisk Test powiadomień](screens/ccm/ccm-080.png)


![Ikona ustawień (koło zębate)](screens/ccm/ccm-083.png)


![Ikony zoom minus/plus](screens/ccm/ccm-084.png)


![Ikony statusu: OK (zielony) i błąd (czerwony)](screens/ccm/ccm-085.png)


![Ikona statusu OK (zielony)](screens/ccm/ccm-088.png)


![Przycisk Pomoc](screens/ccm/ccm-089.png)


![Ikona rozwijania grupy (strzałka w dół)](screens/ccm/ccm-095.png)


![Ikona zwijania grupy (strzałka w górę)](screens/ccm/ccm-096.png)


![Ikona rozwijania grupy (strzałka w dół)](screens/ccm/ccm-099.png)


![Ikona zwijania (strzałka w górę)](screens/ccm/ccm-100.png)


![Ikona rozwijania (strzałka w dół)](screens/ccm/ccm-101.png)


![Ikona kłódki otwartej (odblokowane)](screens/ccm/ccm-105.png)


![Ikona kłódki zamkniętej (zablokowane)](screens/ccm/ccm-108.png)


![Przycisk Wyślij](screens/ccm/ccm-114.png)


![Ikona statusu - dokument Word](screens/ccm/ccm-117.png)


![Opcja menu - wyślij po CET](screens/ccm/ccm-119.png)


![Ikona statusu OK (zielona)](screens/ccm/ccm-142.png)


![Przycisk Tak (potwierdzenie)](screens/ccm/ccm-146.png)


![Mapa etapów procesu FBA z zaznaczonym krokiem walidacji domeny (NOR_03)](screens/nor/image1.png)


![Definicja IVA i parametrów elementu CNEC (RAM, Fmax, FRM, F0,CORE)](screens/nor/image2.png)


![Schemat decyzyjny walidacji domeny DA z punktami kontrolnymi i ryzykami](screens/nor/image3.png)


![Schemat decyzyjny walidacji domeny LTA z gałęzią redukcji LTA](screens/nor/image4.png)


![Diagram przepływu danych między systemami (CN2, Perun, MinIO, SFTP) — kroki 1-11](screens/nor/image5.png)


![Lista pulpitów w aplikacji CCM z wyborem pulpitu DACC FB](screens/nor/image6.png)


![Tabela statusów przepływów FBA — wiersz Paczka ZIP_CCA do Perun](screens/nor/image7.png)


![Tabela statusów FBA — wiersze IVA (F310) i Raporty z Perun](screens/nor/image8.png)


![Ekran startowy logowania do platformy LCCV (TSCNET)](screens/nor/image9.png)


![Formularz logowania lokalnego LCCV (Username/Password)](screens/nor/image10.png)


![Logi obliczeń (Calculation Logs) — zakończone obliczenie DA Estimate security reserve 25/25](screens/nor/image11.png)


![E-mail z raportem VALIDATION_OVERVIEW dla domeny FB (maks. IVA = 0.00)](screens/nor/image12.png)


![Tabela statusów FBA — sekcja Walidacja domeny LTA](screens/nor/image14.png)


![Tabela statusów LTA — wyróżnione wiersze Paczka ZIP_LTA i IVA LTA](screens/nor/image15.png)


![Arkusz lta_curtailment bez redukcji — wszystkie wartości zerowe](screens/nor/image16.png)


![Arkusz lta_curtailment z faktycznymi redukcjami LTA i wartościami RDP](screens/nor/image17.png)


![Arkusz przeciążeń CNEC (Polaniec-Klikowa) — OVERLOAD, F_MAX, F_0 per godzina](screens/nor/image18.png)


![E-mail z raportem lta_curtailment (RLTA) z CCA o redukcji LTA](screens/nor/image19.png)


![Mapa etapów procesu FBA - zaznaczony krok BUP_03 walidacja domeny](screens/bup/image2.png)


![Diagram składowych CNEC - co to jest IVA, RAM, FRM, Fmax](screens/bup/image3.png)


![Tabela przepływów FBA - status sFTP paczki PERUN_DA_CCA podświetlony](screens/bup/image4.png)


![Tabela przepływów FBA - status MinIO paczki PERUN_DA_CCA zaznaczony](screens/bup/image5.png)


![Tabela przepływów FBA - status MinIO paczki PERUN_DA_LTA zaznaczony](screens/bup/image6.png)


![Menu kontekstowe paczki PERUN_DA_CCA - opcja 'pobierz'](screens/bup/image7.png)


![Menu kontekstowe paczki PERUN_DA_LTA - opcja 'pobierz'](screens/bup/image8.png)


![TSCNET Validation - wybór procesu DA CCV i parametrów walidacji](screens/bup/image9.png)


![Pole wgrywania paczki ZIP z danymi TSO (TSCNET)](screens/bup/image10.png)


![Pole wyboru daty walidacji (TSCNET)](screens/bup/image11.png)


![Przycisk 'Estimate security reserve' (TSCNET)](screens/bup/image12.png)


![Komunikat 'Calculation started' (TSCNET)](screens/bup/image13.png)


![Lista obliczeń TSCNET - zadanie 8636 w trakcie liczenia](screens/bup/image14.png)


![Lista obliczeń TSCNET - zadanie 8636 zakończone, wyniki F310/F427](screens/bup/image15.png)


![Link pobrania wyniku F310 (TSCNET)](screens/bup/image16.png)


![Wiersz listy obliczeń TSCNET (1935) z linkami pobrania F310/F427](screens/bup/image17.png)


![TSCNET - podzadania: szacowanie rezerwy i tworzenie raportów (ukończone)](screens/bup/image18.png)


![Menu kontekstowe IVA BACKUP F310 - opcja 'wyślij'](screens/bup/image19.png)


![Wybór pliku F310 z folderu Pobrane do wysłania (dialog Wyślij F310)](screens/bup/image20.png)


![Pulpit DACC FB - plik F310 załadowany do wysłania](screens/bup/image21.png)


![Potwierdzenie 'Plik wysłany' dla F310 (pulpit DACC FB)](screens/bup/image22.png)


![Pulpit DACC FB - tooltip statusu wysyłki IVA F310 (kanały dystrybucji)](screens/bup/image23.png)


![Diagram architektury przepływu danych walidacji (CN2, Minio, CCM, Perun)](screens/bup/image24.png)


![Core CC Tool - dashboard procesu D-9 (Validation of Market Coupling Results)](screens/bup/image25.png)


![Core CC Tool Message Viewer - lista komunikatów (102, 437)](screens/bup/image26.png)


![Message Viewer - komunikat 312 Individual Filtered Critical Branches](screens/bup/image27.png)


![Ikona pola uploadu XML/Zip](screens/bup/image28.png)


![Core CC Tool - ręczne wgrywanie pliku F310 (Manual file upload)](screens/bup/image29.png)


![Message Viewer - komunikat 310 Individual CB validation (Processed/Accepted)](screens/bup/image30.png)


![Rozwinięta paczka AGR_PERUN_DA - lista plików składowych (F109-X427)](screens/bup/image32.png)


![Pulpit Day-Ahead - menu kontekstowe 'wyślij' na pliku paczki](screens/bup/image33.png)


![CCM v1.8.2 - dialog wysylania pliku F333 (pulpit Day-Ahead)](screens/bup/image34.png)


![CCM - wysylanie F515, wybór pliku z eksploratora](screens/bup/image35.png)


![Eksplorator plików - wybór pliku paczki (F109-F315) do wysłania](screens/bup/image36.png)


![Dialog 'Wyślij F109' z załadowanym plikiem zip](screens/bup/image37.png)


![Komunikat 'Plik wysłany'](screens/bup/image39.png)


![Menu IVA BACKUP - opcja 'backup' (ścieżka backup BUP_03)](screens/bup/image40.png)


![Core CC Tool View Results - filtr godzin i wyniki domeny FB](screens/bup/image41.png)


![Core CC Tool View Results - wartości CB (IVA, Max PTDF PL>SK)](screens/bup/image44.jpeg)


![Core CC Tool Bulk edit - zbiorcza redukcja IVA 20% (fallback gdy walidacja zawiodła)](screens/bup/image45.png)


![Błąd TSCNET: niezgodne daty paczki ZIP i obliczenia](screens/bup/image46.png)


![TSCNET - błąd niezgodności dat paczki ZIP (data 2022-05-03)](screens/bup/image47.png)


![Błąd TSCNET: brak plików F100/F109/F308 w paczce](screens/bup/image48.png)


![TSCNET - błąd brakujących plików F100/F109/F308 (2022-05-06)](screens/bup/image49.png)


![TSCNET - obliczenie zakończone błędem ERR-I (24 z 25 timestampów failed)](screens/bup/image50.png)


![Perun: status obliczeńń estymacji rezerwy – 1 godzina nieudana z 24, plus tworzenie raportów.](screens/bup/image52.png)


![Perun: lista zadań per godzina – jedna godzina Failed, reszta Success, dostęp do konsoli.](screens/bup/image53.png)


![CC Tool: wybór instancji procesu DA1 dla wybranej doby (04.10.2023).](screens/bup/image54.png)


![CC Tool: nagłówek Process Detail DA1 – etapy odbioru danych i status godzinowy.](screens/bup/image55.png)


![CC Tool: instancja oznaczona ostrzeżeniem o kandydacie fallback (przesłanka backup).](screens/bup/image56.png)


![Pulpit DA: menu kontekstowe na wierszu IVA BACKUP – opcja backup walidacji domeny FBA.](screens/bup/image57.png)


![Diagram architektury przepływu danych w procedurze IVA Backup (kroki 1–12).](screens/bup/image58.png)


![Pulpit DA: okno potwierdzenia wysłania dokumentu IVA Backup.](screens/bup/image59.png)


![Pulpit DA: pełna tabela przepływów walidacji domeny FBA i LTA ze statusami kolumnowymi.](screens/bup/image62.png)


![Pulpit DA: błąd – backup wymaga wersji dokumentu wyższej niż docelowa.](screens/bup/image63.png)


![MinIO/CCA: katalog wyjściowy backup z plikami F310-v2, RLTA, F320_LTA do pobrania.](screens/bup/image64.png)


![Narzędzie walidacji: Bulk edit – zbiorcza redukcja 20% po awarii Individual Validation Tool.](screens/bup/image65.png)


![Perun Study/Validation: logi obliczeńń, jedno zadanie estymacji rezerwy zakończone błędem.](screens/bup/image66.png)


![Perun: komunikat o nieudanym pobraniu pliku – wycinek samego przycisku.](screens/bup/image67.png)


![Perun Study/Validation: pełny ekran z komunikatem błędu pobierania pliku.](screens/bup/image68.png)


![Perun: wiersz obliczenia estymacji rezerwy DA z akcją Status (sFTP, 4 timestampy).](screens/bup/image69.png)


![Perun: estymacja rezerwy zakończona pomyślnie (24/24), pobieranie plików wyjściowych.](screens/bup/image70.png)


![Perun Configurations: sekcja dodatkowych NEC/wyłączeń i parametry RAO dla obliczeńń backup.](screens/bup/image71.png)


![Perun: formularz dodatkowego wyłączenia – elementy sieci 380 kV i wybór godzin.](screens/bup/image72.png)


![Perun: podgląd zapisanego dodatkowego wyłączenia H001 dla wielu godzin.](screens/bup/image74.png)


![Perun: wycinek wiersza obliczenia z akcją Download F310.](screens/bup/image75.png)


![Pulpit DA: menu kontekstowe IVA BACKUP z opcjami pobierz/wyślij.](screens/bup/image76.png)


![E-mail FB Core Team: brak plików IVA (F310/F310_LTA/raporty) dla doby 2024-03-21.](screens/bup/image77.png)


![Message Viewer: komunikat IVA 310 (PSE→CORE) odrzucony mimo ACK Accepted.](screens/bup/image78.png)


![Perun: lista obliczeńń z wybraną wersją 2 dokumentu F310.](screens/bup/image79.png)


![Wycinek nazwy pliku F310 w wersji v1.](screens/bup/image80.png)


![Wycinek nazwy pliku F310 w wersji v2 (porównanie wersji).](screens/bup/image81.png)


![XML F310: DocumentVersion = 1 w treści dokumentu Flow-Based.](screens/bup/image82.png)


![XML F310: DocumentVersion = 2 – wersja podwyższona do wysyłki backup.](screens/bup/image83.png)


![Eksplorator: folder F320_backup z plikami narzędzia fbc_lta_vertices.](screens/bup/image84.png)


![Konsola backup CCA: pomyślne wygenerowanie F320_CCA z plików F110/F320/F118.](screens/bup/image85.png)


![Eksplorator: pliki wyjściowe backup CCA dla domeny FBA (F320_CCA + mapa wierzchołków).](screens/bup/image86.png)


![Pulpit DA: rozwinięta paczka ZIP_CCA do Perun (pliki składowe domeny FBA).](screens/bup/image87.png)


![Konsola backup CCA: wygenerowano F320_LTA, ale brak danych do F320_CCA.](screens/bup/image88.png)


![Eksplorator: pliki wyjściowe backup CCA dla domeny LTA (F320_LTA + mapa wierzchołków).](screens/bup/image89.png)


![Pulpit DA: rozwinięta paczka ZIP_LTA do Perun (pliki składowe domeny LTA).](screens/bup/image90.png)


![E-mail: raport lta_curtailment (RLTA) z CCA z załącznikami xlsx/xml.](screens/bup/image92.png)


![ZP: ekran redukcji alokacji LT z błędem braku dokumentu RLTA (LTA bis) z CCA.](screens/bup/image93.png)


![ZP: panel importu dokumentu LTA bis – przed wyborem pliku.](screens/bup/image94.png)


![Eksplorator: wybór pliku 20250801-RLTA-v1-CCA-to-ZP.xml do importu w ZP.](screens/bup/image95.png)


![ZP: panel importu z wybranym plikiem LTA bis gotowym do zaimportowania.](screens/bup/image96.png)


![ZP: tabela redukcji alokacji LT wypełniona danymi godzinowymi po imporcie RLTA.](screens/bup/image97.png)


![Pulpit DA: błędy MinIO na paczce CCA i menu kontekstowe z opcją wyślij (ponowna wysyłka).](screens/bup/image98.png)


![Pulpit DA: nagłówek z trybami odświeżania i menu wysyłki paczki ZIP do Perun.](screens/bup/image99.png)


![E-mail FB Core Team: brak pliku F212 dla doby 2024-03-26.](screens/bup/image100.png)


![Status 'Processed' (Message Viewer)](screens/bup/image31.png)


![Przycisk 'Wyślij'](screens/bup/image38.png)


![Menu edycji wyników: Edit Cells / Edit Bulk](screens/bup/image42.png)


![Wycinek samego przycisku zamknięcia (X) – brak kontekstu ekranu.](screens/bup/image73.png)


![Stan bazowy - oba kafelki zielone, plik GLSK poprawny.](screens_fid607/state_01.png)


![Zielony kafelek z oznaczeniem B - sukces ze znacznikiem stanu.](screens_fid607/state_02.png)


![Oba kafelki fioletowe - przetwarzanie w toku.](screens_fid607/state_03.png)


![Oba zielone kafelki ze znacznikiem B - sukces.](screens_fid607/state_04.png)


![Ciemnozielony kafelek W (wysłany) obok jasnozielonego.](screens_fid607/state_05.png)


![Kafelek W (wysłany) obok pustego - brak statusu po prawej.](screens_fid607/state_06.png)


![Wysłany (W) po lewej, czerwony ze znakiem zapytania po prawej - problem/oczekiwanie.](screens_fid607/state_07.png)


![Wysłany (W) po lewej, błąd czerwony po prawej.](screens_fid607/state_08.png)


![Wysłany (W) po lewej, przetwarzanie (fioletowy) po prawej.](screens_fid607/state_09.png)


![Wysłany (W) po lewej, oczekujący w kolejce (granatowy) po prawej.](screens_fid607/state_10.png)


![Wysłany (W) po lewej, zielony ze znacznikiem B po prawej.](screens_fid607/state_11.png)


![Wysłany i zmodyfikowany (W*) po lewej, pusty po prawej.](screens_fid607/state_12.png)


![Zmodyfikowany wysłany (W*) po lewej, czerwony ze znakiem zapytania po prawej.](screens_fid607/state_13.png)


![Zmodyfikowany wysłany (W*) po lewej, błąd czerwony po prawej.](screens_fid607/state_14.png)


![Zmodyfikowany wysłany (W*) po lewej, przetwarzanie (fioletowy) po prawej.](screens_fid607/state_15.png)


![Zmodyfikowany wysłany (W*) po lewej, oczekujący (granatowy) po prawej.](screens_fid607/state_16.png)


![Zielony ze znacznikiem B po lewej, pusty po prawej.](screens_fid607/state_17.png)


![Zielony B po lewej, czerwony ze znakiem zapytania po prawej.](screens_fid607/state_18.png)


![Zielony B po lewej, oczekujący (granatowy) po prawej.](screens_fid607/state_19.png)


![Błąd/alert (czerwony !) po lewej, zielony B po prawej.](screens_fid607/state_20.png)


![Oba kafelki szare - stan nieaktywny/wyłączony.](screens_fid607/state_21.png)


![Oba kafelki czerwone - błąd/awaria po obu stronach.](screens_fid607/state_22.png)


![Czerwony alert (!) po lewej, czerwony ze znakiem zapytania po prawej.](screens_fid607/state_23.png)


![Czerwony alert (!) po lewej, błąd czerwony po prawej.](screens_fid607/state_24.png)


![Czerwony alert (!) po lewej, przetwarzanie (fioletowy) po prawej.](screens_fid607/state_25.png)


![Zielony po lewej, błąd czerwony po prawej.](screens_fid607/state_26.png)


![Zielony po lewej, czerwony ze znakiem zapytania po prawej.](screens_fid607/state_27.png)


![Zielony po lewej, oczekujący (granatowy) po prawej.](screens_fid607/state_28.png)


![Czerwony alert (!) po lewej, oczekujący (granatowy) po prawej.](screens_fid607/state_29.png)


![Przetwarzanie (fioletowy) po lewej, błąd czerwony po prawej.](screens_fid607/state_30.png)


![Przetwarzanie (fioletowy) po lewej, oczekujący (granatowy) po prawej.](screens_fid607/state_31.png)


![Oba kafelki granatowe - oczekiwanie/zakolejkowanie po obu stronach.](screens_fid607/state_32.png)


![1. Panel IDCF: GLSK / CBCORA / RA + „Publikuj Connector”](screens_kreatoridcf/panel.png)


![2. Wybór plików GLSK (.uct)](screens_kreatoridcf/03_wybrane_pliki_gsk.png)


![3. Wybór plików CBCORA (.epc)](screens_kreatoridcf/06_wybrane_pliki_cbcora.png)


![4. Okno „Pliki do publikacji” — wersje](screens_kreatoridcf/okno_publikacji.png)


![5. Postęp: wysyłka na MinIO + pakowanie ZIP](screens_kreatoridcf/okno_postep.png)


![6. LOG: „Publikacja zakończona”](screens_kreatoridcf/log_publikacji.png)


![7. Monitor: statusy zadań (OK / BŁĄD)](screens_kreatoridcf/00_monitor_normal.jpg)


![8. Weryfikacja w pulpicie CCM (IDCC FB)](screens_kreatoridcf/11_ccm_weryfikacja.png)


![Dokument AC FID2-831 w ZP — tabela NTC (EXP 800 / IMP 700), wersja zatwierdzona](screens/ac_zp/image1.png)


![ZP — bilansowe ograniczenia alokacji (intraday): tabela ATC/AAC i panel dokumentów](screens/ac_zp/image2.png)



### TablicaKarty skrócone (kliknij → szczegóły)

📘Proces IDCCKroki istotne dla PSE: IDCC(a) i wspólnie (b)–(d), pliki FIDx, fallbacki.▸ pełna instrukcja

📧Szablony maili19 szablonów operacyjnych Core ID (EN) + kiedy użyć; oznaczone granice PSE.▸ pełna instrukcja

🧰NarzędziaCCM, Core CC Tool, Perun4V, MinIO, ZP, Connector, Kreatory, sFTP, wsparcie.▸ pełna instrukcja

🎨Legenda statusów13 kafelków → enum statusu. Kolor + znacznik = sytuacja pliku.▸ pełna instrukcja

🗂️Katalog plików FIDx126 plików: opis, ścieżka, źródło, TET/CET, profil + warianty stanów.▸ pełna instrukcja

🖥️Czynności w CCMC.1–C.5: pulpit, info, wysyłka przed/po CET, status ręczny, błędy walidacji.▸ pełna instrukcja

✅Walidacja domeny — NORTryb normalny DA: schemat decyzyjny, Perun4V, raporty CNEC/LTA.▸ pełna instrukcja

🛟Walidacja domeny — BUPTryb backup DA: CCA, F320, paczki ZIP, redukcja IVA, RLTA w ZP.▸ pełna instrukcja

🔑GLSK (FIDx-607) — stany32 stany kafelka: sukces, w toku, błędy, wysyłka ręczna.▸ pełna instrukcja

🛠️Kreator IDCFPublikacja GLSK/CBCORA/RA → Connector → MinIO → weryfikacja w CCM.▸ pełna instrukcja

📄AC w ZP (FIDx-831)Ręczna obsługa Allocation Constraints, tabela NTC/ATC, wersjonowanie.▸ pełna instrukcja

🧭Procedury P01–P06Reagowanie na ryzyka + procedury narzędziowe krok po kroku.▸ pełna instrukcja

⚠️Ryzyka U01–U23Katalog ryzyk, kody ACK, ścieżka zgłoszenia: CIZ / WPO / PSE-I.▸ pełna instrukcja

🗄️Buckety MinIO + mapa relacjiPełna mapa lokalizacji plików; narzędzie ↔ ryzyko ↔ procedura.▸ pełna instrukcja



### 1Proces IDCC — kroki istotne dla PSE (BPD)

**Skrót / powiązane**

▸ katalog plików

▸ statusy

IDCC (Intraday Capacity Calculation) — cykliczne, śróddzienne wyznaczanie zdolności przesyłowych w regionie Core. PSE jako TSO dostarcza dane wejściowe, monitoruje strumienie plików i interweniuje przy awariach.



#### Iteracje procesu

| Iteracja | Charakter | Zakres |
| --- | --- | --- | --- | --- |
| IDCC(a) | Pełny przebieg centralny + wyznaczanie ATC | AC, ATC Based Validation, Final NTC |
| IDCC(b)–(d) | Kolejne iteracje śróddzienne (ID2/ID3C/ID3) | GLSK, CGM, RefProg, CB, IVA, NTC, paczki PERUN |



#### Wejścia PSE i bramki czasowe

Każdy plik ma

**TET**

(Target End Time — cel) i

**CET**

(Critical End Time — twardy deadline). Statusy i działania zależą od relacji do tych bramek — patrz

legenda

i

katalog plików

.



#### Opis procesu — kroki istotne dla PSE

Na podstawie

*Core IDCC Flow-Based Business Process Documentation v5.0*

(02-03-2026). Tylko kroki, w których PSE działa lub jest adresatem; nazwy pod-procesów pozostawione po angielsku, IDCC(b)–(d) opisane wspólnie (różnice w tabeli). Kody plików w notacji FIDx.

**Opis procesu — skok do:**

▸ Skróty i pliki PSE

▸ IDCC(a)

▸ IDCC(b)–(d)

▸ Szablony maili

PSE — skróty, zakres i pliki wejściowe

Skróty i pojęcia

SkrótRozwinięcie

IVAIndividual Validation Adjustment
RAMRemaining Available Margin
FRMFlow Reliability Margin
FmaxMaximum allowable flow on a critical branch
CGMCommon Grid Model (scalony model sieci)
IGMIndividual Grid Model (model PSE)
AACAlready Allocated Capacity
NTCNet Transfer Capacity
ATCAvailable Transfer Capacity
PTDFPower Transfer Distribution Factor
RefProgReference Program (założone net positions per strefa)
SARSecurity Analysis Result
CGMESCommon Grid Model Exchange Standard
DACFDay-Ahead Congestion Forecast
IDCFIntraday Congestion Forecast
MCPMarket Coupling Process
CCCtCore Capacity Calculation Tool
TETTarget End Time (limit wysłania danych)
CETCritical End Time (ostateczny termin; ryzyko decouplingu)
GLSKGeneration Load Shift Key
CB / CNECCritical Branch / Critical Network Element and Contingency

Zakres PSE i bramki czasowe

Dostarczenie IGM do RCC (serwer Swissgrid → TSCNET) przed target run DACF/IDCF — tylko IDCC(b)–(d); IDCC(a) tego nie wymaga.
Dostarczenie CB (FIDx-617) i GLSK (FIDx-607) do CCCt w fazie TSO Data Gathering (oba MANDATORY).
Walidacja FBA w Perun4V (publikacja IVA, FIDx-710) oraz monitoring walidacji ATC (FIDx-928) i IVA BACKUP.
Publikacja AC (FIDx-831) do PuTo jako wynik procesu; monitoring finalnych NTC (FIDx-921).
TET = limit wysłania pliku; po jego przekroczeniu uruchamiany jest backup. CET = termin ostateczny — niedotrzymanie grozi decouplingiem rynku dla danej doby.
Notacja czasów w tabeli poniżej: TET / CET (godzina lokalna).

Kluczowe pliki PSE per iteracja

Plik (FIDx)Co toŹródłoIteracjaTET / CET

CB / CBCORA (-617)Critical Branches — CNEC-y PSEKreator(b)/(c)/(d)20:00/20:19 · 00:00/00:56 · 06:20/07:30
GLSK (-607)Generation Load Shift Keys strefy PLKreator(b)/(c)/(d)20:00/20:19 · 00:00/00:56 · 06:20/07:30
IGM/CGM DACF (-620)Merged DACF/IDCF Common Grid Modelproces Core / Kreator(b)/(c)/(d)20:40/21:05 · 02:40/03:30 · 08:30/09:05
RefProg (-632)Reference Program — net positionsproces Core(b)/(c)/(d)20:40/21:05 · 02:40/03:30 · 08:30/09:05
IVA (-710)Individual Validation Adjustment (FBA)Perun4V / CCA backup(b)/(c)/(d)21:30/22:06 · 04:00/04:36 · 09:30/10:06
ATC validation (-928)ATC Based ValidationCore CC Tool(a)/(b)/(c)/(d)13:40/14:20 · 21:40/22:05 · 03:10/03:50 · 08:45/09:20
AC (-831)Allocation Constraints → PuToZP(a)/(b)/(c)/(d)13:50/14:45 · 21:45/21:55 · 04:15/04:25 · 08:40/09:25
Final NTC (-921)Finalne wyniki NTC z IDCCproces Core(a)/(b)/(c)/(d)14:45/14:55 · 21:45/21:49 · 04:15/04:30 · 09:20/09:45

Prefiks kodu = iteracja:

=IDCC(a),

=IDCC(b),

=IDCC(c),

=IDCC(d).

IDCC(a) — kroki istotne dla PSE

PSE działa jako jeden z TSO regionu Core. Poniżej tylko kroki, w których PSE dostarcza dane, waliduje, wysyła pliki lub działa na swoich granicach (50Hertz–PSE, CEPS–PSE, SEPS–PLC). Kroki czysto centralne (CCC/Coreso/RCC), których PSE nie dotyczą, pominięto.

Distribution of Initial Data

CCC wysyła do XBID pliki high-negative NTC (test komunikacji). Krok obejmuje zdolności na granicach PSE — działania wykonuje CCC, a PSE monitoruje wynik na swoich granicach. Przy braku lub negatywnym ACK dla high-negative NTC (FID1-921) CCC stosuje fallback

i informuje mailem #1.

Open gates for AC (Allocation Constraints)

PSE dostarcza plik

(ograniczenia alokacyjne wyznaczone przez PSE). Ścieżka: ZP → Connector 2.0 → Core CC Tool → PuTo. TET 13:50, CET 14:45.

MCR Data Gathering — Shadow Auction Results (przy decouplingu SDAC)

Przy (częściowym) decouplingu na granicach Core PSE otrzymuje mailowe przypomnienie o obowiązku dostarczenia

przez ECP/EDX. Deadline 1: TET 15:43; deadline 2 (przypomnienie): CET 17:24. Po 17:24 PSE wprowadza brakujące DA AAC bezpośrednio w XBID. Fallbacki:

(mail #20 — wezwanie do MD250),

/

(przy błędzie liczenia PSE/TSO dostarcza AAC do XBID, mail #2),

(TSO uploaduje AAC do XBID).

Individual CB and ATC validation

PSE prowadzi

(we własnym zakresie, np. Perun) — czy zdolności nie naruszają granic bezpieczeństwa we własnym obszarze i czy da się temu zapobiec środkami zaradczymi. Okno 40 min, walidacja zawsze min. 25 min nawet w fallbacku/opóźnieniu. PSE musi uwzględnić pliki

(plik zwrotny z walidacji ATC, Core CC Tool → Connector 2.0 → CCM; TET 13:40, CET 14:20). PSE może aktualizować EC/ATC (MD609) dla wirtualnych hubów do końca okna. Fallback opóźnienia okna:

(pauza + wznowienie, zapewnienie 25 min).

Final ID ATC extraction

Otwierane są bramki, w których PSE może dostarczyć indywidualne EC/ATC. Wynik finalny to

(oraz ID1-921-XX per granica), wysyłany do XBID (TET 14:45, CET 14:55, kanał zapasowy sFTP). Uwaga: TSO po obu stronach granicy (w tym PSE) współodpowiadają za sprawdzenie poprawności zdolności wgranych na swojej granicy i potwierdzenie ich do CCC. Fallbacki dotyczące dostarczenia NTC do XBID — patrz tabela poniżej.

Changing individual factors (rLTAincl / rAmrId)

Krok wewnętrzny PSE. PSE może zmienić swoje parametry redukcji wirtualnych zdolności. Harmonogram: D-14 poinformować pozostałych TSO przez Core CCB; D-7 opublikować Market Message do interesariuszy zewnętrznych + NRA; D wprowadzić zmianę w ekstrakcji ATC na poziomie obszaru i granicy (rLTA).

General Fallbacks — przejęcie procesu przez PSE

Gdy ID CCCt jest down i proces oddany TSO: PSE dostarcza policzone AAC do XBID lokalnym narzędziem najpóźniej do 20:00 (warunek startu IDCC(b)) i potwierdza ich obecność do CCC (

). Przy problemie EDX/ECP PSE↔CCCt — PSE informuje USY/CCC i ręcznie wgrywa wejścia przez Message Viewer lub mailem do CCC (

).

KodSytuacjaDziałanie PSEMail #



ID1_1
Brak / negatywny ACK dla high-negative NTC (FID1-921)
Działania po stronie CCC (ponawia wysyłkę przez sFTP i czeka na ACK); PSE monitoruje wynik na swoich granicach
1


ID1_7
Decoupling SDAC — wymagane Shadow Auction (MD250 / FID1-250)
PSE dostarcza MD250 do CCCt (TET 15:43, CET 17:24); po 17:24 brakujące DA AAC bezpośrednio w XBID
20


ID1_8
Błąd obliczeń AAC — przejęcie procesu
PSE otrzymuje wezwanie i przejmuje IDCC(a); dostarcza AAC do XBID
2


ID1_9
Błąd obliczeń AAC
PSE/TSO wgrywa policzone AAC do XBID
—


ID1_12
Brak rozwiązania dla policzonych AAC
PSE (dotknięty TSO) wgrywa AAC do XBID
—


ID1_16
Opóźnione okno walidacji (zapewnienie 25 min)
PSE prowadzi walidację min. 25 min mimo opóźnienia; okno jest pauzowane i wznawiane
—


ID1_23
Brak / negatywny ACK dla NTC (FID1-921) na granicy
PSE (TSO na granicy) współsprawdza poprawność NTC na swojej granicy i potwierdza do CCC
12, 7


ID1_26
ID CCCt down — proces oddany TSO
PSE dostarcza policzone AAC do XBID lokalnym narzędziem do 20:00; potwierdza obecność AAC do CCC
—


ID1_27
Problem EDX/ECP między PSE a CCCt
PSE informuje USY/CCC i ręcznie wgrywa wejścia przez Message Viewer lub przesyła pliki mailem do CCC
—

IDCC(b)–(d) — wspólny przebieg, kroki istotne dla PSE

Procesy

(ID2),

(ID3C) i

(ID3) mają identyczną strukturę pod-procesów. Różnią się jedynie liczbą timestampów (TS), godzinami (TET/CET), prefiksem kodów FID (FID2 / FID3C / FID3) i kodami fallback (ID2_x / ID3C_x / ID3_x). Poniżej opisano przebieg

, z zaznaczeniem różnic. PSE występuje jako

. Pominięto kroki czysto centralne (CCC/Coreso/FBPCM) bez działania PSE.

Różnice między iteracjami

IteracjaPrefiks FIDLiczba TSDeadline AAC (start)NTC do XBID — target / latePo opóźnieniuKody fallback


IDCC(b) / ID2FID2-###24~20:00 (D-1)21:45 / po 21:55restart po IDA2, NTC < 22:30ID2_1 – ID2_25
IDCC(c) / ID3CFID3C-###1802:00 (D-0)(brak osobnego progu late w BPD)—ID3C_1 – ID3C_23
IDCC(d) / ID3FID3-###1207:00 (D-0)09:45 / po 09:55restart po IDA3, NTC < 10:30ID3_1 – ID3_25

TSO Data Gathering

PSE wysyła komplet danych wejściowych dla swojego obszaru. Podstawą jest paczka AAC z XBID (MD830). Pliki PSE z Kreatora IDCF/DACF:

GLSK — Generation and Load Shift Keys, klucze rozdziału generacji/obciążenia strefy PL — FID2-607.
CBCORA — Critical Branches & Outages + Remedial Actions (lista CNEC PSE z wyłączeniami) — FID2-617.
CGM/IGM — 24 indywidualne modele sieci (DACF_IGM_UCT), eksport TSO Data Preparation → Coreso (scalenie do CGM FID2-620).
RefProg — program referencyjny wyznaczany centralnie z AAC grid model, dystrybuowany do PSE — FID2-632.
External Constraints (EC) — PSE może nałożyć ograniczenia na pozycję netto strefy PL (export/import wg wzorów art. 10 ID CCM); funkcja allocation constraints w ID CCt jest niedostępna.
RA / RA Settings, aktualizacje TOPO — środki zaradcze i zmiany topologii IGM.

Pliki przekazywane są przez ECP/EDX lub GUI CCt. Słownik CO aktualizowany w GUI (uwaga: synchronizacja DACC→IDCC o D-1 15:00). Format CB: XML lub XLSX przez konwerter CBCORA.

CGM Data Gathering (pierwszy/drugi/trzeci)

Krok centralny Coreso (scalenie IGM→CGM). Dla PSE istotne: paczka merging jest dostarczana

,

; PSE otrzymuje dystrybucję CGM/RefProg/DA Domain. Działania PSE tylko gdy fallback wymaga ponownej wysyłki IGM.

RefProg Computation

Krok centralny. PSE odbiera wyniki RefProg (

) — wykorzystywane dalej w IVA i jako punkt startowy domeny.

TSO data merging

CCt scala dane wszystkich TSO i odsyła scalone pliki do PSE: Merged GLSK (

), Merged EC, Merged CB, Merged RA Settings, Merged AAC. PSE może

swoje pliki po Data Quality Check (raporty DQC:

dla CGM). Indywidualne przefiltrowane CB PSE:

; Real GLSK:

.

Export CGM at AAC / Initial flow-based computation

Kroki centralne (FBPCM). PSE odbiera wyniki: Initial FB Domain (

), wierzchołki domeny (Vertices,

), Initial Intraday ATC (

) — wejście do walidacji.

Individual Validation (IVA — Perun4V)

PSE samodzielnie waliduje wynik initial FB pod kątem bezpieczeństwa swojego obszaru i ewentualnie koryguje domenę:

Wejście: zagregowana paczka PERUN_ID2 do Perun4V (składowe: Merged GLSK 610, CGM 620, RefProg 632, Initial FB Domain 645, Real GLSK 657, CB 665, Vertices 701, Initial ATC 882, RA).
Walidacja CNEC-based: PSE zmniejsza RAM własnych CNEC, zapisuje korekty + uzasadnienie w pliku IVA (FID2-710) z Perun4V → CCt. IVA stosowane na finalnej domenie FB.
Walidacja ATC-based: PSE ustawia maksymalne ATC na własnych granicach zorientowanych (niższa wartość wygrywa, gdy oba TSO podają wartość).
Okno walidacji ID2: 40 min (TET 21:30 / CET 22:06). Backup IVA generuje CCA (FID2-710, wariant backup) gdy IVA podstawowe brakuje/jest niezgodne.
Raporty z Perun (RAP_PERUN_ID2) — informacyjne.

Final FB Computation

Krok centralny — initial FB aktualizowane o IVA PSE; PSE może też zaktualizować EC. PSE odbiera wyniki i Fallback Report.

ID ATC Extraction (wyniki NTC do XBID)

Wyznaczenie ATC/NTC na bazie najnowszych AAC. PSE odbiera ATC/NTC dla swoich granic (

= Final NTC,

= ATC).

przy ręcznej wysyłce NTC do XBID (sFTP) lub problemie z ACK — TSO po obu stronach granicy sprawdzają poprawność zdolności na swojej granicy. Opóźnienia: patrz tabela różnic (ID2 21:45/21:55; ID3 09:45/09:55).

Export CGM at AAC / Nodal PTDF / Translate Domain to AAC / Net Positions / Distribute Inputs

Kroki centralne (FBPCM). PSE odbiera produkty: CGM at AAC, GLSK Nodal PTDFs (

), AAC FB Domain (

), DQC (990), logi. Brak aktywnego działania PSE poza odbiorem.

Fallbacki istotne dla PSE / TSO

KodIteracja (krok)SytuacjaDziałanie PSE / TSOMail #


ID2_4 / ID3C_4 / ID3_4TSO Data GatheringBrak policzonych AAC z IDCC(a)PSE dostarcza AAC do XBID lokalnym narzędziem przed deadline (ID2 20:00 / ID3C 02:00 / ID3 07:00) i potwierdza CCC obecność AAC w XBID—
ID2_6 / ID3C_6 / ID3_6TSO data mergingBrak obowiązkowego pliku wejściowegoCCC dzwoni do PSE z prośbą o dostarczenie pliku przed CET; PSE dosyła4
ID2_7 / ID3C_7 / ID3_7TSO data mergingBrak/błędny indywidualny GLSK PSEPSE proponuje strategię zastąpienia (replacement) lub poprawia; w razie braku — BD blocked, proces z Fallback Domain3
ID2_8 / ID3C_8 / ID3_8TSO data mergingBrak/błędny indywidualny EC PSEPSE proponuje zastąpienie / poprawia; inaczej Fallback Domain3
ID2_9 / ID3C_9 / ID3_9TSO data mergingBrak/błędny indywidualny plik CB PSEPSE proponuje zastąpienie / poprawia; inaczej Fallback Domain3
ID2_11 / ID3C_11 / ID3_11Initial FB computationFallback zastosowany dla części TSPSE otrzymuje mail z listą TS objętych fallbackiem — bez działań, przyjąć do wiadomości5
ID2_13 / ID3C_13 / ID3_13Final FB computationFallback zastosowany dla części TSPSE otrzymuje mail z listą TS objętych fallbackiem — bez działań, przyjąć do wiadomości5
ID2_15 / ID3_15ID ATC ExtractionNTC po targecie (ID2 21:45 / ID3 09:45)PSE otrzymuje informację; do rynku publikowany jest UMMID2: 24,22 / ID3: 23,22
ID2_16 / ID3_16ID ATC ExtractionNTC po 21:55 / 09:55 — opóźnienie po IDA2/IDA3PSE otrzymuje informację; publikowany jest UMM o opóźnieniu zdolności32,33
ID2_17 / ID3C_15 / ID3_17ID ATC ExtractionNieudana ekstrakcja ATCPSE otrzymuje informację mailem; publikowany jest UMMID2: 2,27 / ID3C: 2,28 / ID3: 2,29
ID2_19 / ID3C_17 / ID3_19ID ATC ExtractionBrak/negatywny ACK dla NTC (921)Współodpowiedzialność PSE: TSO po obu stronach granicy weryfikują poprawność zdolności w XBID i potwierdzają do CCC12,7
ID2_23 / ID3C_21 / ID3_23Cały procesID CCt niedostępny w CET dowolnego krokuPSE otrzymuje informację mailem o awarii; publikowany jest UMMID2: 2,27 / ID3C: 2,28 / ID3: 2,29
ID2_24 / ID3C_22 / ID3_24Cały procesProblem EDX/ECP TSO↔CCtOperator PSE zgłasza do USY/CCC i ręcznie wgrywa dane do CCt (Message Viewer) lub przesyła pliki do CCC mailem—

Szablony maili operacyjnych (Core ID)

Gotowe wzory maili (PL: tylko podtytuł „Kiedy"; treść maili pozostaje po angielsku — to realne komunikaty operacyjne wysyłane w Core ID1/ID2). Szablony oznaczone „⚑ dotyczy granic PSE" zawierają w tabeli granice z udziałem PSE: 50Hertz-PSE, CEPS-PSE oraz SEPS-PLC.



#### PSE — skróty, zakres i pliki wejściowe



##### Skróty i pojęcia

| Skrót | Rozwinięcie |
| --- | --- | --- | --- |
| IVA | Individual Validation Adjustment |
| RAM | Remaining Available Margin |
| FRM | Flow Reliability Margin |
| Fmax | Maximum allowable flow on a critical branch |
| CGM | Common Grid Model (scalony model sieci) |
| IGM | Individual Grid Model (model PSE) |
| AAC | Already Allocated Capacity |
| NTC | Net Transfer Capacity |
| ATC | Available Transfer Capacity |
| PTDF | Power Transfer Distribution Factor |
| RefProg | Reference Program (założone net positions per strefa) |
| SAR | Security Analysis Result |
| CGMES | Common Grid Model Exchange Standard |
| DACF | Day-Ahead Congestion Forecast |
| IDCF | Intraday Congestion Forecast |
| MCP | Market Coupling Process |
| CCCt | Core Capacity Calculation Tool |
| TET | Target End Time (limit wysłania danych) |
| CET | Critical End Time (ostateczny termin; ryzyko decouplingu) |
| GLSK | Generation Load Shift Key |
| CB / CNEC | Critical Branch / Critical Network Element and Contingency |



##### Zakres PSE i bramki czasowe

Dostarczenie

do RCC (serwer Swissgrid → TSCNET) przed target run DACF/IDCF — tylko IDCC(b)–(d); IDCC(a) tego nie wymaga.

Dostarczenie

i

do CCCt w fazie TSO Data Gathering (oba MANDATORY).

Walidacja FBA w Perun4V (publikacja

) oraz monitoring walidacji ATC (FIDx-928) i IVA BACKUP.

Publikacja

do PuTo jako wynik procesu; monitoring finalnych

.

= limit wysłania pliku; po jego przekroczeniu uruchamiany jest backup.

= termin ostateczny — niedotrzymanie grozi decouplingiem rynku dla danej doby.

Notacja czasów w tabeli poniżej:

(godzina lokalna).



##### Kluczowe pliki PSE per iteracja

| Plik (FIDx) | Co to | Źródło | Iteracja | TET / CET |
| --- | --- | --- | --- | --- | --- | --- |
| CB / CBCORA (-617) | Critical Branches — CNEC-y PSE | Kreator | (b)/(c)/(d) | 20:00/20:19 · 00:00/00:56 · 06:20/07:30 |
| GLSK (-607) | Generation Load Shift Keys strefy PL | Kreator | (b)/(c)/(d) | 20:00/20:19 · 00:00/00:56 · 06:20/07:30 |
| IGM/CGM DACF (-620) | Merged DACF/IDCF Common Grid Model | proces Core / Kreator | (b)/(c)/(d) | 20:40/21:05 · 02:40/03:30 · 08:30/09:05 |
| RefProg (-632) | Reference Program — net positions | proces Core | (b)/(c)/(d) | 20:40/21:05 · 02:40/03:30 · 08:30/09:05 |
| IVA (-710) | Individual Validation Adjustment (FBA) | Perun4V / CCA backup | (b)/(c)/(d) | 21:30/22:06 · 04:00/04:36 · 09:30/10:06 |
| ATC validation (-928) | ATC Based Validation | Core CC Tool | (a)/(b)/(c)/(d) | 13:40/14:20 · 21:40/22:05 · 03:10/03:50 · 08:45/09:20 |
| AC (-831) | Allocation Constraints → PuTo | ZP | (a)/(b)/(c)/(d) | 13:50/14:45 · 21:45/21:55 · 04:15/04:25 · 08:40/09:25 |
| Final NTC (-921) | Finalne wyniki NTC z IDCC | proces Core | (a)/(b)/(c)/(d) | 14:45/14:55 · 21:45/21:49 · 04:15/04:30 · 09:20/09:45 |

Prefiks kodu = iteracja:

`FID1`

=IDCC(a),

`FID2`

=IDCC(b),

`FID3C`

=IDCC(c),

`FID3`

=IDCC(d).



#### IDCC(a) — kroki istotne dla PSE

PSE działa jako jeden z TSO regionu Core. Poniżej tylko kroki, w których PSE dostarcza dane, waliduje, wysyła pliki lub działa na swoich granicach (50Hertz–PSE, CEPS–PSE, SEPS–PLC). Kroki czysto centralne (CCC/Coreso/RCC), których PSE nie dotyczą, pominięto.



##### Distribution of Initial Data

CCC wysyła do XBID pliki high-negative NTC (test komunikacji). Krok obejmuje zdolności na granicach PSE — działania wykonuje CCC, a PSE monitoruje wynik na swoich granicach. Przy braku lub negatywnym ACK dla high-negative NTC (FID1-921) CCC stosuje fallback

`ID1_1`

i informuje mailem #1.



##### Open gates for AC (Allocation Constraints)

PSE dostarcza plik

**AC — Allocation Constraints (FID1-831)**

(ograniczenia alokacyjne wyznaczone przez PSE). Ścieżka: ZP → Connector 2.0 → Core CC Tool → PuTo. TET 13:50, CET 14:45.



##### MCR Data Gathering — Shadow Auction Results (przy decouplingu SDAC)

Przy (częściowym) decouplingu na granicach Core PSE otrzymuje mailowe przypomnienie o obowiązku dostarczenia

**MD250 — Shadow Auction Results
(FID1-250)**

przez ECP/EDX. Deadline 1: TET 15:43; deadline 2 (przypomnienie): CET 17:24. Po 17:24 PSE wprowadza brakujące DA AAC bezpośrednio w XBID. Fallbacki:

`ID1_7`

(mail #20 — wezwanie do MD250),

`ID1_8`

/

`ID1_9`

(przy błędzie liczenia PSE/TSO dostarcza AAC do XBID, mail #2),

`ID1_12`

(TSO uploaduje AAC do XBID).



##### Individual CB and ATC validation

PSE prowadzi

**indywidualną walidację**

(we własnym zakresie, np. Perun) — czy zdolności nie naruszają granic bezpieczeństwa we własnym obszarze i czy da się temu zapobiec środkami zaradczymi. Okno 40 min, walidacja zawsze min. 25 min nawet w fallbacku/opóźnieniu. PSE musi uwzględnić pliki

**FID1-928 — ATC Based Validation**

(plik zwrotny z walidacji ATC, Core CC Tool → Connector 2.0 → CCM; TET 13:40, CET 14:20). PSE może aktualizować EC/ATC (MD609) dla wirtualnych hubów do końca okna. Fallback opóźnienia okna:

`ID1_16`

(pauza + wznowienie, zapewnienie 25 min).



##### Final ID ATC extraction

Otwierane są bramki, w których PSE może dostarczyć indywidualne EC/ATC. Wynik finalny to

**FID1-921 — Final Intraday NTC**

(oraz ID1-921-XX per granica), wysyłany do XBID (TET 14:45, CET 14:55, kanał zapasowy sFTP). Uwaga: TSO po obu stronach granicy (w tym PSE) współodpowiadają za sprawdzenie poprawności zdolności wgranych na swojej granicy i potwierdzenie ich do CCC. Fallbacki dotyczące dostarczenia NTC do XBID — patrz tabela poniżej.



##### Changing individual factors (rLTAincl / rAmrId)

Krok wewnętrzny PSE. PSE może zmienić swoje parametry redukcji wirtualnych zdolności. Harmonogram: D-14 poinformować pozostałych TSO przez Core CCB; D-7 opublikować Market Message do interesariuszy zewnętrznych + NRA; D wprowadzić zmianę w ekstrakcji ATC na poziomie obszaru i granicy (rLTA).



##### General Fallbacks — przejęcie procesu przez PSE

Gdy ID CCCt jest down i proces oddany TSO: PSE dostarcza policzone AAC do XBID lokalnym narzędziem najpóźniej do 20:00 (warunek startu IDCC(b)) i potwierdza ich obecność do CCC (

`ID1_26`

). Przy problemie EDX/ECP PSE↔CCCt — PSE informuje USY/CCC i ręcznie wgrywa wejścia przez Message Viewer lub mailem do CCC (

`ID1_27`

).

| Kod | Sytuacja | Działanie PSE | Mail # |
| --- | --- | --- | --- | --- | --- |
| ID1_1 | Brak / negatywny ACK dla high-negative NTC (FID1-921) | Działania po stronie CCC (ponawia wysyłkę przez sFTP i czeka na ACK); PSE monitoruje wynik na swoich granicach | 1 |
| ID1_7 | Decoupling SDAC — wymagane Shadow Auction (MD250 / FID1-250) | PSE dostarcza MD250 do CCCt (TET 15:43, CET 17:24); po 17:24 brakujące DA AAC bezpośrednio w XBID | 20 |
| ID1_8 | Błąd obliczeń AAC — przejęcie procesu | PSE otrzymuje wezwanie i przejmuje IDCC(a); dostarcza AAC do XBID | 2 |
| ID1_9 | Błąd obliczeń AAC | PSE/TSO wgrywa policzone AAC do XBID | — |
| ID1_12 | Brak rozwiązania dla policzonych AAC | PSE (dotknięty TSO) wgrywa AAC do XBID | — |
| ID1_16 | Opóźnione okno walidacji (zapewnienie 25 min) | PSE prowadzi walidację min. 25 min mimo opóźnienia; okno jest pauzowane i wznawiane | — |
| ID1_23 | Brak / negatywny ACK dla NTC (FID1-921) na granicy | PSE (TSO na granicy) współsprawdza poprawność NTC na swojej granicy i potwierdza do CCC | 12, 7 |
| ID1_26 | ID CCCt down — proces oddany TSO | PSE dostarcza policzone AAC do XBID lokalnym narzędziem do 20:00; potwierdza obecność AAC do CCC | — |
| ID1_27 | Problem EDX/ECP między PSE a CCCt | PSE informuje USY/CCC i ręcznie wgrywa wejścia przez Message Viewer lub przesyła pliki mailem do CCC | — |



#### IDCC(b)–(d) — wspólny przebieg, kroki istotne dla PSE

Procesy

**IDCC(b)**

(ID2),

**IDCC(c)**

(ID3C) i

**IDCC(d)**

(ID3) mają identyczną strukturę pod-procesów. Różnią się jedynie liczbą timestampów (TS), godzinami (TET/CET), prefiksem kodów FID (FID2 / FID3C / FID3) i kodami fallback (ID2_x / ID3C_x / ID3_x). Poniżej opisano przebieg

**raz**

, z zaznaczeniem różnic. PSE występuje jako

**TSO**

. Pominięto kroki czysto centralne (CCC/Coreso/FBPCM) bez działania PSE.



##### Różnice między iteracjami

| Iteracja | Prefiks FID | Liczba TS | Deadline AAC (start) | NTC do XBID — target / late | Po opóźnieniu | Kody fallback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IDCC(b) / ID2 | FID2-### | 24 | ~20:00 (D-1) | 21:45 / po 21:55 | restart po IDA2, NTC < 22:30 | ID2_1 – ID2_25 |
| IDCC(c) / ID3C | FID3C-### | 18 | 02:00 (D-0) | (brak osobnego progu late w BPD) | — | ID3C_1 – ID3C_23 |
| IDCC(d) / ID3 | FID3-### | 12 | 07:00 (D-0) | 09:45 / po 09:55 | restart po IDA3, NTC < 10:30 | ID3_1 – ID3_25 |

*Kody FID poniżej podano w wariancie FID2-### (ID2). Dla ID3C/ID3 podstaw prefiks FID3C-### / FID3-### przy tym samym numerze (np. GLSK = FID2-607 / FID3C-607 / FID3-607).*



##### TSO Data Gathering

PSE wysyła komplet danych wejściowych dla swojego obszaru. Podstawą jest paczka AAC z XBID (MD830). Pliki PSE z Kreatora IDCF/DACF:

— Generation and Load Shift Keys, klucze rozdziału generacji/obciążenia strefy PL —

.

— Critical Branches & Outages + Remedial Actions (lista CNEC PSE z wyłączeniami) —

.

— 24 indywidualne modele sieci (DACF_IGM_UCT), eksport TSO Data Preparation → Coreso (scalenie do CGM

).

— program referencyjny wyznaczany centralnie z AAC grid model, dystrybuowany do PSE —

.

— PSE może nałożyć ograniczenia na pozycję netto strefy PL (export/import wg wzorów art. 10 ID CCM); funkcja allocation constraints w ID CCt jest niedostępna.

— środki zaradcze i zmiany topologii IGM.

Pliki przekazywane są przez ECP/EDX lub GUI CCt. Słownik CO aktualizowany w GUI (uwaga: synchronizacja DACC→IDCC o D-1 15:00). Format CB: XML lub XLSX przez konwerter CBCORA.



##### CGM Data Gathering (pierwszy/drugi/trzeci)

Krok centralny Coreso (scalenie IGM→CGM). Dla PSE istotne: paczka merging jest dostarczana

**3× dla ID2**

,

**2× dla ID3C/ID3**

; PSE otrzymuje dystrybucję CGM/RefProg/DA Domain. Działania PSE tylko gdy fallback wymaga ponownej wysyłki IGM.



##### RefProg Computation

Krok centralny. PSE odbiera wyniki RefProg (

**FID2-632**

) — wykorzystywane dalej w IVA i jako punkt startowy domeny.



##### TSO data merging

CCt scala dane wszystkich TSO i odsyła scalone pliki do PSE: Merged GLSK (

**FID2-610**

), Merged EC, Merged CB, Merged RA Settings, Merged AAC. PSE może

**poprawić i ponownie wysłać**

swoje pliki po Data Quality Check (raporty DQC:

**FID2-659**

dla CGM). Indywidualne przefiltrowane CB PSE:

**FID2-665**

; Real GLSK:

**FID2-657**

.



##### Export CGM at AAC / Initial flow-based computation

Kroki centralne (FBPCM). PSE odbiera wyniki: Initial FB Domain (

**FID2-645**

), wierzchołki domeny (Vertices,

**FID2-701**

), Initial Intraday ATC (

**FID2-882**

) — wejście do walidacji.



##### Individual Validation (IVA — Perun4V)

**Kluczowy krok PSE.**

PSE samodzielnie waliduje wynik initial FB pod kątem bezpieczeństwa swojego obszaru i ewentualnie koryguje domenę:

Wejście: zagregowana paczka

do Perun4V (składowe: Merged GLSK 610, CGM 620, RefProg 632, Initial FB Domain 645, Real GLSK 657, CB 665, Vertices 701, Initial ATC 882, RA).

PSE zmniejsza RAM własnych CNEC, zapisuje korekty + uzasadnienie w pliku

z Perun4V → CCt. IVA stosowane na finalnej domenie FB.

PSE ustawia maksymalne ATC na własnych granicach zorientowanych (niższa wartość wygrywa, gdy oba TSO podają wartość).

Okno walidacji ID2:

(TET 21:30 / CET 22:06). Backup IVA generuje CCA (

, wariant backup) gdy IVA podstawowe brakuje/jest niezgodne.

Raporty z Perun (RAP_PERUN_ID2) — informacyjne.



##### Final FB Computation

Krok centralny — initial FB aktualizowane o IVA PSE; PSE może też zaktualizować EC. PSE odbiera wyniki i Fallback Report.



##### ID ATC Extraction (wyniki NTC do XBID)

Wyznaczenie ATC/NTC na bazie najnowszych AAC. PSE odbiera ATC/NTC dla swoich granic (

**FID2-921**

= Final NTC,

**FID2-922**

= ATC).

**Współodpowiedzialność PSE:**

przy ręcznej wysyłce NTC do XBID (sFTP) lub problemie z ACK — TSO po obu stronach granicy sprawdzają poprawność zdolności na swojej granicy. Opóźnienia: patrz tabela różnic (ID2 21:45/21:55; ID3 09:45/09:55).



##### Export CGM at AAC / Nodal PTDF / Translate Domain to AAC / Net Positions / Distribute Inputs

Kroki centralne (FBPCM). PSE odbiera produkty: CGM at AAC, GLSK Nodal PTDFs (

**FID2-935**

), AAC FB Domain (

**FID2-936**

), DQC (990), logi. Brak aktywnego działania PSE poza odbiorem.



##### Fallbacki istotne dla PSE / TSO

| Kod | Iteracja (krok) | Sytuacja | Działanie PSE / TSO | Mail # |
| --- | --- | --- | --- | --- | --- | --- |
| ID2_4 / ID3C_4 / ID3_4 | TSO Data Gathering | Brak policzonych AAC z IDCC(a) | PSE dostarcza AAC do XBID lokalnym narzędziem przed deadline (ID2 20:00 / ID3C 02:00 / ID3 07:00) i potwierdza CCC obecność AAC w XBID | — |
| ID2_6 / ID3C_6 / ID3_6 | TSO data merging | Brak obowiązkowego pliku wejściowego | CCC dzwoni do PSE z prośbą o dostarczenie pliku przed CET; PSE dosyła | 4 |
| ID2_7 / ID3C_7 / ID3_7 | TSO data merging | Brak/błędny indywidualny GLSK PSE | PSE proponuje strategię zastąpienia (replacement) lub poprawia; w razie braku — BD blocked, proces z Fallback Domain | 3 |
| ID2_8 / ID3C_8 / ID3_8 | TSO data merging | Brak/błędny indywidualny EC PSE | PSE proponuje zastąpienie / poprawia; inaczej Fallback Domain | 3 |
| ID2_9 / ID3C_9 / ID3_9 | TSO data merging | Brak/błędny indywidualny plik CB PSE | PSE proponuje zastąpienie / poprawia; inaczej Fallback Domain | 3 |
| ID2_11 / ID3C_11 / ID3_11 | Initial FB computation | Fallback zastosowany dla części TS | PSE otrzymuje mail z listą TS objętych fallbackiem — bez działań, przyjąć do wiadomości | 5 |
| ID2_13 / ID3C_13 / ID3_13 | Final FB computation | Fallback zastosowany dla części TS | PSE otrzymuje mail z listą TS objętych fallbackiem — bez działań, przyjąć do wiadomości | 5 |
| ID2_15 / ID3_15 | ID ATC Extraction | NTC po targecie (ID2 21:45 / ID3 09:45) | PSE otrzymuje informację; do rynku publikowany jest UMM | ID2: 24,22 / ID3: 23,22 |
| ID2_16 / ID3_16 | ID ATC Extraction | NTC po 21:55 / 09:55 — opóźnienie po IDA2/IDA3 | PSE otrzymuje informację; publikowany jest UMM o opóźnieniu zdolności | 32,33 |
| ID2_17 / ID3C_15 / ID3_17 | ID ATC Extraction | Nieudana ekstrakcja ATC | PSE otrzymuje informację mailem; publikowany jest UMM | ID2: 2,27 / ID3C: 2,28 / ID3: 2,29 |
| ID2_19 / ID3C_17 / ID3_19 | ID ATC Extraction | Brak/negatywny ACK dla NTC (921) | Współodpowiedzialność PSE: TSO po obu stronach granicy weryfikują poprawność zdolności w XBID i potwierdzają do CCC | 12,7 |
| ID2_23 / ID3C_21 / ID3_23 | Cały proces | ID CCt niedostępny w CET dowolnego kroku | PSE otrzymuje informację mailem o awarii; publikowany jest UMM | ID2: 2,27 / ID3C: 2,28 / ID3: 2,29 |
| ID2_24 / ID3C_22 / ID3_24 | Cały proces | Problem EDX/ECP TSO↔CCt | Operator PSE zgłasza do USY/CCC i ręcznie wgrywa dane do CCt (Message Viewer) lub przesyła pliki do CCC mailem | — |



#### Szablony maili operacyjnych (Core ID)

Gotowe wzory maili (PL: tylko podtytuł „Kiedy"; treść maili pozostaje po angielsku — to realne komunikaty operacyjne wysyłane w Core ID1/ID2). Szablony oznaczone „⚑ dotyczy granic PSE" zawierają w tabeli granice z udziałem PSE: 50Hertz-PSE, CEPS-PSE oraz SEPS-PLC.

01 — Critical issue in CCCt

Gdy w narzędziu CCCt wystąpi krytyczny problem i operator musi zgłosić go do Core Helpdesk.

FromCCC Operator
ToCore ID Helpdesk
Subject[CORE_ID_01] Critical issue in CCCt

02 — Failed process ⚑ dotyczy granic PSE

Gdy proces CCCt zakończy się niepowodzeniem przed Critical End Time i TSO muszą dostarczyć zdolności przesyłowe lokalnymi narzędziami do XBID.

FromCCC Operator
ToOperational List
Subject[CORE_ID_02] ID1/ID2 – CCCt process failed for BD XX.XX

03 — Replaced input data

Gdy blisko Critical End Time brakuje obowiązkowego pliku wejściowego i strona odpowiedzialna zastępuje brakujące dane danymi z innej doby, aby nie zerwać BD.

FromCCC Operator
ToOperational List
Subject[CORE_ID_03] ID1/ID2 – Input data replaced BD XX.XX

04 — Warning: file missing

Ostrzeżenie o braku pliku wejściowego przy Target End Time bez możliwości zastąpienia — jeśli plik nie dotrze, obliczenia przejdą w tryb fallback.

FromCCC Operator
ToOperational List
Subject[CORE_ID_04] ID1/ID2 – Warning! Missing file for BD XX.XX

05 — Application of fallbacks with CCCt

Gdy któryś krok obliczeniowy CCCt zakończył się z zastosowaniem fallbacku dla wskazanych godzin doby.

FromCCC Operator
ToOperational List
Subject[CORE_ID_05] ID1/ID2 – Fallback applied with CCCt BD XX.XX

06 — Back-up operator appointed to operate the CCCt

Gdy z powodu niedostępności operatora CCC rolę operatora CCCt przejmuje strona zapasowa (back-up).

FromCCC Operator
ToOperational List
Subject[CORE_ID_06] ID1/ID2 – Back-up operator X appointed to operate the CCCt for BD XX.XX

07 — Distribution of NTCs via sFTP ⚑ dotyczy granic PSE

Gdy NTC/High Neg. NTC zostały wysłane do XBID kanałem zapasowym (sFTP) po awarii ECP i TSO mają zweryfikować ich obecność w XBID.

FromCCC Operator
ToOperational List
Subject[CORE_ID_07] ID1/ID2 – Distribution of High Neg. NTCs/NTCs to XBID via secondary channel for BD XX.XX

08 — Distribution of AACs via sFTP

Informacja, że Zero AACs/AACs wysłano do XBID kanałem zapasowym (sFTP) po awarii ECP — bez wymaganych działań ze strony TSO.

FromCCC Operator
ToOperational List
Subject[CORE_ID_08] ID1 – Distribution of Zero AACs/AACs to XBID via secondary channel for BD XX.XX

09 — Manual creation of DACC inputs via backup tools

Gdy z powodu niedostępności narzędzia CORE DA CC pliki wejściowe IDCC tworzone są ręcznie w narzędziach zapasowych (CORE BT / JAO SEC tool).

FromCCC Operator
ToOperational List
Subject[CORE_ID_09] ID1 – Manual creation of DACC inputs via backup tools for BD XX.XX

10 — Missing AAC ACK ⚑ dotyczy granic PSE

Gdy brakuje potwierdzenia (ACK) AAC z XBID — poprawność odbioru sprawdzono w XBID GUI, a ACK podano ręcznie; TSO mają zweryfikować AAC na swoich granicach.

FromCCC Operator
ToOperational List
Subject[CORE_ID_10] ID1 – Missing AAC Acknowledgment from XBID for BD XX.XX

11 — Delayed process

Informacja o opóźnieniu bieżącego kroku procesu IDCC i wpływie na kolejny krok — bez wymaganych działań ze strony TSO.

FromCCC Operator
ToOperational List
Subject[CORE_ID_11] ID1/ID2 – Current IDCC process delayed for BD XX.XX

12 — Manual ACK of Zero AACs and/or NTCs ⚑ dotyczy granic PSE

Gdy wystąpiły problemy z potwierdzeniem (ACK) 0AAC/High Neg. NTC/NTC — poprawne przekazanie do XBID sprawdzono ręcznie w GUI; TSO mają zweryfikować zdolności na swoich granicach.

FromCCC Operator
ToOperational List
Subject[CORE_ID_12] ID1 – Manual ACK of Zero AACs and/or NTCs for BD XX.XX

13 — Manual provisioning of AACs to CCCt

Gdy z powodu problemów łączności XBID–CCCt AAC (TAR) dostarczane są ręcznie do CCCt kanałem zapasowym (sFTP); ryzyko awarii ID2, jeśli problem nie ustąpi.

FromCCC
ToOperational List
Subject[CORE_ID_13] ID2 – Manual delivery of AACs from XBID to CCCt for BD XX.XX

14 — Manual provisioning of SEC tool inputs

Informacja od JAO, że pliki MCR zostały utworzone narzędziem SEC Tool i wgrane do procesu CORE IDCC.

FromJAO Operator
ToCCC, Operational List
Subject[CORE_ID_14] ID1 – Manual delivery of MCR inputs via SEC Tool for BD XX.XX

16 — Incorrect CGM

Gdy połączony DACF Coreso/TSCNET nie został wytworzony i zamiast niego użyto indywidualnego DACF (Coreso lub TSCNET).

FromCCC Operator (Coreso only)
ToOperational List
Subject[CORE_ID_16] ID2 – Combined DACF not available for ID2 process for BD XX.XX

17 — Missing CGM

Gdy połączony DACF nie powstał i nie dało się go zastąpić ani DACF Coreso, ani TSCNET — narzędzie CC zastosowało automatyczny fallback (DA Domain AAC).

FromCCC Operator (Coreso only)
ToOperational List
Subject[CORE_ID_16] ID2 – DACF not available for ID2 process for BD XX.XX

18 — Missing or incorrect AAC grid model

Gdy nie udało się dostarczyć modelu sieci AAC do procesu IDCC(b) — narzędzie CC zastosowało automatyczny fallback (DA Domain AAC).

FromCCC Operator (Coreso only)
ToOperational List
Subject[CORE_ID_18] ID2 – Missing or incorrect AAC grid model used in ID2 process for BD XX.XX

19 — Missing individual inputs due to unavailability of DA CCCt

Gdy z powodu niedostępności narzędzia CORE DA brakuje indywidualnych plików wejściowych IDCC — TSO proszeni o ręczne dostarczenie ich do ID CCCt.

FromCCC Operator (Coreso only)
ToOperational List
Subject[CORE_ID_19] ID2 – Missing inputs due to unavailability of DA CCCt for BD XX.XX

20 — SDAC De-coupling – request for provision of MD-250 files ⚑ dotyczy granic PSE

Gdy w wyniku (częściowego) decouplingu SDAC TSO są proszeni o dostarczenie plików MD-250 do CCCt dla rozłączonych granic w terminach 15:43 / 17:24.

FromCCC Operator
ToOperational List
Subject[CORE_ID_20] ID1 – SDAC De-coupling – request for provision of MD-250 files for BD XX.XX



##### 01 — Critical issue in CCCt

**Kiedy:**

Gdy w narzędziu CCCt wystąpi krytyczny problem i operator musi zgłosić go do Core Helpdesk.

| From | CCC Operator |
| --- | --- | --- | --- |
| To | Core ID Helpdesk |
| Subject | [CORE_ID_01] Critical issue in CCCt |

Dear Core Helpdesk,

Time (day and hour) when the problem occurred;
Process (ID1/ID2)
Business day when the problem occurred;
Description of the situation: when in the process did the problem occur (f.e during initial data gathering)? Which files were available, which settings (for example for replacement) where set during that time and what alarms / events where created?
What steps did the CSO take? For example: pushed a button once or more times, logged off to try again, etc.
Print screens which explain the situation, are highly recommended, since this helps to solve the issue sooner. If possible, please provide these to the Helpdesk.

Best regards,

CCC Operator signature



##### 02 — Failed process ⚑ dotyczy granic PSE

**Kiedy:**

Gdy proces CCCt zakończy się niepowodzeniem przed Critical End Time i TSO muszą dostarczyć zdolności przesyłowe lokalnymi narzędziami do XBID.

| From | CCC Operator |
| --- | --- | --- | --- |
| To | Operational List |
| Subject | [CORE_ID_02] ID1/ID2 – CCCt process failed for BD XX.XX |

Dear all,

We would like to inform you that due to "

issue (Jira ticket FCCM-XXX)" with no solution before Critical End Time, the ID1/ID2 process for BD DD.MM.YYYY has failed to provide capacities.

Zero AACs
High Negative NTCs
Day-ahead AACs (Confirm delivery to RCC in the respective IC)
None – IDCC(a) NTCs will prevail
None – Process failed after final NTCs were delivered
None – High Negative NTCs were sent to XBID (backup tool)

Following files created by the CCCt are attached:

Zero AACs
High Negative NTCs (ID1/ID2-921-XX)
Merged High Negative NTCs (ID1/ID2-921)
Day-ahead AACs NTCs
None

BorderInterconnector/Border LevelProviding TSO(s) of MD250Accepted TSO senders by XBID
50Hertz-PSEInterconnector50Hertz50Hertz, PSE
DE-ATBorderAPGAmprion, APG
AMP-ELIAInterconnectorEliaAmprion, Elia
DE-FRBorderAmprionAmprion, RTE
DE-NLBorderTTNTTG, TTN
CZ-DEBorderCEPSCEPS
CEPS-APGInterconnectorAPGCEPS, APG
CEPS-PSEInterconnectorPSECEPS, PSE
ELES-APGInterconnectorAPGAPG, ELES
ELES-HOPSInterconnectorELESELES, HOPs
ELIA-TTNInterconnectorEliaElia, TTN
HOPS-MAVIRInterconnectorHOPSHOPS, MAVIR
MAVIR-APGInterconnectorAPGAPG, MAVIR
MAVIR-ELESInterconnectorMAVIRELES, MAVIR
MAVIR-TELInterconnectorMAVIRMAVIR, Transelectrica
RTE-ELIAInterconnectorEliaElia, RTE
SEPS-CEPSInterconnectorCEPSCEPS, SEPS
SEPS-MAVIRInterconnectorMAVIRMAVIR, SEPS
SEPS-PLCInterconnectorPSEPSE, SEPS

Please provide confirmation once your borders have been updated in XBID.

We are sorry for the inconvenience. The issue is under further investigation.

Best regards,

CCC Operator signature



##### 03 — Replaced input data

**Kiedy:**

Gdy blisko Critical End Time brakuje obowiązkowego pliku wejściowego i strona odpowiedzialna zastępuje brakujące dane danymi z innej doby, aby nie zerwać BD.

| From | CCC Operator |
| --- | --- | --- | --- |
| To | Operational List |
| Subject | [CORE_ID_03] ID1/ID2 – Input data replaced BD XX.XX |

Dear all,

We would like to inform you that the following mandatory file(s) for the ID1/ID2 process "specify the flow number and responsible party e.g. TSOX-FXXX" were missing close to Critical End Time. To not fail the BD, the responsible party has proposed to replace the missing data with data from BD XX.XX.

Best regards,

CCC Operator signature



##### 04 — Warning: file missing

**Kiedy:**

Ostrzeżenie o braku pliku wejściowego przy Target End Time bez możliwości zastąpienia — jeśli plik nie dotrze, obliczenia przejdą w tryb fallback.

| From | CCC Operator |
| --- | --- | --- | --- |
| To | Operational List |
| Subject | [CORE_ID_04] ID1/ID2 – Warning! Missing file for BD XX.XX |

Dear all,

We would like to inform you that the following file(s) are missing in the ID1/ID2 process with no possibility of replacement in the CCCt at Target End Time: "specify the flow number and responsible party e.g. FXXX from XXX". In case the file(s) are not delivered on time, the computation for BD DD.MM.YYYY will be computed in fallback mode.

Best regards,

CCC Operator signature



##### 05 — Application of fallbacks with CCCt

**Kiedy:**

Gdy któryś krok obliczeniowy CCCt zakończył się z zastosowaniem fallbacku dla wskazanych godzin doby.

| From | CCC Operator |
| --- | --- | --- | --- |
| To | Operational List |
| Subject | [CORE_ID_05] ID1/ID2 – Fallback applied with CCCt BD XX.XX |

Dear all,

We would like to inform you that for the ID1/ID2 process the Calculate enlarged domain / Initial / Final FB Computation / ID ATC Extraction finished with the fallback ID Domain AAC / DA Domain Refprog / DA Domain AAC fallback / Zero Capacity fallback (Negative NTCs) for TSs XX:XX – XX:XX of BD XX.XX.

Best regards,

CCC Operator signature



##### 06 — Back-up operator appointed to operate the CCCt

**Kiedy:**

Gdy z powodu niedostępności operatora CCC rolę operatora CCCt przejmuje strona zapasowa (back-up).

| From | CCC Operator |
| --- | --- | --- | --- |
| To | Operational List |
| Subject | [CORE_ID_06] ID1/ID2 – Back-up operator X appointed to operate the CCCt for BD XX.XX |

Dear all,

We would like to inform you that due to "specify issue (e.g. unavailability of the CCC operator, inability to access CCCt)" during the Core ID1/ID2 process for BD XX.XX, back-up party X will take over the operator role of the CCCt for BD XX.XX.

This issue is under investigation.

Best regards,

CCC Operator signature



##### 07 — Distribution of NTCs via sFTP ⚑ dotyczy granic PSE

**Kiedy:**

Gdy NTC/High Neg. NTC zostały wysłane do XBID kanałem zapasowym (sFTP) po awarii ECP i TSO mają zweryfikować ich obecność w XBID.

| From | CCC Operator |
| --- | --- | --- | --- |
| To | Operational List |
| Subject | [CORE_ID_07] ID1/ID2 – Distribution of High Neg. NTCs/NTCs to XBID via secondary channel for BD XX.XX |

Dear all,

We would like to inform you that High Negative NTCs/NTCs to XBID were distributed via the secondary channel (sFTP). Due to the short time scale, the correct presence of NTCs in XBID cannot be guaranteed. Thus, all TSOs are kindly asked to crosscheck the provided NTCs on XBID if possible. The failed delivery via ECP (primary channel) is under investigation.

Please find attached: Individual NTCs (ID1/ID2-921-XX), Merged NTCs (ID1/ID2-921).

BorderInterconnector/Border LevelProviding TSO(s) of MD250Accepted TSO senders by XBID
50Hertz-PSEInterconnector50Hertz50Hertz, PSE
DE-ATBorderAPGAmprion, APG
AMP-ELIAInterconnectorEliaAmprion, Elia
DE-FRBorderAmprionAmprion, RTE
DE-NLBorderTTNTTG, TTN
CZ-DEBorderCEPSCEPS
CEPS-APGInterconnectorAPGCEPS, APG
CEPS-PSEInterconnectorPSECEPS, PSE
ELES-APGInterconnectorAPGAPG, ELES
ELES-HOPSInterconnectorELESELES, HOPs
ELIA-TTNInterconnectorEliaElia, TTN
HOPS-MAVIRInterconnectorHOPSHOPS, MAVIR
MAVIR-APGInterconnectorAPGAPG, MAVIR
MAVIR-ELESInterconnectorMAVIRELES, MAVIR
MAVIR-TELInterconnectorMAVIRMAVIR, Transelectrica
RTE-ELIAInterconnectorEliaElia, RTE
SEPS-CEPSInterconnectorCEPSCEPS, SEPS
SEPS-MAVIRInterconnectorMAVIRMAVIR, SEPS
SEPS-PLCInterconnectorPSEPSE, SEPS

Please provide confirmation once your borders have been updated in XBID.

Best regards,

CCC Operator signature



##### 08 — Distribution of AACs via sFTP

**Kiedy:**

Informacja, że Zero AACs/AACs wysłano do XBID kanałem zapasowym (sFTP) po awarii ECP — bez wymaganych działań ze strony TSO.

| From | CCC Operator |
| --- | --- | --- | --- |
| To | Operational List |
| Subject | [CORE_ID_08] ID1 – Distribution of Zero AACs/AACs to XBID via secondary channel for BD XX.XX |

Dear all,

We would like to inform you that Zero AACs/AACs were distributed from the CCCt to XBID via the secondary channel (sFTP). The failed delivery via ECP (primary channel) is under investigation.

Please find attached: Individual AACs (ID1-373-XX, ID1-383-XX).

Best regards,

CCC Operator signature



##### 09 — Manual creation of DACC inputs via backup tools

**Kiedy:**

Gdy z powodu niedostępności narzędzia CORE DA CC pliki wejściowe IDCC tworzone są ręcznie w narzędziach zapasowych (CORE BT / JAO SEC tool).

| From | CCC Operator |
| --- | --- | --- | --- |
| To | Operational List |
| Subject | [CORE_ID_09] ID1 – Manual creation of DACC inputs via backup tools for BD XX.XX |

Dear all,

We would like to inform you that due to the unavailability of the CORE DA CC tool the following inputs for the IDCC process were manually created via the backup tools (CORE BT/JAO SEC tool) and uploaded to the CORE IDCC tool:

CORE backup tool:

ID1 – 624 – Merged LTNom
ID1 – 625 – Fallback ATCs for SA
ID1 – 626 – Fallback NTCs for SA
ID1 – 629 – Merged LTA

JAO SEC tool:

ID1 – 646 – SAR DQC
ID1 – 647 – RD ID ATC
ID1 – 648 – Merged AC
ID1 – 649 – RD for AAC

Best regards,

CCC Operator signature



##### 10 — Missing AAC ACK ⚑ dotyczy granic PSE

**Kiedy:**

Gdy brakuje potwierdzenia (ACK) AAC z XBID — poprawność odbioru sprawdzono w XBID GUI, a ACK podano ręcznie; TSO mają zweryfikować AAC na swoich granicach.

| From | CCC Operator |
| --- | --- | --- | --- |
| To | Operational List |
| Subject | [CORE_ID_10] ID1 – Missing AAC Acknowledgment from XBID for BD XX.XX |

Dear all,

Due to missing acknowledgments from XBID, we verified that the XBID GUI is indicating the correct receiving of the latest AAC files. Thus, the ACK was provided manually to the CCCt. The ID1 process continued with the

.

The ACK of AACs is necessary to ensure that AACs and NTCs are provided in the correct order to XBID.

BorderInterconnector/Border LevelProviding TSO(s) of MD250Accepted TSO senders by XBID
50Hertz-PSEInterconnector50Hertz50Hertz, PSE
DE-ATBorderAPGAmprion, APG
AMP-ELIAInterconnectorEliaAmprion, Elia
DE-FRBorderAmprionAmprion, RTE
DE-NLBorderTTNTTG, TTN
CZ-DEBorderCEPSCEPS
CEPS-APGInterconnectorAPGCEPS, APG
CEPS-PSEInterconnectorPSECEPS, PSE
ELES-APGInterconnectorAPGAPG, ELES
ELES-HOPSInterconnectorELESELES, HOPs
ELIA-TTNInterconnectorEliaElia, TTN
HOPS-MAVIRInterconnectorHOPSHOPS, MAVIR
MAVIR-APGInterconnectorAPGAPG, MAVIR
MAVIR-ELESInterconnectorMAVIRELES, MAVIR
MAVIR-TELInterconnectorMAVIRMAVIR, Transelectrica
RTE-ELIAInterconnectorEliaElia, RTE
SEPS-CEPSInterconnectorCEPSCEPS, SEPS
SEPS-MAVIRInterconnectorMAVIRMAVIR, SEPS
SEPS-PLCInterconnectorPSEPSE, SEPS

Please provide confirmation once your borders have been updated in XBID.

Best regards,

CCC Operator signature



##### 11 — Delayed process

**Kiedy:**

Informacja o opóźnieniu bieżącego kroku procesu IDCC i wpływie na kolejny krok — bez wymaganych działań ze strony TSO.

| From | CCC Operator |
| --- | --- | --- | --- |
| To | Operational List |
| Subject | [CORE_ID_11] ID1/ID2 – Current IDCC process delayed for BD XX.XX |

Dear all,

We would like to inform you that due to delay on "describe step delayed" due to "specify cause of delay", the following step "indicate the next step which is impacted" will be delayed (If you know, indicate time when process is planned to continue). Thanks in advance for your understanding.

Best regards,

CCC Operator signature



##### 12 — Manual ACK of Zero AACs and/or NTCs ⚑ dotyczy granic PSE

**Kiedy:**

Gdy wystąpiły problemy z potwierdzeniem (ACK) 0AAC/High Neg. NTC/NTC — poprawne przekazanie do XBID sprawdzono ręcznie w GUI; TSO mają zweryfikować zdolności na swoich granicach.

| From | CCC Operator |
| --- | --- | --- | --- |
| To | Operational List |
| Subject | [CORE_ID_12] ID1 – Manual ACK of Zero AACs and/or NTCs for BD XX.XX |

Dear all,

We would like to inform you that we faced issues with the acknowledgment of 0AACs/High Negative NTCs/NTCs. The correct provisioning to XBID was manually checked (XBID GUI) and confirmed.

BorderInterconnector/Border LevelProviding TSO(s) of MD250Accepted TSO senders by XBID
50Hertz-PSEInterconnector50Hertz50Hertz, PSE
DE-ATBorderAPGAmprion, APG
AMP-ELIAInterconnectorEliaAmprion, Elia
DE-FRBorderAmprionAmprion, RTE
DE-NLBorderTTNTTG, TTN
CZ-DEBorderCEPSCEPS
CEPS-APGInterconnectorAPGCEPS, APG
CEPS-PSEInterconnectorPSECEPS, PSE
ELES-APGInterconnectorAPGAPG, ELES
ELES-HOPSInterconnectorELESELES, HOPs
ELIA-TTNInterconnectorEliaElia, TTN
HOPS-MAVIRInterconnectorHOPSHOPS, MAVIR
MAVIR-APGInterconnectorAPGAPG, MAVIR
MAVIR-ELESInterconnectorMAVIRELES, MAVIR
MAVIR-TELInterconnectorMAVIRMAVIR, Transelectrica
RTE-ELIAInterconnectorEliaElia, RTE
SEPS-CEPSInterconnectorCEPSCEPS, SEPS
SEPS-MAVIRInterconnectorMAVIRMAVIR, SEPS
SEPS-PLCInterconnectorPSEPSE, SEPS

Please provide confirmation once your borders have been updated in XBID.

Best regards,

CCC Operator signature



##### 13 — Manual provisioning of AACs to CCCt

**Kiedy:**

Gdy z powodu problemów łączności XBID–CCCt AAC (TAR) dostarczane są ręcznie do CCCt kanałem zapasowym (sFTP); ryzyko awarii ID2, jeśli problem nie ustąpi.

| From | CCC |
| --- | --- | --- | --- |
| To | Operational List |
| Subject | [CORE_ID_13] ID2 – Manual delivery of AACs from XBID to CCCt for BD XX.XX |

Dear all,

Due to issues with the connection between XBID and the CCCt, AACs (TAR) were manually provided to the CCCt by the means of the secondary channel (sFTP). The issue is under investigation by Unicorn and DBAG.

Best regards,

Operator signature



##### 14 — Manual provisioning of SEC tool inputs

**Kiedy:**

Informacja od JAO, że pliki MCR zostały utworzone narzędziem SEC Tool i wgrane do procesu CORE IDCC.

| From | JAO Operator |
| --- | --- | --- | --- |
| To | CCC, Operational List |
| Subject | [CORE_ID_14] ID1 – Manual delivery of MCR inputs via SEC Tool for BD XX.XX |

Dear all,

JAO successfully created the following files with the SEC Tool and uploaded them to the CORE IDCC process:

ID1 – 646 – SAR DQC
ID1 – 647 – RD ID ATC
ID1 – 648 – Merged AC
ID1 – 649 – RD for AAC

Best regards,

JAO Operator signature



##### 16 — Incorrect CGM

**Kiedy:**

Gdy połączony DACF Coreso/TSCNET nie został wytworzony i zamiast niego użyto indywidualnego DACF (Coreso lub TSCNET).

| From | CCC Operator (Coreso only) |
| --- | --- | --- | --- |
| To | Operational List |
| Subject | [CORE_ID_16] ID2 – Combined DACF not available for ID2 process for BD XX.XX |

Dear all,

The production of the combined Coreso/TSCNET DACF was not successfully completed. Therefore, the individual DACF of Coreso/TSCNET (delete one) has been used instead.

Best regards,

CCC Operator signature



##### 17 — Missing CGM

**Kiedy:**

Gdy połączony DACF nie powstał i nie dało się go zastąpić ani DACF Coreso, ani TSCNET — narzędzie CC zastosowało automatyczny fallback (DA Domain AAC).

| From | CCC Operator (Coreso only) |
| --- | --- | --- | --- |
| To | Operational List |
| Subject | [CORE_ID_16] ID2 – DACF not available for ID2 process for BD XX.XX |

Dear all,

The production of the combined DACF was not successfully completed and it was not possible to substitute either the Coreso or TSCNET DACF in its place. Therefore, the following automatic fallback has been applied by the Core CC tool: DA Domain AAC Fallback.

Best regards,

CCC Operator signature



##### 18 — Missing or incorrect AAC grid model

**Kiedy:**

Gdy nie udało się dostarczyć modelu sieci AAC do procesu IDCC(b) — narzędzie CC zastosowało automatyczny fallback (DA Domain AAC).

| From | CCC Operator (Coreso only) |
| --- | --- | --- | --- |
| To | Operational List |
| Subject | [CORE_ID_18] ID2 – Missing or incorrect AAC grid model used in ID2 process for BD XX.XX |

Dear all,

It was not possible to provide an AAC grid model to the IDCC(b) process. The following automatic fallback has been applied by the Core CC tool: DA Domain AAC Fallback.

Best regards,

CCC Operator signature



##### 19 — Missing individual inputs due to unavailability of DA CCCt

**Kiedy:**

Gdy z powodu niedostępności narzędzia CORE DA brakuje indywidualnych plików wejściowych IDCC — TSO proszeni o ręczne dostarczenie ich do ID CCCt.

| From | CCC Operator (Coreso only) |
| --- | --- | --- | --- |
| To | Operational List |
| Subject | [CORE_ID_19] ID2 – Missing inputs due to unavailability of DA CCCt for BD XX.XX |

Dear all,

Due to the unavailability of the CORE DA tool, the following inputs for the IDCC process are missing:

ID2-606 (317 in DA) - GLSK Pre-Merge Factors
ID2-607 (103 in DA) - Individual Generation and Load Shift Key (GLSK)
ID2-608 (107 in DA) - Individual External Constraints (EC)
ID2-609 (510 in DA) - ECs/ATCs for virtual hubs
ID2-617 (224 in DA) - Individual Critical Branches (CB)
ID2-637 (106 in DA) - Individual Initial RA Settings

Best regards,

CCC Operator signature



##### 20 — SDAC De-coupling – request for provision of MD-250 files ⚑ dotyczy granic PSE

**Kiedy:**

Gdy w wyniku (częściowego) decouplingu SDAC TSO są proszeni o dostarczenie plików MD-250 do CCCt dla rozłączonych granic w terminach 15:43 / 17:24.

| From | CCC Operator |
| --- | --- | --- | --- |
| To | Operational List |
| Subject | [CORE_ID_20] ID1 – SDAC De-coupling – request for provision of MD-250 files for BD XX.XX |

Dear all,

Affected borders:

Note: For information, the first deadline of 15:43 will allow the CCCt to calculate NTCs for the provided borders. If MD250 is not provided by 15:43, the ultimate deadline for submission of MD250 is 17:24 which will allow AACs to be provided by CCCt to XBID. High Negative NTCs would remain in this case. If MD250 files are not submitted by 17:24 for a given border, it is the TSOs' responsibility to upload AACs for the missing border(s) directly to XBID. If AACs are missing for any Core border at 20:00, this will result in the failure of the IDCC(b)/ID2 process.

BorderInterconnector/Border LevelProviding TSO(s) of MD250Accepted TSO senders by XBID
50Hertz-PSEInterconnector50Hertz50Hertz, PSE
DE-ATBorderAPGAmprion, APG
AMP-ELIAInterconnectorEliaAmprion, Elia
DE-FRBorderAmprionAmprion, RTE
DE-NLBorderTTNTTG, TTN
CZ-DEBorderCEPSCEPS
CEPS-APGInterconnectorAPGCEPS, APG
CEPS-PSEInterconnectorPSECEPS, PSE
ELES-APGInterconnectorAPGAPG, ELES
ELES-HOPSInterconnectorELESELES, HOPs
ELIA-TTNInterconnectorEliaElia, TTN
HOPS-MAVIRInterconnectorHOPSHOPS, MAVIR
MAVIR-APGInterconnectorAPGAPG, MAVIR
MAVIR-ELESInterconnectorMAVIRELES, MAVIR
MAVIR-TELInterconnectorMAVIRMAVIR, Transelectrica
RTE-ELIAInterconnectorEliaElia, RTE
SEPS-CEPSInterconnectorCEPSCEPS, SEPS
SEPS-MAVIRInterconnectorMAVIRMAVIR, SEPS
SEPS-PLCInterconnectorPSEPSE, SEPS

Best regards,

CCC Operator signature



### 2Narzędzia

**Skrót / powiązane**

▸ procedury

▸ ryzyka

1. Narzędzia

1.A. Wewnętrzne PSE

CCM (Capacity Calculation Monitoring)

URL: https://ccm.spsm.pse.pl
Funkcja: główny pulpit dyspozytorski; monitoring statusów wszystkich kafelków IDCC; ręczna wysyłka plików (PPM → Wyślij); ustawianie statusu ręcznego 'R'; opcja „Wyślij po CET"
Pulpity: „IDCC FB Pulpit dyspozytorski", „IDCC (do 3C) z ATC i SFTP Pulpit dyspozytorski"
Tryby odświeżania: ultraszybki (10s) / szybki (30s) / wolny (5 min)
Powiązane ryzyko: U01 (brak dostępu)
Procedury: ustawianie statusu ręcznego — patrz Logowanie i nawigacja w CCM

Core CC Tool (CCCt)

URL: (zewnętrzny URL CCCt — zgodnie z aktualną konfiguracją)
Funkcja: system centralny procesu; Message Viewer (status pliku, kody ACK); Manual Upload (ręczna wysyłka pliku z dysku); publikacja wyników do PuTo
Selektor procesu: ID1, ID2, ID3C, ID3 (IDCC) vs domyślny DA (Day-Ahead)
Powiązane ryzyko: U02 (brak dostępu)
Procedury: Logowanie i nawigacja w Core CC Tool, P01 Manual Upload

Perun4V

URL: https://lccv.tscnet.eu
Funkcja: narzędzie walidacji FBA — wykonuje obliczenia IVA dla danej doby; pokazuje status obliczeń (Successful / ERR-I / Process failed); umożliwia ręczne uruchomienie procesu
Logowanie: Local Login → username/password → akceptacja TSCNET Policy
Powiązane ryzyko: U05 (brak dostępu)
Procedury: Logowanie i nawigacja w Perun4V, P03 Ręczne uruchomienie obliczeń

MinIO

URL: https://minio-gui.pse.pl
Funkcja: centralne repozytorium plików procesowych w sieci PSE; buckety: perun/, cca/, mam/
Powiązane ryzyko: U04 (brak dostępu)
Procedury: Logowanie i nawigacja w MinIO, P04 Pobranie z MinIO

Connector 2.0 (CN2)

Lokalizacja: narzędzie transportowe działa w tle
Funkcja: główny kanał transportu plików w PSE: CCM ↔ CCCt ↔ MinIO ↔ Perun4V
Stworzony przez: PSE Innowacje
Powiązane ryzyko: U03 (awaria, obejmuje też scalone U18 — Connector nie kopiuje do bucketów)

ZP (zdolności przesyłowe)

Lokalizacja: aplikacja desktop na komputerze dyspozytorskim
Funkcja: źródło plików AC (FIDx-831) dla iteracji IDCC; bilans AC; generowanie nowych wersji
Powiązane ryzyko: U06 (brak dostępu / brak wersji)
Procedury: Logowanie i nawigacja w ZP, P02 Pobranie z ZP

KreatorDACF&2DAF_CGMES

Lokalizacja: aplikacja PSE / PLANS
Funkcja: generator IGM (Individual Grid Model) i plików wejściowych — dla iteracji IDCC(b): FID2-607 (GLSK), FID2-617 (CBCORA)
Powiązane ryzyko: U06 (brak dostępu / błąd generowania)

KreatorIDCF_CGMES

Lokalizacja: aplikacja PSE / PLANS
Funkcja: dla iteracji IDCC(c), IDCC(d), IDCC(e) generuje modele IGM/CGM oraz pliki GLSK (FIDx-607), CBCORA (FIDx-617) i RA (FIDx_RA — środki zaradcze); publikacja przez Publikuj Connector
Procedura ręczna (backup) ze screenami: Generowanie GLSK + CBCORA + RA w KreatorIDCF — uruchamiana, gdy auto-skrypt Monitora zgłosi BŁĄD
Pełna instrukcja narzędzia: IDCF_InstrUżytk_v5 (rozdz. „Tworzenie plików GLSK, CBCORA oraz RA"; też tworzenie modeli IDCF/IGM, CGMES, weryfikacja N-1)
Powiązane ryzyko: U06

CCA (Capacity Calculation Application)

Lokalizacja: aplikacja wewnętrzna PSE
Funkcja: generowanie raportów walidacyjnych, IVA BACKUP (publikacja do cca/ID_FBCC/out/[BD]/), automatyczne wysyłki backupowe do CCCt
Powiązane ryzyko: U19 (niezgodność wersji IVA/Backup), U23 (brak raportu CCA), U18 scalone z U03 (Connector nie kopiuje IVA do bucketów CCA)
Zgłoszenie: Zespół utrzymania CCA

PuTo (Platforma Udostępniania Transmisyjnych)

Lokalizacja: wewnętrzny system PSE
Funkcja: docelowy odbiorca pliku AC (FIDx-831) po publikacji przez Core CC Tool jako wynik IDCC(a)/IDCC(b)/(c)/(d)

kdm6@pse.pl

Lokalizacja: skrzynka mailowa PSE
Funkcja: kanał pasywny dla raportów: CCA (raporty walidacyjne, LTA_CURTAILMENT, IVA na CNECach), Perun4V (raporty po obliczeniach z informacją o policzonych godzinach i max IVA)
Powiązane ryzyko: U07 (brak dostępu)

sFTP@pse.pl

Lokalizacja: protokół transportowy
Funkcja: transport paczek ZIP z MinIO do Perun4V (i wyniki zwrotnie do MinIO/Connector 2.0)
Powiązane ryzyko: wpisuje się w U03 (jeśli sFTP nie działa, paczki nie dotrą do Perun4V)

1.B. Zewnętrzne (CCC / RCC / TSO)

RCC / TSCNET

Kontakt: operator@tscnet.eu (lista operacyjna do telefonu)
Funkcja: Regional Coordination Centre — koordynacja procesu IDCC; sterowanie fazami centralnymi (CGM merging, Domain calculation, NTC publication)

CORESO

Kontakt: day-ahead.engineer@coreso.eu
Funkcja: koordynacja po stronie operatora procesu

Core CC Tool (centralne procesy)

Funkcja: publikacja wyników centralnych (FIDx-928 walidacja ATC, FID1-921 NTC, ID1-373 AAC); dyspozytor PSE wyłącznie monitoruje — nie wykonuje czynności wykonawczych

ECP/EDX (Energy Communication Platforms)

Funkcja: protokół wymiany TSO ↔ CCCt — automatyczna wysyłka CB/GLSK/EC; ręczny upload przez CCCt GUI; dostarczenie Shadow Auction (MD250)
Powiązane ryzyko: wpisuje się w U21 (Decoupling SDAC — MD250)

XBID

Funkcja: system aukcyjny intraday — odbiorca AAC (ID1-373-XX), NTC (FIDx-921)
Powiązane ryzyko: U20 (AAC Fallback), U22 (Late NTC)

1.C. Zgłoszenie / wsparcie

WPO (Wydział Wsparcia Procesów Operatorskich)

Skład: Słabicki, Jarzęcka, Krzysztoszek, Łukaszewski, Rodo
Funkcja: zgłoszenie operacyjna; decyzje w sytuacjach niestandardowych

CIZ (Centrum Zgłaszania Incydentów PSE)

Lokalizacja: wewnętrzny system PSE
Funkcja: rejestracja incydentów (awarie narzędzi, problemy procesowe); priorytet zależny od fazy procesu

PSE Innowacje

Kanał: wewnętrzny PSE
Funkcja: utrzymanie narzędzi PSE — CCM, Connector 2.0, MinIO, sFTP
Zgłoszenie przy: U01, U03, U04

Zespół utrzymania CCA

Kanał: wewnętrzny PSE Innowacje (zespół CCA)
Funkcja: utrzymanie aplikacji CCA, raportów walidacyjnych, IVA BACKUP, FID1-928
Zgłoszenie przy: U19, U23

Zespół utrzymania ZP

Kanał: wewnętrzny PSE
Funkcja: utrzymanie aplikacji ZP (zdolności przesyłowe) — źródła AC FIDx-831
Zgłoszenie przy: U06 (awaria ZP, brak generowania)



## 1. Narzędzia



### 1.A. Wewnętrzne PSE



#### CCM (Capacity Calculation Monitoring)

https://ccm.spsm.pse.pl

główny pulpit dyspozytorski; monitoring statusów wszystkich kafelków IDCC; ręczna wysyłka plików (PPM → Wyślij); ustawianie statusu ręcznego 'R'; opcja „Wyślij po CET"

,

ultraszybki (10s) / szybki (30s) / wolny (5 min)

(brak dostępu)

ustawianie statusu ręcznego — patrz



#### Core CC Tool (CCCt)

(zewnętrzny URL CCCt — zgodnie z aktualną konfiguracją)

system centralny procesu; Message Viewer (status pliku, kody ACK); Manual Upload (ręczna wysyłka pliku z dysku); publikacja wyników do PuTo

,

,

,

vs domyślny

(brak dostępu)

,

Manual Upload



#### Perun4V

https://lccv.tscnet.eu

narzędzie walidacji FBA — wykonuje obliczenia IVA dla danej doby; pokazuje status obliczeń (Successful / ERR-I / Process failed); umożliwia ręczne uruchomienie procesu

Local Login → username/password → akceptacja TSCNET Policy

(brak dostępu)

,

Ręczne uruchomienie obliczeń



#### MinIO

https://minio-gui.pse.pl

centralne repozytorium plików procesowych w sieci PSE; buckety:

,

,

(brak dostępu)

,

Pobranie z MinIO



#### Connector 2.0 (CN2)

narzędzie transportowe działa w tle

główny kanał transportu plików w PSE: CCM ↔ CCCt ↔ MinIO ↔ Perun4V

PSE Innowacje

(awaria, obejmuje też scalone U18 — Connector nie kopiuje do bucketów)



#### ZP (zdolności przesyłowe)

aplikacja desktop na komputerze dyspozytorskim

źródło plików

dla iteracji IDCC; bilans AC; generowanie nowych wersji

(brak dostępu / brak wersji)

,

Pobranie z ZP



#### KreatorDACF&2DAF_CGMES

aplikacja PSE / PLANS

generator IGM (Individual Grid Model) i plików wejściowych —

: FID2-607 (GLSK), FID2-617 (CBCORA)

(brak dostępu / błąd generowania)



#### KreatorIDCF_CGMES

aplikacja PSE / PLANS

dla iteracji

generuje

oraz pliki

,

i

; publikacja przez

— uruchamiana, gdy auto-skrypt Monitora zgłosi BŁĄD

(rozdz. „Tworzenie plików GLSK, CBCORA oraz RA"; też tworzenie modeli IDCF/IGM, CGMES, weryfikacja N-1)



#### CCA (Capacity Calculation Application)

aplikacja wewnętrzna PSE

generowanie raportów walidacyjnych,

(publikacja do

), automatyczne wysyłki backupowe do CCCt

(niezgodność wersji IVA/Backup),

(brak raportu CCA),

(Connector nie kopiuje IVA do bucketów CCA)



#### PuTo (Platforma Udostępniania Transmisyjnych)

wewnętrzny system PSE

docelowy odbiorca pliku

po publikacji przez Core CC Tool jako wynik IDCC(a)/IDCC(b)/(c)/(d)



#### kdm6@pse.pl

skrzynka mailowa PSE

kanał pasywny dla raportów: CCA (raporty walidacyjne, LTA_CURTAILMENT, IVA na CNECach), Perun4V (raporty po obliczeniach z informacją o policzonych godzinach i max IVA)

(brak dostępu)



#### sFTP@pse.pl

protokół transportowy

transport paczek ZIP z MinIO do Perun4V (i wyniki zwrotnie do MinIO/Connector 2.0)

wpisuje się w

(jeśli sFTP nie działa, paczki nie dotrą do Perun4V)



### 1.B. Zewnętrzne (CCC / RCC / TSO)



#### RCC / TSCNET

operator@tscnet.eu (lista operacyjna do telefonu)

Regional Coordination Centre — koordynacja procesu IDCC; sterowanie fazami centralnymi (CGM merging, Domain calculation, NTC publication)



#### CORESO

day-ahead.engineer@coreso.eu

koordynacja po stronie operatora procesu



#### Core CC Tool (centralne procesy)

publikacja wyników centralnych (FIDx-928 walidacja ATC, FID1-921 NTC, ID1-373 AAC); dyspozytor PSE wyłącznie monitoruje — nie wykonuje czynności wykonawczych



#### ECP/EDX (Energy Communication Platforms)

protokół wymiany TSO ↔ CCCt — automatyczna wysyłka CB/GLSK/EC; ręczny upload przez CCCt GUI; dostarczenie Shadow Auction (MD250)

wpisuje się w

(Decoupling SDAC — MD250)



#### XBID

system aukcyjny intraday — odbiorca AAC (ID1-373-XX), NTC (FIDx-921)

(AAC Fallback),

(Late NTC)



### 1.C. Zgłoszenie / wsparcie



#### WPO (Wydział Wsparcia Procesów Operatorskich)

Słabicki, Jarzęcka, Krzysztoszek, Łukaszewski, Rodo

zgłoszenie operacyjna; decyzje w sytuacjach niestandardowych



#### CIZ (Centrum Zgłaszania Incydentów PSE)

wewnętrzny system PSE

rejestracja incydentów (awarie narzędzi, problemy procesowe); priorytet zależny od fazy procesu



#### PSE Innowacje

wewnętrzny PSE

utrzymanie narzędzi PSE — CCM, Connector 2.0, MinIO, sFTP

,

,



#### Zespół utrzymania CCA

wewnętrzny PSE Innowacje (zespół CCA)

utrzymanie aplikacji CCA, raportów walidacyjnych, IVA BACKUP, FID1-928

,



#### Zespół utrzymania ZP

wewnętrzny PSE

utrzymanie aplikacji ZP (zdolności przesyłowe) — źródła AC FIDx-831

(awaria ZP, brak generowania)



### 3Legenda statusów kafelków

**Skrót / powiązane**

▸ czynności w CCM

▸ stany plików



#### Pełna legenda na pulpicie

Legenda kolorów statusów plików w CCM — pełny opis znaczenia każdego koloru i oznaczenia (R, W, !, ?).



### 4Katalog plików FIDx — opisy i warianty stanów

**Skrót / powiązane**

▸ legenda

▸ obsługa w CCM



#### IDCC(a) — 4 plików



##### MD250 FID1-250

Kod: FID1-250

Profil: SFTP

TET: 17:24

CET: 17:58

Źródło: ECP/EDX

Wersja: 1

MD250 — Shadow Auction Results (FID1-250) — wyniki aukcji rezerwowej wymieniane z CCCt przez ECP/EDX przy decouplingu SDAC. Deadline 1 ~15:43 (TET MCR), Deadline 2 ~17:24.

**Ścieżka:**

ECP/EDX

Core CC Tool

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjnesFTP/ZP wysł.Plik dostarczony prawidłowo na sFTP/ZP — status pozytywny.Brak działań — proces poprawny.sFTP/ZP wysł.Status nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.sFTP/ZP wysł.Plik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.sFTP/ZP wysł.Przedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.sFTP/ZP wysł.Oczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź sFTP/ZP. Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się TET — pliku jeszcze nie ma na sFTP/ZP.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się CET / błąd dostarczenia — brak pliku na sFTP/ZP.Gdy pliku NIE ma na sFTP/ZP → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Minął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### AC FID1-831

Kod: FID1-831

Profil: 2CCT

TET: 13:50

CET: 14:45

Źródło: ZP

Wersja: 2

AC (Allocation Constraints, FID1-831) — plik z wartościami ograniczeń alokacyjnych wyznaczonych przez PSE, publikowany do PuTo i do procesu Core. Format XML, MTU 15 min.

**Ścieżka:**

ZP

→

Connector 2.0

→

Core CC Tool

→

PuTo

+

MinIO

Warianty stanów (32)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool. Dyspozytor ustawił status ręcznie 'R' po weryfikacji w CCTool.Brak działań.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool po CET, ACK napłynął po CET z pozytywnym komunikatem.Brak działań — dostarczone po CET, OK.CCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool oraz otrzymanie potwierdzenia ACK.Brak działań.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — wysyłka ręczna wykonana.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 5 minOK → ustaw 'R' w CCMCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, ale ACK nie napłynął w żądanym czasie i zbliża się CET.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, a otrzymane ACK: (1) zawiera komunikat błędu (najedź kursorem); (2) proces zakończył się błędem — 'Błąd procesu'.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż zapisana) → podnieś numer wersji w aplikacji ZP i wyślij plik ponownie przez Core CC Tool (Manual Upload)kod 30 (rozmiar pliku niezgodny) → pobierz poprawny plik z MinIO lub aplikacji ZP i wyślij ponownieCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem po CET.Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano ACK, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — decyzja ręczna Dyspozytora.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 2-5 minOK → ustaw 'R'CCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — upłynęło więcej niż 2 minuty.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET, a otrzymane ACK: (1) komunikat błędu; (2) proces zakończył się błędem. Typowo kod 20 gateClosed.Postępowanie:Najedź kursorem na status i odczytaj kod ACK (typowo kod 20)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka jest zamknięta → zgłośinny kod → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Otrzymano potwierdzenie ACK z pozytywnym komunikatem (po CET).Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool. Trwa oczekiwanie na ACK — około 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Trwa oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → utrzymaj 'R'brak / awaria → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie otrzymano, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — Dyspozytor zatwierdził zawartość.CCtool wysł.CCtool zwalid.Dokument jeszcze nie został wysłany do CCTool, ACK nie napłynął. Plik nie wymagany (>30 min do TET).Brak działań — czekaj do TET.CCtool wysł.CCtool zwalid.Zbliża się CET — plik niedostarczony lub błąd wysyłki. Stan alarmowy.Postępowanie (alarm):Core CC Tool → sprawdź czy plik dotarł do Core CC ToolJeżeli:plik jest, brak ACK → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak pliku (awaria Connector 2.0) → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykbrak pliku w źródle → Brak pliku lub wersji w aplikacji źródłowej. Otwórz aplikacji ZP, przejdź do bilansu i sprawdź wersję pliku: jeśli wersja jest dostępna — pobierz ją (Pobierz XML); jeśli brakuje — wygeneruj nową wersję; jeśli aplikacja nie działa — zgłoś. pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. Oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → sprawdź rozmiar; pobierz z MinIO i rozpakujJeżeli:zawartość OK mimo rozmiaru → oznacz 'R' (→ powiązany stan)zawartość niepoprawna → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru, a ACK ma status czerwony — typowo kod 30.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → potwierdź rozmiarPobierz poprawny plik z aplikacji ZP (Pobierz XML) i wyślij przez Core CC Tool (Manual Upload) z kolejnym numerem wersjiNadal za mały → zgłoś szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK napłynął po CET z pozytywnym komunikatem. Sprzeczność.Postępowanie:Pobierz z MinIO → rozpakuj → sprawdź zawartośćJeżeli:zawartość OK → oznacz 'R' (→ powiązany stan); zgłośniepoprawna → zgłośCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, ale ACK negatywny (Rejected). Kody: 20/21/30.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś (administrator Core CC Tool otwiera bramkę); sprawdź proces IDx-AC-FORWARDINGkod 21 (wersja nie jest wyższa niż zapisana) → podnieś numer wersji w aplikacji ZP i wyślij plik ponownie przez Core CC Tool (Manual Upload)kod 30 (rozmiar pliku niezgodny) → pobierz poprawny plik z MinIO lub aplikacji ZP i wyślij ponownieCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, trwa oczekiwanie na ACK, który nie napłynął w zadanym czasie (>2-3 min).Postępowanie:Czekaj 5 min → Core CC Tool (⚠ nie wysyłaj ponownie!)Jeżeli:Processed → oznacz 'R' + zgłośRejected → patrz stan kod ACKbrak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, ACK nie napłynął do CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:Processed → oznacz 'R' + zgłoś (→ powiązany stan)Rejected → wyślij ponownie przez Core CC Tool (Manual Upload) "po CET"brak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie napłynął do CET. Krytyczne.Postępowanie (KRYTYCZNE w C):Pobierz poprawny plik z aplikacji ZP i wyślij przez Core CC Tool (Manual Upload) "po CET" (jeśli bramka otwarta)Natychmiast: zgłoś + powiadom RCC szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale walidacja zakończona negatywnie — ACK Rejected po CET.Postępowanie (po CET):Najedź kursorem na status i odczytaj kod ACK (kontekst: rejestracja po CET)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka zamknięta → zgłoś + powiadom RCCkod 21 (wersja nie jest wyższa niż zapisana) → podnieś numer wersji w aplikacji ZP i wyślij plik ponownie przez Core CC Tool (Manual Upload) (jeśli bramka otwarta)kod 30 (rozmiar pliku niezgodny) → pobierz poprawny plik z MinIO lub aplikacji ZP i wyślij ponownie (jeśli bramka otwarta)CCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale ACK walidacji nie napłynął — plik dostarczony, lecz niezwalidowany.Postępowanie (po CET):Core CC Tool → sprawdź status walidacji (plik dostarczony po CET)Jeżeli:Processed → oznacz 'R' w CCM + zgłośRejected → postępuj jak w Stanie 30 (odczytaj kod ACK)brak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Dokument nie został dostarczony do CCTool, ACK nie napłynął. Minął czas CET. KRYTYCZNE — po CET dograć nie można.Postępowanie (KRYTYCZNE — brak naprawy):Telefon do RCC + zgłoś (priorytet P1)Po CET — brak naprawy. Diagnoza przyczyn: ZP · Connector 2.0 · Core CC Tool szczegóły w bazie ryzyk



##### Final Intraday NTC FID1-921

Kod: FID1-921

Profil: SFTP

TET: 14:45

CET: 14:55

Źródło: proces Core

Wersja: 1

Final Intraday NTC (FID1-921) — finalne wyniki NTC (Net Transfer Capacity) z procesu IDCC; zdolności przesyłowe udostępniane na rynek intraday (XBID).

**Ścieżka:**

proces Core / Kreator →

sFTP@pse.pl

/ ZP

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjnesFTP/ZP wysł.Plik dostarczony prawidłowo na sFTP/ZP — status pozytywny.Brak działań — proces poprawny.sFTP/ZP wysł.Status nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.sFTP/ZP wysł.Plik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.sFTP/ZP wysł.Przedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.sFTP/ZP wysł.Oczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź sFTP/ZP. Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się TET — pliku jeszcze nie ma na sFTP/ZP.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się CET / błąd dostarczenia — brak pliku na sFTP/ZP.Gdy pliku NIE ma na sFTP/ZP → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Minął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### ATC Based Validation FID1-928

Kod: FID1-928

Profil: 2CCT

TET: 13:40

CET: 14:20

Źródło: Core CC Tool

Wersja: 1

ATC Based Validation (FID1-928) — plik ZWROTNY: wynik walidacji ATC prowadzonej centralnie w Core CC Tool (strumień odrębny od FBA). NIE jest wysyłany przez TSO; publikowany CCCt → TSO przez Connector 2.0.

**Ścieżka:**

Paczka ATC (PERUN_IDx_ATC) →

Core CC Tool

(walidacja ATC) →

Connector 2.0

→

CCM

Warianty stanów (18)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.Przedwczesne (>30 min do TET). Walidacja ATC jeszcze nie ukończona.Monitoring — sprawdź w aplikacji CCM postęp walidacji paczki PERUN_IDx_ATC.CCtool wysł.CCtool zwalid.Zbliża się TET, brak FIDx-928. Walidacja paczki ATC w toku.Postępowanie:Rozwiń agregat PERUN_IDx_ATC → zweryfikuj składoweJeżeli:brak składowej → uzupełnij brakującą składową w aplikacji CCM ()składowe OK → monitoruj — czekaj na wynik walidacjiCCtool wysł.CCtool zwalid.Zbliża się CET — brak wyniku walidacji ATC. Stan alarmowy.Postępowanie (zbliża się CET):Ostatnia szansa: dokończ uzupełnienia paczki ATC w CCM; sprawdź Core CC Tool (Message Viewer)Jeżeli:plik dotrze → OK — koniecbłąd → odczytaj kod ACK (patrz powiązany stan)brak → zgłośCCtool wysł.CCtool zwalid.Minął CET, brak FIDx-928. KRYTYCZNE — brak lokalnego fallbacku.Postępowanie (KRYTYCZNE — minął CET):⛔ STOP — żadnych działań ręcznych. Brak lokalnego fallbacku (brak wyniku ATC w czasie → Dyspozytor nie wykonuje dalszych czynności).Zgłoś + telefon do RCC szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Happy Day — walidacja ATC zakończona poprawnie, wynik opublikowany.Brak interwencji — walidacja ATC zakończona poprawnie.CCtool wysł.CCtool zwalid.Wynik dotarł, ale ACK negatywny (Rejected).Postępowanie:Core CC Tool (Message Viewer) → odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś (administrator Core CC Tool otwiera bramkę)kod 21 (błąd procesowy CCCt) → zgłoś — błąd procesu w Core CC Toolkod 30 (rozmiar niezgodny) → patrz stan rozmiarCCtool wysł.CCtool zwalid.Wynik dotarł, ACK nie napłynął w czasie (timeout).Postępowanie:Czekaj 5 min → Core CC Tool (Message Viewer)Jeżeli:Processed → oznacz 'R' w CCMbrak >10 min → zgłoś — sprawdź transport zwrotny Connector 2.0 (R18)CCtool wysł.CCtool zwalid.Wynik dotarł, brak ACK do CET.Postępowanie:Sprawdź transport zwrotny Connector 2.0Jeżeli:transport OK, ACK błąd → odczytaj kod ACK (patrz powiązany stan)awaria transportu → zgłoś (R18)CCtool wysł.CCtool zwalid.Wynik dotarł, ACK napłynął po CET — pozytywny.Walidacja opóźniona, ale OK (ACK po CET pozytywny).CCtool wysł.CCtool zwalid.Status nadany ręcznie 'R' (nietypowe dla pliku zwrotnego).Brak działań — status nadany ręcznie przez Dyspozytora (nietypowe dla pliku zwrotnego).CCtool wysł.CCtool zwalid.Niepoprawny rozmiar wyniku FIDx-928.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → sprawdź rozmiar (pobranie ponownie nie ma sensu — plik zwrotny)Jeżeli:zawartość OK mimo rozmiaru → oznacz 'R' w CCMzawartość niepoprawna → zgłoś + telefon do RCCCCtool wysł.CCtool zwalid.Niepoprawny rozmiar + brak ACK (timeout).Postępowanie:Core CC Tool (Message Viewer) → sprawdź statusJeżeli:Processed → oznacz 'R' w CCMbrak → zgłoś + telefon do RCCCCtool wysł.CCtool zwalid.Niepoprawny rozmiar + ACK negatywny.Postępowanie:Core CC Tool (Message Viewer) → odczytaj kod ACKJeżeli:kod 20 (bramka zamknięta) → zgłoś (administrator Core CC Tool)kod 30 (rozmiar) → patrz powiązany staninny → zgłoś + telefon do RCCCCtool wysł.CCtool zwalid.Niepoprawny rozmiar + brak ACK do CET. KRYTYCZNE.Postępowanie (KRYTYCZNE):⛔ Krytyczne — minął CET, niepoprawny rozmiar i brak ACK.Zgłoś + telefon do RCC szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.FIDx-928 dostarczony po CET — walidacja OK.Walidacja zakończona po terminie — OK.CCtool wysł.CCtool zwalid.Wysyłka zwrotna trwa (transport Connector 2.0).Postępowanie:Czekaj 5 min (transport zwrotny Connector 2.0)Jeżeli:zmieniło się na zielony → OK — koniecbrak >10 min → zgłoś (R18)CCtool wysł.CCtool zwalid.Status ręczny przyznany (nietypowe dla pliku zwrotnego).Brak działań — status ręczny przyznany przez Dyspozytora (nietypowe dla pliku zwrotnego).CCtool wysł.CCtool zwalid.TET zbliża się, ACK błąd już teraz (błąd paczki ATC).Postępowanie:Core CC Tool (Message Viewer) → odczytaj błąd paczki ATCJeżeli:błąd składowej → uzupełnij składową w aplikacji CCMinny → odczytaj kod ACK (patrz powiązany stan)



#### IDCC(b) — 41 plików



##### 24 modele IGM DACF_IGM_UCT

Kod: DACF_IGM_UCT

Profil: SFTP

TET: 20:00

CET: 20:19

Źródło: KreatorDACF&2DAF_CGMES

Wersja: 1

24 modele IGM (DACF_IGM_UCT) — indywidualne modele sieci (Individual Grid Model) na 24 godziny doby, format UCT/CGMES; przygotowanie i eksport TSO Data Preparation.

**Ścieżka:**

KreatorDACF&2DAF_CGMES

→

sFTP@pse.pl

(Swissgrid)

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjnesFTP/ZP wysł.Plik dostarczony prawidłowo na sFTP/ZP — status pozytywny.Brak działań — proces poprawny.sFTP/ZP wysł.Status nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.sFTP/ZP wysł.Plik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.sFTP/ZP wysł.Przedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.sFTP/ZP wysł.Oczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź sFTP/ZP. Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się TET — pliku jeszcze nie ma na sFTP/ZP.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się CET / błąd dostarczenia — brak pliku na sFTP/ZP.Gdy pliku NIE ma na sFTP/ZP → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Minął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### GLSK FID2-607

Kod: FID2-607

Profil: 2CCT

TET: 20:00

CET: 20:19

Źródło: KreatorDACF&2DAF_CGMES

Wersja: 1

GLSK (Generation and Load Shift Keys, FID2-607) — klucze rozdziału zmian generacji/obciążenia dla strefy PL; dane wejściowe Initial TSO receiving.

**Ścieżka:**

KreatorDACF&2DAF_CGMES

→

Connector 2.0

→

Core CC Tool

→

MinIO

Warianty stanów (32)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool. Dyspozytor ustawił status ręcznie 'R' po weryfikacji w CCTool.Brak działań.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool po CET, ACK napłynął po CET z pozytywnym komunikatem.Brak działań — dostarczone po CET, OK.CCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool oraz otrzymanie potwierdzenia ACK.Brak działań.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — wysyłka ręczna wykonana.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 5 minOK → ustaw 'R' w CCMCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, ale ACK nie napłynął w żądanym czasie i zbliża się CET.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, a otrzymane ACK: (1) zawiera komunikat błędu (najedź kursorem); (2) proces zakończył się błędem — 'Błąd procesu'.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż zapisana) → wygeneruj kolejną wersję w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)kod 30 (rozmiar pliku niezgodny) → wygeneruj ponownie w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem po CET.Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano ACK, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — decyzja ręczna Dyspozytora.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 2-5 minOK → ustaw 'R'CCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — upłynęło więcej niż 2 minuty.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET, a otrzymane ACK: (1) komunikat błędu; (2) proces zakończył się błędem. Typowo kod 20 gateClosed.Postępowanie:Najedź kursorem na status i odczytaj kod ACK (typowo kod 20)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka jest zamknięta → zgłośinny kod → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Otrzymano potwierdzenie ACK z pozytywnym komunikatem (po CET).Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool. Trwa oczekiwanie na ACK — około 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Trwa oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → utrzymaj 'R'brak / awaria → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie otrzymano, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — Dyspozytor zatwierdził zawartość.CCtool wysł.CCtool zwalid.Dokument jeszcze nie został wysłany do CCTool, ACK nie napłynął. Plik nie wymagany (>30 min do TET).Brak działań — czekaj do TET.CCtool wysł.CCtool zwalid.Zbliża się CET — plik niedostarczony lub błąd wysyłki. Stan alarmowy.Postępowanie (alarm):Core CC Tool → sprawdź czy plik dotarł do Core CC ToolJeżeli:plik jest, brak ACK → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak pliku (awaria Connector 2.0) → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykbrak pliku w źródle → Brak pliku lub wersji w aplikacji źródłowej. Otwórz KreatorIDCF_CGMES i wygeneruj plik ponownie (kolejna wersja); jeśli aplikacja nie działa — zgłoś. pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. Oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → sprawdź rozmiar; pobierz z MinIO i rozpakujJeżeli:zawartość OK mimo rozmiaru → oznacz 'R' (→ powiązany stan)zawartość niepoprawna → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru, a ACK ma status czerwony — typowo kod 30.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → potwierdź rozmiarWygeneruj poprawny plik w KreatorIDCF_CGMES (kolejna wersja) i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)Nadal za mały → zgłoś szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK napłynął po CET z pozytywnym komunikatem. Sprzeczność.Postępowanie:Pobierz z MinIO → rozpakuj → sprawdź zawartośćJeżeli:zawartość OK → oznacz 'R' (→ powiązany stan); zgłośniepoprawna → zgłośCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, ale ACK negatywny (Rejected). Kody: 20/21/30.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś (administrator Core CC Tool otwiera bramkę); sprawdź proces IDx-AC-FORWARDINGkod 21 (wersja nie jest wyższa niż zapisana) → wygeneruj kolejną wersję w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)kod 30 (rozmiar pliku niezgodny) → wygeneruj ponownie w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, trwa oczekiwanie na ACK, który nie napłynął w zadanym czasie (>2-3 min).Postępowanie:Czekaj 5 min → Core CC Tool (⚠ nie wysyłaj ponownie!)Jeżeli:Processed → oznacz 'R' + zgłośRejected → patrz stan kod ACKbrak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, ACK nie napłynął do CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:Processed → oznacz 'R' + zgłoś (→ powiązany stan)Rejected → wyślij ponownie przez Core CC Tool (Manual Upload) "po CET"brak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie napłynął do CET. Krytyczne.Postępowanie (KRYTYCZNE w C):Wygeneruj poprawny plik w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami) "po CET" (jeśli bramka otwarta)Natychmiast: zgłoś + powiadom RCC szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale walidacja zakończona negatywnie — ACK Rejected po CET.Postępowanie (po CET):Najedź kursorem na status i odczytaj kod ACK (kontekst: rejestracja po CET)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka zamknięta → zgłoś + powiadom RCCkod 21 (wersja nie jest wyższa niż zapisana) → wygeneruj kolejną wersję w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami) (jeśli bramka otwarta)kod 30 (rozmiar pliku niezgodny) → wygeneruj ponownie w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami) (jeśli bramka otwarta)CCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale ACK walidacji nie napłynął — plik dostarczony, lecz niezwalidowany.Postępowanie (po CET):Core CC Tool → sprawdź status walidacji (plik dostarczony po CET)Jeżeli:Processed → oznacz 'R' w CCM + zgłośRejected → postępuj jak w Stanie 30 (odczytaj kod ACK)brak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Dokument nie został dostarczony do CCTool, ACK nie napłynął. Minął czas CET. KRYTYCZNE — po CET dograć nie można.Postępowanie (KRYTYCZNE — brak naprawy):Telefon do RCC + zgłoś (priorytet P1)Po CET — brak naprawy. Diagnoza przyczyn: Kreator · Connector 2.0 · Core CC Tool szczegóły w bazie ryzyk



##### Merged Generation and Load Shift Keys (GLSK) FID2-610

Kod: FID2-610

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: proces Core

Wersja: 1

Merged GLSK (FID2-610) — scalone GLSK wszystkich TSO regionu Core. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Merged Generation and Load Shift Keys (GLSK) FID2-610

Kod: FID2-610

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: proces Core

Wersja: 1

Merged GLSK (FID2-610) — scalone GLSK wszystkich TSO regionu Core. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### CBCORA FID2-617

Kod: FID2-617

Profil: 2CCT

TET: 20:00

CET: 20:19

Źródło: KreatorDACF&2DAF_CGMES

Wersja: 1

CBCORA (Critical Branches & Critical Outages with Remedial Actions, FID2-617) — lista krytycznych elementów sieci (CNEC) PSE wraz z wyłączeniami; dane wejściowe TSO.

**Ścieżka:**

KreatorDACF&2DAF_CGMES

→

Connector 2.0

→

Core CC Tool

→

MinIO

Warianty stanów (32)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool. Dyspozytor ustawił status ręcznie 'R' po weryfikacji w CCTool.Brak działań.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool po CET, ACK napłynął po CET z pozytywnym komunikatem.Brak działań — dostarczone po CET, OK.CCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool oraz otrzymanie potwierdzenia ACK.Brak działań.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — wysyłka ręczna wykonana.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 5 minOK → ustaw 'R' w CCMCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, ale ACK nie napłynął w żądanym czasie i zbliża się CET.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, a otrzymane ACK: (1) zawiera komunikat błędu (najedź kursorem); (2) proces zakończył się błędem — 'Błąd procesu'.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż zapisana) → wygeneruj kolejną wersję w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)kod 30 (rozmiar pliku niezgodny) → wygeneruj ponownie w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem po CET.Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano ACK, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — decyzja ręczna Dyspozytora.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 2-5 minOK → ustaw 'R'CCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — upłynęło więcej niż 2 minuty.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET, a otrzymane ACK: (1) komunikat błędu; (2) proces zakończył się błędem. Typowo kod 20 gateClosed.Postępowanie:Najedź kursorem na status i odczytaj kod ACK (typowo kod 20)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka jest zamknięta → zgłośinny kod → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Otrzymano potwierdzenie ACK z pozytywnym komunikatem (po CET).Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool. Trwa oczekiwanie na ACK — około 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Trwa oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → utrzymaj 'R'brak / awaria → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie otrzymano, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — Dyspozytor zatwierdził zawartość.CCtool wysł.CCtool zwalid.Dokument jeszcze nie został wysłany do CCTool, ACK nie napłynął. Plik nie wymagany (>30 min do TET).Brak działań — czekaj do TET.CCtool wysł.CCtool zwalid.Zbliża się CET — plik niedostarczony lub błąd wysyłki. Stan alarmowy.Postępowanie (alarm):Core CC Tool → sprawdź czy plik dotarł do Core CC ToolJeżeli:plik jest, brak ACK → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak pliku (awaria Connector 2.0) → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykbrak pliku w źródle → Brak pliku lub wersji w aplikacji źródłowej. Otwórz KreatorIDCF_CGMES i wygeneruj plik ponownie (kolejna wersja); jeśli aplikacja nie działa — zgłoś. pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. Oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → sprawdź rozmiar; pobierz z MinIO i rozpakujJeżeli:zawartość OK mimo rozmiaru → oznacz 'R' (→ powiązany stan)zawartość niepoprawna → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru, a ACK ma status czerwony — typowo kod 30.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → potwierdź rozmiarWygeneruj poprawny plik w KreatorIDCF_CGMES (kolejna wersja) i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)Nadal za mały → zgłoś szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK napłynął po CET z pozytywnym komunikatem. Sprzeczność.Postępowanie:Pobierz z MinIO → rozpakuj → sprawdź zawartośćJeżeli:zawartość OK → oznacz 'R' (→ powiązany stan); zgłośniepoprawna → zgłośCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, ale ACK negatywny (Rejected). Kody: 20/21/30.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś (administrator Core CC Tool otwiera bramkę); sprawdź proces IDx-AC-FORWARDINGkod 21 (wersja nie jest wyższa niż zapisana) → wygeneruj kolejną wersję w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)kod 30 (rozmiar pliku niezgodny) → wygeneruj ponownie w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, trwa oczekiwanie na ACK, który nie napłynął w zadanym czasie (>2-3 min).Postępowanie:Czekaj 5 min → Core CC Tool (⚠ nie wysyłaj ponownie!)Jeżeli:Processed → oznacz 'R' + zgłośRejected → patrz stan kod ACKbrak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, ACK nie napłynął do CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:Processed → oznacz 'R' + zgłoś (→ powiązany stan)Rejected → wyślij ponownie przez Core CC Tool (Manual Upload) "po CET"brak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie napłynął do CET. Krytyczne.Postępowanie (KRYTYCZNE w C):Wygeneruj poprawny plik w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami) "po CET" (jeśli bramka otwarta)Natychmiast: zgłoś + powiadom RCC szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale walidacja zakończona negatywnie — ACK Rejected po CET.Postępowanie (po CET):Najedź kursorem na status i odczytaj kod ACK (kontekst: rejestracja po CET)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka zamknięta → zgłoś + powiadom RCCkod 21 (wersja nie jest wyższa niż zapisana) → wygeneruj kolejną wersję w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami) (jeśli bramka otwarta)kod 30 (rozmiar pliku niezgodny) → wygeneruj ponownie w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami) (jeśli bramka otwarta)CCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale ACK walidacji nie napłynął — plik dostarczony, lecz niezwalidowany.Postępowanie (po CET):Core CC Tool → sprawdź status walidacji (plik dostarczony po CET)Jeżeli:Processed → oznacz 'R' w CCM + zgłośRejected → postępuj jak w Stanie 30 (odczytaj kod ACK)brak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Dokument nie został dostarczony do CCTool, ACK nie napłynął. Minął czas CET. KRYTYCZNE — po CET dograć nie można.Postępowanie (KRYTYCZNE — brak naprawy):Telefon do RCC + zgłoś (priorytet P1)Po CET — brak naprawy. Diagnoza przyczyn: Kreator · Connector 2.0 · Core CC Tool szczegóły w bazie ryzyk



##### Merged DACF/IDCF Common Grid Model (CGM) FID2-620

Kod: FID2-620

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: proces Core / Kreator

Wersja: 5

Merged DACF/IDCF Common Grid Model (CGM, FID2-620) — scalony wspólny model sieci zbudowany z modeli indywidualnych (IGM) TSO. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Merged DACF/IDCF Common Grid Model (CGM) FID2-620

Kod: FID2-620

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: proces Core / Kreator

Wersja: 5

Merged DACF/IDCF Common Grid Model (CGM, FID2-620) — scalony wspólny model sieci zbudowany z modeli indywidualnych (IGM) TSO. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Reference Program (RefProg) FID2-632

Kod: FID2-632

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: proces Core

Wersja: 3

Reference Program (RefProg, FID2-632) — program referencyjny: planowane salda wymiany międzyobszarowej. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Reference Program (RefProg) FID2-632

Kod: FID2-632

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: proces Core

Wersja: 3

Reference Program (RefProg, FID2-632) — program referencyjny: planowane salda wymiany międzyobszarowej. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Reference Program (RefProg) FID2-632

Kod: FID2-632

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: proces Core

Wersja: 3

Reference Program (RefProg, FID2-632) — program referencyjny: planowane salda wymiany międzyobszarowej. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Reference Program (RefProg) FID2-632

Kod: FID2-632

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: proces Core

Wersja: 3

Reference Program (RefProg, FID2-632) — program referencyjny: planowane salda wymiany międzyobszarowej. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial FB Domain (Virgin RefProg Bal) FID2-645

Kod: FID2-645

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: Perun4V / proces Core

Wersja: 1

Initial FB Domain (Virgin / RefProg Bal, FID2-645) — początkowa domena Flow-Based. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial FB Domain (RefProg Bal) FID2-645

Kod: FID2-645

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: Perun4V / proces Core

Wersja: 1

Initial FB Domain (Virgin / RefProg Bal, FID2-645) — początkowa domena Flow-Based. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial FB Domain (RefProg Bal) FID2-645

Kod: FID2-645

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: Perun4V / proces Core

Wersja: 1

Initial FB Domain (Virgin / RefProg Bal, FID2-645) — początkowa domena Flow-Based. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial FB Domain (Virgin RefProg Bal) FID2-645

Kod: FID2-645

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: Perun4V / proces Core

Wersja: 1

Initial FB Domain (Virgin / RefProg Bal, FID2-645) — początkowa domena Flow-Based. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial FB Domain (RefProg Bal) FID2-645

Kod: FID2-645

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: Perun4V / proces Core

Wersja: 1

Initial FB Domain (Virgin / RefProg Bal, FID2-645) — początkowa domena Flow-Based. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Real Generation and Load Shift Keys (GLSK) FID2-657

Kod: FID2-657

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: Kreator

Wersja: 1

Real GLSK (FID2-657) — rzeczywiste klucze GLSK (po dostosowaniu do bieżącego stanu). Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Real Generation and Load Shift Keys (GLSK) FID2-657

Kod: FID2-657

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: Kreator

Wersja: 1

Real GLSK (FID2-657) — rzeczywiste klucze GLSK (po dostosowaniu do bieżącego stanu). Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### CGM Data Quality Check FID2-659

Kod: FID2-659

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: proces Core

Wersja: 1

CGM Data Quality Check (FID2-659) — raport kontroli jakości danych scalonego modelu CGM. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### CGM Data Quality Check FID2-659

Kod: FID2-659

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: proces Core

Wersja: 1

CGM Data Quality Check (FID2-659) — raport kontroli jakości danych scalonego modelu CGM. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Individual Filtered Critical Branches (CB) FID2-665

Kod: FID2-665

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: Kreator

Wersja: 1

Individual Filtered Critical Branches (CB, FID2-665) — indywidualne, przefiltrowane gałęzie krytyczne PSE. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Individual Filtered Critical Branches (CB) FID2-665

Kod: FID2-665

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: Kreator

Wersja: 1

Individual Filtered Critical Branches (CB, FID2-665) — indywidualne, przefiltrowane gałęzie krytyczne PSE. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Vertices of Initial FB Domain FID2-701

Kod: FID2-701

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: Perun4V

Wersja: 1

Vertices of Initial FB Domain (FID2-701) — wierzchołki początkowej domeny Flow-Based. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Vertices of Initial FB Domain/CB Validation file ATC FID2-701_ATC

Kod: FID2-701_ATC

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: Perun4V

Wersja: 1

Vertices / CB Validation file ATC (FID2-701_ATC) — wierzchołki domeny / plik walidacji CB dla ścieżki ATC. Składowa paczki ATC.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Vertices of Initial FB Domain/CB Validation file ATC FID2-701_ATC

Kod: FID2-701_ATC

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: Perun4V

Wersja: 1

Vertices / CB Validation file ATC (FID2-701_ATC) — wierzchołki domeny / plik walidacji CB dla ścieżki ATC. Składowa paczki ATC.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### IVA FID2-710

Kod: FID2-710

Profil: 3COL

TET: 21:30

CET: 22:06

Źródło: Perun4V

Wersja: 1

IVA — Individual Validation Adjustment (FID2-710) — wynik indywidualnej walidacji domeny Flow-Based (z Perun4V); korekta domeny po walidacji TSO.

**Ścieżka:**

Perun4V

→

MinIO

Connector 2.0

→

CCM

Warianty stanów (46)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.MinIODokument został wysłany prawidłowo do CCTool i na MINIO, otrzymano potwierdzenie ACK z pozytywnym komunikatem (komunikat statusu powinien się pojawić po najechaniu kursorem na status).Brak — proces przebiegł poprawnie.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, Dokument ACK (CCTool zwalid.) napłynął po CET z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, nie otrzymano potwierdzenia ACK, natomiast Dyspozytor ustawił status ręcznie 'R' po weryfikacji po stronie CCTool, iż proces został zrealizowany poprawnie.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO po CET, Dokument ACK (CCTool zwalid.) napłynął po CET z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO oraz otrzymanie potwierdzenia ACK.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu aplikacji CCM w jednym miejscu (np. z menu bocznego „CCTool wysł." bądź „MINIO" korzystając z opcji „Wyślij"). Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Po 5 min jeśli proces przebiegł poprawnie → ustaw 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM, ale nie napłynął ACK w żądanym czasie i zbliża się Critical End Time dla obsługi tego dokumentu.Monitoring CCCt MV; jeśli proces OK → status 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM, a otrzymane potwierdzenie ACK (CCTool zwalid.): (1) zawiera komunikat błędu (najedź kursorem na status); (2) proces zakończył się błędem — „Błąd procesu".Weryfikacja sytuacji w CCTool. Decyzja Dyspozytora o ewentualnej kolejnej iteracji.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem po CET.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Weryfikacja w CCCt MV; jeśli Processed → status 'R' ręcznie. Diagnostyka CN2 zwrotny → zgłoś.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano ACK, natomiast Dyspozytor ustawił status ręcznie 'R' po weryfikacji po stronie CCTool, iż proces został zrealizowany poprawnie.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM po CET (opcja „Wyślij po CET"). Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — upłynęło więcej niż 2 minuty (czas oczekiwania można sprawdzić najeżdżając kursorem na status).Weryfikacja sytuacji w CCTool; jeśli proces przebiegł poprawnie → ustaw status 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM po CET, a otrzymane potwierdzenie ACK (CCTool zwalid.): (1) zawiera komunikat błędu; (2) proces zakończył się błędem — „Błąd procesu".Weryfikacja sytuacji w CCTool. Zgłoś.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM po CET. Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM po CET. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Diagnostyka CN2 zwrotny → zgłoś.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Weryfikacja w CCTool; po 5 min jeśli proces przebiegł poprawnie → ustaw 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — upłynęło więcej niż 2 minuty.Weryfikacja w CCTool; jeśli proces przebiegł poprawnie → ustaw 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Diagnostyka CN2 zwrotny → zgłoś.CCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru (w informacjach o wielkości rozmiaru dostępna z poziomu menu bocznego na statusie). Nie otrzymano potwierdzenie ACK, natomiast Dyspozytor ustawił status ręcznie 'R' po weryfikacji po stronie CCTool, iż proces został zrealizowany poprawnie.Zgłoś informacyjnie (ew. zmiana konfiguracji rozmiaru).CCtool wysł.CCtool zwalid.MinIODokument jeszcze nie został wysłany ani do CCTool ani na MINIO, w związku z tym potwierdzenie ACK nie napłynęło.Brak — monitoring. Plik nie wymagany (>30 min do TET).CCtool wysł.CCtool zwalid.MinIOZbliża się TET (21:30), a dokument nie został jeszcze obsłużony.Brak. Czujność i przygotowanie. Sprawdź Perun4V (status obliczeń); sprawdź CN2; przygotuj się na ewentualne IVA BACKUP od CCA. Jeśli sytuacja się utrzyma → Kategoria C (powiązany stan).CCtool wysł.CCtool zwalid.MinIOWysyłka do CCTool trwa i oczekiwany jest ACK, dokument dostarczony na MINIO.Jeśli taki status „CCTool wysł." trwa dłużej niż 5 minut należy zweryfikować stan w CCTool, ewentualnie zgłosić problem.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, trwa oczekiwanie na potwierdzenie ACK (status powinien się utrzymać krócej niż 3 minuty).Brak. Czekaj do 3-5 min na ACK; po tym czasie → stan timeout.CCtool wysł.CCtool zwalid.MinIOWysyłka do CCTool trwa i oczekiwany jest ACK. Dokument dostarczony na MINIO nie spełnia kryterium rozmiaru (w informacjach o wielkości rozmiaru dostępna z poziomu menu bocznego na statusie).Jeśli taki status „CCTool wysł." trwa dłużej niż 5 minut → zweryfikować stan w CCTool, ew. zgłosić problem Zweryfikować dokument IVA czy jest poprawny (pobierając go z CCM i rozpakowując) — pomimo zbyt małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOZbliża się CET (22:06), a dokument nie został jeszcze obsłużony.Procedura (wg Confluence): Jeśli zbliża się CET (poniżej 3 minut) możliwa jest ręczna wysyłka IVA Backup z menu bocznego na poniższej pozycji pulpitu. Alternatywnie: R08 (Perun4V awaria), R09 (ERR-I), R10 (Process failed).CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, potwierdzenie ACK ma status czerwony co może oznaczać: (1) zawiera komunikat błędu (najedź kursorem na status); (2) proces zakończył się błędem — „Błąd procesu".Procedura: R05 — reakcja per kod ACK (20 gateClosed / 21 duplicatedVersion / 30 file size). Należy zweryfikować sytuację w CCTool.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, trwa oczekiwanie na potwierdzenie ACK, które nie napłynęło w zadanym czasie (po najechaniu na znak zapytania można sprawdzić ile upłynęło czasu).Procedura: R06. Jeśli po około 3 minutach nie pojawi się status ACK wraz z informacją dostępną po najechaniu na status → należy zweryfikować sytuację w CCTool.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO. Dokument ACK (CCTool zwalid.) nie napłynął do CET.Procedury: R06, R18. Należy zweryfikować sytuację w CCTool. W przypadku wygenerowania ACK po stronie CCTool — sytuację zgłosić.CCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru (w informacjach o wielkości rozmiaru dostępna z poziomu menu bocznego na statusie). Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Procedura: R05. Zweryfikować dokument IVA czy jest poprawny (pobierając go z CCM i rozpakowując) — pomimo zbyt małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 1 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.), które nie napłynęło w zadanym czasie (po najechaniu na znak zapytania można sprawdzić ile upłynęło czasu).Procedura: R05, R06. Jeśli po około 3 minutach nie pojawi się status ACK wraz z informacją po najechaniu na status → zweryfikować sytuację w CCTool Zweryfikować dokument IVA (pobranie z CCM i rozpakowanie) — pomimo małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru, a otrzymane potwierdzenie ACK (CCTool zwalid.): (1) zawiera komunikat błędu; (2) proces zakończył się błędem — „Błąd procesu".Procedura: R05. Należy zweryfikować sytuację w CCTool Zweryfikować dokument IVA czy jest poprawny (pobranie z CCM i rozpakowanie) — pomimo małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru. Dokument ACK (CCTool zwalid.) napłynął po CET z pozytywnym komunikatem.Należy zweryfikować dokument IVA czy jest poprawny i czy został przyjęty w CCTool Jeśli plik z pkt. 1 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCTool Po weryfikacji można nadać 'R' → Stan #21 (Kategoria A).CCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru. Dokument ACK (CCTool zwalid.) nie napłynął do CET.Zweryfikować sytuację w CCTool — w przypadku wygenerowania ACK po stronie CCTool sytuację zgłosić Zweryfikować dokument IVA (pobranie z CCM i rozpakowanie) — pomimo małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO po CET, potwierdzenie ACK ma status czerwony co może oznaczać: (1) zawiera komunikat błędu; (2) proces zakończył się błędem — „Błąd procesu".Procedura: R05. Należy zweryfikować sytuację w CCTool.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO po CET. Dokument ACK (CCTool zwalid.) nie napłynął do CET.Procedury: R06, R18. Należy zweryfikować sytuację w CCTool, w przypadku wygenerowania ACK po stronie CCTool sytuację zgłosić.CCtool wysł.CCtool zwalid.MinIODokument nie został dostarczony ani do CCTool ani na MINIO, w związku z tym potwierdzenie ACK nie napłynęło. Minął czas CET.Procedura (wg Confluence): Należy zweryfikować czy dokument IVA jest w PERUN. Jeśli TAK to należy go niezwłocznie pozyskać ręcznie i wysłać ją bezpośrednio z CCM bądź z GUI CCTool Procedury IDCC: R10 (Process failed) — oczekuj IVA BACKUP v1 od CCA; brak → R19 (CN2 nie kopiuje do CCA), R23 (brak raportu CCA). Zgłoś (CIZ, WPO, PSE-I) + telefon CCC. ❌ Zakaz fallbacku 20% Fmax z DA.MinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### IVA Backup FID2-710

Kod: FID2-710

Profil: MIN

TET: 21:30

CET: 22:06

Źródło: CCA

Wersja: 1

IVA Backup (FID2-710) — backupowa wersja IVA generowana przez CCA (publikowana do cca/…/out/), na wypadek braku/niezgodności IVA podstawowego.

**Ścieżka:**

CCA

→

MinIO

→

CCM

Warianty stanów (46)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.MinIODokument został wysłany prawidłowo do CCTool i na MINIO, otrzymano potwierdzenie ACK z pozytywnym komunikatem (komunikat statusu powinien się pojawić po najechaniu kursorem na status).Brak — proces przebiegł poprawnie.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, Dokument ACK (CCTool zwalid.) napłynął po CET z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, nie otrzymano potwierdzenia ACK, natomiast Dyspozytor ustawił status ręcznie 'R' po weryfikacji po stronie CCTool, iż proces został zrealizowany poprawnie.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO po CET, Dokument ACK (CCTool zwalid.) napłynął po CET z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO oraz otrzymanie potwierdzenia ACK.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu aplikacji CCM w jednym miejscu (np. z menu bocznego „CCTool wysł." bądź „MINIO" korzystając z opcji „Wyślij"). Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Po 5 min jeśli proces przebiegł poprawnie → ustaw 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM, ale nie napłynął ACK w żądanym czasie i zbliża się Critical End Time dla obsługi tego dokumentu.Monitoring CCCt MV; jeśli proces OK → status 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM, a otrzymane potwierdzenie ACK (CCTool zwalid.): (1) zawiera komunikat błędu (najedź kursorem na status); (2) proces zakończył się błędem — „Błąd procesu".Weryfikacja sytuacji w CCTool. Decyzja Dyspozytora o ewentualnej kolejnej iteracji.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem po CET.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Weryfikacja w CCCt MV; jeśli Processed → status 'R' ręcznie. Diagnostyka CN2 zwrotny → zgłoś.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano ACK, natomiast Dyspozytor ustawił status ręcznie 'R' po weryfikacji po stronie CCTool, iż proces został zrealizowany poprawnie.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM po CET (opcja „Wyślij po CET"). Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — upłynęło więcej niż 2 minuty (czas oczekiwania można sprawdzić najeżdżając kursorem na status).Weryfikacja sytuacji w CCTool; jeśli proces przebiegł poprawnie → ustaw status 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM po CET, a otrzymane potwierdzenie ACK (CCTool zwalid.): (1) zawiera komunikat błędu; (2) proces zakończył się błędem — „Błąd procesu".Weryfikacja sytuacji w CCTool. Zgłoś.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM po CET. Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM po CET. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Diagnostyka CN2 zwrotny → zgłoś.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Weryfikacja w CCTool; po 5 min jeśli proces przebiegł poprawnie → ustaw 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — upłynęło więcej niż 2 minuty.Weryfikacja w CCTool; jeśli proces przebiegł poprawnie → ustaw 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Diagnostyka CN2 zwrotny → zgłoś.CCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru (w informacjach o wielkości rozmiaru dostępna z poziomu menu bocznego na statusie). Nie otrzymano potwierdzenie ACK, natomiast Dyspozytor ustawił status ręcznie 'R' po weryfikacji po stronie CCTool, iż proces został zrealizowany poprawnie.Zgłoś informacyjnie (ew. zmiana konfiguracji rozmiaru).CCtool wysł.CCtool zwalid.MinIODokument jeszcze nie został wysłany ani do CCTool ani na MINIO, w związku z tym potwierdzenie ACK nie napłynęło.Brak — monitoring. Plik nie wymagany (>30 min do TET).CCtool wysł.CCtool zwalid.MinIOZbliża się TET (21:30), a dokument nie został jeszcze obsłużony.Brak. Czujność i przygotowanie. Sprawdź Perun4V (status obliczeń); sprawdź CN2; przygotuj się na ewentualne IVA BACKUP od CCA. Jeśli sytuacja się utrzyma → Kategoria C (powiązany stan).CCtool wysł.CCtool zwalid.MinIOWysyłka do CCTool trwa i oczekiwany jest ACK, dokument dostarczony na MINIO.Jeśli taki status „CCTool wysł." trwa dłużej niż 5 minut należy zweryfikować stan w CCTool, ewentualnie zgłosić problem.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, trwa oczekiwanie na potwierdzenie ACK (status powinien się utrzymać krócej niż 3 minuty).Brak. Czekaj do 3-5 min na ACK; po tym czasie → stan timeout.CCtool wysł.CCtool zwalid.MinIOWysyłka do CCTool trwa i oczekiwany jest ACK. Dokument dostarczony na MINIO nie spełnia kryterium rozmiaru (w informacjach o wielkości rozmiaru dostępna z poziomu menu bocznego na statusie).Jeśli taki status „CCTool wysł." trwa dłużej niż 5 minut → zweryfikować stan w CCTool, ew. zgłosić problem Zweryfikować dokument IVA czy jest poprawny (pobierając go z CCM i rozpakowując) — pomimo zbyt małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOZbliża się CET (22:06), a dokument nie został jeszcze obsłużony.Procedura (wg Confluence): Jeśli zbliża się CET (poniżej 3 minut) możliwa jest ręczna wysyłka IVA Backup z menu bocznego na poniższej pozycji pulpitu. Alternatywnie: R08 (Perun4V awaria), R09 (ERR-I), R10 (Process failed).CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, potwierdzenie ACK ma status czerwony co może oznaczać: (1) zawiera komunikat błędu (najedź kursorem na status); (2) proces zakończył się błędem — „Błąd procesu".Procedura: R05 — reakcja per kod ACK (20 gateClosed / 21 duplicatedVersion / 30 file size). Należy zweryfikować sytuację w CCTool.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, trwa oczekiwanie na potwierdzenie ACK, które nie napłynęło w zadanym czasie (po najechaniu na znak zapytania można sprawdzić ile upłynęło czasu).Procedura: R06. Jeśli po około 3 minutach nie pojawi się status ACK wraz z informacją dostępną po najechaniu na status → należy zweryfikować sytuację w CCTool.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO. Dokument ACK (CCTool zwalid.) nie napłynął do CET.Procedury: R06, R18. Należy zweryfikować sytuację w CCTool. W przypadku wygenerowania ACK po stronie CCTool — sytuację zgłosić.CCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru (w informacjach o wielkości rozmiaru dostępna z poziomu menu bocznego na statusie). Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Procedura: R05. Zweryfikować dokument IVA czy jest poprawny (pobierając go z CCM i rozpakowując) — pomimo zbyt małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 1 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.), które nie napłynęło w zadanym czasie (po najechaniu na znak zapytania można sprawdzić ile upłynęło czasu).Procedura: R05, R06. Jeśli po około 3 minutach nie pojawi się status ACK wraz z informacją po najechaniu na status → zweryfikować sytuację w CCTool Zweryfikować dokument IVA (pobranie z CCM i rozpakowanie) — pomimo małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru, a otrzymane potwierdzenie ACK (CCTool zwalid.): (1) zawiera komunikat błędu; (2) proces zakończył się błędem — „Błąd procesu".Procedura: R05. Należy zweryfikować sytuację w CCTool Zweryfikować dokument IVA czy jest poprawny (pobranie z CCM i rozpakowanie) — pomimo małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru. Dokument ACK (CCTool zwalid.) napłynął po CET z pozytywnym komunikatem.Należy zweryfikować dokument IVA czy jest poprawny i czy został przyjęty w CCTool Jeśli plik z pkt. 1 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCTool Po weryfikacji można nadać 'R' → Stan #21 (Kategoria A).CCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru. Dokument ACK (CCTool zwalid.) nie napłynął do CET.Zweryfikować sytuację w CCTool — w przypadku wygenerowania ACK po stronie CCTool sytuację zgłosić Zweryfikować dokument IVA (pobranie z CCM i rozpakowanie) — pomimo małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO po CET, potwierdzenie ACK ma status czerwony co może oznaczać: (1) zawiera komunikat błędu; (2) proces zakończył się błędem — „Błąd procesu".Procedura: R05. Należy zweryfikować sytuację w CCTool.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO po CET. Dokument ACK (CCTool zwalid.) nie napłynął do CET.Procedury: R06, R18. Należy zweryfikować sytuację w CCTool, w przypadku wygenerowania ACK po stronie CCTool sytuację zgłosić.CCtool wysł.CCtool zwalid.MinIODokument nie został dostarczony ani do CCTool ani na MINIO, w związku z tym potwierdzenie ACK nie napłynęło. Minął czas CET.Procedura (wg Confluence): Należy zweryfikować czy dokument IVA jest w PERUN. Jeśli TAK to należy go niezwłocznie pozyskać ręcznie i wysłać ją bezpośrednio z CCM bądź z GUI CCTool Procedury IDCC: R10 (Process failed) — oczekuj IVA BACKUP v1 od CCA; brak → R19 (CN2 nie kopiuje do CCA), R23 (brak raportu CCA). Zgłoś (CIZ, WPO, PSE-I) + telefon CCC. ❌ Zakaz fallbacku 20% Fmax z DA.MinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### IVA_ATC FID2-710_ATC

Kod: FID2-710_ATC

Profil: MIN

TET: 21:40

CET: 22:05

Źródło: Perun4V

Wersja: 1

IVA_ATC (FID2-710_ATC) — IVA dla odrębnej ścieżki walidacji domeny ATC.

**Ścieżka:**

Perun4V

→

MinIO

Connector 2.0

→

CCM

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### IVA_ATC FID2-710_ATC

Kod: FID2-710_ATC

Profil: MIN

TET: 21:40

CET: 22:05

Źródło: Perun4V

Wersja: 1

IVA_ATC (FID2-710_ATC) — IVA dla odrębnej ścieżki walidacji domeny ATC.

**Ścieżka:**

Perun4V

→

MinIO

Connector 2.0

→

CCM

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### AC FID2-831

Kod: FID2-831

Profil: 2CCT

TET: 21:45

CET: 21:55

Źródło: ZP

Wersja: 1

AC (Allocation Constraints, FID2-831) — plik z wartościami ograniczeń alokacyjnych wyznaczonych przez PSE, publikowany do PuTo i do procesu Core. Format XML, MTU 15 min.

**Ścieżka:**

ZP

→

Connector 2.0

→

Core CC Tool

→

PuTo

+

MinIO

Warianty stanów (32)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool. Dyspozytor ustawił status ręcznie 'R' po weryfikacji w CCTool.Brak działań.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool po CET, ACK napłynął po CET z pozytywnym komunikatem.Brak działań — dostarczone po CET, OK.CCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool oraz otrzymanie potwierdzenia ACK.Brak działań.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — wysyłka ręczna wykonana.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 5 minOK → ustaw 'R' w CCMCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, ale ACK nie napłynął w żądanym czasie i zbliża się CET.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, a otrzymane ACK: (1) zawiera komunikat błędu (najedź kursorem); (2) proces zakończył się błędem — 'Błąd procesu'.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż zapisana) → podnieś numer wersji w aplikacji ZP i wyślij plik ponownie przez Core CC Tool (Manual Upload)kod 30 (rozmiar pliku niezgodny) → pobierz poprawny plik z MinIO lub aplikacji ZP i wyślij ponownieCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem po CET.Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano ACK, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — decyzja ręczna Dyspozytora.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 2-5 minOK → ustaw 'R'CCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — upłynęło więcej niż 2 minuty.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET, a otrzymane ACK: (1) komunikat błędu; (2) proces zakończył się błędem. Typowo kod 20 gateClosed.Postępowanie:Najedź kursorem na status i odczytaj kod ACK (typowo kod 20)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka jest zamknięta → zgłośinny kod → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Otrzymano potwierdzenie ACK z pozytywnym komunikatem (po CET).Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool. Trwa oczekiwanie na ACK — około 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Trwa oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → utrzymaj 'R'brak / awaria → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie otrzymano, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — Dyspozytor zatwierdził zawartość.CCtool wysł.CCtool zwalid.Dokument jeszcze nie został wysłany do CCTool, ACK nie napłynął. Plik nie wymagany (>30 min do TET).Brak działań — czekaj do TET.CCtool wysł.CCtool zwalid.Zbliża się CET — plik niedostarczony lub błąd wysyłki. Stan alarmowy.Postępowanie (alarm):Core CC Tool → sprawdź czy plik dotarł do Core CC ToolJeżeli:plik jest, brak ACK → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak pliku (awaria Connector 2.0) → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykbrak pliku w źródle → Brak pliku lub wersji w aplikacji źródłowej. Otwórz aplikacji ZP, przejdź do bilansu i sprawdź wersję pliku: jeśli wersja jest dostępna — pobierz ją (Pobierz XML); jeśli brakuje — wygeneruj nową wersję; jeśli aplikacja nie działa — zgłoś. pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. Oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → sprawdź rozmiar; pobierz z MinIO i rozpakujJeżeli:zawartość OK mimo rozmiaru → oznacz 'R' (→ powiązany stan)zawartość niepoprawna → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru, a ACK ma status czerwony — typowo kod 30.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → potwierdź rozmiarPobierz poprawny plik z aplikacji ZP (Pobierz XML) i wyślij przez Core CC Tool (Manual Upload) z kolejnym numerem wersjiNadal za mały → zgłoś szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK napłynął po CET z pozytywnym komunikatem. Sprzeczność.Postępowanie:Pobierz z MinIO → rozpakuj → sprawdź zawartośćJeżeli:zawartość OK → oznacz 'R' (→ powiązany stan); zgłośniepoprawna → zgłośCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, ale ACK negatywny (Rejected). Kody: 20/21/30.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś (administrator Core CC Tool otwiera bramkę); sprawdź proces IDx-AC-FORWARDINGkod 21 (wersja nie jest wyższa niż zapisana) → podnieś numer wersji w aplikacji ZP i wyślij plik ponownie przez Core CC Tool (Manual Upload)kod 30 (rozmiar pliku niezgodny) → pobierz poprawny plik z MinIO lub aplikacji ZP i wyślij ponownieCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, trwa oczekiwanie na ACK, który nie napłynął w zadanym czasie (>2-3 min).Postępowanie:Czekaj 5 min → Core CC Tool (⚠ nie wysyłaj ponownie!)Jeżeli:Processed → oznacz 'R' + zgłośRejected → patrz stan kod ACKbrak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, ACK nie napłynął do CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:Processed → oznacz 'R' + zgłoś (→ powiązany stan)Rejected → wyślij ponownie przez Core CC Tool (Manual Upload) "po CET"brak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie napłynął do CET. Krytyczne.Postępowanie (KRYTYCZNE w C):Pobierz poprawny plik z aplikacji ZP i wyślij przez Core CC Tool (Manual Upload) "po CET" (jeśli bramka otwarta)Natychmiast: zgłoś + powiadom RCC szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale walidacja zakończona negatywnie — ACK Rejected po CET.Postępowanie (po CET):Najedź kursorem na status i odczytaj kod ACK (kontekst: rejestracja po CET)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka zamknięta → zgłoś + powiadom RCCkod 21 (wersja nie jest wyższa niż zapisana) → podnieś numer wersji w aplikacji ZP i wyślij plik ponownie przez Core CC Tool (Manual Upload) (jeśli bramka otwarta)kod 30 (rozmiar pliku niezgodny) → pobierz poprawny plik z MinIO lub aplikacji ZP i wyślij ponownie (jeśli bramka otwarta)CCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale ACK walidacji nie napłynął — plik dostarczony, lecz niezwalidowany.Postępowanie (po CET):Core CC Tool → sprawdź status walidacji (plik dostarczony po CET)Jeżeli:Processed → oznacz 'R' w CCM + zgłośRejected → postępuj jak w Stanie 30 (odczytaj kod ACK)brak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Dokument nie został dostarczony do CCTool, ACK nie napłynął. Minął czas CET. KRYTYCZNE — po CET dograć nie można.Postępowanie (KRYTYCZNE — brak naprawy):Telefon do RCC + zgłoś (priorytet P1)Po CET — brak naprawy. Diagnoza przyczyn: ZP · Connector 2.0 · Core CC Tool szczegóły w bazie ryzyk



##### Initial Intraday ATCs FID2-882

Kod: FID2-882

Profil: MIN

TET: 20:30

CET: 20:50

Źródło: proces Core

Wersja: 1

Initial Intraday ATCs (FID2-882) — początkowe wartości ATC dla intraday; wejście walidacji ATC. Składowa paczki.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial Intraday ATCs FID2-882

Kod: FID2-882

Profil: MIN

TET: 20:30

CET: 20:50

Źródło: proces Core

Wersja: 1

Initial Intraday ATCs (FID2-882) — początkowe wartości ATC dla intraday; wejście walidacji ATC. Składowa paczki.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial Intraday ATCs FID2-882

Kod: FID2-882

Profil: MIN

TET: 20:30

CET: 20:50

Źródło: proces Core

Wersja: 1

Initial Intraday ATCs (FID2-882) — początkowe wartości ATC dla intraday; wejście walidacji ATC. Składowa paczki.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Final Intraday NTC FID2-921

Kod: FID2-921

Profil: SFTP

TET: 21:45

CET: 21:49

Źródło: proces Core

Wersja: 1

Final Intraday NTC (FID2-921) — finalne wyniki NTC (Net Transfer Capacity) z procesu IDCC; zdolności przesyłowe udostępniane na rynek intraday (XBID).

**Ścieżka:**

proces Core / Kreator →

sFTP@pse.pl

/ ZP

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjnesFTP/ZP wysł.Plik dostarczony prawidłowo na sFTP/ZP — status pozytywny.Brak działań — proces poprawny.sFTP/ZP wysł.Status nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.sFTP/ZP wysł.Plik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.sFTP/ZP wysł.Przedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.sFTP/ZP wysł.Oczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź sFTP/ZP. Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się TET — pliku jeszcze nie ma na sFTP/ZP.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się CET / błąd dostarczenia — brak pliku na sFTP/ZP.Gdy pliku NIE ma na sFTP/ZP → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Minął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### ATC Based Validation FID2-928

Kod: FID2-928

Profil: 2CCT

TET: 21:40

CET: 22:05

Źródło: Core CC Tool

Wersja: 1

ATC Based Validation (FID2-928) — plik ZWROTNY: wynik walidacji ATC prowadzonej centralnie w Core CC Tool (strumień odrębny od FBA). NIE jest wysyłany przez TSO; publikowany CCCt → TSO przez Connector 2.0.

**Ścieżka:**

Paczka ATC (PERUN_IDx_ATC) →

Core CC Tool

(walidacja ATC) →

Connector 2.0

→

CCM

Warianty stanów (18)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.Przedwczesne (>30 min do TET). Walidacja ATC jeszcze nie ukończona.Monitoring — sprawdź w aplikacji CCM postęp walidacji paczki PERUN_IDx_ATC.CCtool wysł.CCtool zwalid.Zbliża się TET, brak FIDx-928. Walidacja paczki ATC w toku.Postępowanie:Rozwiń agregat PERUN_IDx_ATC → zweryfikuj składoweJeżeli:brak składowej → uzupełnij brakującą składową w aplikacji CCM ()składowe OK → monitoruj — czekaj na wynik walidacjiCCtool wysł.CCtool zwalid.Zbliża się CET — brak wyniku walidacji ATC. Stan alarmowy.Postępowanie (zbliża się CET):Ostatnia szansa: dokończ uzupełnienia paczki ATC w CCM; sprawdź Core CC Tool (Message Viewer)Jeżeli:plik dotrze → OK — koniecbłąd → odczytaj kod ACK (patrz powiązany stan)brak → zgłośCCtool wysł.CCtool zwalid.Minął CET, brak FIDx-928. KRYTYCZNE — brak lokalnego fallbacku.Postępowanie (KRYTYCZNE — minął CET):⛔ STOP — żadnych działań ręcznych. Brak lokalnego fallbacku (brak wyniku ATC w czasie → Dyspozytor nie wykonuje dalszych czynności).Zgłoś + telefon do RCC szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Happy Day — walidacja ATC zakończona poprawnie, wynik opublikowany.Brak interwencji — walidacja ATC zakończona poprawnie.CCtool wysł.CCtool zwalid.Wynik dotarł, ale ACK negatywny (Rejected).Postępowanie:Core CC Tool (Message Viewer) → odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś (administrator Core CC Tool otwiera bramkę)kod 21 (błąd procesowy CCCt) → zgłoś — błąd procesu w Core CC Toolkod 30 (rozmiar niezgodny) → patrz stan rozmiarCCtool wysł.CCtool zwalid.Wynik dotarł, ACK nie napłynął w czasie (timeout).Postępowanie:Czekaj 5 min → Core CC Tool (Message Viewer)Jeżeli:Processed → oznacz 'R' w CCMbrak >10 min → zgłoś — sprawdź transport zwrotny Connector 2.0 (R18)CCtool wysł.CCtool zwalid.Wynik dotarł, brak ACK do CET.Postępowanie:Sprawdź transport zwrotny Connector 2.0Jeżeli:transport OK, ACK błąd → odczytaj kod ACK (patrz powiązany stan)awaria transportu → zgłoś (R18)CCtool wysł.CCtool zwalid.Wynik dotarł, ACK napłynął po CET — pozytywny.Walidacja opóźniona, ale OK (ACK po CET pozytywny).CCtool wysł.CCtool zwalid.Status nadany ręcznie 'R' (nietypowe dla pliku zwrotnego).Brak działań — status nadany ręcznie przez Dyspozytora (nietypowe dla pliku zwrotnego).CCtool wysł.CCtool zwalid.Niepoprawny rozmiar wyniku FIDx-928.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → sprawdź rozmiar (pobranie ponownie nie ma sensu — plik zwrotny)Jeżeli:zawartość OK mimo rozmiaru → oznacz 'R' w CCMzawartość niepoprawna → zgłoś + telefon do RCCCCtool wysł.CCtool zwalid.Niepoprawny rozmiar + brak ACK (timeout).Postępowanie:Core CC Tool (Message Viewer) → sprawdź statusJeżeli:Processed → oznacz 'R' w CCMbrak → zgłoś + telefon do RCCCCtool wysł.CCtool zwalid.Niepoprawny rozmiar + ACK negatywny.Postępowanie:Core CC Tool (Message Viewer) → odczytaj kod ACKJeżeli:kod 20 (bramka zamknięta) → zgłoś (administrator Core CC Tool)kod 30 (rozmiar) → patrz powiązany staninny → zgłoś + telefon do RCCCCtool wysł.CCtool zwalid.Niepoprawny rozmiar + brak ACK do CET. KRYTYCZNE.Postępowanie (KRYTYCZNE):⛔ Krytyczne — minął CET, niepoprawny rozmiar i brak ACK.Zgłoś + telefon do RCC szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.FIDx-928 dostarczony po CET — walidacja OK.Walidacja zakończona po terminie — OK.CCtool wysł.CCtool zwalid.Wysyłka zwrotna trwa (transport Connector 2.0).Postępowanie:Czekaj 5 min (transport zwrotny Connector 2.0)Jeżeli:zmieniło się na zielony → OK — koniecbrak >10 min → zgłoś (R18)CCtool wysł.CCtool zwalid.Status ręczny przyznany (nietypowe dla pliku zwrotnego).Brak działań — status ręczny przyznany przez Dyspozytora (nietypowe dla pliku zwrotnego).CCtool wysł.CCtool zwalid.TET zbliża się, ACK błąd już teraz (błąd paczki ATC).Postępowanie:Core CC Tool (Message Viewer) → odczytaj błąd paczki ATCJeżeli:błąd składowej → uzupełnij składową w aplikacji CCMinny → odczytaj kod ACK (patrz powiązany stan)



##### AGR Paczka ZIP ID2 PERUN_ID2

Kod: PERUN_ID2

Profil: 2MS

TET: 20:40

CET: 21:05

Źródło: agregacja

Wersja: 1

AGR Paczka ZIP (PERUN_ID2) — zagregowana paczka wejściowa do Perun4V (proces FBA); zawiera składowe: scalone GLSK, CGM, RefProg, początkową domenę FB, CB, wierzchołki, RA.

**Ścieżka:**

Agregacja składowych →

MinIO

sFTP@pse.pl

→

Perun4V

Warianty stanów (10)

Status kafelkaSytuacjaDziałania awaryjneMinIOsFTP/ZP wysł.Paczka dostarczona prawidłowo na MinIO i sFTP/ZP.Brak działań — proces poprawny.MinIOsFTP/ZP wysł.Status nadany ręcznie 'R' po weryfikacji.Brak działań — decyzja ręczna.MinIOsFTP/ZP wysł.Paczka dostarczona po CET — status pozytywny.Brak działań — po CET OK.MinIOsFTP/ZP wysł.Przedwczesne — paczka jeszcze niewymagana.Monitoring — czekaj do TET.MinIOsFTP/ZP wysł.Zbliża się TET — paczka niekompletna / brak.Sprawdź agregację składowych. Gdy brak → zagreguj/pobierz ręcznie i wrzuć (Manual Upload / wysyłka na sFTP).MinIOsFTP/ZP wysł.Na MinIO OK, brak / błąd na sFTP/ZP.Gdy brak na sFTP → wyślij plik ręcznie ze źródła na sFTP/ZP.MinIOsFTP/ZP wysł.Brak / błąd na MinIO, OK na sFTP/ZP.Gdy brak na MinIO → pobierz/wygeneruj ręcznie i wgraj przez Manual Upload (GUI Core CC Tool).MinIOsFTP/ZP wysł.Transfer w toku (MinIO i sFTP/ZP).Czekaj 5 min → sprawdź MinIO i sFTP. Gdy brak → ręcznie (Manual Upload / wysyłka na sFTP).MinIOsFTP/ZP wysł.Zbliża się CET — brak / błąd na MinIO i sFTP/ZP.Gdy brak na MinIO → Manual Upload; gdy brak na sFTP → wyślij ręcznie.MinIOsFTP/ZP wysł.Minął CET — paczka niedostarczona. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Postępowanie krytyczne.



##### AGR Paczka ZIP_ATC ID2 do Perun PERUN_ID2_ATC

Kod: PERUN_ID2_ATC

Profil: 2MS

TET: 20:40

CET: 21:05

Źródło: agregacja

Wersja: 1

AGR Paczka ZIP_ATC (PERUN_ID2_ATC) — paczka wejściowa dla odrębnej ścieżki walidacji domeny ATC.

**Ścieżka:**

Agregacja składowych →

MinIO

sFTP@pse.pl

→

Perun4V

Warianty stanów (10)

Status kafelkaSytuacjaDziałania awaryjneMinIOsFTP/ZP wysł.Paczka dostarczona prawidłowo na MinIO i sFTP/ZP.Brak działań — proces poprawny.MinIOsFTP/ZP wysł.Status nadany ręcznie 'R' po weryfikacji.Brak działań — decyzja ręczna.MinIOsFTP/ZP wysł.Paczka dostarczona po CET — status pozytywny.Brak działań — po CET OK.MinIOsFTP/ZP wysł.Przedwczesne — paczka jeszcze niewymagana.Monitoring — czekaj do TET.MinIOsFTP/ZP wysł.Zbliża się TET — paczka niekompletna / brak.Sprawdź agregację składowych. Gdy brak → zagreguj/pobierz ręcznie i wrzuć (Manual Upload / wysyłka na sFTP).MinIOsFTP/ZP wysł.Na MinIO OK, brak / błąd na sFTP/ZP.Gdy brak na sFTP → wyślij plik ręcznie ze źródła na sFTP/ZP.MinIOsFTP/ZP wysł.Brak / błąd na MinIO, OK na sFTP/ZP.Gdy brak na MinIO → pobierz/wygeneruj ręcznie i wgraj przez Manual Upload (GUI Core CC Tool).MinIOsFTP/ZP wysł.Transfer w toku (MinIO i sFTP/ZP).Czekaj 5 min → sprawdź MinIO i sFTP. Gdy brak → ręcznie (Manual Upload / wysyłka na sFTP).MinIOsFTP/ZP wysł.Zbliża się CET — brak / błąd na MinIO i sFTP/ZP.Gdy brak na MinIO → Manual Upload; gdy brak na sFTP → wyślij ręcznie.MinIOsFTP/ZP wysł.Minął CET — paczka niedostarczona. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Postępowanie krytyczne.



##### Raporty ID2 z Perun RAP_PERUN_ID2

Kod: RAP_PERUN_ID2

Profil: SFTP

TET: 21:30

CET: 21:33

Źródło: Perun4V

Wersja: 1

Raporty z Perun (RAP_PERUN_ID2) — raporty walidacyjne z procesu Perun4V (charakter informacyjny).

**Ścieżka:**

Perun4V

→

kdm6@pse.pl

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjnesFTP/ZP wysł.Plik dostarczony prawidłowo na sFTP/ZP — status pozytywny.Brak działań — proces poprawny.sFTP/ZP wysł.Status nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.sFTP/ZP wysł.Plik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.sFTP/ZP wysł.Przedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.sFTP/ZP wysł.Oczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź sFTP/ZP. Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się TET — pliku jeszcze nie ma na sFTP/ZP.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się CET / błąd dostarczenia — brak pliku na sFTP/ZP.Gdy pliku NIE ma na sFTP/ZP → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Minął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Raporty ID2 ATC z Perun RAP_PERUN_ID2_ATC

Kod: RAP_PERUN_ID2_ATC

Profil: SFTP

TET: 21:40

CET: 22:05

Źródło: Perun4V

Wersja: 1

Raporty z Perun (RAP_PERUN_ID2_ATC) — raporty walidacyjne z procesu Perun4V (charakter informacyjny).

**Ścieżka:**

Perun4V

→

kdm6@pse.pl

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjnesFTP/ZP wysł.Plik dostarczony prawidłowo na sFTP/ZP — status pozytywny.Brak działań — proces poprawny.sFTP/ZP wysł.Status nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.sFTP/ZP wysł.Plik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.sFTP/ZP wysł.Przedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.sFTP/ZP wysł.Oczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź sFTP/ZP. Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się TET — pliku jeszcze nie ma na sFTP/ZP.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się CET / błąd dostarczenia — brak pliku na sFTP/ZP.Gdy pliku NIE ma na sFTP/ZP → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Minął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Plik ze środkami zaradczymi z aplikacji KreatorDACF_CGMES XID_RA

Kod: XID_RA

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: KreatorIDCF_CGMES

Wersja: 3

Plik ze środkami zaradczymi (RA, XID_RA) — remedial actions wygenerowane w Kreatorze; publikowane razem z GLSK/CBCORA i jako składowa paczki.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Plik ze środkami zaradczymi z aplikacji KreatorDACF_CGMES XID_RA

Kod: XID_RA

Profil: MIN

TET: 20:40

CET: 21:05

Źródło: KreatorIDCF_CGMES

Wersja: 3

Plik ze środkami zaradczymi (RA, XID_RA) — remedial actions wygenerowane w Kreatorze; publikowane razem z GLSK/CBCORA i jako składowa paczki.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



#### IDCC(c) — 40 plików



##### GLSK FID3C-607

Kod: FID3C-607

Profil: 2CCT

TET: 00:00

CET: 00:56

Źródło: KreatorDACF&2DAF_CGMES

Wersja: 3

GLSK (Generation and Load Shift Keys, FID3C-607) — klucze rozdziału zmian generacji/obciążenia dla strefy PL; dane wejściowe Initial TSO receiving.

**Ścieżka:**

KreatorDACF&2DAF_CGMES

→

Connector 2.0

→

Core CC Tool

→

MinIO

Warianty stanów (32)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool. Dyspozytor ustawił status ręcznie 'R' po weryfikacji w CCTool.Brak działań.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool po CET, ACK napłynął po CET z pozytywnym komunikatem.Brak działań — dostarczone po CET, OK.CCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool oraz otrzymanie potwierdzenia ACK.Brak działań.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — wysyłka ręczna wykonana.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 5 minOK → ustaw 'R' w CCMCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, ale ACK nie napłynął w żądanym czasie i zbliża się CET.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, a otrzymane ACK: (1) zawiera komunikat błędu (najedź kursorem); (2) proces zakończył się błędem — 'Błąd procesu'.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż zapisana) → wygeneruj kolejną wersję w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)kod 30 (rozmiar pliku niezgodny) → wygeneruj ponownie w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem po CET.Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano ACK, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — decyzja ręczna Dyspozytora.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 2-5 minOK → ustaw 'R'CCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — upłynęło więcej niż 2 minuty.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET, a otrzymane ACK: (1) komunikat błędu; (2) proces zakończył się błędem. Typowo kod 20 gateClosed.Postępowanie:Najedź kursorem na status i odczytaj kod ACK (typowo kod 20)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka jest zamknięta → zgłośinny kod → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Otrzymano potwierdzenie ACK z pozytywnym komunikatem (po CET).Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool. Trwa oczekiwanie na ACK — około 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Trwa oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → utrzymaj 'R'brak / awaria → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie otrzymano, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — Dyspozytor zatwierdził zawartość.CCtool wysł.CCtool zwalid.Dokument jeszcze nie został wysłany do CCTool, ACK nie napłynął. Plik nie wymagany (>30 min do TET).Brak działań — czekaj do TET.CCtool wysł.CCtool zwalid.Zbliża się CET — plik niedostarczony lub błąd wysyłki. Stan alarmowy.Postępowanie (alarm):Core CC Tool → sprawdź czy plik dotarł do Core CC ToolJeżeli:plik jest, brak ACK → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak pliku (awaria Connector 2.0) → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykbrak pliku w źródle → Brak pliku lub wersji w aplikacji źródłowej. Otwórz KreatorIDCF_CGMES i wygeneruj plik ponownie (kolejna wersja); jeśli aplikacja nie działa — zgłoś. pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. Oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → sprawdź rozmiar; pobierz z MinIO i rozpakujJeżeli:zawartość OK mimo rozmiaru → oznacz 'R' (→ powiązany stan)zawartość niepoprawna → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru, a ACK ma status czerwony — typowo kod 30.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → potwierdź rozmiarWygeneruj poprawny plik w KreatorIDCF_CGMES (kolejna wersja) i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)Nadal za mały → zgłoś szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK napłynął po CET z pozytywnym komunikatem. Sprzeczność.Postępowanie:Pobierz z MinIO → rozpakuj → sprawdź zawartośćJeżeli:zawartość OK → oznacz 'R' (→ powiązany stan); zgłośniepoprawna → zgłośCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, ale ACK negatywny (Rejected). Kody: 20/21/30.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś (administrator Core CC Tool otwiera bramkę); sprawdź proces IDx-AC-FORWARDINGkod 21 (wersja nie jest wyższa niż zapisana) → wygeneruj kolejną wersję w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)kod 30 (rozmiar pliku niezgodny) → wygeneruj ponownie w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, trwa oczekiwanie na ACK, który nie napłynął w zadanym czasie (>2-3 min).Postępowanie:Czekaj 5 min → Core CC Tool (⚠ nie wysyłaj ponownie!)Jeżeli:Processed → oznacz 'R' + zgłośRejected → patrz stan kod ACKbrak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, ACK nie napłynął do CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:Processed → oznacz 'R' + zgłoś (→ powiązany stan)Rejected → wyślij ponownie przez Core CC Tool (Manual Upload) "po CET"brak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie napłynął do CET. Krytyczne.Postępowanie (KRYTYCZNE w C):Wygeneruj poprawny plik w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami) "po CET" (jeśli bramka otwarta)Natychmiast: zgłoś + powiadom RCC szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale walidacja zakończona negatywnie — ACK Rejected po CET.Postępowanie (po CET):Najedź kursorem na status i odczytaj kod ACK (kontekst: rejestracja po CET)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka zamknięta → zgłoś + powiadom RCCkod 21 (wersja nie jest wyższa niż zapisana) → wygeneruj kolejną wersję w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami) (jeśli bramka otwarta)kod 30 (rozmiar pliku niezgodny) → wygeneruj ponownie w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami) (jeśli bramka otwarta)CCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale ACK walidacji nie napłynął — plik dostarczony, lecz niezwalidowany.Postępowanie (po CET):Core CC Tool → sprawdź status walidacji (plik dostarczony po CET)Jeżeli:Processed → oznacz 'R' w CCM + zgłośRejected → postępuj jak w Stanie 30 (odczytaj kod ACK)brak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Dokument nie został dostarczony do CCTool, ACK nie napłynął. Minął czas CET. KRYTYCZNE — po CET dograć nie można.Postępowanie (KRYTYCZNE — brak naprawy):Telefon do RCC + zgłoś (priorytet P1)Po CET — brak naprawy. Diagnoza przyczyn: Kreator · Connector 2.0 · Core CC Tool szczegóły w bazie ryzyk



##### Merged Generation and Load Shift Keys (GLSK) FID3C-610

Kod: FID3C-610

Profil: MIN

TET: 02:40

CET: 03:30

Źródło: proces Core

Wersja: 1

Merged GLSK (FID3C-610) — scalone GLSK wszystkich TSO regionu Core. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Merged Generation and Load Shift Keys (GLSK) FID3C-610

Kod: FID3C-610

Profil: MIN

TET: 02:40

CET: 03:30

Źródło: proces Core

Wersja: 1

Merged GLSK (FID3C-610) — scalone GLSK wszystkich TSO regionu Core. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### CBCORA FID3C-617

Kod: FID3C-617

Profil: 2CCT

TET: 00:00

CET: 00:56

Źródło: KreatorDACF&2DAF_CGMES

Wersja: 3

CBCORA (Critical Branches & Critical Outages with Remedial Actions, FID3C-617) — lista krytycznych elementów sieci (CNEC) PSE wraz z wyłączeniami; dane wejściowe TSO.

**Ścieżka:**

KreatorDACF&2DAF_CGMES

→

Connector 2.0

→

Core CC Tool

→

MinIO

Warianty stanów (32)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool. Dyspozytor ustawił status ręcznie 'R' po weryfikacji w CCTool.Brak działań.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool po CET, ACK napłynął po CET z pozytywnym komunikatem.Brak działań — dostarczone po CET, OK.CCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool oraz otrzymanie potwierdzenia ACK.Brak działań.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — wysyłka ręczna wykonana.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 5 minOK → ustaw 'R' w CCMCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, ale ACK nie napłynął w żądanym czasie i zbliża się CET.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, a otrzymane ACK: (1) zawiera komunikat błędu (najedź kursorem); (2) proces zakończył się błędem — 'Błąd procesu'.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż zapisana) → wygeneruj kolejną wersję w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)kod 30 (rozmiar pliku niezgodny) → wygeneruj ponownie w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem po CET.Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano ACK, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — decyzja ręczna Dyspozytora.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 2-5 minOK → ustaw 'R'CCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — upłynęło więcej niż 2 minuty.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET, a otrzymane ACK: (1) komunikat błędu; (2) proces zakończył się błędem. Typowo kod 20 gateClosed.Postępowanie:Najedź kursorem na status i odczytaj kod ACK (typowo kod 20)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka jest zamknięta → zgłośinny kod → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Otrzymano potwierdzenie ACK z pozytywnym komunikatem (po CET).Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool. Trwa oczekiwanie na ACK — około 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Trwa oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → utrzymaj 'R'brak / awaria → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie otrzymano, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — Dyspozytor zatwierdził zawartość.CCtool wysł.CCtool zwalid.Dokument jeszcze nie został wysłany do CCTool, ACK nie napłynął. Plik nie wymagany (>30 min do TET).Brak działań — czekaj do TET.CCtool wysł.CCtool zwalid.Zbliża się CET — plik niedostarczony lub błąd wysyłki. Stan alarmowy.Postępowanie (alarm):Core CC Tool → sprawdź czy plik dotarł do Core CC ToolJeżeli:plik jest, brak ACK → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak pliku (awaria Connector 2.0) → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykbrak pliku w źródle → Brak pliku lub wersji w aplikacji źródłowej. Otwórz KreatorIDCF_CGMES i wygeneruj plik ponownie (kolejna wersja); jeśli aplikacja nie działa — zgłoś. pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. Oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → sprawdź rozmiar; pobierz z MinIO i rozpakujJeżeli:zawartość OK mimo rozmiaru → oznacz 'R' (→ powiązany stan)zawartość niepoprawna → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru, a ACK ma status czerwony — typowo kod 30.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → potwierdź rozmiarWygeneruj poprawny plik w KreatorIDCF_CGMES (kolejna wersja) i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)Nadal za mały → zgłoś szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK napłynął po CET z pozytywnym komunikatem. Sprzeczność.Postępowanie:Pobierz z MinIO → rozpakuj → sprawdź zawartośćJeżeli:zawartość OK → oznacz 'R' (→ powiązany stan); zgłośniepoprawna → zgłośCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, ale ACK negatywny (Rejected). Kody: 20/21/30.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś (administrator Core CC Tool otwiera bramkę); sprawdź proces IDx-AC-FORWARDINGkod 21 (wersja nie jest wyższa niż zapisana) → wygeneruj kolejną wersję w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)kod 30 (rozmiar pliku niezgodny) → wygeneruj ponownie w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, trwa oczekiwanie na ACK, który nie napłynął w zadanym czasie (>2-3 min).Postępowanie:Czekaj 5 min → Core CC Tool (⚠ nie wysyłaj ponownie!)Jeżeli:Processed → oznacz 'R' + zgłośRejected → patrz stan kod ACKbrak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, ACK nie napłynął do CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:Processed → oznacz 'R' + zgłoś (→ powiązany stan)Rejected → wyślij ponownie przez Core CC Tool (Manual Upload) "po CET"brak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie napłynął do CET. Krytyczne.Postępowanie (KRYTYCZNE w C):Wygeneruj poprawny plik w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami) "po CET" (jeśli bramka otwarta)Natychmiast: zgłoś + powiadom RCC szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale walidacja zakończona negatywnie — ACK Rejected po CET.Postępowanie (po CET):Najedź kursorem na status i odczytaj kod ACK (kontekst: rejestracja po CET)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka zamknięta → zgłoś + powiadom RCCkod 21 (wersja nie jest wyższa niż zapisana) → wygeneruj kolejną wersję w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami) (jeśli bramka otwarta)kod 30 (rozmiar pliku niezgodny) → wygeneruj ponownie w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami) (jeśli bramka otwarta)CCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale ACK walidacji nie napłynął — plik dostarczony, lecz niezwalidowany.Postępowanie (po CET):Core CC Tool → sprawdź status walidacji (plik dostarczony po CET)Jeżeli:Processed → oznacz 'R' w CCM + zgłośRejected → postępuj jak w Stanie 30 (odczytaj kod ACK)brak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Dokument nie został dostarczony do CCTool, ACK nie napłynął. Minął czas CET. KRYTYCZNE — po CET dograć nie można.Postępowanie (KRYTYCZNE — brak naprawy):Telefon do RCC + zgłoś (priorytet P1)Po CET — brak naprawy. Diagnoza przyczyn: Kreator · Connector 2.0 · Core CC Tool szczegóły w bazie ryzyk



##### Merged DACF/IDCF Common Grid Model (CGM) FID3C-620

Kod: FID3C-620

Profil: MIN

TET: 02:40

CET: 03:30

Źródło: proces Core / Kreator

Wersja: 4

Merged DACF/IDCF Common Grid Model (CGM, FID3C-620) — scalony wspólny model sieci zbudowany z modeli indywidualnych (IGM) TSO. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Merged DACF/IDCF Common Grid Model (CGM) FID3C-620

Kod: FID3C-620

Profil: MIN

TET: 02:40

CET: 03:30

Źródło: proces Core / Kreator

Wersja: 4

Merged DACF/IDCF Common Grid Model (CGM, FID3C-620) — scalony wspólny model sieci zbudowany z modeli indywidualnych (IGM) TSO. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Reference Program (RefProg) FID3C-632

Kod: FID3C-632

Profil: MIN

TET: 02:40

CET: 03:30

Źródło: proces Core

Wersja: 3

Reference Program (RefProg, FID3C-632) — program referencyjny: planowane salda wymiany międzyobszarowej. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Reference Program (RefProg) FID3C-632

Kod: FID3C-632

Profil: MIN

TET: 02:40

CET: 03:30

Źródło: proces Core

Wersja: 3

Reference Program (RefProg, FID3C-632) — program referencyjny: planowane salda wymiany międzyobszarowej. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Reference Program (RefProg) FID3C-632

Kod: FID3C-632

Profil: MIN

TET: 02:40

CET: 03:30

Źródło: proces Core

Wersja: 3

Reference Program (RefProg, FID3C-632) — program referencyjny: planowane salda wymiany międzyobszarowej. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Reference Program (RefProg) FID3C-632

Kod: FID3C-632

Profil: MIN

TET: 02:40

CET: 03:30

Źródło: proces Core

Wersja: 3

Reference Program (RefProg, FID3C-632) — program referencyjny: planowane salda wymiany międzyobszarowej. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial FB Domain (Virgin RefProg Bal) FID3C-645

Kod: FID3C-645

Profil: MIN

TET: 03:00

CET: 03:30

Źródło: Perun4V / proces Core

Wersja: 1

Initial FB Domain (Virgin / RefProg Bal, FID3C-645) — początkowa domena Flow-Based. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial FB Domain (Virgin RefProg Bal) FID3C-645

Kod: FID3C-645

Profil: MIN

TET: 03:00

CET: 03:30

Źródło: Perun4V / proces Core

Wersja: 1

Initial FB Domain (Virgin / RefProg Bal, FID3C-645) — początkowa domena Flow-Based. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial FB Domain (RefProg Bal) FID3C-645

Kod: FID3C-645

Profil: MIN

TET: 03:00

CET: 03:30

Źródło: Perun4V / proces Core

Wersja: 1

Initial FB Domain (Virgin / RefProg Bal, FID3C-645) — początkowa domena Flow-Based. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial FB Domain (Virgin RefProg Bal) FID3C-645

Kod: FID3C-645

Profil: MIN

TET: 03:00

CET: 03:30

Źródło: Perun4V / proces Core

Wersja: 1

Initial FB Domain (Virgin / RefProg Bal, FID3C-645) — początkowa domena Flow-Based. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial FB Domain (Virgin RefProg Bal) FID3C-645

Kod: FID3C-645

Profil: MIN

TET: 03:00

CET: 03:30

Źródło: Perun4V / proces Core

Wersja: 1

Initial FB Domain (Virgin / RefProg Bal, FID3C-645) — początkowa domena Flow-Based. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Real Generation and Load Shift Keys (GLSK) FID3C-657

Kod: FID3C-657

Profil: MIN

TET: 03:00

CET: 03:30

Źródło: Kreator

Wersja: 1

Real GLSK (FID3C-657) — rzeczywiste klucze GLSK (po dostosowaniu do bieżącego stanu). Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Real Generation and Load Shift Keys (GLSK) FID3C-657

Kod: FID3C-657

Profil: MIN

TET: 03:00

CET: 03:30

Źródło: Kreator

Wersja: 1

Real GLSK (FID3C-657) — rzeczywiste klucze GLSK (po dostosowaniu do bieżącego stanu). Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### CGM Data Quality Check FID3C-659

Kod: FID3C-659

Profil: MIN

TET: 03:00

CET: 03:30

Źródło: proces Core

Wersja: 1

CGM Data Quality Check (FID3C-659) — raport kontroli jakości danych scalonego modelu CGM. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### CGM Data Quality Check FID3C-659

Kod: FID3C-659

Profil: MIN

TET: 03:00

CET: 03:30

Źródło: proces Core

Wersja: 1

CGM Data Quality Check (FID3C-659) — raport kontroli jakości danych scalonego modelu CGM. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Individual Filtered Critical Branches (CB) FID3C-665

Kod: FID3C-665

Profil: MIN

TET: 03:00

CET: 03:30

Źródło: Kreator

Wersja: 1

Individual Filtered Critical Branches (CB, FID3C-665) — indywidualne, przefiltrowane gałęzie krytyczne PSE. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Individual Filtered Critical Branches (CB) FID3C-665

Kod: FID3C-665

Profil: MIN

TET: 03:00

CET: 03:30

Źródło: Kreator

Wersja: 1

Individual Filtered Critical Branches (CB, FID3C-665) — indywidualne, przefiltrowane gałęzie krytyczne PSE. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Vertices of Initial FB Domain FID3C-701

Kod: FID3C-701

Profil: MIN

TET: 03:00

CET: 03:30

Źródło: Perun4V

Wersja: 1

Vertices of Initial FB Domain (FID3C-701) — wierzchołki początkowej domeny Flow-Based. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Vertices of Initial FB Domain/CB Validation file ATC FID3C-701_ATC

Kod: FID3C-701_ATC

Profil: MIN

TET: 03:00

CET: 03:30

Źródło: Perun4V

Wersja: 1

Vertices / CB Validation file ATC (FID3C-701_ATC) — wierzchołki domeny / plik walidacji CB dla ścieżki ATC. Składowa paczki ATC.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Vertices of Initial FB Domain/CB Validation file ATC FID3C-701_ATC

Kod: FID3C-701_ATC

Profil: MIN

TET: 03:00

CET: 03:30

Źródło: Perun4V

Wersja: 1

Vertices / CB Validation file ATC (FID3C-701_ATC) — wierzchołki domeny / plik walidacji CB dla ścieżki ATC. Składowa paczki ATC.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### IVA FID3C-710

Kod: FID3C-710

Profil: 3COL

TET: 04:00

CET: 04:36

Źródło: Perun4V

Wersja: 1

IVA — Individual Validation Adjustment (FID3C-710) — wynik indywidualnej walidacji domeny Flow-Based (z Perun4V); korekta domeny po walidacji TSO.

**Ścieżka:**

Perun4V

→

MinIO

Connector 2.0

→

CCM

Warianty stanów (46)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.MinIODokument został wysłany prawidłowo do CCTool i na MINIO, otrzymano potwierdzenie ACK z pozytywnym komunikatem (komunikat statusu powinien się pojawić po najechaniu kursorem na status).Brak — proces przebiegł poprawnie.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, Dokument ACK (CCTool zwalid.) napłynął po CET z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, nie otrzymano potwierdzenia ACK, natomiast Dyspozytor ustawił status ręcznie 'R' po weryfikacji po stronie CCTool, iż proces został zrealizowany poprawnie.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO po CET, Dokument ACK (CCTool zwalid.) napłynął po CET z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO oraz otrzymanie potwierdzenia ACK.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu aplikacji CCM w jednym miejscu (np. z menu bocznego „CCTool wysł." bądź „MINIO" korzystając z opcji „Wyślij"). Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Po 5 min jeśli proces przebiegł poprawnie → ustaw 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM, ale nie napłynął ACK w żądanym czasie i zbliża się Critical End Time dla obsługi tego dokumentu.Monitoring CCCt MV; jeśli proces OK → status 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM, a otrzymane potwierdzenie ACK (CCTool zwalid.): (1) zawiera komunikat błędu (najedź kursorem na status); (2) proces zakończył się błędem — „Błąd procesu".Weryfikacja sytuacji w CCTool. Decyzja Dyspozytora o ewentualnej kolejnej iteracji.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem po CET.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Weryfikacja w CCCt MV; jeśli Processed → status 'R' ręcznie. Diagnostyka CN2 zwrotny → zgłoś.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano ACK, natomiast Dyspozytor ustawił status ręcznie 'R' po weryfikacji po stronie CCTool, iż proces został zrealizowany poprawnie.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM po CET (opcja „Wyślij po CET"). Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — upłynęło więcej niż 2 minuty (czas oczekiwania można sprawdzić najeżdżając kursorem na status).Weryfikacja sytuacji w CCTool; jeśli proces przebiegł poprawnie → ustaw status 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM po CET, a otrzymane potwierdzenie ACK (CCTool zwalid.): (1) zawiera komunikat błędu; (2) proces zakończył się błędem — „Błąd procesu".Weryfikacja sytuacji w CCTool. Zgłoś.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM po CET. Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM po CET. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Diagnostyka CN2 zwrotny → zgłoś.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Weryfikacja w CCTool; po 5 min jeśli proces przebiegł poprawnie → ustaw 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — upłynęło więcej niż 2 minuty.Weryfikacja w CCTool; jeśli proces przebiegł poprawnie → ustaw 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Diagnostyka CN2 zwrotny → zgłoś.CCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru (w informacjach o wielkości rozmiaru dostępna z poziomu menu bocznego na statusie). Nie otrzymano potwierdzenie ACK, natomiast Dyspozytor ustawił status ręcznie 'R' po weryfikacji po stronie CCTool, iż proces został zrealizowany poprawnie.Zgłoś informacyjnie (ew. zmiana konfiguracji rozmiaru).CCtool wysł.CCtool zwalid.MinIODokument jeszcze nie został wysłany ani do CCTool ani na MINIO, w związku z tym potwierdzenie ACK nie napłynęło.Brak — monitoring. Plik nie wymagany (>30 min do TET).CCtool wysł.CCtool zwalid.MinIOZbliża się TET (21:30), a dokument nie został jeszcze obsłużony.Brak. Czujność i przygotowanie. Sprawdź Perun4V (status obliczeń); sprawdź CN2; przygotuj się na ewentualne IVA BACKUP od CCA. Jeśli sytuacja się utrzyma → Kategoria C (powiązany stan).CCtool wysł.CCtool zwalid.MinIOWysyłka do CCTool trwa i oczekiwany jest ACK, dokument dostarczony na MINIO.Jeśli taki status „CCTool wysł." trwa dłużej niż 5 minut należy zweryfikować stan w CCTool, ewentualnie zgłosić problem.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, trwa oczekiwanie na potwierdzenie ACK (status powinien się utrzymać krócej niż 3 minuty).Brak. Czekaj do 3-5 min na ACK; po tym czasie → stan timeout.CCtool wysł.CCtool zwalid.MinIOWysyłka do CCTool trwa i oczekiwany jest ACK. Dokument dostarczony na MINIO nie spełnia kryterium rozmiaru (w informacjach o wielkości rozmiaru dostępna z poziomu menu bocznego na statusie).Jeśli taki status „CCTool wysł." trwa dłużej niż 5 minut → zweryfikować stan w CCTool, ew. zgłosić problem Zweryfikować dokument IVA czy jest poprawny (pobierając go z CCM i rozpakowując) — pomimo zbyt małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOZbliża się CET (22:06), a dokument nie został jeszcze obsłużony.Procedura (wg Confluence): Jeśli zbliża się CET (poniżej 3 minut) możliwa jest ręczna wysyłka IVA Backup z menu bocznego na poniższej pozycji pulpitu. Alternatywnie: R08 (Perun4V awaria), R09 (ERR-I), R10 (Process failed).CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, potwierdzenie ACK ma status czerwony co może oznaczać: (1) zawiera komunikat błędu (najedź kursorem na status); (2) proces zakończył się błędem — „Błąd procesu".Procedura: R05 — reakcja per kod ACK (20 gateClosed / 21 duplicatedVersion / 30 file size). Należy zweryfikować sytuację w CCTool.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, trwa oczekiwanie na potwierdzenie ACK, które nie napłynęło w zadanym czasie (po najechaniu na znak zapytania można sprawdzić ile upłynęło czasu).Procedura: R06. Jeśli po około 3 minutach nie pojawi się status ACK wraz z informacją dostępną po najechaniu na status → należy zweryfikować sytuację w CCTool.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO. Dokument ACK (CCTool zwalid.) nie napłynął do CET.Procedury: R06, R18. Należy zweryfikować sytuację w CCTool. W przypadku wygenerowania ACK po stronie CCTool — sytuację zgłosić.CCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru (w informacjach o wielkości rozmiaru dostępna z poziomu menu bocznego na statusie). Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Procedura: R05. Zweryfikować dokument IVA czy jest poprawny (pobierając go z CCM i rozpakowując) — pomimo zbyt małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 1 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.), które nie napłynęło w zadanym czasie (po najechaniu na znak zapytania można sprawdzić ile upłynęło czasu).Procedura: R05, R06. Jeśli po około 3 minutach nie pojawi się status ACK wraz z informacją po najechaniu na status → zweryfikować sytuację w CCTool Zweryfikować dokument IVA (pobranie z CCM i rozpakowanie) — pomimo małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru, a otrzymane potwierdzenie ACK (CCTool zwalid.): (1) zawiera komunikat błędu; (2) proces zakończył się błędem — „Błąd procesu".Procedura: R05. Należy zweryfikować sytuację w CCTool Zweryfikować dokument IVA czy jest poprawny (pobranie z CCM i rozpakowanie) — pomimo małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru. Dokument ACK (CCTool zwalid.) napłynął po CET z pozytywnym komunikatem.Należy zweryfikować dokument IVA czy jest poprawny i czy został przyjęty w CCTool Jeśli plik z pkt. 1 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCTool Po weryfikacji można nadać 'R' → Stan #21 (Kategoria A).CCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru. Dokument ACK (CCTool zwalid.) nie napłynął do CET.Zweryfikować sytuację w CCTool — w przypadku wygenerowania ACK po stronie CCTool sytuację zgłosić Zweryfikować dokument IVA (pobranie z CCM i rozpakowanie) — pomimo małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO po CET, potwierdzenie ACK ma status czerwony co może oznaczać: (1) zawiera komunikat błędu; (2) proces zakończył się błędem — „Błąd procesu".Procedura: R05. Należy zweryfikować sytuację w CCTool.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO po CET. Dokument ACK (CCTool zwalid.) nie napłynął do CET.Procedury: R06, R18. Należy zweryfikować sytuację w CCTool, w przypadku wygenerowania ACK po stronie CCTool sytuację zgłosić.CCtool wysł.CCtool zwalid.MinIODokument nie został dostarczony ani do CCTool ani na MINIO, w związku z tym potwierdzenie ACK nie napłynęło. Minął czas CET.Procedura (wg Confluence): Należy zweryfikować czy dokument IVA jest w PERUN. Jeśli TAK to należy go niezwłocznie pozyskać ręcznie i wysłać ją bezpośrednio z CCM bądź z GUI CCTool Procedury IDCC: R10 (Process failed) — oczekuj IVA BACKUP v1 od CCA; brak → R19 (CN2 nie kopiuje do CCA), R23 (brak raportu CCA). Zgłoś (CIZ, WPO, PSE-I) + telefon CCC. ❌ Zakaz fallbacku 20% Fmax z DA.MinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### IVA Backup FID3C-710

Kod: FID3C-710

Profil: MIN

TET: 04:00

CET: 04:36

Źródło: CCA

Wersja: 1

IVA Backup (FID3C-710) — backupowa wersja IVA generowana przez CCA (publikowana do cca/…/out/), na wypadek braku/niezgodności IVA podstawowego.

**Ścieżka:**

CCA

→

MinIO

→

CCM

Warianty stanów (46)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.MinIODokument został wysłany prawidłowo do CCTool i na MINIO, otrzymano potwierdzenie ACK z pozytywnym komunikatem (komunikat statusu powinien się pojawić po najechaniu kursorem na status).Brak — proces przebiegł poprawnie.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, Dokument ACK (CCTool zwalid.) napłynął po CET z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, nie otrzymano potwierdzenia ACK, natomiast Dyspozytor ustawił status ręcznie 'R' po weryfikacji po stronie CCTool, iż proces został zrealizowany poprawnie.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO po CET, Dokument ACK (CCTool zwalid.) napłynął po CET z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO oraz otrzymanie potwierdzenia ACK.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu aplikacji CCM w jednym miejscu (np. z menu bocznego „CCTool wysł." bądź „MINIO" korzystając z opcji „Wyślij"). Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Po 5 min jeśli proces przebiegł poprawnie → ustaw 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM, ale nie napłynął ACK w żądanym czasie i zbliża się Critical End Time dla obsługi tego dokumentu.Monitoring CCCt MV; jeśli proces OK → status 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM, a otrzymane potwierdzenie ACK (CCTool zwalid.): (1) zawiera komunikat błędu (najedź kursorem na status); (2) proces zakończył się błędem — „Błąd procesu".Weryfikacja sytuacji w CCTool. Decyzja Dyspozytora o ewentualnej kolejnej iteracji.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem po CET.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Weryfikacja w CCCt MV; jeśli Processed → status 'R' ręcznie. Diagnostyka CN2 zwrotny → zgłoś.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano ACK, natomiast Dyspozytor ustawił status ręcznie 'R' po weryfikacji po stronie CCTool, iż proces został zrealizowany poprawnie.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM po CET (opcja „Wyślij po CET"). Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — upłynęło więcej niż 2 minuty (czas oczekiwania można sprawdzić najeżdżając kursorem na status).Weryfikacja sytuacji w CCTool; jeśli proces przebiegł poprawnie → ustaw status 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM po CET, a otrzymane potwierdzenie ACK (CCTool zwalid.): (1) zawiera komunikat błędu; (2) proces zakończył się błędem — „Błąd procesu".Weryfikacja sytuacji w CCTool. Zgłoś.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM po CET. Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM po CET. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Diagnostyka CN2 zwrotny → zgłoś.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Weryfikacja w CCTool; po 5 min jeśli proces przebiegł poprawnie → ustaw 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — upłynęło więcej niż 2 minuty.Weryfikacja w CCTool; jeśli proces przebiegł poprawnie → ustaw 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Diagnostyka CN2 zwrotny → zgłoś.CCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru (w informacjach o wielkości rozmiaru dostępna z poziomu menu bocznego na statusie). Nie otrzymano potwierdzenie ACK, natomiast Dyspozytor ustawił status ręcznie 'R' po weryfikacji po stronie CCTool, iż proces został zrealizowany poprawnie.Zgłoś informacyjnie (ew. zmiana konfiguracji rozmiaru).CCtool wysł.CCtool zwalid.MinIODokument jeszcze nie został wysłany ani do CCTool ani na MINIO, w związku z tym potwierdzenie ACK nie napłynęło.Brak — monitoring. Plik nie wymagany (>30 min do TET).CCtool wysł.CCtool zwalid.MinIOZbliża się TET (21:30), a dokument nie został jeszcze obsłużony.Brak. Czujność i przygotowanie. Sprawdź Perun4V (status obliczeń); sprawdź CN2; przygotuj się na ewentualne IVA BACKUP od CCA. Jeśli sytuacja się utrzyma → Kategoria C (powiązany stan).CCtool wysł.CCtool zwalid.MinIOWysyłka do CCTool trwa i oczekiwany jest ACK, dokument dostarczony na MINIO.Jeśli taki status „CCTool wysł." trwa dłużej niż 5 minut należy zweryfikować stan w CCTool, ewentualnie zgłosić problem.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, trwa oczekiwanie na potwierdzenie ACK (status powinien się utrzymać krócej niż 3 minuty).Brak. Czekaj do 3-5 min na ACK; po tym czasie → stan timeout.CCtool wysł.CCtool zwalid.MinIOWysyłka do CCTool trwa i oczekiwany jest ACK. Dokument dostarczony na MINIO nie spełnia kryterium rozmiaru (w informacjach o wielkości rozmiaru dostępna z poziomu menu bocznego na statusie).Jeśli taki status „CCTool wysł." trwa dłużej niż 5 minut → zweryfikować stan w CCTool, ew. zgłosić problem Zweryfikować dokument IVA czy jest poprawny (pobierając go z CCM i rozpakowując) — pomimo zbyt małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOZbliża się CET (22:06), a dokument nie został jeszcze obsłużony.Procedura (wg Confluence): Jeśli zbliża się CET (poniżej 3 minut) możliwa jest ręczna wysyłka IVA Backup z menu bocznego na poniższej pozycji pulpitu. Alternatywnie: R08 (Perun4V awaria), R09 (ERR-I), R10 (Process failed).CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, potwierdzenie ACK ma status czerwony co może oznaczać: (1) zawiera komunikat błędu (najedź kursorem na status); (2) proces zakończył się błędem — „Błąd procesu".Procedura: R05 — reakcja per kod ACK (20 gateClosed / 21 duplicatedVersion / 30 file size). Należy zweryfikować sytuację w CCTool.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, trwa oczekiwanie na potwierdzenie ACK, które nie napłynęło w zadanym czasie (po najechaniu na znak zapytania można sprawdzić ile upłynęło czasu).Procedura: R06. Jeśli po około 3 minutach nie pojawi się status ACK wraz z informacją dostępną po najechaniu na status → należy zweryfikować sytuację w CCTool.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO. Dokument ACK (CCTool zwalid.) nie napłynął do CET.Procedury: R06, R18. Należy zweryfikować sytuację w CCTool. W przypadku wygenerowania ACK po stronie CCTool — sytuację zgłosić.CCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru (w informacjach o wielkości rozmiaru dostępna z poziomu menu bocznego na statusie). Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Procedura: R05. Zweryfikować dokument IVA czy jest poprawny (pobierając go z CCM i rozpakowując) — pomimo zbyt małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 1 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.), które nie napłynęło w zadanym czasie (po najechaniu na znak zapytania można sprawdzić ile upłynęło czasu).Procedura: R05, R06. Jeśli po około 3 minutach nie pojawi się status ACK wraz z informacją po najechaniu na status → zweryfikować sytuację w CCTool Zweryfikować dokument IVA (pobranie z CCM i rozpakowanie) — pomimo małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru, a otrzymane potwierdzenie ACK (CCTool zwalid.): (1) zawiera komunikat błędu; (2) proces zakończył się błędem — „Błąd procesu".Procedura: R05. Należy zweryfikować sytuację w CCTool Zweryfikować dokument IVA czy jest poprawny (pobranie z CCM i rozpakowanie) — pomimo małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru. Dokument ACK (CCTool zwalid.) napłynął po CET z pozytywnym komunikatem.Należy zweryfikować dokument IVA czy jest poprawny i czy został przyjęty w CCTool Jeśli plik z pkt. 1 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCTool Po weryfikacji można nadać 'R' → Stan #21 (Kategoria A).CCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru. Dokument ACK (CCTool zwalid.) nie napłynął do CET.Zweryfikować sytuację w CCTool — w przypadku wygenerowania ACK po stronie CCTool sytuację zgłosić Zweryfikować dokument IVA (pobranie z CCM i rozpakowanie) — pomimo małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO po CET, potwierdzenie ACK ma status czerwony co może oznaczać: (1) zawiera komunikat błędu; (2) proces zakończył się błędem — „Błąd procesu".Procedura: R05. Należy zweryfikować sytuację w CCTool.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO po CET. Dokument ACK (CCTool zwalid.) nie napłynął do CET.Procedury: R06, R18. Należy zweryfikować sytuację w CCTool, w przypadku wygenerowania ACK po stronie CCTool sytuację zgłosić.CCtool wysł.CCtool zwalid.MinIODokument nie został dostarczony ani do CCTool ani na MINIO, w związku z tym potwierdzenie ACK nie napłynęło. Minął czas CET.Procedura (wg Confluence): Należy zweryfikować czy dokument IVA jest w PERUN. Jeśli TAK to należy go niezwłocznie pozyskać ręcznie i wysłać ją bezpośrednio z CCM bądź z GUI CCTool Procedury IDCC: R10 (Process failed) — oczekuj IVA BACKUP v1 od CCA; brak → R19 (CN2 nie kopiuje do CCA), R23 (brak raportu CCA). Zgłoś (CIZ, WPO, PSE-I) + telefon CCC. ❌ Zakaz fallbacku 20% Fmax z DA.MinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### IVA_ATC FID3C-710_ATC

Kod: FID3C-710_ATC

Profil: MIN

TET: 03:10

CET: 03:50

Źródło: Perun4V

Wersja: 1

IVA_ATC (FID3C-710_ATC) — IVA dla odrębnej ścieżki walidacji domeny ATC.

**Ścieżka:**

Perun4V

→

MinIO

Connector 2.0

→

CCM

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### IVA_ATC FID3C-710_ATC

Kod: FID3C-710_ATC

Profil: MIN

TET: 03:10

CET: 03:50

Źródło: Perun4V

Wersja: 1

IVA_ATC (FID3C-710_ATC) — IVA dla odrębnej ścieżki walidacji domeny ATC.

**Ścieżka:**

Perun4V

→

MinIO

Connector 2.0

→

CCM

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### AC FID3C-831

Kod: FID3C-831

Profil: 2CCT

TET: 04:15

CET: 04:25

Źródło: ZP

Wersja: 3

AC (Allocation Constraints, FID3C-831) — plik z wartościami ograniczeń alokacyjnych wyznaczonych przez PSE, publikowany do PuTo i do procesu Core. Format XML, MTU 15 min.

**Ścieżka:**

ZP

→

Connector 2.0

→

Core CC Tool

→

PuTo

+

MinIO

Warianty stanów (32)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool. Dyspozytor ustawił status ręcznie 'R' po weryfikacji w CCTool.Brak działań.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool po CET, ACK napłynął po CET z pozytywnym komunikatem.Brak działań — dostarczone po CET, OK.CCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool oraz otrzymanie potwierdzenia ACK.Brak działań.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — wysyłka ręczna wykonana.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 5 minOK → ustaw 'R' w CCMCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, ale ACK nie napłynął w żądanym czasie i zbliża się CET.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, a otrzymane ACK: (1) zawiera komunikat błędu (najedź kursorem); (2) proces zakończył się błędem — 'Błąd procesu'.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż zapisana) → podnieś numer wersji w aplikacji ZP i wyślij plik ponownie przez Core CC Tool (Manual Upload)kod 30 (rozmiar pliku niezgodny) → pobierz poprawny plik z MinIO lub aplikacji ZP i wyślij ponownieCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem po CET.Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano ACK, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — decyzja ręczna Dyspozytora.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 2-5 minOK → ustaw 'R'CCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — upłynęło więcej niż 2 minuty.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET, a otrzymane ACK: (1) komunikat błędu; (2) proces zakończył się błędem. Typowo kod 20 gateClosed.Postępowanie:Najedź kursorem na status i odczytaj kod ACK (typowo kod 20)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka jest zamknięta → zgłośinny kod → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Otrzymano potwierdzenie ACK z pozytywnym komunikatem (po CET).Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool. Trwa oczekiwanie na ACK — około 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Trwa oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → utrzymaj 'R'brak / awaria → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie otrzymano, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — Dyspozytor zatwierdził zawartość.CCtool wysł.CCtool zwalid.Dokument jeszcze nie został wysłany do CCTool, ACK nie napłynął. Plik nie wymagany (>30 min do TET).Brak działań — czekaj do TET.CCtool wysł.CCtool zwalid.Zbliża się CET — plik niedostarczony lub błąd wysyłki. Stan alarmowy.Postępowanie (alarm):Core CC Tool → sprawdź czy plik dotarł do Core CC ToolJeżeli:plik jest, brak ACK → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak pliku (awaria Connector 2.0) → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykbrak pliku w źródle → Brak pliku lub wersji w aplikacji źródłowej. Otwórz aplikacji ZP, przejdź do bilansu i sprawdź wersję pliku: jeśli wersja jest dostępna — pobierz ją (Pobierz XML); jeśli brakuje — wygeneruj nową wersję; jeśli aplikacja nie działa — zgłoś. pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. Oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → sprawdź rozmiar; pobierz z MinIO i rozpakujJeżeli:zawartość OK mimo rozmiaru → oznacz 'R' (→ powiązany stan)zawartość niepoprawna → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru, a ACK ma status czerwony — typowo kod 30.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → potwierdź rozmiarPobierz poprawny plik z aplikacji ZP (Pobierz XML) i wyślij przez Core CC Tool (Manual Upload) z kolejnym numerem wersjiNadal za mały → zgłoś szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK napłynął po CET z pozytywnym komunikatem. Sprzeczność.Postępowanie:Pobierz z MinIO → rozpakuj → sprawdź zawartośćJeżeli:zawartość OK → oznacz 'R' (→ powiązany stan); zgłośniepoprawna → zgłośCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, ale ACK negatywny (Rejected). Kody: 20/21/30.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś (administrator Core CC Tool otwiera bramkę); sprawdź proces IDx-AC-FORWARDINGkod 21 (wersja nie jest wyższa niż zapisana) → podnieś numer wersji w aplikacji ZP i wyślij plik ponownie przez Core CC Tool (Manual Upload)kod 30 (rozmiar pliku niezgodny) → pobierz poprawny plik z MinIO lub aplikacji ZP i wyślij ponownieCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, trwa oczekiwanie na ACK, który nie napłynął w zadanym czasie (>2-3 min).Postępowanie:Czekaj 5 min → Core CC Tool (⚠ nie wysyłaj ponownie!)Jeżeli:Processed → oznacz 'R' + zgłośRejected → patrz stan kod ACKbrak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, ACK nie napłynął do CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:Processed → oznacz 'R' + zgłoś (→ powiązany stan)Rejected → wyślij ponownie przez Core CC Tool (Manual Upload) "po CET"brak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie napłynął do CET. Krytyczne.Postępowanie (KRYTYCZNE w C):Pobierz poprawny plik z aplikacji ZP i wyślij przez Core CC Tool (Manual Upload) "po CET" (jeśli bramka otwarta)Natychmiast: zgłoś + powiadom RCC szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale walidacja zakończona negatywnie — ACK Rejected po CET.Postępowanie (po CET):Najedź kursorem na status i odczytaj kod ACK (kontekst: rejestracja po CET)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka zamknięta → zgłoś + powiadom RCCkod 21 (wersja nie jest wyższa niż zapisana) → podnieś numer wersji w aplikacji ZP i wyślij plik ponownie przez Core CC Tool (Manual Upload) (jeśli bramka otwarta)kod 30 (rozmiar pliku niezgodny) → pobierz poprawny plik z MinIO lub aplikacji ZP i wyślij ponownie (jeśli bramka otwarta)CCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale ACK walidacji nie napłynął — plik dostarczony, lecz niezwalidowany.Postępowanie (po CET):Core CC Tool → sprawdź status walidacji (plik dostarczony po CET)Jeżeli:Processed → oznacz 'R' w CCM + zgłośRejected → postępuj jak w Stanie 30 (odczytaj kod ACK)brak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Dokument nie został dostarczony do CCTool, ACK nie napłynął. Minął czas CET. KRYTYCZNE — po CET dograć nie można.Postępowanie (KRYTYCZNE — brak naprawy):Telefon do RCC + zgłoś (priorytet P1)Po CET — brak naprawy. Diagnoza przyczyn: ZP · Connector 2.0 · Core CC Tool szczegóły w bazie ryzyk



##### Initial Intraday ATCs FID3C-882

Kod: FID3C-882

Profil: MIN

TET: 03:00

CET: 03:20

Źródło: proces Core

Wersja: 1

Initial Intraday ATCs (FID3C-882) — początkowe wartości ATC dla intraday; wejście walidacji ATC. Składowa paczki.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial Intraday ATCs FID3C-882

Kod: FID3C-882

Profil: MIN

TET: 03:00

CET: 03:20

Źródło: proces Core

Wersja: 1

Initial Intraday ATCs (FID3C-882) — początkowe wartości ATC dla intraday; wejście walidacji ATC. Składowa paczki.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial Intraday ATCs FID3C-882

Kod: FID3C-882

Profil: MIN

TET: 03:00

CET: 03:20

Źródło: proces Core

Wersja: 1

Initial Intraday ATCs (FID3C-882) — początkowe wartości ATC dla intraday; wejście walidacji ATC. Składowa paczki.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Final Intraday NTCs FID3C-921

Kod: FID3C-921

Profil: SFTP

TET: 04:15

CET: 04:30

Źródło: proces Core

Wersja: 1

Final Intraday NTC (FID3C-921) — finalne wyniki NTC (Net Transfer Capacity) z procesu IDCC; zdolności przesyłowe udostępniane na rynek intraday (XBID).

**Ścieżka:**

proces Core / Kreator →

sFTP@pse.pl

/ ZP

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjnesFTP/ZP wysł.Plik dostarczony prawidłowo na sFTP/ZP — status pozytywny.Brak działań — proces poprawny.sFTP/ZP wysł.Status nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.sFTP/ZP wysł.Plik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.sFTP/ZP wysł.Przedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.sFTP/ZP wysł.Oczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź sFTP/ZP. Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się TET — pliku jeszcze nie ma na sFTP/ZP.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się CET / błąd dostarczenia — brak pliku na sFTP/ZP.Gdy pliku NIE ma na sFTP/ZP → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Minął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### ATC Based Validation FID3C-928

Kod: FID3C-928

Profil: 2CCT

TET: 03:10

CET: 03:50

Źródło: Core CC Tool

Wersja: 1

ATC Based Validation (FID3C-928) — plik ZWROTNY: wynik walidacji ATC prowadzonej centralnie w Core CC Tool (strumień odrębny od FBA). NIE jest wysyłany przez TSO; publikowany CCCt → TSO przez Connector 2.0.

**Ścieżka:**

Paczka ATC (PERUN_IDx_ATC) →

Core CC Tool

(walidacja ATC) →

Connector 2.0

→

CCM

Warianty stanów (18)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.Przedwczesne (>30 min do TET). Walidacja ATC jeszcze nie ukończona.Monitoring — sprawdź w aplikacji CCM postęp walidacji paczki PERUN_IDx_ATC.CCtool wysł.CCtool zwalid.Zbliża się TET, brak FIDx-928. Walidacja paczki ATC w toku.Postępowanie:Rozwiń agregat PERUN_IDx_ATC → zweryfikuj składoweJeżeli:brak składowej → uzupełnij brakującą składową w aplikacji CCM ()składowe OK → monitoruj — czekaj na wynik walidacjiCCtool wysł.CCtool zwalid.Zbliża się CET — brak wyniku walidacji ATC. Stan alarmowy.Postępowanie (zbliża się CET):Ostatnia szansa: dokończ uzupełnienia paczki ATC w CCM; sprawdź Core CC Tool (Message Viewer)Jeżeli:plik dotrze → OK — koniecbłąd → odczytaj kod ACK (patrz powiązany stan)brak → zgłośCCtool wysł.CCtool zwalid.Minął CET, brak FIDx-928. KRYTYCZNE — brak lokalnego fallbacku.Postępowanie (KRYTYCZNE — minął CET):⛔ STOP — żadnych działań ręcznych. Brak lokalnego fallbacku (brak wyniku ATC w czasie → Dyspozytor nie wykonuje dalszych czynności).Zgłoś + telefon do RCC szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Happy Day — walidacja ATC zakończona poprawnie, wynik opublikowany.Brak interwencji — walidacja ATC zakończona poprawnie.CCtool wysł.CCtool zwalid.Wynik dotarł, ale ACK negatywny (Rejected).Postępowanie:Core CC Tool (Message Viewer) → odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś (administrator Core CC Tool otwiera bramkę)kod 21 (błąd procesowy CCCt) → zgłoś — błąd procesu w Core CC Toolkod 30 (rozmiar niezgodny) → patrz stan rozmiarCCtool wysł.CCtool zwalid.Wynik dotarł, ACK nie napłynął w czasie (timeout).Postępowanie:Czekaj 5 min → Core CC Tool (Message Viewer)Jeżeli:Processed → oznacz 'R' w CCMbrak >10 min → zgłoś — sprawdź transport zwrotny Connector 2.0 (R18)CCtool wysł.CCtool zwalid.Wynik dotarł, brak ACK do CET.Postępowanie:Sprawdź transport zwrotny Connector 2.0Jeżeli:transport OK, ACK błąd → odczytaj kod ACK (patrz powiązany stan)awaria transportu → zgłoś (R18)CCtool wysł.CCtool zwalid.Wynik dotarł, ACK napłynął po CET — pozytywny.Walidacja opóźniona, ale OK (ACK po CET pozytywny).CCtool wysł.CCtool zwalid.Status nadany ręcznie 'R' (nietypowe dla pliku zwrotnego).Brak działań — status nadany ręcznie przez Dyspozytora (nietypowe dla pliku zwrotnego).CCtool wysł.CCtool zwalid.Niepoprawny rozmiar wyniku FIDx-928.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → sprawdź rozmiar (pobranie ponownie nie ma sensu — plik zwrotny)Jeżeli:zawartość OK mimo rozmiaru → oznacz 'R' w CCMzawartość niepoprawna → zgłoś + telefon do RCCCCtool wysł.CCtool zwalid.Niepoprawny rozmiar + brak ACK (timeout).Postępowanie:Core CC Tool (Message Viewer) → sprawdź statusJeżeli:Processed → oznacz 'R' w CCMbrak → zgłoś + telefon do RCCCCtool wysł.CCtool zwalid.Niepoprawny rozmiar + ACK negatywny.Postępowanie:Core CC Tool (Message Viewer) → odczytaj kod ACKJeżeli:kod 20 (bramka zamknięta) → zgłoś (administrator Core CC Tool)kod 30 (rozmiar) → patrz powiązany staninny → zgłoś + telefon do RCCCCtool wysł.CCtool zwalid.Niepoprawny rozmiar + brak ACK do CET. KRYTYCZNE.Postępowanie (KRYTYCZNE):⛔ Krytyczne — minął CET, niepoprawny rozmiar i brak ACK.Zgłoś + telefon do RCC szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.FIDx-928 dostarczony po CET — walidacja OK.Walidacja zakończona po terminie — OK.CCtool wysł.CCtool zwalid.Wysyłka zwrotna trwa (transport Connector 2.0).Postępowanie:Czekaj 5 min (transport zwrotny Connector 2.0)Jeżeli:zmieniło się na zielony → OK — koniecbrak >10 min → zgłoś (R18)CCtool wysł.CCtool zwalid.Status ręczny przyznany (nietypowe dla pliku zwrotnego).Brak działań — status ręczny przyznany przez Dyspozytora (nietypowe dla pliku zwrotnego).CCtool wysł.CCtool zwalid.TET zbliża się, ACK błąd już teraz (błąd paczki ATC).Postępowanie:Core CC Tool (Message Viewer) → odczytaj błąd paczki ATCJeżeli:błąd składowej → uzupełnij składową w aplikacji CCMinny → odczytaj kod ACK (patrz powiązany stan)



##### AGR Paczka ZIP ID3C do Perun PERUN_ID3C

Kod: PERUN_ID3C

Profil: 2MS

TET: 03:00

CET: 03:30

Źródło: agregacja

Wersja: 1

AGR Paczka ZIP (PERUN_ID3C) — zagregowana paczka wejściowa do Perun4V (proces FBA); zawiera składowe: scalone GLSK, CGM, RefProg, początkową domenę FB, CB, wierzchołki, RA.

**Ścieżka:**

Agregacja składowych →

MinIO

sFTP@pse.pl

→

Perun4V

Warianty stanów (10)

Status kafelkaSytuacjaDziałania awaryjneMinIOsFTP/ZP wysł.Paczka dostarczona prawidłowo na MinIO i sFTP/ZP.Brak działań — proces poprawny.MinIOsFTP/ZP wysł.Status nadany ręcznie 'R' po weryfikacji.Brak działań — decyzja ręczna.MinIOsFTP/ZP wysł.Paczka dostarczona po CET — status pozytywny.Brak działań — po CET OK.MinIOsFTP/ZP wysł.Przedwczesne — paczka jeszcze niewymagana.Monitoring — czekaj do TET.MinIOsFTP/ZP wysł.Zbliża się TET — paczka niekompletna / brak.Sprawdź agregację składowych. Gdy brak → zagreguj/pobierz ręcznie i wrzuć (Manual Upload / wysyłka na sFTP).MinIOsFTP/ZP wysł.Na MinIO OK, brak / błąd na sFTP/ZP.Gdy brak na sFTP → wyślij plik ręcznie ze źródła na sFTP/ZP.MinIOsFTP/ZP wysł.Brak / błąd na MinIO, OK na sFTP/ZP.Gdy brak na MinIO → pobierz/wygeneruj ręcznie i wgraj przez Manual Upload (GUI Core CC Tool).MinIOsFTP/ZP wysł.Transfer w toku (MinIO i sFTP/ZP).Czekaj 5 min → sprawdź MinIO i sFTP. Gdy brak → ręcznie (Manual Upload / wysyłka na sFTP).MinIOsFTP/ZP wysł.Zbliża się CET — brak / błąd na MinIO i sFTP/ZP.Gdy brak na MinIO → Manual Upload; gdy brak na sFTP → wyślij ręcznie.MinIOsFTP/ZP wysł.Minął CET — paczka niedostarczona. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Postępowanie krytyczne.



##### AGR Paczka ZIP_ATC ID3C do Perun PERUN_ID3C_ATC

Kod: PERUN_ID3C_ATC

Profil: 2MS

TET: 03:00

CET: 03:30

Źródło: agregacja

Wersja: 1

AGR Paczka ZIP_ATC (PERUN_ID3C_ATC) — paczka wejściowa dla odrębnej ścieżki walidacji domeny ATC.

**Ścieżka:**

Agregacja składowych →

MinIO

sFTP@pse.pl

→

Perun4V

Warianty stanów (10)

Status kafelkaSytuacjaDziałania awaryjneMinIOsFTP/ZP wysł.Paczka dostarczona prawidłowo na MinIO i sFTP/ZP.Brak działań — proces poprawny.MinIOsFTP/ZP wysł.Status nadany ręcznie 'R' po weryfikacji.Brak działań — decyzja ręczna.MinIOsFTP/ZP wysł.Paczka dostarczona po CET — status pozytywny.Brak działań — po CET OK.MinIOsFTP/ZP wysł.Przedwczesne — paczka jeszcze niewymagana.Monitoring — czekaj do TET.MinIOsFTP/ZP wysł.Zbliża się TET — paczka niekompletna / brak.Sprawdź agregację składowych. Gdy brak → zagreguj/pobierz ręcznie i wrzuć (Manual Upload / wysyłka na sFTP).MinIOsFTP/ZP wysł.Na MinIO OK, brak / błąd na sFTP/ZP.Gdy brak na sFTP → wyślij plik ręcznie ze źródła na sFTP/ZP.MinIOsFTP/ZP wysł.Brak / błąd na MinIO, OK na sFTP/ZP.Gdy brak na MinIO → pobierz/wygeneruj ręcznie i wgraj przez Manual Upload (GUI Core CC Tool).MinIOsFTP/ZP wysł.Transfer w toku (MinIO i sFTP/ZP).Czekaj 5 min → sprawdź MinIO i sFTP. Gdy brak → ręcznie (Manual Upload / wysyłka na sFTP).MinIOsFTP/ZP wysł.Zbliża się CET — brak / błąd na MinIO i sFTP/ZP.Gdy brak na MinIO → Manual Upload; gdy brak na sFTP → wyślij ręcznie.MinIOsFTP/ZP wysł.Minął CET — paczka niedostarczona. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Postępowanie krytyczne.



##### Raporty ID3C z Perun RAP_PERUN_ID3C

Kod: RAP_PERUN_ID3C

Profil: SFTP

TET: 03:20

CET: 03:50

Źródło: Perun4V

Wersja: 1

Raporty z Perun (RAP_PERUN_ID3C) — raporty walidacyjne z procesu Perun4V (charakter informacyjny).

**Ścieżka:**

Perun4V

→

kdm6@pse.pl

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjnesFTP/ZP wysł.Plik dostarczony prawidłowo na sFTP/ZP — status pozytywny.Brak działań — proces poprawny.sFTP/ZP wysł.Status nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.sFTP/ZP wysł.Plik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.sFTP/ZP wysł.Przedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.sFTP/ZP wysł.Oczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź sFTP/ZP. Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się TET — pliku jeszcze nie ma na sFTP/ZP.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się CET / błąd dostarczenia — brak pliku na sFTP/ZP.Gdy pliku NIE ma na sFTP/ZP → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Minął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Raporty ID3C ATC z Perun RAP_PERUN_ID3C_ATC

Kod: RAP_PERUN_ID3C_ATC

Profil: SFTP

TET: 03:20

CET: 03:50

Źródło: Perun4V

Wersja: 1

Raporty z Perun (RAP_PERUN_ID3C_ATC) — raporty walidacyjne z procesu Perun4V (charakter informacyjny).

**Ścieżka:**

Perun4V

→

kdm6@pse.pl

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjnesFTP/ZP wysł.Plik dostarczony prawidłowo na sFTP/ZP — status pozytywny.Brak działań — proces poprawny.sFTP/ZP wysł.Status nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.sFTP/ZP wysł.Plik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.sFTP/ZP wysł.Przedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.sFTP/ZP wysł.Oczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź sFTP/ZP. Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się TET — pliku jeszcze nie ma na sFTP/ZP.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się CET / błąd dostarczenia — brak pliku na sFTP/ZP.Gdy pliku NIE ma na sFTP/ZP → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Minął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Plik ze środkami zaradczymi z aplikacji KreatorDACF_CGMES XID3C_RA

Kod: XID3C_RA

Profil: MIN

TET: 03:00

CET: 03:30

Źródło: KreatorIDCF_CGMES

Wersja: 3

Plik ze środkami zaradczymi (RA, XID3C_RA) — remedial actions wygenerowane w Kreatorze; publikowane razem z GLSK/CBCORA i jako składowa paczki.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Plik ze środkami zaradczymi z aplikacji KreatorDACF_CGMES XID3C_RA

Kod: XID3C_RA

Profil: MIN

TET: 03:00

CET: 03:30

Źródło: KreatorIDCF_CGMES

Wersja: 3

Plik ze środkami zaradczymi (RA, XID3C_RA) — remedial actions wygenerowane w Kreatorze; publikowane razem z GLSK/CBCORA i jako składowa paczki.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



#### IDCC(d) — 40 plików



##### GLSK FID3-607

Kod: FID3-607

Profil: 2CCT

TET: 06:20

CET: 07:30

Źródło: KreatorDACF&2DAF_CGMES

Wersja: 3

GLSK (Generation and Load Shift Keys, FID3-607) — klucze rozdziału zmian generacji/obciążenia dla strefy PL; dane wejściowe Initial TSO receiving.

**Ścieżka:**

KreatorDACF&2DAF_CGMES

→

Connector 2.0

→

Core CC Tool

→

MinIO

Warianty stanów (32)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool. Dyspozytor ustawił status ręcznie 'R' po weryfikacji w CCTool.Brak działań.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool po CET, ACK napłynął po CET z pozytywnym komunikatem.Brak działań — dostarczone po CET, OK.CCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool oraz otrzymanie potwierdzenia ACK.Brak działań.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — wysyłka ręczna wykonana.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 5 minOK → ustaw 'R' w CCMCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, ale ACK nie napłynął w żądanym czasie i zbliża się CET.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, a otrzymane ACK: (1) zawiera komunikat błędu (najedź kursorem); (2) proces zakończył się błędem — 'Błąd procesu'.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż zapisana) → wygeneruj kolejną wersję w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)kod 30 (rozmiar pliku niezgodny) → wygeneruj ponownie w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem po CET.Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano ACK, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — decyzja ręczna Dyspozytora.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 2-5 minOK → ustaw 'R'CCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — upłynęło więcej niż 2 minuty.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET, a otrzymane ACK: (1) komunikat błędu; (2) proces zakończył się błędem. Typowo kod 20 gateClosed.Postępowanie:Najedź kursorem na status i odczytaj kod ACK (typowo kod 20)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka jest zamknięta → zgłośinny kod → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Otrzymano potwierdzenie ACK z pozytywnym komunikatem (po CET).Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool. Trwa oczekiwanie na ACK — około 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Trwa oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → utrzymaj 'R'brak / awaria → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie otrzymano, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — Dyspozytor zatwierdził zawartość.CCtool wysł.CCtool zwalid.Dokument jeszcze nie został wysłany do CCTool, ACK nie napłynął. Plik nie wymagany (>30 min do TET).Brak działań — czekaj do TET.CCtool wysł.CCtool zwalid.Zbliża się CET — plik niedostarczony lub błąd wysyłki. Stan alarmowy.Postępowanie (alarm):Core CC Tool → sprawdź czy plik dotarł do Core CC ToolJeżeli:plik jest, brak ACK → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak pliku (awaria Connector 2.0) → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykbrak pliku w źródle → Brak pliku lub wersji w aplikacji źródłowej. Otwórz KreatorIDCF_CGMES i wygeneruj plik ponownie (kolejna wersja); jeśli aplikacja nie działa — zgłoś. pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. Oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → sprawdź rozmiar; pobierz z MinIO i rozpakujJeżeli:zawartość OK mimo rozmiaru → oznacz 'R' (→ powiązany stan)zawartość niepoprawna → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru, a ACK ma status czerwony — typowo kod 30.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → potwierdź rozmiarWygeneruj poprawny plik w KreatorIDCF_CGMES (kolejna wersja) i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)Nadal za mały → zgłoś szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK napłynął po CET z pozytywnym komunikatem. Sprzeczność.Postępowanie:Pobierz z MinIO → rozpakuj → sprawdź zawartośćJeżeli:zawartość OK → oznacz 'R' (→ powiązany stan); zgłośniepoprawna → zgłośCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, ale ACK negatywny (Rejected). Kody: 20/21/30.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś (administrator Core CC Tool otwiera bramkę); sprawdź proces IDx-AC-FORWARDINGkod 21 (wersja nie jest wyższa niż zapisana) → wygeneruj kolejną wersję w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)kod 30 (rozmiar pliku niezgodny) → wygeneruj ponownie w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, trwa oczekiwanie na ACK, który nie napłynął w zadanym czasie (>2-3 min).Postępowanie:Czekaj 5 min → Core CC Tool (⚠ nie wysyłaj ponownie!)Jeżeli:Processed → oznacz 'R' + zgłośRejected → patrz stan kod ACKbrak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, ACK nie napłynął do CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:Processed → oznacz 'R' + zgłoś (→ powiązany stan)Rejected → wyślij ponownie przez Core CC Tool (Manual Upload) "po CET"brak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie napłynął do CET. Krytyczne.Postępowanie (KRYTYCZNE w C):Wygeneruj poprawny plik w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami) "po CET" (jeśli bramka otwarta)Natychmiast: zgłoś + powiadom RCC szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale walidacja zakończona negatywnie — ACK Rejected po CET.Postępowanie (po CET):Najedź kursorem na status i odczytaj kod ACK (kontekst: rejestracja po CET)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka zamknięta → zgłoś + powiadom RCCkod 21 (wersja nie jest wyższa niż zapisana) → wygeneruj kolejną wersję w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami) (jeśli bramka otwarta)kod 30 (rozmiar pliku niezgodny) → wygeneruj ponownie w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami) (jeśli bramka otwarta)CCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale ACK walidacji nie napłynął — plik dostarczony, lecz niezwalidowany.Postępowanie (po CET):Core CC Tool → sprawdź status walidacji (plik dostarczony po CET)Jeżeli:Processed → oznacz 'R' w CCM + zgłośRejected → postępuj jak w Stanie 30 (odczytaj kod ACK)brak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Dokument nie został dostarczony do CCTool, ACK nie napłynął. Minął czas CET. KRYTYCZNE — po CET dograć nie można.Postępowanie (KRYTYCZNE — brak naprawy):Telefon do RCC + zgłoś (priorytet P1)Po CET — brak naprawy. Diagnoza przyczyn: Kreator · Connector 2.0 · Core CC Tool szczegóły w bazie ryzyk



##### Merged Generation and Load Shift Keys (GLSK) FID3-610

Kod: FID3-610

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: proces Core

Wersja: 1

Merged GLSK (FID3-610) — scalone GLSK wszystkich TSO regionu Core. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Merged Generation and Load Shift Keys (GLSK) FID3-610

Kod: FID3-610

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: proces Core

Wersja: 1

Merged GLSK (FID3-610) — scalone GLSK wszystkich TSO regionu Core. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### CBCORA FID3-617

Kod: FID3-617

Profil: 2CCT

TET: 06:20

CET: 07:30

Źródło: KreatorDACF&2DAF_CGMES

Wersja: 3

CBCORA (Critical Branches & Critical Outages with Remedial Actions, FID3-617) — lista krytycznych elementów sieci (CNEC) PSE wraz z wyłączeniami; dane wejściowe TSO.

**Ścieżka:**

KreatorDACF&2DAF_CGMES

→

Connector 2.0

→

Core CC Tool

→

MinIO

Warianty stanów (32)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool. Dyspozytor ustawił status ręcznie 'R' po weryfikacji w CCTool.Brak działań.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool po CET, ACK napłynął po CET z pozytywnym komunikatem.Brak działań — dostarczone po CET, OK.CCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool oraz otrzymanie potwierdzenia ACK.Brak działań.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — wysyłka ręczna wykonana.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 5 minOK → ustaw 'R' w CCMCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, ale ACK nie napłynął w żądanym czasie i zbliża się CET.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, a otrzymane ACK: (1) zawiera komunikat błędu (najedź kursorem); (2) proces zakończył się błędem — 'Błąd procesu'.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż zapisana) → wygeneruj kolejną wersję w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)kod 30 (rozmiar pliku niezgodny) → wygeneruj ponownie w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem po CET.Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano ACK, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — decyzja ręczna Dyspozytora.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 2-5 minOK → ustaw 'R'CCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — upłynęło więcej niż 2 minuty.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET, a otrzymane ACK: (1) komunikat błędu; (2) proces zakończył się błędem. Typowo kod 20 gateClosed.Postępowanie:Najedź kursorem na status i odczytaj kod ACK (typowo kod 20)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka jest zamknięta → zgłośinny kod → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Otrzymano potwierdzenie ACK z pozytywnym komunikatem (po CET).Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool. Trwa oczekiwanie na ACK — około 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Trwa oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → utrzymaj 'R'brak / awaria → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie otrzymano, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — Dyspozytor zatwierdził zawartość.CCtool wysł.CCtool zwalid.Dokument jeszcze nie został wysłany do CCTool, ACK nie napłynął. Plik nie wymagany (>30 min do TET).Brak działań — czekaj do TET.CCtool wysł.CCtool zwalid.Zbliża się CET — plik niedostarczony lub błąd wysyłki. Stan alarmowy.Postępowanie (alarm):Core CC Tool → sprawdź czy plik dotarł do Core CC ToolJeżeli:plik jest, brak ACK → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak pliku (awaria Connector 2.0) → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykbrak pliku w źródle → Brak pliku lub wersji w aplikacji źródłowej. Otwórz KreatorIDCF_CGMES i wygeneruj plik ponownie (kolejna wersja); jeśli aplikacja nie działa — zgłoś. pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. Oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → sprawdź rozmiar; pobierz z MinIO i rozpakujJeżeli:zawartość OK mimo rozmiaru → oznacz 'R' (→ powiązany stan)zawartość niepoprawna → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru, a ACK ma status czerwony — typowo kod 30.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → potwierdź rozmiarWygeneruj poprawny plik w KreatorIDCF_CGMES (kolejna wersja) i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)Nadal za mały → zgłoś szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK napłynął po CET z pozytywnym komunikatem. Sprzeczność.Postępowanie:Pobierz z MinIO → rozpakuj → sprawdź zawartośćJeżeli:zawartość OK → oznacz 'R' (→ powiązany stan); zgłośniepoprawna → zgłośCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, ale ACK negatywny (Rejected). Kody: 20/21/30.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś (administrator Core CC Tool otwiera bramkę); sprawdź proces IDx-AC-FORWARDINGkod 21 (wersja nie jest wyższa niż zapisana) → wygeneruj kolejną wersję w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)kod 30 (rozmiar pliku niezgodny) → wygeneruj ponownie w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami)CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, trwa oczekiwanie na ACK, który nie napłynął w zadanym czasie (>2-3 min).Postępowanie:Czekaj 5 min → Core CC Tool (⚠ nie wysyłaj ponownie!)Jeżeli:Processed → oznacz 'R' + zgłośRejected → patrz stan kod ACKbrak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, ACK nie napłynął do CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:Processed → oznacz 'R' + zgłoś (→ powiązany stan)Rejected → wyślij ponownie przez Core CC Tool (Manual Upload) "po CET"brak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie napłynął do CET. Krytyczne.Postępowanie (KRYTYCZNE w C):Wygeneruj poprawny plik w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami) "po CET" (jeśli bramka otwarta)Natychmiast: zgłoś + powiadom RCC szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale walidacja zakończona negatywnie — ACK Rejected po CET.Postępowanie (po CET):Najedź kursorem na status i odczytaj kod ACK (kontekst: rejestracja po CET)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka zamknięta → zgłoś + powiadom RCCkod 21 (wersja nie jest wyższa niż zapisana) → wygeneruj kolejną wersję w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami) (jeśli bramka otwarta)kod 30 (rozmiar pliku niezgodny) → wygeneruj ponownie w KreatorIDCF_CGMES i opublikuj (Publikuj Connector) · szczegółowa procedura (ze screenami) (jeśli bramka otwarta)CCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale ACK walidacji nie napłynął — plik dostarczony, lecz niezwalidowany.Postępowanie (po CET):Core CC Tool → sprawdź status walidacji (plik dostarczony po CET)Jeżeli:Processed → oznacz 'R' w CCM + zgłośRejected → postępuj jak w Stanie 30 (odczytaj kod ACK)brak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie wygeneruj plik w KreatorIDCF_CGMES i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Dokument nie został dostarczony do CCTool, ACK nie napłynął. Minął czas CET. KRYTYCZNE — po CET dograć nie można.Postępowanie (KRYTYCZNE — brak naprawy):Telefon do RCC + zgłoś (priorytet P1)Po CET — brak naprawy. Diagnoza przyczyn: Kreator · Connector 2.0 · Core CC Tool szczegóły w bazie ryzyk



##### Merged DACF/IDCF Common Grid Model (CGM) FID3-620

Kod: FID3-620

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: proces Core / Kreator

Wersja: 4

Merged DACF/IDCF Common Grid Model (CGM, FID3-620) — scalony wspólny model sieci zbudowany z modeli indywidualnych (IGM) TSO. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Merged DACF/IDCF Common Grid Model (CGM) FID3-620

Kod: FID3-620

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: proces Core / Kreator

Wersja: 4

Merged DACF/IDCF Common Grid Model (CGM, FID3-620) — scalony wspólny model sieci zbudowany z modeli indywidualnych (IGM) TSO. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Reference Program (RefProg) FID3-632

Kod: FID3-632

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: proces Core

Wersja: 3

Reference Program (RefProg, FID3-632) — program referencyjny: planowane salda wymiany międzyobszarowej. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Reference Program (RefProg) FID3-632

Kod: FID3-632

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: proces Core

Wersja: 3

Reference Program (RefProg, FID3-632) — program referencyjny: planowane salda wymiany międzyobszarowej. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Reference Program (RefProg) FID3-632

Kod: FID3-632

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: proces Core

Wersja: 3

Reference Program (RefProg, FID3-632) — program referencyjny: planowane salda wymiany międzyobszarowej. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Reference Program (RefProg) FID3-632

Kod: FID3-632

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: proces Core

Wersja: 3

Reference Program (RefProg, FID3-632) — program referencyjny: planowane salda wymiany międzyobszarowej. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial FB Domain (RefProg Bal) FID3-645

Kod: FID3-645

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: Perun4V / proces Core

Wersja: 1

Initial FB Domain (Virgin / RefProg Bal, FID3-645) — początkowa domena Flow-Based. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial FB Domain (RefProg Bal) FID3-645

Kod: FID3-645

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: Perun4V / proces Core

Wersja: 1

Initial FB Domain (Virgin / RefProg Bal, FID3-645) — początkowa domena Flow-Based. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial FB Domain (RefProg Bal) FID3-645

Kod: FID3-645

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: Perun4V / proces Core

Wersja: 1

Initial FB Domain (Virgin / RefProg Bal, FID3-645) — początkowa domena Flow-Based. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial FB Domain (Virgin RefProg Bal) FID3-645

Kod: FID3-645

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: Perun4V / proces Core

Wersja: 1

Initial FB Domain (Virgin / RefProg Bal, FID3-645) — początkowa domena Flow-Based. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial FB Domain (RefProg Bal) FID3-645

Kod: FID3-645

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: Perun4V / proces Core

Wersja: 1

Initial FB Domain (Virgin / RefProg Bal, FID3-645) — początkowa domena Flow-Based. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Real Generation and Load Shift Keys (GLSK) FID3-657

Kod: FID3-657

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: Kreator

Wersja: 1

Real GLSK (FID3-657) — rzeczywiste klucze GLSK (po dostosowaniu do bieżącego stanu). Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Real Generation and Load Shift Keys (GLSK) FID3-657

Kod: FID3-657

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: Kreator

Wersja: 1

Real GLSK (FID3-657) — rzeczywiste klucze GLSK (po dostosowaniu do bieżącego stanu). Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### CGM Data Quality Check FID3-659

Kod: FID3-659

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: proces Core

Wersja: 1

CGM Data Quality Check (FID3-659) — raport kontroli jakości danych scalonego modelu CGM. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### CGM Data Quality Check FID3-659

Kod: FID3-659

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: proces Core

Wersja: 1

CGM Data Quality Check (FID3-659) — raport kontroli jakości danych scalonego modelu CGM. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Individual Filtered Critical Branches (CB) FID3-665

Kod: FID3-665

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: Kreator

Wersja: 1

Individual Filtered Critical Branches (CB, FID3-665) — indywidualne, przefiltrowane gałęzie krytyczne PSE. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Individual Filtered Critical Branches (CB) FID3-665

Kod: FID3-665

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: Kreator

Wersja: 1

Individual Filtered Critical Branches (CB, FID3-665) — indywidualne, przefiltrowane gałęzie krytyczne PSE. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Vertices of Initial FB Domain FID3-701

Kod: FID3-701

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: Perun4V

Wersja: 1

Vertices of Initial FB Domain (FID3-701) — wierzchołki początkowej domeny Flow-Based. Składowa paczki PERUN.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Vertices of Initial FB Domain/CB Validation file ATC FID3-701_ATC

Kod: FID3-701_ATC

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: Perun4V

Wersja: 1

Vertices / CB Validation file ATC (FID3-701_ATC) — wierzchołki domeny / plik walidacji CB dla ścieżki ATC. Składowa paczki ATC.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Vertices of Initial FB Domain/CB Validation file ATC FID3-701_ATC

Kod: FID3-701_ATC

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: Perun4V

Wersja: 1

Vertices / CB Validation file ATC (FID3-701_ATC) — wierzchołki domeny / plik walidacji CB dla ścieżki ATC. Składowa paczki ATC.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### IVA FID3-710

Kod: FID3-710

Profil: 3COL

TET: 09:30

CET: 10:06

Źródło: Perun4V

Wersja: 1

IVA — Individual Validation Adjustment (FID3-710) — wynik indywidualnej walidacji domeny Flow-Based (z Perun4V); korekta domeny po walidacji TSO.

**Ścieżka:**

Perun4V

→

MinIO

Connector 2.0

→

CCM

Warianty stanów (46)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.MinIODokument został wysłany prawidłowo do CCTool i na MINIO, otrzymano potwierdzenie ACK z pozytywnym komunikatem (komunikat statusu powinien się pojawić po najechaniu kursorem na status).Brak — proces przebiegł poprawnie.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, Dokument ACK (CCTool zwalid.) napłynął po CET z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, nie otrzymano potwierdzenia ACK, natomiast Dyspozytor ustawił status ręcznie 'R' po weryfikacji po stronie CCTool, iż proces został zrealizowany poprawnie.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO po CET, Dokument ACK (CCTool zwalid.) napłynął po CET z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO oraz otrzymanie potwierdzenia ACK.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu aplikacji CCM w jednym miejscu (np. z menu bocznego „CCTool wysł." bądź „MINIO" korzystając z opcji „Wyślij"). Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Po 5 min jeśli proces przebiegł poprawnie → ustaw 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM, ale nie napłynął ACK w żądanym czasie i zbliża się Critical End Time dla obsługi tego dokumentu.Monitoring CCCt MV; jeśli proces OK → status 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM, a otrzymane potwierdzenie ACK (CCTool zwalid.): (1) zawiera komunikat błędu (najedź kursorem na status); (2) proces zakończył się błędem — „Błąd procesu".Weryfikacja sytuacji w CCTool. Decyzja Dyspozytora o ewentualnej kolejnej iteracji.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem po CET.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Weryfikacja w CCCt MV; jeśli Processed → status 'R' ręcznie. Diagnostyka CN2 zwrotny → zgłoś.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano ACK, natomiast Dyspozytor ustawił status ręcznie 'R' po weryfikacji po stronie CCTool, iż proces został zrealizowany poprawnie.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM po CET (opcja „Wyślij po CET"). Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — upłynęło więcej niż 2 minuty (czas oczekiwania można sprawdzić najeżdżając kursorem na status).Weryfikacja sytuacji w CCTool; jeśli proces przebiegł poprawnie → ustaw status 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM po CET, a otrzymane potwierdzenie ACK (CCTool zwalid.): (1) zawiera komunikat błędu; (2) proces zakończył się błędem — „Błąd procesu".Weryfikacja sytuacji w CCTool. Zgłoś.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM po CET. Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM po CET. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Diagnostyka CN2 zwrotny → zgłoś.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Weryfikacja w CCTool; po 5 min jeśli proces przebiegł poprawnie → ustaw 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — upłynęło więcej niż 2 minuty.Weryfikacja w CCTool; jeśli proces przebiegł poprawnie → ustaw 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Diagnostyka CN2 zwrotny → zgłoś.CCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru (w informacjach o wielkości rozmiaru dostępna z poziomu menu bocznego na statusie). Nie otrzymano potwierdzenie ACK, natomiast Dyspozytor ustawił status ręcznie 'R' po weryfikacji po stronie CCTool, iż proces został zrealizowany poprawnie.Zgłoś informacyjnie (ew. zmiana konfiguracji rozmiaru).CCtool wysł.CCtool zwalid.MinIODokument jeszcze nie został wysłany ani do CCTool ani na MINIO, w związku z tym potwierdzenie ACK nie napłynęło.Brak — monitoring. Plik nie wymagany (>30 min do TET).CCtool wysł.CCtool zwalid.MinIOZbliża się TET (21:30), a dokument nie został jeszcze obsłużony.Brak. Czujność i przygotowanie. Sprawdź Perun4V (status obliczeń); sprawdź CN2; przygotuj się na ewentualne IVA BACKUP od CCA. Jeśli sytuacja się utrzyma → Kategoria C (powiązany stan).CCtool wysł.CCtool zwalid.MinIOWysyłka do CCTool trwa i oczekiwany jest ACK, dokument dostarczony na MINIO.Jeśli taki status „CCTool wysł." trwa dłużej niż 5 minut należy zweryfikować stan w CCTool, ewentualnie zgłosić problem.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, trwa oczekiwanie na potwierdzenie ACK (status powinien się utrzymać krócej niż 3 minuty).Brak. Czekaj do 3-5 min na ACK; po tym czasie → stan timeout.CCtool wysł.CCtool zwalid.MinIOWysyłka do CCTool trwa i oczekiwany jest ACK. Dokument dostarczony na MINIO nie spełnia kryterium rozmiaru (w informacjach o wielkości rozmiaru dostępna z poziomu menu bocznego na statusie).Jeśli taki status „CCTool wysł." trwa dłużej niż 5 minut → zweryfikować stan w CCTool, ew. zgłosić problem Zweryfikować dokument IVA czy jest poprawny (pobierając go z CCM i rozpakowując) — pomimo zbyt małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOZbliża się CET (22:06), a dokument nie został jeszcze obsłużony.Procedura (wg Confluence): Jeśli zbliża się CET (poniżej 3 minut) możliwa jest ręczna wysyłka IVA Backup z menu bocznego na poniższej pozycji pulpitu. Alternatywnie: R08 (Perun4V awaria), R09 (ERR-I), R10 (Process failed).CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, potwierdzenie ACK ma status czerwony co może oznaczać: (1) zawiera komunikat błędu (najedź kursorem na status); (2) proces zakończył się błędem — „Błąd procesu".Procedura: R05 — reakcja per kod ACK (20 gateClosed / 21 duplicatedVersion / 30 file size). Należy zweryfikować sytuację w CCTool.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, trwa oczekiwanie na potwierdzenie ACK, które nie napłynęło w zadanym czasie (po najechaniu na znak zapytania można sprawdzić ile upłynęło czasu).Procedura: R06. Jeśli po około 3 minutach nie pojawi się status ACK wraz z informacją dostępną po najechaniu na status → należy zweryfikować sytuację w CCTool.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO. Dokument ACK (CCTool zwalid.) nie napłynął do CET.Procedury: R06, R18. Należy zweryfikować sytuację w CCTool. W przypadku wygenerowania ACK po stronie CCTool — sytuację zgłosić.CCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru (w informacjach o wielkości rozmiaru dostępna z poziomu menu bocznego na statusie). Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Procedura: R05. Zweryfikować dokument IVA czy jest poprawny (pobierając go z CCM i rozpakowując) — pomimo zbyt małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 1 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.), które nie napłynęło w zadanym czasie (po najechaniu na znak zapytania można sprawdzić ile upłynęło czasu).Procedura: R05, R06. Jeśli po około 3 minutach nie pojawi się status ACK wraz z informacją po najechaniu na status → zweryfikować sytuację w CCTool Zweryfikować dokument IVA (pobranie z CCM i rozpakowanie) — pomimo małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru, a otrzymane potwierdzenie ACK (CCTool zwalid.): (1) zawiera komunikat błędu; (2) proces zakończył się błędem — „Błąd procesu".Procedura: R05. Należy zweryfikować sytuację w CCTool Zweryfikować dokument IVA czy jest poprawny (pobranie z CCM i rozpakowanie) — pomimo małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru. Dokument ACK (CCTool zwalid.) napłynął po CET z pozytywnym komunikatem.Należy zweryfikować dokument IVA czy jest poprawny i czy został przyjęty w CCTool Jeśli plik z pkt. 1 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCTool Po weryfikacji można nadać 'R' → Stan #21 (Kategoria A).CCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru. Dokument ACK (CCTool zwalid.) nie napłynął do CET.Zweryfikować sytuację w CCTool — w przypadku wygenerowania ACK po stronie CCTool sytuację zgłosić Zweryfikować dokument IVA (pobranie z CCM i rozpakowanie) — pomimo małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO po CET, potwierdzenie ACK ma status czerwony co może oznaczać: (1) zawiera komunikat błędu; (2) proces zakończył się błędem — „Błąd procesu".Procedura: R05. Należy zweryfikować sytuację w CCTool.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO po CET. Dokument ACK (CCTool zwalid.) nie napłynął do CET.Procedury: R06, R18. Należy zweryfikować sytuację w CCTool, w przypadku wygenerowania ACK po stronie CCTool sytuację zgłosić.CCtool wysł.CCtool zwalid.MinIODokument nie został dostarczony ani do CCTool ani na MINIO, w związku z tym potwierdzenie ACK nie napłynęło. Minął czas CET.Procedura (wg Confluence): Należy zweryfikować czy dokument IVA jest w PERUN. Jeśli TAK to należy go niezwłocznie pozyskać ręcznie i wysłać ją bezpośrednio z CCM bądź z GUI CCTool Procedury IDCC: R10 (Process failed) — oczekuj IVA BACKUP v1 od CCA; brak → R19 (CN2 nie kopiuje do CCA), R23 (brak raportu CCA). Zgłoś (CIZ, WPO, PSE-I) + telefon CCC. ❌ Zakaz fallbacku 20% Fmax z DA.MinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### IVA Backup FID3-710

Kod: FID3-710

Profil: MIN

TET: 09:30

CET: 10:06

Źródło: CCA

Wersja: 1

IVA Backup (FID3-710) — backupowa wersja IVA generowana przez CCA (publikowana do cca/…/out/), na wypadek braku/niezgodności IVA podstawowego.

**Ścieżka:**

CCA

→

MinIO

→

CCM

Warianty stanów (46)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.MinIODokument został wysłany prawidłowo do CCTool i na MINIO, otrzymano potwierdzenie ACK z pozytywnym komunikatem (komunikat statusu powinien się pojawić po najechaniu kursorem na status).Brak — proces przebiegł poprawnie.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, Dokument ACK (CCTool zwalid.) napłynął po CET z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, nie otrzymano potwierdzenia ACK, natomiast Dyspozytor ustawił status ręcznie 'R' po weryfikacji po stronie CCTool, iż proces został zrealizowany poprawnie.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO po CET, Dokument ACK (CCTool zwalid.) napłynął po CET z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO oraz otrzymanie potwierdzenia ACK.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu aplikacji CCM w jednym miejscu (np. z menu bocznego „CCTool wysł." bądź „MINIO" korzystając z opcji „Wyślij"). Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Po 5 min jeśli proces przebiegł poprawnie → ustaw 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM, ale nie napłynął ACK w żądanym czasie i zbliża się Critical End Time dla obsługi tego dokumentu.Monitoring CCCt MV; jeśli proces OK → status 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM, a otrzymane potwierdzenie ACK (CCTool zwalid.): (1) zawiera komunikat błędu (najedź kursorem na status); (2) proces zakończył się błędem — „Błąd procesu".Weryfikacja sytuacji w CCTool. Decyzja Dyspozytora o ewentualnej kolejnej iteracji.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem po CET.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Weryfikacja w CCCt MV; jeśli Processed → status 'R' ręcznie. Diagnostyka CN2 zwrotny → zgłoś.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano ACK, natomiast Dyspozytor ustawił status ręcznie 'R' po weryfikacji po stronie CCTool, iż proces został zrealizowany poprawnie.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM po CET (opcja „Wyślij po CET"). Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — upłynęło więcej niż 2 minuty (czas oczekiwania można sprawdzić najeżdżając kursorem na status).Weryfikacja sytuacji w CCTool; jeśli proces przebiegł poprawnie → ustaw status 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument wysłany ręcznie z poziomu CCM po CET, a otrzymane potwierdzenie ACK (CCTool zwalid.): (1) zawiera komunikat błędu; (2) proces zakończył się błędem — „Błąd procesu".Weryfikacja sytuacji w CCTool. Zgłoś.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM po CET. Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.MinIODokument IVA prawidłowo wysłany ręcznie z poziomu CCM po CET. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Diagnostyka CN2 zwrotny → zgłoś.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Weryfikacja w CCTool; po 5 min jeśli proces przebiegł poprawnie → ustaw 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — upłynęło więcej niż 2 minuty.Weryfikacja w CCTool; jeśli proces przebiegł poprawnie → ustaw 'R' dla ACK.CCtool wysł.CCtool zwalid.MinIODokument IVA został oznaczony ręcznie jako wysłany prawidłowo do CCTool i na MINIO. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Diagnostyka CN2 zwrotny → zgłoś.CCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru (w informacjach o wielkości rozmiaru dostępna z poziomu menu bocznego na statusie). Nie otrzymano potwierdzenie ACK, natomiast Dyspozytor ustawił status ręcznie 'R' po weryfikacji po stronie CCTool, iż proces został zrealizowany poprawnie.Zgłoś informacyjnie (ew. zmiana konfiguracji rozmiaru).CCtool wysł.CCtool zwalid.MinIODokument jeszcze nie został wysłany ani do CCTool ani na MINIO, w związku z tym potwierdzenie ACK nie napłynęło.Brak — monitoring. Plik nie wymagany (>30 min do TET).CCtool wysł.CCtool zwalid.MinIOZbliża się TET (21:30), a dokument nie został jeszcze obsłużony.Brak. Czujność i przygotowanie. Sprawdź Perun4V (status obliczeń); sprawdź CN2; przygotuj się na ewentualne IVA BACKUP od CCA. Jeśli sytuacja się utrzyma → Kategoria C (powiązany stan).CCtool wysł.CCtool zwalid.MinIOWysyłka do CCTool trwa i oczekiwany jest ACK, dokument dostarczony na MINIO.Jeśli taki status „CCTool wysł." trwa dłużej niż 5 minut należy zweryfikować stan w CCTool, ewentualnie zgłosić problem.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, trwa oczekiwanie na potwierdzenie ACK (status powinien się utrzymać krócej niż 3 minuty).Brak. Czekaj do 3-5 min na ACK; po tym czasie → stan timeout.CCtool wysł.CCtool zwalid.MinIOWysyłka do CCTool trwa i oczekiwany jest ACK. Dokument dostarczony na MINIO nie spełnia kryterium rozmiaru (w informacjach o wielkości rozmiaru dostępna z poziomu menu bocznego na statusie).Jeśli taki status „CCTool wysł." trwa dłużej niż 5 minut → zweryfikować stan w CCTool, ew. zgłosić problem Zweryfikować dokument IVA czy jest poprawny (pobierając go z CCM i rozpakowując) — pomimo zbyt małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOZbliża się CET (22:06), a dokument nie został jeszcze obsłużony.Procedura (wg Confluence): Jeśli zbliża się CET (poniżej 3 minut) możliwa jest ręczna wysyłka IVA Backup z menu bocznego na poniższej pozycji pulpitu. Alternatywnie: R08 (Perun4V awaria), R09 (ERR-I), R10 (Process failed).CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, potwierdzenie ACK ma status czerwony co może oznaczać: (1) zawiera komunikat błędu (najedź kursorem na status); (2) proces zakończył się błędem — „Błąd procesu".Procedura: R05 — reakcja per kod ACK (20 gateClosed / 21 duplicatedVersion / 30 file size). Należy zweryfikować sytuację w CCTool.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO, trwa oczekiwanie na potwierdzenie ACK, które nie napłynęło w zadanym czasie (po najechaniu na znak zapytania można sprawdzić ile upłynęło czasu).Procedura: R06. Jeśli po około 3 minutach nie pojawi się status ACK wraz z informacją dostępną po najechaniu na status → należy zweryfikować sytuację w CCTool.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO. Dokument ACK (CCTool zwalid.) nie napłynął do CET.Procedury: R06, R18. Należy zweryfikować sytuację w CCTool. W przypadku wygenerowania ACK po stronie CCTool — sytuację zgłosić.CCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru (w informacjach o wielkości rozmiaru dostępna z poziomu menu bocznego na statusie). Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.) — około 2 minut trwa taki status.Procedura: R05. Zweryfikować dokument IVA czy jest poprawny (pobierając go z CCM i rozpakowując) — pomimo zbyt małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 1 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru. Trwa oczekiwanie na potwierdzenie ACK (CCTool zwalid.), które nie napłynęło w zadanym czasie (po najechaniu na znak zapytania można sprawdzić ile upłynęło czasu).Procedura: R05, R06. Jeśli po około 3 minutach nie pojawi się status ACK wraz z informacją po najechaniu na status → zweryfikować sytuację w CCTool Zweryfikować dokument IVA (pobranie z CCM i rozpakowanie) — pomimo małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru, a otrzymane potwierdzenie ACK (CCTool zwalid.): (1) zawiera komunikat błędu; (2) proces zakończył się błędem — „Błąd procesu".Procedura: R05. Należy zweryfikować sytuację w CCTool Zweryfikować dokument IVA czy jest poprawny (pobranie z CCM i rozpakowanie) — pomimo małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru. Dokument ACK (CCTool zwalid.) napłynął po CET z pozytywnym komunikatem.Należy zweryfikować dokument IVA czy jest poprawny i czy został przyjęty w CCTool Jeśli plik z pkt. 1 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCTool Po weryfikacji można nadać 'R' → Stan #21 (Kategoria A).CCtool wysł.CCtool zwalid.MinIOWysłany dokument nie spełnia kryterium rozmiaru. Dokument ACK (CCTool zwalid.) nie napłynął do CET.Zweryfikować sytuację w CCTool — w przypadku wygenerowania ACK po stronie CCTool sytuację zgłosić Zweryfikować dokument IVA (pobranie z CCM i rozpakowanie) — pomimo małego rozmiaru sytuacja może być OK Jeśli plik z pkt. 2 jest niepoprawny → pozyskać IVA z PERUN i wysłać bezpośrednio z CCM bądź z GUI CCToolCCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO po CET, potwierdzenie ACK ma status czerwony co może oznaczać: (1) zawiera komunikat błędu; (2) proces zakończył się błędem — „Błąd procesu".Procedura: R05. Należy zweryfikować sytuację w CCTool.CCtool wysł.CCtool zwalid.MinIODokument wysłany prawidłowo do CCTool i na MINIO po CET. Dokument ACK (CCTool zwalid.) nie napłynął do CET.Procedury: R06, R18. Należy zweryfikować sytuację w CCTool, w przypadku wygenerowania ACK po stronie CCTool sytuację zgłosić.CCtool wysł.CCtool zwalid.MinIODokument nie został dostarczony ani do CCTool ani na MINIO, w związku z tym potwierdzenie ACK nie napłynęło. Minął czas CET.Procedura (wg Confluence): Należy zweryfikować czy dokument IVA jest w PERUN. Jeśli TAK to należy go niezwłocznie pozyskać ręcznie i wysłać ją bezpośrednio z CCM bądź z GUI CCTool Procedury IDCC: R10 (Process failed) — oczekuj IVA BACKUP v1 od CCA; brak → R19 (CN2 nie kopiuje do CCA), R23 (brak raportu CCA). Zgłoś (CIZ, WPO, PSE-I) + telefon CCC. ❌ Zakaz fallbacku 20% Fmax z DA.MinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### IVA_ATC FID3-710_ATC

Kod: FID3-710_ATC

Profil: MIN

TET: 08:45

CET: 09:20

Źródło: Perun4V

Wersja: 1

IVA_ATC (FID3-710_ATC) — IVA dla odrębnej ścieżki walidacji domeny ATC.

**Ścieżka:**

Perun4V

→

MinIO

Connector 2.0

→

CCM

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### IVA_ATC FID3-710_ATC

Kod: FID3-710_ATC

Profil: MIN

TET: 08:45

CET: 09:20

Źródło: Perun4V

Wersja: 1

IVA_ATC (FID3-710_ATC) — IVA dla odrębnej ścieżki walidacji domeny ATC.

**Ścieżka:**

Perun4V

→

MinIO

Connector 2.0

→

CCM

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### AC FID3-831

Kod: FID3-831

Profil: 2CCT

TET: 08:40

CET: 09:25

Źródło: ZP

Wersja: 4

AC (Allocation Constraints, FID3-831) — plik z wartościami ograniczeń alokacyjnych wyznaczonych przez PSE, publikowany do PuTo i do procesu Core. Format XML, MTU 15 min.

**Ścieżka:**

ZP

→

Connector 2.0

→

Core CC Tool

→

PuTo

+

MinIO

Warianty stanów (32)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool. Dyspozytor ustawił status ręcznie 'R' po weryfikacji w CCTool.Brak działań.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool po CET, ACK napłynął po CET z pozytywnym komunikatem.Brak działań — dostarczone po CET, OK.CCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool oraz otrzymanie potwierdzenia ACK.Brak działań.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — wysyłka ręczna wykonana.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 5 minOK → ustaw 'R' w CCMCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, ale ACK nie napłynął w żądanym czasie i zbliża się CET.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, a otrzymane ACK: (1) zawiera komunikat błędu (najedź kursorem); (2) proces zakończył się błędem — 'Błąd procesu'.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż zapisana) → podnieś numer wersji w aplikacji ZP i wyślij plik ponownie przez Core CC Tool (Manual Upload)kod 30 (rozmiar pliku niezgodny) → pobierz poprawny plik z MinIO lub aplikacji ZP i wyślij ponownieCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem po CET.Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano ACK, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — decyzja ręczna Dyspozytora.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 2-5 minOK → ustaw 'R'CCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — upłynęło więcej niż 2 minuty.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET, a otrzymane ACK: (1) komunikat błędu; (2) proces zakończył się błędem. Typowo kod 20 gateClosed.Postępowanie:Najedź kursorem na status i odczytaj kod ACK (typowo kod 20)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka jest zamknięta → zgłośinny kod → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Otrzymano potwierdzenie ACK z pozytywnym komunikatem (po CET).Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool. Trwa oczekiwanie na ACK — około 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Trwa oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → utrzymaj 'R'brak / awaria → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie otrzymano, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — Dyspozytor zatwierdził zawartość.CCtool wysł.CCtool zwalid.Dokument jeszcze nie został wysłany do CCTool, ACK nie napłynął. Plik nie wymagany (>30 min do TET).Brak działań — czekaj do TET.CCtool wysł.CCtool zwalid.Zbliża się CET — plik niedostarczony lub błąd wysyłki. Stan alarmowy.Postępowanie (alarm):Core CC Tool → sprawdź czy plik dotarł do Core CC ToolJeżeli:plik jest, brak ACK → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak pliku (awaria Connector 2.0) → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykbrak pliku w źródle → Brak pliku lub wersji w aplikacji źródłowej. Otwórz aplikacji ZP, przejdź do bilansu i sprawdź wersję pliku: jeśli wersja jest dostępna — pobierz ją (Pobierz XML); jeśli brakuje — wygeneruj nową wersję; jeśli aplikacja nie działa — zgłoś. pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. Oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → sprawdź rozmiar; pobierz z MinIO i rozpakujJeżeli:zawartość OK mimo rozmiaru → oznacz 'R' (→ powiązany stan)zawartość niepoprawna → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru, a ACK ma status czerwony — typowo kod 30.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → potwierdź rozmiarPobierz poprawny plik z aplikacji ZP (Pobierz XML) i wyślij przez Core CC Tool (Manual Upload) z kolejnym numerem wersjiNadal za mały → zgłoś szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK napłynął po CET z pozytywnym komunikatem. Sprzeczność.Postępowanie:Pobierz z MinIO → rozpakuj → sprawdź zawartośćJeżeli:zawartość OK → oznacz 'R' (→ powiązany stan); zgłośniepoprawna → zgłośCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, ale ACK negatywny (Rejected). Kody: 20/21/30.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś (administrator Core CC Tool otwiera bramkę); sprawdź proces IDx-AC-FORWARDINGkod 21 (wersja nie jest wyższa niż zapisana) → podnieś numer wersji w aplikacji ZP i wyślij plik ponownie przez Core CC Tool (Manual Upload)kod 30 (rozmiar pliku niezgodny) → pobierz poprawny plik z MinIO lub aplikacji ZP i wyślij ponownieCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, trwa oczekiwanie na ACK, który nie napłynął w zadanym czasie (>2-3 min).Postępowanie:Czekaj 5 min → Core CC Tool (⚠ nie wysyłaj ponownie!)Jeżeli:Processed → oznacz 'R' + zgłośRejected → patrz stan kod ACKbrak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, ACK nie napłynął do CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:Processed → oznacz 'R' + zgłoś (→ powiązany stan)Rejected → wyślij ponownie przez Core CC Tool (Manual Upload) "po CET"brak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie napłynął do CET. Krytyczne.Postępowanie (KRYTYCZNE w C):Pobierz poprawny plik z aplikacji ZP i wyślij przez Core CC Tool (Manual Upload) "po CET" (jeśli bramka otwarta)Natychmiast: zgłoś + powiadom RCC szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale walidacja zakończona negatywnie — ACK Rejected po CET.Postępowanie (po CET):Najedź kursorem na status i odczytaj kod ACK (kontekst: rejestracja po CET)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka zamknięta → zgłoś + powiadom RCCkod 21 (wersja nie jest wyższa niż zapisana) → podnieś numer wersji w aplikacji ZP i wyślij plik ponownie przez Core CC Tool (Manual Upload) (jeśli bramka otwarta)kod 30 (rozmiar pliku niezgodny) → pobierz poprawny plik z MinIO lub aplikacji ZP i wyślij ponownie (jeśli bramka otwarta)CCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale ACK walidacji nie napłynął — plik dostarczony, lecz niezwalidowany.Postępowanie (po CET):Core CC Tool → sprawdź status walidacji (plik dostarczony po CET)Jeżeli:Processed → oznacz 'R' w CCM + zgłośRejected → postępuj jak w Stanie 30 (odczytaj kod ACK)brak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Dokument nie został dostarczony do CCTool, ACK nie napłynął. Minął czas CET. KRYTYCZNE — po CET dograć nie można.Postępowanie (KRYTYCZNE — brak naprawy):Telefon do RCC + zgłoś (priorytet P1)Po CET — brak naprawy. Diagnoza przyczyn: ZP · Connector 2.0 · Core CC Tool szczegóły w bazie ryzyk



##### Initial Intraday ATCs FID3-882

Kod: FID3-882

Profil: MIN

TET: 08:30

CET: 08:50

Źródło: proces Core

Wersja: 1

Initial Intraday ATCs (FID3-882) — początkowe wartości ATC dla intraday; wejście walidacji ATC. Składowa paczki.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial Intraday ATCs FID3-882

Kod: FID3-882

Profil: MIN

TET: 08:30

CET: 08:50

Źródło: proces Core

Wersja: 1

Initial Intraday ATCs (FID3-882) — początkowe wartości ATC dla intraday; wejście walidacji ATC. Składowa paczki.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Initial Intraday ATCs FID3-882

Kod: FID3-882

Profil: MIN

TET: 08:30

CET: 08:50

Źródło: proces Core

Wersja: 1

Initial Intraday ATCs (FID3-882) — początkowe wartości ATC dla intraday; wejście walidacji ATC. Składowa paczki.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Final Intraday NTC FID3-921

Kod: FID3-921

Profil: SFTP

TET: 09:20

CET: 09:45

Źródło: proces Core

Wersja: 1

Final Intraday NTC (FID3-921) — finalne wyniki NTC (Net Transfer Capacity) z procesu IDCC; zdolności przesyłowe udostępniane na rynek intraday (XBID).

**Ścieżka:**

proces Core / Kreator →

sFTP@pse.pl

/ ZP

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjnesFTP/ZP wysł.Plik dostarczony prawidłowo na sFTP/ZP — status pozytywny.Brak działań — proces poprawny.sFTP/ZP wysł.Status nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.sFTP/ZP wysł.Plik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.sFTP/ZP wysł.Przedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.sFTP/ZP wysł.Oczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź sFTP/ZP. Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się TET — pliku jeszcze nie ma na sFTP/ZP.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się CET / błąd dostarczenia — brak pliku na sFTP/ZP.Gdy pliku NIE ma na sFTP/ZP → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Minął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### ATC Based Validation FID3-928

Kod: FID3-928

Profil: 2CCT

TET: 08:45

CET: 09:20

Źródło: Core CC Tool

Wersja: 1

ATC Based Validation (FID3-928) — plik ZWROTNY: wynik walidacji ATC prowadzonej centralnie w Core CC Tool (strumień odrębny od FBA). NIE jest wysyłany przez TSO; publikowany CCCt → TSO przez Connector 2.0.

**Ścieżka:**

Paczka ATC (PERUN_IDx_ATC) →

Core CC Tool

(walidacja ATC) →

Connector 2.0

→

CCM

Warianty stanów (18)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.Przedwczesne (>30 min do TET). Walidacja ATC jeszcze nie ukończona.Monitoring — sprawdź w aplikacji CCM postęp walidacji paczki PERUN_IDx_ATC.CCtool wysł.CCtool zwalid.Zbliża się TET, brak FIDx-928. Walidacja paczki ATC w toku.Postępowanie:Rozwiń agregat PERUN_IDx_ATC → zweryfikuj składoweJeżeli:brak składowej → uzupełnij brakującą składową w aplikacji CCM ()składowe OK → monitoruj — czekaj na wynik walidacjiCCtool wysł.CCtool zwalid.Zbliża się CET — brak wyniku walidacji ATC. Stan alarmowy.Postępowanie (zbliża się CET):Ostatnia szansa: dokończ uzupełnienia paczki ATC w CCM; sprawdź Core CC Tool (Message Viewer)Jeżeli:plik dotrze → OK — koniecbłąd → odczytaj kod ACK (patrz powiązany stan)brak → zgłośCCtool wysł.CCtool zwalid.Minął CET, brak FIDx-928. KRYTYCZNE — brak lokalnego fallbacku.Postępowanie (KRYTYCZNE — minął CET):⛔ STOP — żadnych działań ręcznych. Brak lokalnego fallbacku (brak wyniku ATC w czasie → Dyspozytor nie wykonuje dalszych czynności).Zgłoś + telefon do RCC szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Happy Day — walidacja ATC zakończona poprawnie, wynik opublikowany.Brak interwencji — walidacja ATC zakończona poprawnie.CCtool wysł.CCtool zwalid.Wynik dotarł, ale ACK negatywny (Rejected).Postępowanie:Core CC Tool (Message Viewer) → odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś (administrator Core CC Tool otwiera bramkę)kod 21 (błąd procesowy CCCt) → zgłoś — błąd procesu w Core CC Toolkod 30 (rozmiar niezgodny) → patrz stan rozmiarCCtool wysł.CCtool zwalid.Wynik dotarł, ACK nie napłynął w czasie (timeout).Postępowanie:Czekaj 5 min → Core CC Tool (Message Viewer)Jeżeli:Processed → oznacz 'R' w CCMbrak >10 min → zgłoś — sprawdź transport zwrotny Connector 2.0 (R18)CCtool wysł.CCtool zwalid.Wynik dotarł, brak ACK do CET.Postępowanie:Sprawdź transport zwrotny Connector 2.0Jeżeli:transport OK, ACK błąd → odczytaj kod ACK (patrz powiązany stan)awaria transportu → zgłoś (R18)CCtool wysł.CCtool zwalid.Wynik dotarł, ACK napłynął po CET — pozytywny.Walidacja opóźniona, ale OK (ACK po CET pozytywny).CCtool wysł.CCtool zwalid.Status nadany ręcznie 'R' (nietypowe dla pliku zwrotnego).Brak działań — status nadany ręcznie przez Dyspozytora (nietypowe dla pliku zwrotnego).CCtool wysł.CCtool zwalid.Niepoprawny rozmiar wyniku FIDx-928.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → sprawdź rozmiar (pobranie ponownie nie ma sensu — plik zwrotny)Jeżeli:zawartość OK mimo rozmiaru → oznacz 'R' w CCMzawartość niepoprawna → zgłoś + telefon do RCCCCtool wysł.CCtool zwalid.Niepoprawny rozmiar + brak ACK (timeout).Postępowanie:Core CC Tool (Message Viewer) → sprawdź statusJeżeli:Processed → oznacz 'R' w CCMbrak → zgłoś + telefon do RCCCCtool wysł.CCtool zwalid.Niepoprawny rozmiar + ACK negatywny.Postępowanie:Core CC Tool (Message Viewer) → odczytaj kod ACKJeżeli:kod 20 (bramka zamknięta) → zgłoś (administrator Core CC Tool)kod 30 (rozmiar) → patrz powiązany staninny → zgłoś + telefon do RCCCCtool wysł.CCtool zwalid.Niepoprawny rozmiar + brak ACK do CET. KRYTYCZNE.Postępowanie (KRYTYCZNE):⛔ Krytyczne — minął CET, niepoprawny rozmiar i brak ACK.Zgłoś + telefon do RCC szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.FIDx-928 dostarczony po CET — walidacja OK.Walidacja zakończona po terminie — OK.CCtool wysł.CCtool zwalid.Wysyłka zwrotna trwa (transport Connector 2.0).Postępowanie:Czekaj 5 min (transport zwrotny Connector 2.0)Jeżeli:zmieniło się na zielony → OK — koniecbrak >10 min → zgłoś (R18)CCtool wysł.CCtool zwalid.Status ręczny przyznany (nietypowe dla pliku zwrotnego).Brak działań — status ręczny przyznany przez Dyspozytora (nietypowe dla pliku zwrotnego).CCtool wysł.CCtool zwalid.TET zbliża się, ACK błąd już teraz (błąd paczki ATC).Postępowanie:Core CC Tool (Message Viewer) → odczytaj błąd paczki ATCJeżeli:błąd składowej → uzupełnij składową w aplikacji CCMinny → odczytaj kod ACK (patrz powiązany stan)



##### AGR Paczka ZIP ID3 do Perun PERUN_ID3

Kod: PERUN_ID3

Profil: 2MS

TET: 08:30

CET: 09:05

Źródło: agregacja

Wersja: 1

AGR Paczka ZIP (PERUN_ID3) — zagregowana paczka wejściowa do Perun4V (proces FBA); zawiera składowe: scalone GLSK, CGM, RefProg, początkową domenę FB, CB, wierzchołki, RA.

**Ścieżka:**

Agregacja składowych →

MinIO

sFTP@pse.pl

→

Perun4V

Warianty stanów (10)

Status kafelkaSytuacjaDziałania awaryjneMinIOsFTP/ZP wysł.Paczka dostarczona prawidłowo na MinIO i sFTP/ZP.Brak działań — proces poprawny.MinIOsFTP/ZP wysł.Status nadany ręcznie 'R' po weryfikacji.Brak działań — decyzja ręczna.MinIOsFTP/ZP wysł.Paczka dostarczona po CET — status pozytywny.Brak działań — po CET OK.MinIOsFTP/ZP wysł.Przedwczesne — paczka jeszcze niewymagana.Monitoring — czekaj do TET.MinIOsFTP/ZP wysł.Zbliża się TET — paczka niekompletna / brak.Sprawdź agregację składowych. Gdy brak → zagreguj/pobierz ręcznie i wrzuć (Manual Upload / wysyłka na sFTP).MinIOsFTP/ZP wysł.Na MinIO OK, brak / błąd na sFTP/ZP.Gdy brak na sFTP → wyślij plik ręcznie ze źródła na sFTP/ZP.MinIOsFTP/ZP wysł.Brak / błąd na MinIO, OK na sFTP/ZP.Gdy brak na MinIO → pobierz/wygeneruj ręcznie i wgraj przez Manual Upload (GUI Core CC Tool).MinIOsFTP/ZP wysł.Transfer w toku (MinIO i sFTP/ZP).Czekaj 5 min → sprawdź MinIO i sFTP. Gdy brak → ręcznie (Manual Upload / wysyłka na sFTP).MinIOsFTP/ZP wysł.Zbliża się CET — brak / błąd na MinIO i sFTP/ZP.Gdy brak na MinIO → Manual Upload; gdy brak na sFTP → wyślij ręcznie.MinIOsFTP/ZP wysł.Minął CET — paczka niedostarczona. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Postępowanie krytyczne.



##### AGR Paczka ZIP_ATC ID3 do Perun PERUN_ID3_ATC

Kod: PERUN_ID3_ATC

Profil: 2MS

TET: 08:30

CET: 09:05

Źródło: agregacja

Wersja: 1

AGR Paczka ZIP_ATC (PERUN_ID3_ATC) — paczka wejściowa dla odrębnej ścieżki walidacji domeny ATC.

**Ścieżka:**

Agregacja składowych →

MinIO

sFTP@pse.pl

→

Perun4V

Warianty stanów (10)

Status kafelkaSytuacjaDziałania awaryjneMinIOsFTP/ZP wysł.Paczka dostarczona prawidłowo na MinIO i sFTP/ZP.Brak działań — proces poprawny.MinIOsFTP/ZP wysł.Status nadany ręcznie 'R' po weryfikacji.Brak działań — decyzja ręczna.MinIOsFTP/ZP wysł.Paczka dostarczona po CET — status pozytywny.Brak działań — po CET OK.MinIOsFTP/ZP wysł.Przedwczesne — paczka jeszcze niewymagana.Monitoring — czekaj do TET.MinIOsFTP/ZP wysł.Zbliża się TET — paczka niekompletna / brak.Sprawdź agregację składowych. Gdy brak → zagreguj/pobierz ręcznie i wrzuć (Manual Upload / wysyłka na sFTP).MinIOsFTP/ZP wysł.Na MinIO OK, brak / błąd na sFTP/ZP.Gdy brak na sFTP → wyślij plik ręcznie ze źródła na sFTP/ZP.MinIOsFTP/ZP wysł.Brak / błąd na MinIO, OK na sFTP/ZP.Gdy brak na MinIO → pobierz/wygeneruj ręcznie i wgraj przez Manual Upload (GUI Core CC Tool).MinIOsFTP/ZP wysł.Transfer w toku (MinIO i sFTP/ZP).Czekaj 5 min → sprawdź MinIO i sFTP. Gdy brak → ręcznie (Manual Upload / wysyłka na sFTP).MinIOsFTP/ZP wysł.Zbliża się CET — brak / błąd na MinIO i sFTP/ZP.Gdy brak na MinIO → Manual Upload; gdy brak na sFTP → wyślij ręcznie.MinIOsFTP/ZP wysł.Minął CET — paczka niedostarczona. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Postępowanie krytyczne.



##### Raporty ID3 z Perun RAP_PERUN_ID3

Kod: RAP_PERUN_ID3

Profil: SFTP

TET: 08:50

CET: 09:20

Źródło: Perun4V

Wersja: 1

Raporty z Perun (RAP_PERUN_ID3) — raporty walidacyjne z procesu Perun4V (charakter informacyjny).

**Ścieżka:**

Perun4V

→

kdm6@pse.pl

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjnesFTP/ZP wysł.Plik dostarczony prawidłowo na sFTP/ZP — status pozytywny.Brak działań — proces poprawny.sFTP/ZP wysł.Status nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.sFTP/ZP wysł.Plik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.sFTP/ZP wysł.Przedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.sFTP/ZP wysł.Oczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź sFTP/ZP. Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się TET — pliku jeszcze nie ma na sFTP/ZP.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się CET / błąd dostarczenia — brak pliku na sFTP/ZP.Gdy pliku NIE ma na sFTP/ZP → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Minął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Raporty ID3 ATC z Perun RAP_PERUN_ID3_ATC

Kod: RAP_PERUN_ID3_ATC

Profil: SFTP

TET: 08:50

CET: 09:20

Źródło: Perun4V

Wersja: 1

Raporty z Perun (RAP_PERUN_ID3_ATC) — raporty walidacyjne z procesu Perun4V (charakter informacyjny).

**Ścieżka:**

Perun4V

→

kdm6@pse.pl

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjnesFTP/ZP wysł.Plik dostarczony prawidłowo na sFTP/ZP — status pozytywny.Brak działań — proces poprawny.sFTP/ZP wysł.Status nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.sFTP/ZP wysł.Plik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.sFTP/ZP wysł.Przedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.sFTP/ZP wysł.Oczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź sFTP/ZP. Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się TET — pliku jeszcze nie ma na sFTP/ZP.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Zbliża się CET / błąd dostarczenia — brak pliku na sFTP/ZP.Gdy pliku NIE ma na sFTP/ZP → wyślij plik ręcznie ze źródła na sFTP/ZP.sFTP/ZP wysł.Minął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Plik ze środkami zaradczymi z aplikacji KreatorDACF_CGMES XID3_RA

Kod: XID3_RA

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: KreatorIDCF_CGMES

Wersja: 3

Plik ze środkami zaradczymi (RA, XID3_RA) — remedial actions wygenerowane w Kreatorze; publikowane razem z GLSK/CBCORA i jako składowa paczki.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



##### Plik ze środkami zaradczymi z aplikacji KreatorDACF_CGMES XID3_RA

Kod: XID3_RA

Profil: MIN

TET: 08:30

CET: 09:05

Źródło: KreatorIDCF_CGMES

Wersja: 3

Plik ze środkami zaradczymi (RA, XID3_RA) — remedial actions wygenerowane w Kreatorze; publikowane razem z GLSK/CBCORA i jako składowa paczki.

**Ścieżka:**

proces Core / Kreator → paczka PERUN →

MinIO

Warianty stanów (8)

Status kafelkaSytuacjaDziałania awaryjneMinIOPlik dostarczony prawidłowo na MinIO — status pozytywny.Brak działań — proces poprawny.MinIOStatus nadany ręcznie literą 'R' przez Dyspozytora po weryfikacji.Brak działań — decyzja ręczna Dyspozytora.MinIOPlik dostarczony po CET — status pozytywny.Brak działań — dostarczone po CET, OK.MinIOPrzedwczesne (>30 min do TET) — plik jeszcze niewymagany.Monitoring — czekaj do TET.MinIOOczekiwanie / transfer w toku (stan przejściowy).Czekaj 5 min → sprawdź MinIO. Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się TET — pliku jeszcze nie ma na MinIO.Sprawdź źródło (Kreator / Perun4V / Core CC Tool). Gdy brak → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOZbliża się CET / błąd dostarczenia — brak pliku na MinIO.Gdy pliku NIE ma na MinIO → pobierz/wygeneruj plik ręcznie ze źródła i wgraj przez Manual Upload (GUI Core CC Tool) / wyślij z CCM.MinIOMinął CET — plik niedostarczony. Krytyczne.Zgłoś (CIZ/WPO/PSE-I). Po CET — postępowanie krytyczne (brak lokalnego fallbacku).



#### IDA3 — 1 plików



##### AC FID2-831

Kod: FID2-831

Profil: 2CCT

TET: 09:45

CET: 09:55

Źródło: ZP

Wersja: 3

AC (Allocation Constraints, FID2-831) — plik z wartościami ograniczeń alokacyjnych wyznaczonych przez PSE, publikowany do PuTo i do procesu Core. Format XML, MTU 15 min.

**Ścieżka:**

ZP

→

Connector 2.0

→

Core CC Tool

→

PuTo

+

MinIO

Warianty stanów (32)

Status kafelkaSytuacjaDziałania awaryjneCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — proces poprawny.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool. Dyspozytor ustawił status ręcznie 'R' po weryfikacji w CCTool.Brak działań.CCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool po CET, ACK napłynął po CET z pozytywnym komunikatem.Brak działań — dostarczone po CET, OK.CCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool oraz otrzymanie potwierdzenia ACK.Brak działań.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem.Brak działań — wysyłka ręczna wykonana.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 5 minOK → ustaw 'R' w CCMCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, ale ACK nie napłynął w żądanym czasie i zbliża się CET.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM, a otrzymane ACK: (1) zawiera komunikat błędu (najedź kursorem); (2) proces zakończył się błędem — 'Błąd procesu'.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż zapisana) → podnieś numer wersji w aplikacji ZP i wyślij plik ponownie przez Core CC Tool (Manual Upload)kod 30 (rozmiar pliku niezgodny) → pobierz poprawny plik z MinIO lub aplikacji ZP i wyślij ponownieCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Otrzymano potwierdzenie ACK z pozytywnym komunikatem po CET.Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM. Nie otrzymano ACK, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — decyzja ręczna Dyspozytora.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — około 2 min.Postępowanie:Czekaj 2-5 minOK → ustaw 'R'CCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET. Trwa oczekiwanie na potwierdzenie ACK — upłynęło więcej niż 2 minuty.Postępowanie:Core CC Tool → sprawdź czy plik dotarł (Message Viewer)Jeżeli:OK → oznacz 'R' w CCMbłąd → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany ręcznie z poziomu CCM po CET, a otrzymane ACK: (1) komunikat błędu; (2) proces zakończył się błędem. Typowo kod 20 gateClosed.Postępowanie:Najedź kursorem na status i odczytaj kod ACK (typowo kod 20)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka jest zamknięta → zgłośinny kod → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Otrzymano potwierdzenie ACK z pozytywnym komunikatem (po CET).Brak działań — ręczna + ACK po CET, OK.CCtool wysł.CCtool zwalid.Dokument prawidłowo wysłany ręcznie z poziomu CCM po CET. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → oznacz 'R' w CCM + zgłośbrak / awaria zwrotna → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo do CCTool. Trwa oczekiwanie na ACK — około 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Trwa oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:Czekaj 5 minOK → 'R' dla ACKCCtool wysł.CCtool zwalid.Dokument oznaczony ręcznie jako wysłany prawidłowo. Nie otrzymano potwierdzenia ACK — upłynął czas CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:OK (Processed) → utrzymaj 'R'brak / awaria → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie otrzymano, Dyspozytor ustawił status 'R' po weryfikacji w CCTool.Brak działań — Dyspozytor zatwierdził zawartość.CCtool wysł.CCtool zwalid.Dokument jeszcze nie został wysłany do CCTool, ACK nie napłynął. Plik nie wymagany (>30 min do TET).Brak działań — czekaj do TET.CCtool wysł.CCtool zwalid.Zbliża się CET — plik niedostarczony lub błąd wysyłki. Stan alarmowy.Postępowanie (alarm):Core CC Tool → sprawdź czy plik dotarł do Core CC ToolJeżeli:plik jest, brak ACK → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykbrak pliku (awaria Connector 2.0) → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykbrak pliku w źródle → Brak pliku lub wersji w aplikacji źródłowej. Otwórz aplikacji ZP, przejdź do bilansu i sprawdź wersję pliku: jeśli wersja jest dostępna — pobierz ją (Pobierz XML); jeśli brakuje — wygeneruj nową wersję; jeśli aplikacja nie działa — zgłoś. pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. Oczekiwanie na ACK — upłynęło więcej niż 2 min.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → sprawdź rozmiar; pobierz z MinIO i rozpakujJeżeli:zawartość OK mimo rozmiaru → oznacz 'R' (→ powiązany stan)zawartość niepoprawna → Plik został odrzucony — odczytaj kod błędu z potwierdzenia ACK i zareaguj zależnie od kodu:kod 20 (bramka dla pliku zamknięta) — zgłoś administratorowi Core CC Toolkod 21 (wersja nie jest wyższa niż już zapisana) — w źródle podnieś numer wersji i wyślij plik ponowniekod 30 (rozmiar pliku niezgodny) — pobierz poprawny plik i wyślij ponownie pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru, a ACK ma status czerwony — typowo kod 30.Postępowanie:W aplikacji CCM kliknij plik lewym przyciskiem myszy → Informacje → potwierdź rozmiarPobierz poprawny plik z aplikacji ZP (Pobierz XML) i wyślij przez Core CC Tool (Manual Upload) z kolejnym numerem wersjiNadal za mały → zgłoś szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK napłynął po CET z pozytywnym komunikatem. Sprzeczność.Postępowanie:Pobierz z MinIO → rozpakuj → sprawdź zawartośćJeżeli:zawartość OK → oznacz 'R' (→ powiązany stan); zgłośniepoprawna → zgłośCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo do CCTool, ale ACK negatywny (Rejected). Kody: 20/21/30.Postępowanie:Najedź kursorem na status i odczytaj kod ACKJeżeli:kod 20 (bramka dla pliku zamknięta) → zgłoś (administrator Core CC Tool otwiera bramkę); sprawdź proces IDx-AC-FORWARDINGkod 21 (wersja nie jest wyższa niż zapisana) → podnieś numer wersji w aplikacji ZP i wyślij plik ponownie przez Core CC Tool (Manual Upload)kod 30 (rozmiar pliku niezgodny) → pobierz poprawny plik z MinIO lub aplikacji ZP i wyślij ponownieCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, trwa oczekiwanie na ACK, który nie napłynął w zadanym czasie (>2-3 min).Postępowanie:Czekaj 5 min → Core CC Tool (⚠ nie wysyłaj ponownie!)Jeżeli:Processed → oznacz 'R' + zgłośRejected → patrz stan kod ACKbrak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzykCCtool wysł.CCtool zwalid.Dokument wysłany prawidłowo, ACK nie napłynął do CET.Postępowanie:Core CC Tool → sprawdź statusJeżeli:Processed → oznacz 'R' + zgłoś (→ powiązany stan)Rejected → wyślij ponownie przez Core CC Tool (Manual Upload) "po CET"brak → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Wysłany dokument nie spełnia kryterium rozmiaru. ACK nie napłynął do CET. Krytyczne.Postępowanie (KRYTYCZNE w C):Pobierz poprawny plik z aplikacji ZP i wyślij przez Core CC Tool (Manual Upload) "po CET" (jeśli bramka otwarta)Natychmiast: zgłoś + powiadom RCC szczegóły w bazie ryzykCCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale walidacja zakończona negatywnie — ACK Rejected po CET.Postępowanie (po CET):Najedź kursorem na status i odczytaj kod ACK (kontekst: rejestracja po CET)Jeżeli:kod 20 (bramka dla pliku zamknięta) → po CET bramka zamknięta → zgłoś + powiadom RCCkod 21 (wersja nie jest wyższa niż zapisana) → podnieś numer wersji w aplikacji ZP i wyślij plik ponownie przez Core CC Tool (Manual Upload) (jeśli bramka otwarta)kod 30 (rozmiar pliku niezgodny) → pobierz poprawny plik z MinIO lub aplikacji ZP i wyślij ponownie (jeśli bramka otwarta)CCtool wysł.CCtool zwalid.Dokument zarejestrowany w CCTool po CET (wysyłka pozytywna), ale ACK walidacji nie napłynął — plik dostarczony, lecz niezwalidowany.Postępowanie (po CET):Core CC Tool → sprawdź status walidacji (plik dostarczony po CET)Jeżeli:Processed → oznacz 'R' w CCM + zgłośRejected → postępuj jak w Stanie 30 (odczytaj kod ACK)brak wpisu → Awaria transportu plików (Connector 2.0). Zgłoś awarię. W międzyczasie pobierz plik ze źródła (aplikacji ZP) i wyślij go ręcznie przez Core CC Tool (Manual Upload). pełny opis w bazie ryzyk + powiadom RCCCCtool wysł.CCtool zwalid.Dokument nie został dostarczony do CCTool, ACK nie napłynął. Minął czas CET. KRYTYCZNE — po CET dograć nie można.Postępowanie (KRYTYCZNE — brak naprawy):Telefon do RCC + zgłoś (priorytet P1)Po CET — brak naprawy. Diagnoza przyczyn: ZP · Connector 2.0 · Core CC Tool szczegóły w bazie ryzyk



### 5Czynności w CCM (C.1–C.5)

**Skrót / powiązane**

▸ legenda

▸ procedury awaryjne

Pulpit dyspozytorski CCM (

`ccm.spsm.pse.pl`

) — główne miejsce monitorowania statusów wszystkich plików IDCC i ręcznej interwencji.

Główny pulpit IDCC — pełna lista plików FIDx procesu z czasami granicznymi i kolumnami statusów wysyłki/walidacji.

**Otwarcie właściwego pulpitu i wybór doby**

Zaloguj się do CCM. Wybierz pulpit „IDCC FB Pulpit dyspozytorski” lub „IDCC (do 3C) z ATC i SFTP”. Z kalendarza ustaw dobę monitorowaną. Ustaw tryb odświeżania (ultraszybki 10 s / szybki 30 s / wolny 5 min).

Lista dostępnych pulpitów dyspozytorskich w CCM — wybór pulpitu DACC FB lub IDCC.

Wybór doby handlowej z kalendarza (przykład: 9 września 2025).

Wybór trybu automatycznego odświeżania pulpitu (10 s / 30 s / 5 min).

**Identyfikacja wiersza, kolumny i kafelka**

Odszukaj wiersz pliku (FIDx-…) i kolumnę kanału (CCTool wysł. / CCTool zwalid. / MinIO / sFTP/ZP). Kolor i znacznik kafelka = aktualny status (patrz legenda).

Pulpit 'IDCC (do 3C) z ATC i SFTP' z trzema kartami przeglądarki i kafelkami statusów plików FIDx.

**Wyświetlenie informacji o pliku**

PPM na kafelku → „Informacje”. Popup pokazuje opis pliku, ścieżkę, TET/CET, kod ACK i ewentualny błąd walidacji.

Menu kontekstowe PPM: status ręczny, informacje, pobierz, wyślij

Popup Informacje FID2-665 - błąd: za mały rozmiar pliku

**Wysłanie pliku przed Critical End Time**

PPM na kafelku → „Wyślij” (lub „Wyślij do CCTool”). Wskaż plik, potwierdź. Obserwuj postęp do komunikatu „Plik wysłany”.

Okno wysyłania pliku FID2-657 (puste)

Okno wysyłania z wybranym plikiem FID2-657

Plik FID2-657 wysłany pomyślnie

**Wysłanie pliku po Critical End Time / status ręczny**

Po CET użyj „Wyślij po CET”. Status ręczny: PPM → „Status ręczny” → wybór (Nowa wersja / Tylko zmiana statusu); cofnięcie przez „Przywróć poprzedni status”.

Popup statusu ręcznego - wariant Nowa wersja

Popup statusu ręcznego - wariant Tylko zmiana statusu

Popup przywrócenia poprzedniego statusu

**Najczęstsze błędy walidacji:**

„Za mały rozmiar pliku!” (rozmiar poniżej progu MinIO), kod 39 (zły FID w nazwie), kod 40 (zła data w nazwie), blokada wersji backup („wersja musi być wyższa od docelowej”).

Pulpit CCM — pełna galeria (89 ekranów + 42 ikon)

Elementy interfejsu (ikony i przyciski, rozmiar rzeczywisty):



### 6Walidacja domeny FBA — tryb normalny (NOR)

**Skrót / powiązane**

▸ tryb backup

▸ Perun4V

Tryb normalny Day-Ahead: schemat decyzyjny walidacji domeny DA/LTA, obliczenia w Perun4V, raporty CNEC i redukcji LTA.

Walidacja NOR — pełna galeria (18 ekranów)



### 7Walidacja domeny FBA — tryb backup (BUP)

**Skrót / powiązane**

▸ tryb normalny

▸ P01–P06

Tryb backup Day-Ahead: generowanie wierzchołków zapasowym narzędziem CCA (F320), paczki ZIP_CCA/ZIP_LTA, estymacja rezerwy w Perun, redukcja IVA, import RLTA do ZP.

Walidacja BUP — pełna galeria (90 ekranów + 4 ikon)

Elementy interfejsu (ikony i przyciski, rozmiar rzeczywisty):



### 8GLSK (FIDx-607) — katalog stanów

**Skrót / powiązane**

▸ legenda

▸ publikacja GLSK

Plik GLSK (Generation Load Shift Keys, FIDx-607) — 32 udokumentowane stany kafelka (para lewy×prawy kanał): sukces, przetwarzanie, oczekiwanie, błędy oraz wysyłka ręczna.

GLSK 607 — stany kafelka — pełna galeria (32 ekranów)



### 9Kreator IDCF — publikacja RA / GLSK / CBCORA

**Skrót / powiązane**

▸ weryfikacja w CCM

▸ GLSK

KreatorIDCF_CGMES — publikacja środków zaradczych RA oraz plików GLSK/CBCORA przez Connector → MinIO, z weryfikacją w CCM.

1. Panel IDCF: GLSK / CBCORA / RA + „Publikuj Connector”

2. Wybór plików GLSK (.uct)

3. Wybór plików CBCORA (.epc)

4. Okno „Pliki do publikacji” — wersje

5. Postęp: wysyłka na MinIO + pakowanie ZIP

6. LOG: „Publikacja zakończona”

7. Monitor: statusy zadań (OK / BŁĄD)

8. Weryfikacja w pulpicie CCM (IDCC FB)



### 10AC w ZP (FIDx-831)

**Skrót / powiązane**

▸ plik FID2-831

▸ ZP

Plik AC (Allocation Constraints, FIDx-831) — ręczna obsługa w aplikacji ZP: tabela ograniczeń NTC/ATC, wersjonowanie, zatwierdzanie.

Dokument AC FID2-831 w ZP — tabela NTC (EXP 800 / IMP 700), wersja zatwierdzona

ZP — bilansowe ograniczenia alokacji (intraday): tabela ATC/AAC i panel dokumentów



### 11Procedury P01–P06

**Skrót / powiązane**

▸ ryzyka

▸ CCM

Pełne procedury reagujące na ryzyka oraz procedury narzędziowe krok po kroku.

4. Procedury

4.A. Procedury reagujące na ryzyka (P01–P06)

Pełne opisy: Karta_ryzyk_IDCC.md. Skrót poniżej.

— w odpowiedzi na

,

,

,

. Procedura:

.

— w odpowiedzi na

,

. Dotyczy FIDx-831. Procedura:

.

— w odpowiedzi na

. Procedura:

.

— w odpowiedzi na

,

. Procedura:

.

— dla składowych paczki (FIDx-610 Merged GLSK ≠ FIDx-607 raw GLSK).

— przy każdym ręcznym działaniu. Pola: data, iteracja, FID, stan przed/po, procedura, ryzyko, wersja, zgłoszenie, uwagi.

4.B. Procedury narzędziowe (krok po kroku)

Logowanie i nawigacja w CCM

Otwórz przeglądarkę → https://ccm.spsm.pse.pl
Zaloguj (na środowisku produkcyjnym proces automatyczny dla stanowiska dyspozytorskiego)
Lista pulpitów → kliknij ikonę oka 👁 obok wybranego pulpitu
Wybierz dobę biznesową (strzałki ← →) lub kliknij kalendarz 📅
Tryby odświeżania: ultraszybki (10s) / szybki (30s) / wolny (5 min, domyślny)

najedź na wiersz →

→ wskaż plik z dysku → potwierdź → kafelek →

→

po ACK

najedź →

→ wskaż plik → potwierdź

PPM na wierszu →

→ wybierz 'R' → zatwierdź

LPM na kolumnie statusu → menu →

→ rozmiar, lokalizacja MinIO, data dostarczenia

Logowanie i nawigacja w Core CC Tool

📖 BUP DA Ryzyko 2 (str. 17), Rys. 11–13

Otwórz przeglądarkę → URL CCCt (wewn.)
Zaloguj danymi dyspozytorskimi
Selektor procesu (obok niebieskiego pola u góry) → wybierz ID1 / ID2 / ID3C / ID3 (zamiast domyślnego DA)
Na niebieskim tle → wybierz Business Day
Process Instance (lewe menu) → wybierz dla daty (lub wyczyść filtry)
Message Viewer → pole Message Definition → wpisz np. FID1-831 → Apply
Sprawdź kolumnę Status: Processed / Rejected / brak wpisu
Pobranie pliku: strzałka w dół po prawej stronie wiersza
Manual Upload: przycisk Manual Upload → wskaż plik z dysku → Upload file → odśwież → Message Viewer

Logowanie i nawigacja w MinIO

📖 BUP DA Ryzyko 3 (str. 22)

Otwórz przeglądarkę → https://minio-gui.pse.pl
Zaloguj danymi dyspozytorskimi
Lewy panel → Buckets → wybierz bucket (perun, cca, mam)
Nawiguj do podfolderu (np. cca/ID_FBCC/in/yyyymmdd/)
Pobierz plik: ikona Download po prawej stronie wiersza pliku
Alternatywnie (z poziomu CCM): kafelek MinIO → LPM → Pobierz → wskaż katalog lokalny

Logowanie i nawigacja w ZP

📖 AC manuall ZP.docx

Otwórz aplikację ZP (zdolności przesyłowe) — desktop
Zaloguj danymi dyspozytorskimi
Główne okno → zakładka bilans AC
Górna część listy dokumentów → wybierz FID1-831 (lub odpowiedni FIDx-831 dla iteracji)
Pobranie pliku: kliknij Pobierz XML → plik zapisany lokalnie
Generowanie nowej wersji (gdy brak):
   - Wróć do okna bilans AC
   - Wybierz wersję
   - Kliknij niebieski przycisk Nowa wersja
   - Po wygenerowaniu wróć do kroku 5 (Pobierz XML)

Logowanie i nawigacja w Perun4V

📖 BUP DA Ryzyko 1 (str. 9), NOR DA §2.3.2.2

Otwórz przeglądarkę → https://lccv.tscnet.eu
Kliknij Local Login
Wpisz Username i Password → zaznacz Read and accept the TSCNET Policy → Login
Główne okno — lista obliczeń per data
Sprawdź dostarczającego (typowo sFTP@pse.pl)
Sprawdź status obliczeń: Calculating / Successful / ERR-I / Process failed
Wczytanie paczki: sekcja Select timestamp date → wybierz BD → przeciągnij plik ZIP na pole (lub kliknij i wybierz z dysku)
Uruchomienie obliczeń: kliknij przycisk uruchamiania
Status → Details — szczegóły per godzina, kolumna [Result]
Pobranie wyniku (F310/IVA): po zakończeniu obliczeń kliknij download



## 4. Procedury



### 4.A. Procedury reagujące na ryzyka (P01–P06)

Pełne opisy:

. Skrót poniżej.

**P01 — GUI CCCt Manual Upload**

— w odpowiedzi na

U03

,

U09

,

U10

,

U11

. Procedura:

4.B Logowanie i nawigacja w CCCt

.

**P02 — Pobranie z ZP → GUI CCCt**

— w odpowiedzi na

U03

,

U06

. Dotyczy FIDx-831. Procedura:

4.B Logowanie i nawigacja w ZP

.

**P03 — Ręczne uruchomienie obliczeń w Perun4V**

— w odpowiedzi na

U14

. Procedura:

4.B Logowanie i nawigacja w Perun4V

.

**P04 — Pobranie z MinIO → CCM Wyślij**

— w odpowiedzi na

U08

,

U09

. Procedura:

4.B Logowanie i nawigacja w MinIO

.

**P05 — Pobranie z CCCt Message Viewer → CCM Wyślij**

— dla składowych paczki (FIDx-610 Merged GLSK ≠ FIDx-607 raw GLSK).

**P06 — Wpis w karcie A.4**

— przy każdym ręcznym działaniu. Pola: data, iteracja, FID, stan przed/po, procedura, ryzyko, wersja, zgłoszenie, uwagi.



### 4.B. Procedury narzędziowe (krok po kroku)



#### Logowanie i nawigacja w CCM

Otwórz przeglądarkę → https://ccm.spsm.pse.pl

Zaloguj (na środowisku produkcyjnym proces automatyczny dla stanowiska dyspozytorskiego)

Lista pulpitów → kliknij ikonę oka 👁 obok wybranego pulpitu

Wybierz dobę biznesową (strzałki ← →) lub kliknij kalendarz 📅

Tryby odświeżania: ultraszybki (10s) / szybki (30s) / wolny (5 min, domyślny)

**Wysyłka pliku (przed CET):**

najedź na wiersz →

**PPM → Wyślij**

→ wskaż plik z dysku → potwierdź → kafelek →

`ciemnozielony W`

→

`zielony`

po ACK

**Wysyłka po CET:**

najedź →

**PPM → Wyślij po CET**

→ wskaż plik → potwierdź

**Ustaw status ręcznie 'R':**

PPM na wierszu →

**Ustaw status ręcznie**

→ wybierz 'R' → zatwierdź

*(❓ dokładna ścieżka — do weryfikacji w CCM Instrukcji Dyspozytora v2.6, rozdz. „Zmiana statusu dokumentu na wysłany ręcznie")*

**Informacje o pliku:**

LPM na kolumnie statusu → menu →

**Informacje**

→ rozmiar, lokalizacja MinIO, data dostarczenia



#### Logowanie i nawigacja w Core CC Tool

📖 BUP DA Ryzyko 2 (str. 17), Rys. 11–13

Otwórz przeglądarkę → URL CCCt (wewn.)

Zaloguj danymi dyspozytorskimi

(obok niebieskiego pola u góry) → wybierz

/

/

/

(zamiast domyślnego

)

Na niebieskim tle → wybierz

(lewe menu) → wybierz dla daty (lub wyczyść filtry)

→ pole

→ wpisz np.

→

Sprawdź

:

/

/ brak wpisu

strzałka w dół po prawej stronie wiersza

przycisk

→ wskaż plik z dysku →

→ odśwież → Message Viewer



#### Logowanie i nawigacja w MinIO

📖 BUP DA Ryzyko 3 (str. 22)

Otwórz przeglądarkę → https://minio-gui.pse.pl

Zaloguj danymi dyspozytorskimi

Lewy panel →

→ wybierz bucket (

,

,

)

Nawiguj do podfolderu (np.

)

ikona

po prawej stronie wiersza pliku

(z poziomu CCM): kafelek

→ LPM →

→ wskaż katalog lokalny



#### Logowanie i nawigacja w ZP

📖 AC manuall ZP.docx

Otwórz aplikację

(zdolności przesyłowe) — desktop

Zaloguj danymi dyspozytorskimi

→ zakładka

Górna część listy dokumentów → wybierz

(lub odpowiedni FIDx-831 dla iteracji)

kliknij

→ plik zapisany lokalnie

(gdy brak): - Wróć do okna

- Wybierz wersję - Kliknij niebieski przycisk

- Po wygenerowaniu wróć do kroku 5 (Pobierz XML)



#### Logowanie i nawigacja w Perun4V

📖 BUP DA Ryzyko 1 (str. 9), NOR DA §2.3.2.2

Otwórz przeglądarkę → https://lccv.tscnet.eu

Kliknij

Wpisz

i

→ zaznacz

→

— lista obliczeń per data

Sprawdź dostarczającego (typowo

)

Sprawdź status obliczeń:

/

/

/

sekcja

→ wybierz BD → przeciągnij plik ZIP na pole (lub kliknij i wybierz z dysku)

kliknij przycisk uruchamiania

— szczegóły per godzina, kolumna

(F310/IVA): po zakończeniu obliczeń kliknij download



### 12Ryzyka U01–U23 i kody ACK

**Skrót / powiązane**

▸ procedury

▸ zgłoszenia

3. Ryzyka uniwersalne U01–U23

Pełne karty ryzyk z opisami, objawami, działaniami i zgłoszeniem: patrz Karta_ryzyk_IDCC.md. Poniżej skrót + mapowanie do dokumentów źródłowych.

3.A. Grupa I — Dostępność narzędzi

- HTML §9: R06 | BUP DA: #27 (str. 69) | NOR DA: #27

- HTML §9: R07 | BUP DA: #11 (str. 47) | NOR DA: #11

—

- HTML §9: R09 + R16 | BUP DA: #1 (str. 9), #2 (str. 17), #10 (str. 46), #16 (str. 54), #24 | NOR DA: #2, #10, #16, #24

- BUP DA: #2 (częściowo), #24, #25 (str. 67) | NOR DA: #24, #25

- BUP DA: #4 (str. 26), #17 | NOR DA: #4, #17

- Nowe (zidentyfikowane w trakcie pracy); pokrywa ZP, Kreatory, CCA

- BUP DA: #25 (częściowo)

3.B. Grupa II — Plik i dostarczenie

- HTML §9: R04 | BUP DA: #3 (str. 22), #28 | Stany: czarny, czerwony, pomarańczowy

- HTML §9: R04 (rozszerzony) | ACK kod 30 (file size mismatch); „Message has some invalid timeSeries…"

- HTML §9: R05 | BUP DA: #13 (str. 49) | Kody ACK: 20 (gateClosed), 21 (duplicatedVersion), 22 (Negative — historyczny), 30 (size)

- HTML §9: R05 (zawężenie) | BUP DA: #12 (str. 48)

- ACK kod 21 (duplicatedVersion), kod 40 (Backup version lower)

- Stan: fioletowy; bez działań naprawczych poza

3.C. Grupa III — Proces obliczeniowy (Perun4V / IVA)

- HTML §9: R01 | BUP DA: #1 (str. 9)

- HTML §9: R02 | BUP DA: #6 (str. 29), #20

- HTML §9: R03 | BUP DA: #7 (str. 39), #21

3.D. Grupa IV — Strumień ATC

- HTML §9: R11 | Dotyczy: FIDx-928

3.E. Grupa V — Transport zwrotny

→ scalone z

- HTML §9: R12 | Dotyczy: FIDx-710 (3COL) vs FIDx-710 (MIN — IVA Backup)

3.F. Grupa VI — Zgłoszenie zewnętrzna

- HTML §9: R13 | Deadliny: 20:00 D-1 (IDCC(b)), 02:00 D (IDCC(c)), 07:00 D (IDCC(d))

- HTML §9: R14 | Plik: FID1-250 (Shadow Auction)

- HTML §9: R15 | Plik: FIDx-921

- HTML §9: R20 | BUP DA: #26 (str. 69) | Bucket:

3.G. Tabela kodów ACK (CCCt)

Kod
Treść
Działanie




0
Message fully accepted
OK


20
Gate for provided message definition is not opened
Bramka zamknięta — sprawdź TET/CET; CCCt IDx-AC-FORWARDING → admin CCCt + zgłoś


21
Provided version is not higher than already stored data (duplicatedVersion)
Podbić wersję; ponów P01


22
~~Delivered constraint value is negative~~
❌ Nieaktualny (CCCt akceptuje wartości ujemne)


30
File size mismatch
P04 lub P02; weryfikuj zawartość → P01


40
Backup version lower
NIE wysyłać backup z niższą wersją


41
Backup not available
→ U23


42
Backup validation failed
Raport CCA; zgłoś


—
Message has some invalid timeSeries that does not meet primary MTU rules
Poprawić strukturę pliku → P01


—
Błąd procesu
Proces CCCt zakończony błędem; zgłoś



## 3. Ryzyka uniwersalne U01–U23

Pełne karty ryzyk z opisami, objawami, działaniami i zgłoszeniem: patrz

. Poniżej

.



### 3.A. Grupa I — Dostępność narzędzi

**U01 — Brak dostępu do CCM**

*(CCM)*

- HTML §9: R06 | BUP DA: #27 (str. 69) | NOR DA: #27

**U02 — Brak dostępu do Core CC Tool**

*(Core CC Tool)*

- HTML §9: R07 | BUP DA: #11 (str. 47) | NOR DA: #11

**U03 — Brak dostępu / awaria Connector 2.0**

*(Connector 2.0)*

—

*obejmuje też scalone U18 (CN2 nie kopiuje do bucketów)*

- HTML §9: R09 + R16 | BUP DA: #1 (str. 9), #2 (str. 17), #10 (str. 46), #16 (str. 54), #24 | NOR DA: #2, #10, #16, #24

**U04 — Brak dostępu do MinIO**

*(MinIO)*

- BUP DA: #2 (częściowo), #24, #25 (str. 67) | NOR DA: #24, #25

**U05 — Brak dostępu do Perun4V**

*(Perun4V)*

- BUP DA: #4 (str. 26), #17 | NOR DA: #4, #17

**U06 — Brak dostępu do źródła pliku**

*(ZP, KreatorDACF&2DAF_CGMES, KreatorIDCF_CGMES, CCA)*

- Nowe (zidentyfikowane w trakcie pracy); pokrywa ZP, Kreatory, CCA

**U07 — Brak dostępu do poczty kdm6**

*(kdm6@pse.pl)*

- BUP DA: #25 (częściowo)



### 3.B. Grupa II — Plik i dostarczenie

**U08 — Plik niedostarczony w czasie**

- HTML §9: R04 | BUP DA: #3 (str. 22), #28 | Stany: czarny, czerwony, pomarańczowy

**U09 — Plik dostarczony, ale błędny (rozmiar / struktura)**

- HTML §9: R04 (rozszerzony) | ACK kod 30 (file size mismatch); „Message has some invalid timeSeries…"

**U10 — ACK negatywny (odrzucenie)**

- HTML §9: R05 | BUP DA: #13 (str. 49) | Kody ACK: 20 (gateClosed), 21 (duplicatedVersion), 22 (Negative — historyczny), 30 (size)

**U11 — Brak ACK (timeout)**

- HTML §9: R05 (zawężenie) | BUP DA: #12 (str. 48)

**U12 — Niezgodność wersji pliku**

- ACK kod 21 (duplicatedVersion), kod 40 (Backup version lower)

**U13 — Plik dostarczony po CET (informacyjne)**

- Stan: fioletowy; bez działań naprawczych poza

P06



### 3.C. Grupa III — Proces obliczeniowy (Perun4V / IVA)

**U14 — Brak uruchomienia obliczeń w Perun4V**

- HTML §9: R01 | BUP DA: #1 (str. 9)

**U15 — ERR-I (część TS niepoliczona)**

- HTML §9: R02 | BUP DA: #6 (str. 29), #20

**U16 — Process failed (wszystkie TS niepoliczone)**

- HTML §9: R03 | BUP DA: #7 (str. 39), #21



### 3.D. Grupa IV — Strumień ATC

**U17 — Niezakończenie walidacji ATC w czasie**

- HTML §9: R11 | Dotyczy: FIDx-928



### 3.E. Grupa V — Transport zwrotny

**~~U18~~**

→ scalone z

U03

**U19 — Niezgodność wersji IVA / IVA BACKUP**

- HTML §9: R12 | Dotyczy: FIDx-710 (3COL) vs FIDx-710 (MIN — IVA Backup)



### 3.F. Grupa VI — Zgłoszenie zewnętrzna

**U20 — AAC Fallback**

*(XBID)*

- HTML §9: R13 | Deadliny: 20:00 D-1 (IDCC(b)), 02:00 D (IDCC(c)), 07:00 D (IDCC(d))

**U21 — Decoupling SDAC — konieczność MD250**

*(ECP/EDX)*

- HTML §9: R14 | Plik: FID1-250 (Shadow Auction)

**U22 — Late NTC delivery po IDA2**

*(XBID)*

- HTML §9: R15 | Plik: FIDx-921

**U23 — Brak raportu CCA**

*(CCA)*

- HTML §9: R20 | BUP DA: #26 (str. 69) | Bucket:

`cca/ID_FBCC/out/[BD]/`



### 3.G. Tabela kodów ACK (CCCt)

| Kod | Treść | Działanie |
| --- | --- | --- | --- | --- |
| 0 | Message fully accepted | OK |
| 20 | Gate for provided message definition is not opened | Bramka zamknięta — sprawdź TET/CET; CCCt IDx-AC-FORWARDING → admin CCCt + zgłoś |
| 21 | Provided version is not higher than already stored data (duplicatedVersion) | Podbić wersję; ponów P01 |
| 22 | ~~Delivered constraint value is negative~~ | ❌ Nieaktualny (CCCt akceptuje wartości ujemne) |
| 30 | File size mismatch | P04 lub P02; weryfikuj zawartość → P01 |
| 40 | Backup version lower | NIE wysyłać backup z niższą wersją |
| 41 | Backup not available | → U23 |
| 42 | Backup validation failed | Raport CCA; zgłoś |
| — | Message has some invalid timeSeries that does not meet primary MTU rules | Poprawić strukturę pliku → P01 |
| — | Błąd procesu | Proces CCCt zakończony błędem; zgłoś |



### 13Buckety MinIO i mapa relacji

**Skrót / powiązane**

▸ pliki

▸ MinIO

5. Buckety MinIO

Bucket
Pełna ścieżka
Zawartość
Źródło




perun/
perun/DA_FBCC/in/yyyy-mm-dd/
Paczki wejściowe DA do Perun4V
BUP DA §6, NOR DA


perun/
perun/ID_FBCC/in/yyyy-mm-dd/
Paczki wejściowe IDCC do Perun4V
HTML §6


perun/
perun/DA_FBCC/out/yyyy-mm-dd/
Wyniki DA z Perun4V (IVA F310, raporty)
BUP DA


perun/
perun/ID_FBCC/out/yyyy-mm-dd/
Wyniki IDCC z Perun4V (IVA FIDx-710, raporty)
HTML §6


cca/
cca/DA_FBCC/out/[BD]/
IVA BACKUP + raporty CCA (DA)
BUP DA §6, HTML §6


cca/
cca/ID_FBCC/out/[BD]/
IVA BACKUP + raporty CCA (IDCC)
HTML §6, Aneks A.3


cca/
cca/ID_FBCC/in/yyyymmdd/yyyymmdd-FIDx-831-v*
Pliki AC (FIDx-831) — wejście CCA
uzgodnienie z użytkownikiem


mam/
(do uzupełnienia)
❓ — nieznana zawartość, do dopytania PSE Innowacje (TODO-5)
—

6. Mapa relacji

6.A. Macierz narzędzie × ryzyko

Narzędzie
Ryzyko gdy niedostępne
Ryzyko transportowe / procesowe
Zespół utrzymania




CCM
U01
—
zgłoś


Core CC Tool
U02
U10, U11, U12
RCC / TSCNET


Perun4V
U05
U14, U15, U16
RCC / TSCNET


MinIO
U04
—
zgłoś


Connector 2.0
U03
obejmuje też scalone U18
zgłoś


ZP
U06
—
zgłoś


KreatorDACF&2DAF_CGMES
U06
—
PLANS


CCA
—
U19, U23
zgłoś


PuTo
(pośrednio przez CCCt)
—
wewn. PSE


kdm6@pse.pl
U07
—
utrzymanie poczty PSE


sFTP@pse.pl
(część U03)
—
zgłoś


ECP/EDX
—
U21
TSCNET


XBID
—
U20, U22
zewn.

6.B. Macierz stan kafelka × procedura backupowa (skrót)

Stan kafelka (uniwersalny)
Typowe ryzyka
Sugerowana ścieżka




szary/szary (przed TET)
—
monitoring


pomarańczowy/* (TET zbliża się)
U03, U06, U08
CCCt MV → MinIO → źródło (ZP)


czerwony/* (CET zbliża się)
U03, U08, U10
P02/P04 → P01


czarny/czarny (po CET)
U03, U08
KRYTYCZNE — zgłoś + telefon RCC / TSCNET


zielony/czerwony (ACK Rejected)
U10
per kod ACK (20/21/30)


zielony/czerwony ? (timeout)
U11
CCCt MV → P01


zielony/zielony (Happy Day)
—
brak


czerwony ! / * (size mismatch)
U09
P04 / P02 → P01


ciemnozielony W / zielony
U03
P06 wpis A.4


fioletowy / fioletowy
U13
P06


zielony R / zielony R
U13
P06


red_pulse (IVA Backup)
U19
porównaj wersje IVA vs Backup



## 5. Buckety MinIO

| Bucket | Pełna ścieżka | Zawartość | Źródło |
| --- | --- | --- | --- | --- | --- |
| perun/ | perun/DA_FBCC/in/yyyy-mm-dd/ | Paczki wejściowe DA do Perun4V | BUP DA §6, NOR DA |
| perun/ | perun/ID_FBCC/in/yyyy-mm-dd/ | Paczki wejściowe IDCC do Perun4V | HTML §6 |
| perun/ | perun/DA_FBCC/out/yyyy-mm-dd/ | Wyniki DA z Perun4V (IVA F310, raporty) | BUP DA |
| perun/ | perun/ID_FBCC/out/yyyy-mm-dd/ | Wyniki IDCC z Perun4V (IVA FIDx-710, raporty) | HTML §6 |
| cca/ | cca/DA_FBCC/out/[BD]/ | IVA BACKUP + raporty CCA (DA) | BUP DA §6, HTML §6 |
| cca/ | cca/ID_FBCC/out/[BD]/ | IVA BACKUP + raporty CCA (IDCC) | HTML §6, Aneks A.3 |
| cca/ | cca/ID_FBCC/in/yyyymmdd/yyyymmdd-FIDx-831-v* | Pliki AC (FIDx-831) — wejście CCA | uzgodnienie z użytkownikiem |
| mam/ | (do uzupełnienia) | ❓ — nieznana zawartość, do dopytania PSE Innowacje (TODO-5) | — |

**Katalog sieciowy zapisu plików ręcznie pobranych z CCCt:**

`\\uo-data\ZUO\Pion_UOD\Wydzial_DP\MODELE\5_DYSP\FBA\Pliki wejściowe do DA FBA\rrrMMdd\PERUN\`

*(BUP DA)*

*(❓ analogiczna ścieżka dla IDCC — do weryfikacji)*



## 6. Mapa relacji



### 6.A. Macierz narzędzie × ryzyko

| Narzędzie | Ryzyko gdy niedostępne | Ryzyko transportowe / procesowe | Zespół utrzymania |
| --- | --- | --- | --- | --- | --- |
| CCM | U01 | — | zgłoś |
| Core CC Tool | U02 | U10, U11, U12 | RCC / TSCNET |
| Perun4V | U05 | U14, U15, U16 | RCC / TSCNET |
| MinIO | U04 | — | zgłoś |
| Connector 2.0 | U03 | obejmuje też scalone U18 | zgłoś |
| ZP | U06 | — | zgłoś |
| KreatorDACF&2DAF_CGMES | U06 | — | PLANS |
| CCA | — | U19, U23 | zgłoś |
| PuTo | (pośrednio przez CCCt) | — | wewn. PSE |
| kdm6@pse.pl | U07 | — | utrzymanie poczty PSE |
| sFTP@pse.pl | (część U03) | — | zgłoś |
| ECP/EDX | — | U21 | TSCNET |
| XBID | — | U20, U22 | zewn. |



### 6.B. Macierz stan kafelka × procedura backupowa (skrót)

| Stan kafelka (uniwersalny) | Typowe ryzyka | Sugerowana ścieżka |
| --- | --- | --- | --- | --- |
| szary/szary (przed TET) | — | monitoring |
| pomarańczowy/* (TET zbliża się) | U03, U06, U08 | CCCt MV → MinIO → źródło (ZP) |
| czerwony/* (CET zbliża się) | U03, U08, U10 | P02/P04 → P01 |
| czarny/czarny (po CET) | U03, U08 | KRYTYCZNE — zgłoś + telefon RCC / TSCNET |
| zielony/czerwony (ACK Rejected) | U10 | per kod ACK (20/21/30) |
| zielony/czerwony ? (timeout) | U11 | CCCt MV → P01 |
| zielony/zielony (Happy Day) | — | brak |
| czerwony ! / * (size mismatch) | U09 | P04 / P02 → P01 |
| ciemnozielony W / zielony | U03 | P06 wpis A.4 |
| fioletowy / fioletowy | U13 | P06 |
| zielony R / zielony R | U13 | P06 |
| red_pulse (IVA Backup) | U19 | porównaj wersje IVA vs Backup |


