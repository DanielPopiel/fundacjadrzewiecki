#!/usr/bin/env python3
"""Generuje en/index.html z index.html (PL). Uruchom po każdej zmianie wersji polskiej:
   python3 tools/build_en.py
Każda para musi wystąpić w pliku — jeśli tekst PL się zmienił, skrypt zgłosi błąd i trzeba poprawić parę."""
import pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
s = (root/'index.html').read_text(encoding='utf-8')

PAIRS = [
# --- head ---
('<html lang="pl">','<html lang="en">'),
('<title>Fundacja im. Stefana Drzewieckiego — Głębiny, przestworza i kosmos</title>',
 '<title>Stefan Drzewiecki Foundation — The Deep, the Sky and Space</title>'),
('content="Fundacja Historii Podboju Głębin, Przestworzy i Kosmosu im. Stefana Drzewieckiego — popularyzacja historycznego dorobku polskiej techniki podwodnej, lotniczej i kosmicznej: ubiory specjalne i urządzenia zapewniające przetrwanie człowieka."',
 'content="The Stefan Drzewiecki Foundation for the History of the Conquest of the Deep, the Sky and Space — promoting the historical legacy of Polish underwater, aviation and space technology: special purpose garments and equipment that keep people alive."'),
# --- pasek ---
('alt="Godło Fundacji im. Stefana Drzewieckiego"','alt="Emblem of the Stefan Drzewiecki Foundation"'),
('<b>Fundacja im. Stefana Drzewieckiego</b>\n        <small>Historia podboju głębin, przestworzy i kosmosu</small>',
 '<b>Stefan Drzewiecki Foundation</b>\n        <small>History of conquering the deep, the sky and space</small>'),
('<nav aria-label="Nawigacja">','<nav aria-label="Navigation">'),
('<a href="#fundacja">Fundacja</a>','<a href="#fundacja">Foundation</a>'),
('<a href="#dno">Kontakt</a>','<a href="#dno">Contact</a>'),
('<a href="./" hreflang="pl" lang="pl" aria-current="true">PL</a><i></i><a href="en/" hreflang="en" lang="en">EN</a>',
 '<a href="../" hreflang="pl" lang="pl">PL</a><i></i><a href="./" hreflang="en" lang="en" aria-current="true">EN</a>'),
('id="hint">Zanurz się<','id="hint">Dive in<'),
# --- hero ---
('<h1>Fundacja im.&nbsp;Stefana Drzewieckiego<span class="thin sub">Głębiny, przestworza, kosmos</span></h1>',
 '<h1>Stefan Drzewiecki Foundation<span class="thin sub">The deep, the sky, space</span></h1>'),
('''<p class="lead">Popularyzujemy historyczny dorobek polskiej techniki podwodnej, lotniczej
      i&nbsp;kosmicznej — ubiory specjalne i&nbsp;urządzenia, dzięki którym człowiek przetrwał
      tam, gdzie natura go nie przewidziała.</p>''',
 '''<p class="lead">We promote the historical legacy of Polish underwater, aviation and space
      technology — the special purpose garments and equipment that allowed people to survive where
      nature never meant them to go.</p>'''),
# --- fundacja ---
('<h2>Ubiory specjalne <em>i&nbsp;wyposażenie</em></h2>','<h2>Special purpose garments <em>and equipment</em></h2>'),
('''<p class="lead">Fundacja im. Stefana Drzewieckiego to inicjatywa mająca na celu popularyzację
          i&nbsp;zwiększanie świadomości społecznej w&nbsp;zakresie historycznego dorobku polskiej techniki
          podwodnej, lotniczej oraz kosmicznej. Głównym obszarem zainteresowań fundacji są ubiory specjalne
          oraz urządzenia zapewniające przetrwanie człowieka w&nbsp;wymienionych wyżej środowiskach.</p>''',
 '''<p class="lead">The Stefan Drzewiecki Foundation is an initiative that aims to promote and raise
          public awareness of the historical achievements of Polish underwater, aviation and space technology.
          Our main area of interest is special purpose garments and equipment that keep people alive in these
          environments.</p>'''),
('''<p class="muted">Fundacja historyczna im. Stefana Drzewieckiego to przedsięwzięcie umożliwiające
          w&nbsp;sposób formalny realizować działalność informacyjną oraz edukacyjną w&nbsp;oparciu
          o&nbsp;zainteresowania i&nbsp;pasję założycieli — Rafała Ducha oraz Łukasza Jaczuna.</p>''',
 '''<p class="muted">As a historical foundation, it gives a formal framework to the informational and
          educational work driven by the interests and passion of its founders — Rafał Duch and
          Łukasz Jaczun.</p>'''),
('''<p class="muted">Poprzez naszą aktywność wydawniczą, wystawienniczą chcielibyśmy uświadomić odbiorców
          o&nbsp;wyzwaniach stojących przed odkrywcami głębin, przestworzy i&nbsp;kosmosu oraz upamiętnić
          wysiłki konstruktorów i&nbsp;naukowców, stale przesuwających granice naszych osiągnięć technicznych.</p>''',
 '''<p class="muted">Through our publications and exhibitions we want to show the challenges faced by
          the explorers of the deep, the sky and space, and to commemorate the work of the engineers and
          scientists who keep pushing the limits of what technology can achieve.</p>'''),
('alt="Dwóch mężczyzn w historycznym umundurowaniu lotniczym idzie płytą lotniska — jeden w ubiorze wysokościowym z wężem tlenowym, drugi w skórzanej kurtce i czapce oficerskiej"',
 'alt="Two men in historical aviation uniforms walking across an airfield — one in a high-altitude suit with an oxygen hose, the other in a leather jacket and officer\'s cap"'),
('<b>Fot. FoxTwo.pl</b>','<b>Photo: FoxTwo.pl</b>'),
# --- żywioły ---
('<h2>Głębiny i&nbsp;niebo <em>w&nbsp;jednej historii</em></h2>','<h2>The deep and the sky <em>in one story</em></h2>'),
('''<p class="lead">W kontekście polskiej techniki, na szczególne zwrócenie uwagi zasługuje ścisła
          współpraca ośrodków badawczych zajmujących się zagadnieniami lotniczo-kosmicznymi oraz techniką
          podwodną.</p>''',
 '''<p class="lead">In the history of Polish technology, the close cooperation between research centres
          working on aerospace and on underwater technology deserves special attention.</p>'''),
('''<p class="muted">Stąd też pomysł na przedstawienie tych tematów razem i&nbsp;wybór patrona naszej
          fundacji — badacza, wynalazcy w&nbsp;tych trzech dziedzinach.</p>''',
 '''<p class="muted">That is why we present these subjects together, and why we chose as our patron
          a researcher and inventor active in all three fields.</p>'''),
('''<p class="muted">Mamy nadzieję, że nasze działania zainspirują kolejne pokolenia do dalszego
          rozwijania cywilizacji technicznej, umożliwiającej kontynuację największej przygody ludzkości —
          odkrywania nowych światów.</p>''',
 '''<p class="muted">We hope our work will inspire new generations to keep developing the technical
          civilisation that makes humanity's greatest adventure possible — the discovery of new worlds.</p>'''),
('alt="Dwóch nurków w historycznym sprzęcie nurkowym stoi na nabrzeżu o zachodzie słońca"',
 'alt="Two divers in historical diving gear standing on a quay at sunset"'),
('<b>Fot. Łukasz Jaczun</b>','<b>Photo: Łukasz Jaczun</b>'),
# --- patron ---
('''<p class="lead">Patron fundacji to działacz towarzystw naukowych Francji, Rosji i&nbsp;Polski,
          należący do grona najwybitniejszych inżynierów polskich XIX wieku, pionier żeglugi podwodnej,
          techniki lotniczej. W&nbsp;historii zapisał się jako wynalazca łączący rozważania teoretyczne
          z&nbsp;eksperymentem.</p>''',
 '''<p class="lead">Our patron was a member of scientific societies in France, Russia and Poland, one of
          the most outstanding Polish engineers of the 19th century and a pioneer of submarine navigation
          and aviation technology. He is remembered as an inventor who combined theory with experiment.</p>'''),
('''<p class="muted">Do jego bogatego dorobku zalicza się m.in. skonstruowanie pierwszych okrętów
          podwodnych o&nbsp;napędzie strugowodnym oraz o&nbsp;zasilaniu elektrycznym z&nbsp;akumulatorów;
          samolotu samostatecznego, opracowanie ogólnej teorii śruby okrętowej oraz śmigła lotniczego —
          w&nbsp;tym uzyskanie patentów na śmigła o&nbsp;łopatach nastawnych i&nbsp;samonastawnych.</p>''',
 '''<p class="muted">His many achievements include building the first submarines with water-jet
          propulsion and with battery-powered electric drive, designing an inherently stable aircraft, and
          developing a general theory of the ship's screw and the aircraft propeller — including patents
          for adjustable-pitch and self-adjusting propeller blades.</p>'''),
('''<p class="muted">W wolnej Polsce należał do grupy założycielskiej Warszawskiej Akademii Nauk
          Technicznych. W&nbsp;1928 roku za uchwałą Ligi Obrony Powietrznej i&nbsp;Przeciwgazowej Państwa
          otrzymał tytuł jej honorowego członka.</p>''',
 '''<p class="muted">In independent Poland he was one of the founders of the Warsaw Academy of Technical
          Sciences. In 1928 the League for Air and Anti-Gas Defence of the State made him an honorary
          member.</p>'''),
('''<p class="muted">Uważający się za Polaka i&nbsp;zawsze manifestujący swą polskość Stefan Drzewiecki
          zapisał Polsce w&nbsp;spadku cały swój dorobek naukowy. Niestety, zbiory pozostawione przez niego
          zostały najprawdopodobniej zniszczone w&nbsp;wyniku działań wojennych kampanii wrześniowej.</p>''',
 '''<p class="muted">Always proud of his Polish identity, Stefan Drzewiecki bequeathed his entire
          scientific legacy to Poland. Sadly, his collections were most likely destroyed during the fighting
          of September 1939.</p>'''),
('alt="Stefan Drzewiecki, portret archiwalny"','alt="Stefan Drzewiecki, archival portrait"'),
# --- kontakt ---
('<div class="eyebrow">Kontakt</div>','<div class="eyebrow">Contact</div>'),
('<h2>Zejdź z&nbsp;nami <em>głębiej</em></h2>','<h2>Dive deeper <em>with us</em></h2>'),
('<p class="lead">Fundacja Historii Podboju Głębin, Przestworzy i&nbsp;Kosmosu im.&nbsp;Stefana Drzewieckiego</p>',
 '<p class="lead">Stefan Drzewiecki Foundation for the History of the Conquest of the Deep, the Sky and Space</p>'),
('<span>Prezes Fundacji</span>','<span>President</span>'),
('<span>Wiceprezes Fundacji</span>','<span>Vice-President</span>'),
('?subject=Kontakt%20—%20Fundacja%20im.%20Stefana%20Drzewieckiego">Napisz do nas</a>',
 '?subject=Contact%20—%20Stefan%20Drzewiecki%20Foundation">Write to us</a>'),
('<span class="go">Otwórz profil →</span>','<span class="go">Open profile →</span>'),
('alt="Kod QR do profilu fundacji na Instagramie"><small>Zeskanuj</small>','alt="QR code for the foundation\'s Instagram profile"><small>Scan</small>'),
('alt="Kod QR do profilu fundacji na Facebooku"><small>Zeskanuj</small>','alt="QR code for the foundation\'s Facebook page"><small>Scan</small>'),
# --- lightbox / stopka ---
('aria-label="Powiększone zdjęcie"','aria-label="Enlarged photo"'),
('aria-label="Zamknij"','aria-label="Close"'),
("'Powiększ zdjęcie'","'Enlarge photo'"),
('<span>© 2026 Fundacja im. Stefana Drzewieckiego</span>','<span>© 2026 Stefan Drzewiecki Foundation</span>'),
('''<span>Zdjęcia pilotów: FoxTwo.pl — Michał Wajnchold, Leszek Kujawski, Przemek Szynkora · Statyści: Mikołaj Żukowski, Tytus Chaładus<br>Sesja zdjęciowa z samolotem MiG-19 dzięki uprzejmości 31.&nbsp;Bazy Lotnictwa Taktycznego</span>''',
 '''<span>Pilot photos: FoxTwo.pl — Michał Wajnchold, Leszek Kujawski, Przemek Szynkora · Cast: Mikołaj Żukowski, Tytus Chaładus<br>MiG-19 photo session courtesy of the 31st Tactical Air Base</span>'''),
('<span class="credit">Strona: Daniel Popiel','<span class="credit">Website: Daniel Popiel'),
]
bad=[a[:60] for a,b in PAIRS if s.count(a)<1]
if bad:
    print('Nie znaleziono w index.html:', *bad, sep='\n  '); sys.exit(1)
for a,b in PAIRS: s=s.replace(a,b)
# ścieżki zasobów o poziom wyżej
s=s.replace('src="assets/','src="../assets/').replace('href="assets/','href="../assets/').replace("'assets/","'../assets/")
(root/'en').mkdir(exist_ok=True)
(root/'en'/'index.html').write_text(s,encoding='utf-8')
print('OK: en/index.html')
