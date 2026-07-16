# KARTY IDCC — szybkie kroki działania

Każdy krok linkuje do pełnej procedury `PROCEDURA_IDCC_TSO_v7-final.html`.

## 🟢 Start dyżuru

1. [Zaloguj się do CCM, otwórz pulpit IDCC i ustaw dobę](PROCEDURA_IDCC_TSO_v7-final.html#ccm-c1)
1. [Sprawdź bramki czasowe bieżącej iteracji](PROCEDURA_IDCC_TSO_v7-final.html#hlbp-zbiorcza)
1. [Przejdź checklistę przed iteracją](PROCEDURA_IDCC_TSO_v7-final.html#aneks)

## 👁 Monitorowanie IDCC(b)/(c)/(d)

1. [Wykonaj 6 kroków przebiegu nominalnego](PROCEDURA_IDCC_TSO_v7-final.html#hd-6krokow)
1. [Perun4V: sprawdź timestampy (0 Failed)](PROCEDURA_IDCC_TSO_v7-final.html#maski-perun)
1. [Oceń raport CCA z kdm6 (TS + zasadność IVA)](PROCEDURA_IDCC_TSO_v7-final.html#hd-6krokow)
1. [Rozpoznaj status kafelka wg legendy](PROCEDURA_IDCC_TSO_v7-final.html#sec-legenda)
1. [Sprawdź opis pliku i stany w katalogu](PROCEDURA_IDCC_TSO_v7-final.html#sec-katalog)

## 👁 Monitorowanie IDCC(a)

1. [Monitoruj FID1-928: v2 zielona po 13:15 D-1](PROCEDURA_IDCC_TSO_v7-final.html#hd-a)
1. [Brak v2 po 14:30 → MinIO cca/… → telefon do operatora procesu](PROCEDURA_IDCC_TSO_v7-final.html#hd-a)
1. [Pilnuj AC (FID1-831) z ZP i finalnych NTC (FID1-921)](PROCEDURA_IDCC_TSO_v7-final.html#aczp)
1. [Kroki PSE w iteracji (a) wg BPD](PROCEDURA_IDCC_TSO_v7-final.html#proc-a)

## 📤 Wysyłka ręczna i status R

1. [Wyślij plik przed CET: PPM → Wyślij](PROCEDURA_IDCC_TSO_v7-final.html#ccm-c4)
1. [Wyślij po CET: PPM → Wyślij po CET](PROCEDURA_IDCC_TSO_v7-final.html#ccm-c5)
1. [Ustaw / przywróć status ręczny R](PROCEDURA_IDCC_TSO_v7-final.html#ccm-c5)
1. [Sprawdź maskę pliku przed wysyłką](PROCEDURA_IDCC_TSO_v7-final.html#maski-iva)

## ⚠️ Kafelki alarmowe

1. [Czerwony „?" (brak ACK) → Message Viewer CCCt](PROCEDURA_IDCC_TSO_v7-final.html#R04)
1. [Czerwony „!" (za mały plik) → procedura B2](PROCEDURA_IDCC_TSO_v7-final.html#hd-b2)
1. [Czarny agregat (brak ZIP) → procedura B3](PROCEDURA_IDCC_TSO_v7-final.html#hd-b3)
1. [ACK Rejected → odczytaj kod (20/21/30)](PROCEDURA_IDCC_TSO_v7-final.html#ccm-ack)
1. [Scenariusze backupowe S.1–S.13](PROCEDURA_IDCC_TSO_v7-final.html#ccm-scen)

## 🧯 Walidacja — problemy

1. [ERR-I (część TS) → czekaj na IVA BACKUP v2+](PROCEDURA_IDCC_TSO_v7-final.html#hd-erri)
1. [Process failed (0 TS) → wyślij BACKUP v1](PROCEDURA_IDCC_TSO_v7-final.html#hd-pf)
1. [Brak SFTP >30 min → ręczna walidacja B1](PROCEDURA_IDCC_TSO_v7-final.html#hd-b1)
1. [Awaria ECP/EDX → Manual Upload IVA (B4)](PROCEDURA_IDCC_TSO_v7-final.html#hd-b4)
1. [Tryb backup BUP (paczka ręczna, F308)](PROCEDURA_IDCC_TSO_v7-final.html#wal-bup)

## 🛠 Awarie narzędzi

1. [Brak dostępu do CCM](PROCEDURA_IDCC_TSO_v7-final.html#R01)
1. [Brak dostępu do Core CC Tool](PROCEDURA_IDCC_TSO_v7-final.html#R03)
1. [Ręczny upload do CCCt (Manual Upload)](PROCEDURA_IDCC_TSO_v7-final.html#P01)
1. [Pobranie pliku ze źródła (aplikacja ZP)](PROCEDURA_IDCC_TSO_v7-final.html#P02)
1. [Ręczne uruchomienie obliczeń Perun4V](PROCEDURA_IDCC_TSO_v7-final.html#P03)
1. [Obsługa MinIO / Perun4V / CCCt — pełna instrukcja](PROCEDURA_IDCC_TSO_v7-final.html#sec-ops)

## 📦 Dane wejściowe PSE

1. [Dostarcz IGM do RCC (DACF/IDCF)](PROCEDURA_IDCC_TSO_v7-final.html#s4a)
1. [TSO Data Gathering — komplet plików](PROCEDURA_IDCC_TSO_v7-final.html#s4b)
1. [Wygeneruj i wyślij CB (FIDx-617)](PROCEDURA_IDCC_TSO_v7-final.html#s4c)
1. [Wygeneruj i wyślij GLSK (FIDx-607)](PROCEDURA_IDCC_TSO_v7-final.html#s4d)
1. [Publikacja z Kreatora IDCF (GLSK/CBCORA/RA)](PROCEDURA_IDCC_TSO_v7-final.html#sec-kreator)

## 📣 Komunikacja i reakcja

1. [Wybierz właściwy szablon maila Core ID](PROCEDURA_IDCC_TSO_v7-final.html#proc-mail)
1. [Telefony i adresy: CCC / USY / kdm6](PROCEDURA_IDCC_TSO_v7-final.html#kontakty)
1. [Znajdź ryzyko i skrót działania (R01–R29)](PROCEDURA_IDCC_TSO_v7-final.html#sec-ryzyka)
1. [Automatyczne fallbacki i działania backupowe iteracji (b)–(d)](PROCEDURA_IDCC_TSO_v7-final.html#proc-bcd)
