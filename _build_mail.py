#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buduje samodzielny plik HTML (mail/instrukcja) z opisem prac i zrzutami."""
import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IMGS = {
    'cover':  '/tmp/mail/01_cover-0001.png',
    'header': '/tmp/mail/02_header-0002.png',
    'proc':   '/tmp/mail/03_proc-0023.png',
    'risk':   '/tmp/mail/04_risk-1421.png',
}
def b64(p):
    return 'data:image/png;base64,' + base64.b64encode(Path(p).read_bytes()).decode()

IMG = {k: b64(v) for k, v in IMGS.items()}

HTML = f'''<!DOCTYPE html><html lang="pl"><head><meta charset="utf-8">
<style>
 body{{font-family:"Segoe UI",Arial,sans-serif;color:#1b2733;max-width:820px;margin:0 auto;
       padding:28px;line-height:1.62;font-size:15px;}}
 h1{{color:#1F4E78;font-size:22px;border-bottom:3px solid #1F4E78;padding-bottom:8px;}}
 h2{{color:#1F4E78;font-size:17px;margin-top:30px;border-left:4px solid #1F4E78;padding-left:10px;}}
 .lead{{color:#42526E;}}
 .step{{background:#F4F7FB;border:1px solid #DCE6F1;border-radius:8px;padding:14px 18px;margin:16px 0;}}
 .step .no{{display:inline-block;background:#1F4E78;color:#fff;border-radius:50%;width:26px;height:26px;
            text-align:center;line-height:26px;font-weight:700;margin-right:8px;}}
 .step h3{{display:inline;color:#1F4E78;font-size:16px;}}
 .why{{color:#5a6b7a;font-style:italic;margin-top:6px;}}
 figure{{margin:18px 0;border:1px solid #DCE6F1;border-radius:8px;padding:10px;background:#fafcff;}}
 figure img{{width:100%;border:1px solid #d0dae5;border-radius:4px;}}
 figcaption{{font-size:13px;color:#5a6b7a;margin-top:8px;text-align:center;}}
 ol.proc{{margin:8px 0;}} ol.proc li{{margin:6px 0;}}
 .box{{background:#FFF8E6;border-left:4px solid #E0A100;border-radius:0 6px 6px 0;padding:12px 16px;margin:18px 0;}}
 code{{background:#eef2f7;padding:1px 6px;border-radius:3px;font-size:13px;}}
 .sig{{margin-top:30px;color:#42526E;}}
</style></head><body>

<p>Cześć Łukasz,</p>
<p class="lead">Poniżej opis tego, co przygotowałem dla pulpitu dyspozytorskiego CCM w procesie
IDCC, oraz powody poszczególnych decyzji. Całość opisałem krokami, w kolejności wykonania.
Na końcu znajdziesz to, co pozostaje do uruchomienia po stronie wdrożenia.</p>

<h1>Materiał wynikowy</h1>
<p>Do uruchomienia potrzebne są dwa pliki. Pierwszy to dokument <code>info.pdf</code> z opisami
plików oraz pełną bazą ryzyk. Drugi to zestaw podpowiedzi <code>staticHints</code> wczytywany
do komponentu pulpitu. Dokument <code>info.pdf</code> zawiera kotwice, dzięki którym przejście
pod adres <code>/assets/info.pdf#FID1_831</code> otwiera właściwą stronę.</p>

<h1>Wykonane kroki</h1>

<div class="step"><span class="no">1</span><h3>Zebranie danych źródłowych</h3>
<p>Złożyłem komplet stanów kafelków dla wszystkich plików z jednego arkusza referencyjnego.
Łącznie objąłem siedemdziesiąt jeden plików oraz tysiąc czterysta czternaście stanów.</p>
<p class="why">Powód: arkusz zawiera kompletną i spójną treść dla każdego stanu, więc opisy
i procedury pochodzą z jednego, uzgodnionego źródła.</p></div>

<div class="step"><span class="no">2</span><h3>Wybór klucza identyfikującego plik</h3>
<p>Sprawdziłem unikalność na danych pulpitu. Nazwa przepływu nie jest unikalna — wartość
„AC" występuje pięć razy, „GLSK" oraz „CBCORA" po trzy razy. Połączenie obszaru i kodu
również się powtarza. Kod dokumentu pozostaje najpewniejszym identyfikatorem, a jego
powtórzenia oznaczają ten sam dokument w tej samej roli.</p>
<p class="why">Powód: klucz oparty na nazwie zlałby kilka różnych plików w jedną podpowiedź.
Kod jest stabilny i wynika z nazewnictwa plików oraz procesu.</p></div>

<div class="step"><span class="no">3</span><h3>Mapowanie statusów kafelków na nazwy</h3>
<p>Przypisałem każdy wygląd kafelka do nazwy statusu zgodnie z przesłaną legendą. Kafelek
pomarańczowy odpowiada statusowi „ostrzeżenie", kafelek szary ze znakiem zapytania statusowi
„proces w toku", kafelek czerwony statusowi „błąd", kafelek fioletowy statusowi „dostarczenie
po czasie krytycznym", a kafelek czarny statusowi „przekroczony czas".</p>
<p class="why">Powód: program dobiera podpowiedź na podstawie statusu widocznego kafelka,
więc mapowanie musi być zgodne z legendą, a nie z subiektywną oceną sytuacji.</p></div>

<div class="step"><span class="no">4</span><h3>Usunięcie pola dodatkowego i martwych odnośników</h3>
<p>Usunąłem pole z opisem repozytoriów plików oraz wszystkie odnośniki prowadzące do osobnej
strony inwentarza. Nazwy narzędzi oraz ścieżka przepływu pliku pozostają jako czysty,
czytelny tekst.</p>
<p class="why">Powód: pulpit nie udostępnia tej osobnej strony, więc odnośniki prowadziłyby
donikąd i tylko zaśmiecały obiekt.</p></div>

<div class="step"><span class="no">5</span><h3>Połączenie bazy ryzyk z dokumentem PDF</h3>
<p>Dołączyłem pełną bazę ryzyk, od pierwszego do dwudziestego dziewiątego, do tego samego
dokumentu <code>info.pdf</code> jako osobne strony z kotwicami. Odnośniki do ryzyk w
podpowiedziach prowadzą teraz do <code>/assets/info.pdf#R05</code> i pokrewnych.</p>
<p class="why">Powód: ustaliliśmy, że pulpit ma serwować wyłącznie dokument PDF. Dzięki
połączeniu całość działa na jednym pliku, bez dodatkowych stron.</p></div>

<div class="step"><span class="no">6</span><h3>Formatowanie procedur i odnośników</h3>
<p>Procedury złożyłem w czytelną hierarchię: krok główny, warunek „jeżeli" oraz zagnieżdżone
kody potwierdzeń. Stany bez działania, takie jak „brak działań" oraz „monitorowanie",
wyróżniłem osobnym formatowaniem. Odnośniki do ryzyk zamieniłem na czytelne, klikalne
hasła, na przykład „pełny opis ryzyka", bez numerów i nawiasów.</p>
<p class="why">Powód: dyspozytor ma odczytać kolejność działań w kilka sekund, a odnośnik
ma być zrozumiały bez znajomości kodów wewnętrznych.</p></div>

<div class="step"><span class="no">7</span><h3>Profesjonalny szablon dokumentu i jeden przypadek na stronę</h3>
<p>Przygotowałem szablon graficzny w stylu naszej instrukcji. Każdy stan jest osobnym arkuszem
na jednej stronie, z paskiem kontekstu, kolorem kategorii, kafelkami statusów oraz boksem
procedury. Poniżej cztery zrzuty pokazujące efekt.</p>
</div>

<figure><img src="{IMG['cover']}" alt="okładka">
<figcaption>Strona tytułowa dokumentu z liczbą plików, stanów oraz ryzyk.</figcaption></figure>

<figure><img src="{IMG['header']}" alt="arkusz pliku">
<figcaption>Strona pliku: kod, profil, czasy docelowy i krytyczny, opis pliku, ścieżka przepływu
oraz kontakt. Pod spodem pierwszy stan jako samodzielny arkusz.</figcaption></figure>

<figure><img src="{IMG['proc']}" alt="procedura">
<figcaption>Stan z rozbudowaną procedurą: krok główny, warunek „jeżeli", zagnieżdżone kody
potwierdzeń oraz klikalne odnośniki do pełnych opisów ryzyk.</figcaption></figure>

<figure><img src="{IMG['risk']}" alt="ryzyko">
<figcaption>Strona ryzyka wewnątrz tego samego dokumentu, dostępna pod kotwicą.</figcaption></figure>

<h1>Do uruchomienia po stronie wdrożenia</h1>
<ol class="proc">
<li>Udostępnić dokument <code>info.pdf</code> pod adresem <code>/assets/info.pdf</code>.</li>
<li>W odnośniku „więcej o pliku" zamienić myślnik na podkreślenie, ponieważ kotwice w
dokumencie używają podkreślenia, na przykład <code>FID1_831</code>. Odnośniki do ryzyk
nie zawierają myślnika i działają bez zmian.</li>
<li>Wczytać zestaw <code>staticHints</code> do komponentu pulpitu.</li>
</ol>

<div class="box">Jedyna rzecz do potwierdzenia: pozostawiłem w treści procedur numery kodów
potwierdzeń, ponieważ dyspozytor odczytuje je wprost z systemu. Jeżeli mają zniknąć, usunę je
w jednym przebiegu.</div>

<p class="sig">Pozdrawiam,<br>Dawid</p>
</body></html>'''

out = ROOT / 'CCM' / 'mail_opis_prac.html'
out.write_text(HTML, encoding='utf-8')
print(f'Zapisano: {out}  ({len(HTML):,} B)')
