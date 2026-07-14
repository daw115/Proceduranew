# Stickery IDCC — wkład (karty skrócone z hiperłączami)

Hiperłącza prowadzą do kotwic dokumentu `PROCEDURA_IDCC_TSO_v6.html`. Format: tytuł, skrót 1–3 zdania, linki.

## 📘 Proces IDCC

Kroki istotne dla PSE: IDCC(a) i wspólnie (b)–(d), pliki FIDx, fallbacki.

- **Pełna instrukcja:** [PROCEDURA_IDCC_TSO_v6.html#sec-proces](PROCEDURA_IDCC_TSO_v6.html#sec-proces)
- Powiązane — katalog plików: [PROCEDURA_IDCC_TSO_v6.html#sec-katalog](PROCEDURA_IDCC_TSO_v6.html#sec-katalog)
- Powiązane — statusy: [PROCEDURA_IDCC_TSO_v6.html#sec-legenda](PROCEDURA_IDCC_TSO_v6.html#sec-legenda)

## 📧 Szablony maili

19 szablonów operacyjnych Core ID (EN) + kiedy użyć; oznaczone granice PSE.

- **Pełna instrukcja:** [PROCEDURA_IDCC_TSO_v6.html#proc-mail](PROCEDURA_IDCC_TSO_v6.html#proc-mail)

## 🧰 Narzędzia

CCM, Core CC Tool, Perun4V, MinIO, ZP, Connector, Kreatory, sFTP, wsparcie.

- **Pełna instrukcja:** [PROCEDURA_IDCC_TSO_v6.html#sec-narzedzia](PROCEDURA_IDCC_TSO_v6.html#sec-narzedzia)
- Powiązane — procedury: [PROCEDURA_IDCC_TSO_v6.html#sec-procedury](PROCEDURA_IDCC_TSO_v6.html#sec-procedury)
- Powiązane — ryzyka: [PROCEDURA_IDCC_TSO_v6.html#sec-ryzyka](PROCEDURA_IDCC_TSO_v6.html#sec-ryzyka)

## 🎨 Legenda statusów

13 kafelków → enum statusu. Kolor + znacznik = sytuacja pliku.

- **Pełna instrukcja:** [PROCEDURA_IDCC_TSO_v6.html#sec-legenda](PROCEDURA_IDCC_TSO_v6.html#sec-legenda)
- Powiązane — czynności w CCM: [PROCEDURA_IDCC_TSO_v6.html#sec-ccm](PROCEDURA_IDCC_TSO_v6.html#sec-ccm)
- Powiązane — stany plików: [PROCEDURA_IDCC_TSO_v6.html#sec-katalog](PROCEDURA_IDCC_TSO_v6.html#sec-katalog)

## 🗂️ Katalog plików FIDx

126 plików: opis, ścieżka, źródło, TET/CET, profil + warianty stanów.

- **Pełna instrukcja:** [PROCEDURA_IDCC_TSO_v6.html#sec-katalog](PROCEDURA_IDCC_TSO_v6.html#sec-katalog)
- Powiązane — legenda: [PROCEDURA_IDCC_TSO_v6.html#sec-legenda](PROCEDURA_IDCC_TSO_v6.html#sec-legenda)
- Powiązane — obsługa w CCM: [PROCEDURA_IDCC_TSO_v6.html#sec-ccm](PROCEDURA_IDCC_TSO_v6.html#sec-ccm)

## 🖥️ Czynności w CCM

C.1–C.5: pulpit, info, wysyłka przed/po CET, status ręczny, błędy walidacji.

- **Pełna instrukcja:** [PROCEDURA_IDCC_TSO_v6.html#sec-ccm](PROCEDURA_IDCC_TSO_v6.html#sec-ccm)
- Powiązane — legenda: [PROCEDURA_IDCC_TSO_v6.html#sec-legenda](PROCEDURA_IDCC_TSO_v6.html#sec-legenda)
- Powiązane — procedury awaryjne: [PROCEDURA_IDCC_TSO_v6.html#sec-procedury](PROCEDURA_IDCC_TSO_v6.html#sec-procedury)

## ✅ Walidacja domeny — NOR

Tryb normalny DA: schemat decyzyjny, Perun4V, raporty CNEC/LTA.

- **Pełna instrukcja:** [PROCEDURA_IDCC_TSO_v6.html#sec-nor](PROCEDURA_IDCC_TSO_v6.html#sec-nor)
- Powiązane — tryb backup: [PROCEDURA_IDCC_TSO_v6.html#sec-bup](PROCEDURA_IDCC_TSO_v6.html#sec-bup)
- Powiązane — Perun4V: [PROCEDURA_IDCC_TSO_v6.html#sec-narzedzia](PROCEDURA_IDCC_TSO_v6.html#sec-narzedzia)

## 🛟 Walidacja domeny — BUP

Tryb backup DA: CCA, F320, paczki ZIP, redukcja IVA, RLTA w ZP.

- **Pełna instrukcja:** [PROCEDURA_IDCC_TSO_v6.html#sec-bup](PROCEDURA_IDCC_TSO_v6.html#sec-bup)
- Powiązane — tryb normalny: [PROCEDURA_IDCC_TSO_v6.html#sec-nor](PROCEDURA_IDCC_TSO_v6.html#sec-nor)
- Powiązane — P01–P06: [PROCEDURA_IDCC_TSO_v6.html#sec-procedury](PROCEDURA_IDCC_TSO_v6.html#sec-procedury)

## 🔑 GLSK (FIDx-607) — stany

32 stany kafelka: sukces, w toku, błędy, wysyłka ręczna.

- **Pełna instrukcja:** [PROCEDURA_IDCC_TSO_v6.html#sec-fid607](PROCEDURA_IDCC_TSO_v6.html#sec-fid607)
- Powiązane — legenda: [PROCEDURA_IDCC_TSO_v6.html#sec-legenda](PROCEDURA_IDCC_TSO_v6.html#sec-legenda)
- Powiązane — publikacja GLSK: [PROCEDURA_IDCC_TSO_v6.html#sec-kreator](PROCEDURA_IDCC_TSO_v6.html#sec-kreator)

## 🛠️ Kreator IDCF

Publikacja GLSK/CBCORA/RA → Connector → MinIO → weryfikacja w CCM.

- **Pełna instrukcja:** [PROCEDURA_IDCC_TSO_v6.html#sec-kreator](PROCEDURA_IDCC_TSO_v6.html#sec-kreator)
- Powiązane — weryfikacja w CCM: [PROCEDURA_IDCC_TSO_v6.html#sec-ccm](PROCEDURA_IDCC_TSO_v6.html#sec-ccm)
- Powiązane — GLSK: [PROCEDURA_IDCC_TSO_v6.html#sec-fid607](PROCEDURA_IDCC_TSO_v6.html#sec-fid607)

## 📄 AC w ZP (FIDx-831)

Ręczna obsługa Allocation Constraints, tabela NTC/ATC, wersjonowanie.

- **Pełna instrukcja:** [PROCEDURA_IDCC_TSO_v6.html#sec-aczp](PROCEDURA_IDCC_TSO_v6.html#sec-aczp)
- Powiązane — plik FID2-831: [PROCEDURA_IDCC_TSO_v6.html#sec-katalog](PROCEDURA_IDCC_TSO_v6.html#sec-katalog)
- Powiązane — ZP: [PROCEDURA_IDCC_TSO_v6.html#sec-narzedzia](PROCEDURA_IDCC_TSO_v6.html#sec-narzedzia)

## 🧭 Procedury P01–P06

Reagowanie na ryzyka + procedury narzędziowe krok po kroku.

- **Pełna instrukcja:** [PROCEDURA_IDCC_TSO_v6.html#sec-procedury](PROCEDURA_IDCC_TSO_v6.html#sec-procedury)
- Powiązane — ryzyka: [PROCEDURA_IDCC_TSO_v6.html#sec-ryzyka](PROCEDURA_IDCC_TSO_v6.html#sec-ryzyka)
- Powiązane — CCM: [PROCEDURA_IDCC_TSO_v6.html#sec-ccm](PROCEDURA_IDCC_TSO_v6.html#sec-ccm)

## ⚠️ Ryzyka U01–U23

Katalog ryzyk, kody ACK, ścieżka zgłoszenia: CIZ / WPO / PSE-I.

- **Pełna instrukcja:** [PROCEDURA_IDCC_TSO_v6.html#sec-ryzyka](PROCEDURA_IDCC_TSO_v6.html#sec-ryzyka)
- Powiązane — procedury: [PROCEDURA_IDCC_TSO_v6.html#sec-procedury](PROCEDURA_IDCC_TSO_v6.html#sec-procedury)
- Powiązane — zgłoszenia: [PROCEDURA_IDCC_TSO_v6.html#sec-narzedzia](PROCEDURA_IDCC_TSO_v6.html#sec-narzedzia)

## 🗄️ Buckety MinIO + mapa relacji

Pełna mapa lokalizacji plików; narzędzie ↔ ryzyko ↔ procedura.

- **Pełna instrukcja:** [PROCEDURA_IDCC_TSO_v6.html#sec-minio](PROCEDURA_IDCC_TSO_v6.html#sec-minio)
- Powiązane — pliki: [PROCEDURA_IDCC_TSO_v6.html#sec-katalog](PROCEDURA_IDCC_TSO_v6.html#sec-katalog)
- Powiązane — MinIO: [PROCEDURA_IDCC_TSO_v6.html#sec-narzedzia](PROCEDURA_IDCC_TSO_v6.html#sec-narzedzia)
