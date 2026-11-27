# -*- coding: utf-8 -*-
"""Dzial poradnikow. Tresc merytoryczna, stan prawny na listopad 2026.
Zadnych wymyslonych liczb: ceny i kwoty tylko tam, gdzie pochodza ze zrodla."""

STAN = 'listopad 2026'

ART = []

ART.append({
 'slug':'ile-kosztuje-remont-zabytku',
 'h1':'Ile kosztuje remont zabytku i od czego zależy cena',
 'tyt':'Ile kosztuje remont zabytku · Arcada Concept',
 'opis':'Dlaczego nie ma cennika za metr, co podnosi koszt remontu zabytku i które pozycje najczęściej giną w ofertach wykonawców.',
 'czas':'9 min',
 'lead':'Nikt uczciwy nie poda ceny za metr remontu zabytku, dopóki nie wie, co dokładnie jest objęte wpisem do rejestru. Zakres ochrony wymusza metodę, a metoda ustala cenę - nie odwrotnie.',
 'skrot':['Cenę ustala zakres wpisu, nie powierzchnia',
          'Ekspertyza przed zakupem kosztuje najmniej w całym procesie',
          'Etapowanie prac jest tańsze niż jeden duży rok'],
 'sekcje':[
  ('Dlaczego nie ma cennika','''<p>W zwykłym budynku remont wycenia się od zakresu robót: tyle metrów tynku, tyle okien, tyle dachu. W zabytku ten sam metr tynku może oznaczać trzy zupełnie różne roboty. Raz będzie to skucie i położenie nowego tynku wapiennego. Raz odsalanie, uzupełnianie i scalenie kolorystyczne tynku, który trzeba zachować. A raz badania stratygraficzne, bo pod trzema warstwami farby jest dekoracja, o której nikt nie wiedział.</p>
<p>Różnica w koszcie między tymi trzema wariantami jest wielokrotna. Dopóki nie wiadomo, który wariant dopuszcza konserwator, cena za metr jest zgadywaniem.</p>'''),
  ('Siedem rzeczy, które realnie podnoszą koszt','''<ol>
<li><strong>Zakres wpisu do rejestru.</strong> Jeśli chroniona jest cała substancja budynku, a nie tylko bryła i elewacje, wymiana przestaje być opcją w środku budynku też.</li>
<li><strong>Stan konstrukcji.</strong> Zawilgocony mur, zagrzybione belki stropowe i skorodowane nadproża to prace, których nie widać na zdjęciu po remoncie, a zjadają największą część budżetu.</li>
<li><strong>Dostępność materiału.</strong> Cegła o nietypowym wymiarze, dachówka z określonej cegielni, gont z konkretnego gatunku drewna - każdy z tych elementów trzeba znaleźć albo wykonać na zamówienie.</li>
<li><strong>Wymóg odtworzenia zamiast wymiany.</strong> Naprawa historycznej stolarki okiennej bywa droższa niż nowe okno, bo to praca stolarska, nie zakup produktu.</li>
<li><strong>Dostęp.</strong> Wieża, sklepienie, strop nad nawą - rusztowanie i zabezpieczenia potrafią być osobną, dużą pozycją.</li>
<li><strong>Sezonowość prac mokrych.</strong> Tynki, zaprawy i scalenia mają temperaturowe okno robocze. Przerwa zimowa to nie opóźnienie, to warunek technologiczny.</li>
<li><strong>Badania i nadzory.</strong> Badania stratygraficzne, nadzór archeologiczny, nadzór autorski, dokumentacja powykonawcza. Pozycje obowiązkowe, które w tanich ofertach po prostu nie występują.</li>
</ol>'''),
  ('Co da się oszacować przed ekspertyzą, a czego nie','''<p>Przed wizją lokalną da się odpowiedzialnie powiedzieć, w jakiej kolejności prowadzić prace, jakie dokumenty będą potrzebne i jakie programy dotacyjne obejmują ten typ obiektu. Nie da się podać kwoty.</p>
<p>Po oględzinach i wglądzie w decyzję o wpisie da się już wskazać widełki dla etapu, który jest najpilniejszy - zwykle są to prace zabezpieczające, czyli dach, odwodnienie i stabilizacja konstrukcji. Dopiero projekt i uzgodnienia z konserwatorem dają liczbę, którą można wstawić do wniosku o dotację.</p>
<div class="uwaga"><p>Odwrotna kolejność - najpierw kwota, potem zakres - kończy się aneksami. Umowa podpisana na kwotę sprzed badań jest umową na kwotę, która się zmieni.</p></div>'''),
  ('Pozycje, które najczęściej giną w ofertach','''<p>Oferta, która wygląda na tanią, zwykle nie zawiera tego, co i tak trzeba będzie zrobić. Przy porównywaniu ofert warto sprawdzić, czy w każdej są:</p>
<ul>
<li>program prac konserwatorskich albo projekt budowlany, zależnie od zakresu</li>
<li>badania: stratygraficzne, mykologiczne, wilgotnościowe, w razie potrzeby archeologiczne</li>
<li>nadzór autorski i nadzór konserwatorski w trakcie robót</li>
<li>dokumentacja powykonawcza, wymagana przy rozliczeniu pozwolenia i dotacji</li>
<li>rusztowania, zabezpieczenia i zadaszenia tymczasowe</li>
<li>utylizacja i zabezpieczenie elementów przeznaczonych do ponownego wbudowania</li>
</ul>
<p>Jeśli dwie oferty różnią się o połowę, prawie zawsze różnią się tymi pozycjami, a nie stawką za robociznę.</p>'''),
  ('Co obniża koszt','''<p>Trzy mechanizmy działają naprawdę.</p>
<p><strong>Etapowanie.</strong> Rozbicie prac na lata pozwala wejść w kilka naborów dotacyjnych pod rząd i nie finansować wszystkiego z własnych środków. Warunek: etapy muszą być zamknięte technologicznie, a nie przerwane w połowie.</p>
<p><strong>Dotacje.</strong> Program ministra, dotacja wojewódzkiego konserwatora i dotacje gminne działają równolegle i mają różne terminy. Opisaliśmy je na stronie <a class="inl" href="dofinansowania.html">Dofinansowania</a>.</p>
<p><strong>Kolejność od zabezpieczenia.</strong> Dach i odwodnienie najpierw. Każdy rok, w którym woda wchodzi w mur, zwiększa zakres prac w środku.</p>'''),
  ('Od czego zaczynamy my','''<p>Od pomiaru i od decyzji o wpisie. Inwentaryzacja skanerem i, gdzie ma to sens, nalot dronem dają podkład, na którym da się policzyć powierzchnie i objętości bez zgadywania. Decyzja o wpisie mówi, czego nie wolno dotknąć. Te dwa dokumenty razem zamieniają rozmowę o cenie w rozmowę o zakresie.</p>
<p>Zakres naszych prac na każdym etapie opisaliśmy w <a class="inl" href="uslugi.html">Usługach</a>.</p>'''),
 ],
 'faq':[
  ('Podacie cenę za metr kwadratowy?','Nie, bo w zabytku ten sam metr może oznaczać trzy różne technologie o wielokrotnie różnym koszcie. Po oględzinach i wglądzie w decyzję o wpisie podajemy widełki dla konkretnego etapu prac.'),
  ('Dlaczego ekspertyza kosztuje, jeśli jeszcze nic nie budujemy?','Bo to jedyny moment, w którym decyzje są jeszcze tanie. Ekspertyza przed zakupem albo przed projektem przesuwa ryzyko z placu budowy na papier.'),
  ('Czy taniej wyjdzie wymienić niż naprawić?','W zwykłym budynku zwykle tak. W zabytku wpisanym do rejestru wymiana często nie jest dopuszczalna, więc porównanie nie ma zastosowania. Tam, gdzie konserwator dopuszcza oba warianty, liczymy je równolegle i pokazujemy różnicę.'),
 ],
 'zrodla':[],
})

ART.append({
 'slug':'co-wolno-zmienic-w-zabytku',
 'h1':'Co wolno, a czego nie wolno zmienić w budynku pod ochroną',
 'tyt':'Co wolno zmienić w zabytku · Arcada Concept',
 'opis':'Rejestr, gminna ewidencja i strefa ochrony w planie - trzy różne poziomy ochrony i trzy różne procedury. Co wymaga pozwolenia, a co uzgodnienia.',
 'czas':'10 min',
 'lead':'Trzy budynki przy tej samej ulicy mogą mieć trzy różne reżimy prawne. O tym, co wolno, decyduje nie wiek budynku ani jego wygląd, ale forma ochrony i zakres wpisu.',
 'skrot':['Rejestr zabytków: pozwolenie konserwatora przed pracami',
          'Gminna ewidencja: uzgodnienie w procedurze budowlanej',
          'Zakres wpisu jest ważniejszy niż sam fakt wpisu'],
 'sekcje':[
  ('Trzy poziomy ochrony','''<p>Zacznijmy od tego, co właściwie chroni Wasz budynek. To jest pierwsze pytanie w każdej rozmowie i zaskakująco często właściciel nie zna odpowiedzi.</p>
<table><thead><tr><th scope="col">Forma ochrony</th><th scope="col">Kto prowadzi</th><th scope="col">Co trzeba zrobić przed pracami</th></tr></thead><tbody>
<tr><td>Wpis do rejestru zabytków</td><td class="c">wojewódzki konserwator zabytków</td><td class="c">pozwolenie konserwatorskie</td></tr>
<tr><td>Gminna ewidencja zabytków</td><td class="c">wójt, burmistrz, prezydent miasta</td><td class="c">uzgodnienie w postępowaniu budowlanym</td></tr>
<tr><td>Strefa ochrony w planie miejscowym</td><td class="c">gmina</td><td class="c">zgodność z zapisami planu</td></tr>
</tbody></table>
<p>Te formy się nie wykluczają. Budynek wpisany do rejestru zwykle jest również ujęty w gminnej ewidencji i często stoi w strefie ochrony konserwatorskiej wyznaczonej w planie.</p>'''),
  ('Zakres wpisu, czyli dokument, od którego wszystko zależy','''<p>Wpis do rejestru nie jest jednakowy dla wszystkich obiektów. Decyzja o wpisie określa, co konkretnie jest chronione. Bywa, że to cały budynek wraz z wystrojem wnętrz, stolarką i otoczeniem. Bywa, że tylko bryła i elewacje. Bywa, że ochrona obejmuje też układ wnętrz, ale nie ich wykończenie.</p>
<p>Ta różnica przekłada się wprost na to, co wolno. W obiekcie, gdzie chroniona jest tylko bryła i elewacja, przebudowa wnętrz bywa realna. W obiekcie, gdzie wpis obejmuje substancję zabytkową, każda ścianka działowa jest tematem do uzgodnienia.</p>
<div class="uwaga"><p>Pierwsze, o co prosimy przy nowym obiekcie, to kopia decyzji o wpisie do rejestru wraz z uzasadnieniem. Bez niej planowanie prac jest planowaniem w ciemno.</p></div>'''),
  ('Obiekt z rejestru: co wymaga pozwolenia','''<p>Przy zabytku wpisanym do rejestru pozwolenia wojewódzkiego konserwatora zabytków wymagają, zgodnie z art. 36 ustawy o ochronie zabytków i opiece nad zabytkami, między innymi:</p>
<ul>
<li>prace konserwatorskie, restauratorskie i roboty budowlane przy zabytku</li>
<li>roboty budowlane w otoczeniu zabytku</li>
<li>zmiana przeznaczenia zabytku lub sposobu korzystania z niego</li>
<li>podział zabytku na części oraz zmiana jego części składowych</li>
<li>umieszczanie na zabytku urządzeń technicznych, tablic, reklam i napisów</li>
<li>inne działania, które mogłyby naruszyć substancję zabytku lub zmienić jego wygląd</li>
</ul>
<p>Ostatni punkt jest szerszy, niż się wydaje. Montaż klimatyzatora na elewacji, wymiana rynien na inny profil, nowa posadzka w kruchcie - to wszystko wchodzi w ten katalog.</p>'''),
  ('Obiekt tylko w ewidencji: uzgodnienie, nie pozwolenie','''<p>Jeśli budynek nie jest w rejestrze, ale jest ujęty w gminnej ewidencji zabytków, osobnego pozwolenia konserwatorskiego nie wydaje się. Działa inny mechanizm: zgodnie z art. 39 Prawa budowlanego organ administracji architektoniczno-budowlanej wydaje pozwolenie na budowę lub rozbiórkę takiego obiektu w uzgodnieniu z wojewódzkim konserwatorem zabytków, a konserwator ma 30 dni na zajęcie stanowiska.</p>
<p>W praktyce oznacza to dwie rzeczy. Po pierwsze, ścieżka jest krótsza. Po drugie, ograniczenia merytoryczne bywają bardzo podobne, bo konserwator ocenia ten sam projekt, tylko w innym trybie.</p>
<p>Warto wiedzieć, że sam wpis do gminnej ewidencji nie otwiera drogi do dotacji wojewódzkiego konserwatora - te dotyczą obiektów z rejestru. Część gmin prowadzi natomiast własne programy dotacyjne obejmujące również obiekty z ewidencji.</p>'''),
  ('Czego konserwator zwykle nie zaakceptuje','''<p>Lista nie jest przepisem, tylko podsumowaniem praktyki.</p>
<ul>
<li>Stolarka z PVC w miejscu historycznej stolarki drewnianej</li>
<li>Ocieplenie elewacji od zewnątrz tam, gdzie elewacja ma wartość zabytkową</li>
<li>Zmiana podziału okien, wielkości otworów i rytmu elewacji</li>
<li>Tynki i zaprawy cementowe na murze ceglanym z zaprawą wapienną</li>
<li>Blacha trapezowa albo dachówka o innym profilu na dachu historycznym</li>
<li>Nowe otwory w elewacji frontowej</li>
</ul>'''),
  ('Co da się uzgodnić częściej, niż ludzie myślą','''<p>Ochrona konserwatorska nie oznacza, że budynku nie można używać. Przy dobrze przygotowanej dokumentacji realne są:</p>
<ul>
<li>ocieplenie od wewnątrz w technologii paroprzepuszczalnej</li>
<li>nowe instalacje prowadzone trasami, które nie naruszają substancji</li>
<li>adaptacja poddasza, jeśli nie zmienia bryły i więźby</li>
<li>winda albo platforma w miejscu, które nie koliduje z układem wnętrz</li>
<li>zmiana funkcji, jeśli nie wymusza przebudowy chronionych elementów</li>
<li>usunięcie późniejszych dobudówek, które nie są objęte wpisem</li>
</ul>
<p>Różnica między odmową a zgodą to zwykle jakość dokumentacji, nie sam pomysł.</p>'''),
  ('Konsekwencje prac bez zgody','''<p>Prace wykonane bez wymaganego pozwolenia albo uzgodnienia nie stają się legalne przez to, że są już zrobione. Organ ochrony zabytków może nakazać przywrócenie stanu poprzedniego albo doprowadzenie zabytku do należytego stanu, a ustawa przewiduje też odpowiedzialność karną i wykroczeniową za uszkodzenie lub zniszczenie zabytku.</p>
<p>Osobny, bardzo praktyczny skutek: prace wykonane bez pozwolenia przekreślają możliwość rozliczenia ich w dotacji i w uldze podatkowej.</p>'''),
 ],
 'faq':[
  ('Czy mogę ocieplić dom wpisany do rejestru?','Od zewnątrz zwykle nie, jeśli elewacja ma wartość zabytkową. Od wewnątrz tak, przy użyciu materiałów paroprzepuszczalnych i po uzgodnieniu rozwiązania. Każdy przypadek wymaga sprawdzenia, jak wygląda mur i jak zachowuje się wilgoć.'),
  ('Czy mogę wyburzyć szpecącą dobudówkę?','Jeśli dobudówka nie jest objęta wpisem, zwykle tak - ale rozbiórka przy zabytku z rejestru i tak wymaga pozwolenia konserwatorskiego, a rozbiórka obiektu wpisanego do rejestru wymaga dodatkowo decyzji ministra wydawanej przez Generalnego Konserwatora Zabytków.'),
  ('Kto płaci za nadzór archeologiczny?','Inwestor. Dlatego warto wiedzieć o takim wymogu przed podpisaniem umowy z wykonawcą, a nie po wejściu koparki.'),
  ('Skąd mam wiedzieć, co obejmuje wpis?','Z decyzji o wpisie do rejestru i z karty ewidencyjnej obiektu. Kopie uzyskuje się w wojewódzkim urzędzie ochrony zabytków, a wykazy obiektów z rejestru publikują konserwatorzy wojewódzcy i Narodowy Instytut Dziedzictwa.'),
 ],
 'zrodla':[('Ustawa o ochronie zabytków i opiece nad zabytkami - art. 36','https://www.gov.pl/web/wuoz-katowice/gminna-ewidencja-zabytkow'),
           ('Prawo budowlane - art. 39','https://sip.lex.pl/akty-prawne/dzu-dziennik-ustaw/prawo-budowlane-16796118/art-39'),
           ('Wykazy zabytków wpisanych do rejestru - NID','https://nid.pl/zasoby/rejestr-zabytkow-zasoby/')],
})

ART.append({
 'slug':'pozwolenie-konserwatorskie',
 'h1':'Pozwolenie konserwatorskie krok po kroku',
 'tyt':'Pozwolenie konserwatorskie - procedura · Arcada',
 'opis':'Kiedy potrzebne jest pozwolenie wojewódzkiego konserwatora zabytków, co dołącza się do wniosku, kto może kierować robotami i ile to trwa.',
 'czas':'11 min',
 'lead':'Pozwolenie konserwatorskie to osobna decyzja, niezależna od pozwolenia na budowę. Wydaje ją wojewódzki konserwator zabytków i w większości przypadków musi być pierwsza.',
 'skrot':['Pozwolenie konserwatorskie i pozwolenie na budowę to dwie różne decyzje',
          'Kierownik robót musi mieć 18 miesięcy praktyki przy zabytkach z rejestru',
          'Najczęstszy powód opóźnienia to wezwanie do uzupełnienia wniosku'],
 'sekcje':[
  ('Kiedy jest potrzebne','''<p>Pozwolenia wojewódzkiego konserwatora zabytków wymagają prace przy zabytku wpisanym do rejestru - konserwatorskie, restauratorskie i roboty budowlane - a także badania konserwatorskie i architektoniczne, roboty w otoczeniu zabytku, zmiana przeznaczenia obiektu, podział zabytku, umieszczanie urządzeń technicznych, tablic i reklam oraz inne działania mogące naruszyć substancję albo zmienić wygląd zabytku.</p>
<p>Jeśli obiekt nie jest w rejestrze, a tylko w gminnej ewidencji zabytków, osobnego pozwolenia nie ma - jest uzgodnienie w postępowaniu budowlanym. Różnice między tymi trybami opisaliśmy w tekście <a class="inl" href="poradnik-co-wolno-zmienic-w-zabytku.html">Co wolno, a czego nie wolno zmienić w budynku pod ochroną</a>.</p>'''),
  ('Co zawiera wniosek','''<p>Przepisy wykonawcze do ustawy określają zawartość wniosku dość precyzyjnie. Dla pozwolenia na roboty budowlane są to:</p>
<ul>
<li>dane wnioskodawcy</li>
<li>wskazanie zabytku wraz z miejscem jego położenia</li>
<li>przewidywany termin rozpoczęcia i zakończenia robót</li>
<li>dane osoby kierującej robotami i osoby wykonującej nadzór inwestorski, wraz z dokumentami potwierdzającymi ich kwalifikacje</li>
</ul>
<p>Do wniosku dołącza się projekt budowlany albo tę jego część, która pozwala ocenić wpływ planowanych robót na zabytek, oraz dokument potwierdzający tytuł prawny do obiektu albo oświadczenie o jego posiadaniu. Przy pracach konserwatorskich i restauratorskich zamiast projektu budowlanego składa się program prac.</p>
<div class="uwaga"><p>Termin we wniosku nie jest formalnością. Decyzja zwykle wskazuje okres, w którym prace mają być wykonane. Wniosek z terminem „jak najszybciej” wraca do uzupełnienia.</p></div>'''),
  ('Kto może prowadzić prace','''<p>Ustawa stawia wymogi osobom, a nie firmom. Przy zabytkach nieruchomych wpisanych do rejestru robotami budowlanymi kieruje albo nadzór inwestorski wykonuje osoba, która ma uprawnienia budowlane według Prawa budowlanego i przez co najmniej 18 miesięcy brała udział w robotach budowlanych prowadzonych przy zabytkach nieruchomych wpisanych do rejestru lub do inwentarza muzeum będącego instytucją kultury. Tak mówi art. 37c ustawy o ochronie zabytków i opiece nad zabytkami.</p>
<p>Prace konserwatorskie i restauratorskie oraz badania konserwatorskie mają własne wymogi kwalifikacyjne, oparte na wykształceniu w zakresie konserwacji i restauracji oraz na praktyce przy zabytkach z rejestru.</p>
<p>Praktyczna konsekwencja: wykonawca bez takiej osoby w zespole nie przejdzie etapu wniosku, nawet jeśli cena jest atrakcyjna. W postępowaniach publicznych ten warunek bywa powodem wykluczenia ofert.</p>'''),
  ('Ile to trwa','''<p>Postępowanie prowadzi się według Kodeksu postępowania administracyjnego, więc podstawowy termin to miesiąc, a w sprawach szczególnie skomplikowanych dwa miesiące. W praktyce liczy się co innego: ile razy wniosek wróci do uzupełnienia. Każde wezwanie zatrzymuje bieg terminu.</p>
<p>Dlatego realny harmonogram liczymy od momentu złożenia kompletnego wniosku, a nie pierwszego. Przy obiektach, gdzie potrzebne są badania poprzedzające projekt, cały etap przygotowania bywa dłuższy niż samo postępowanie.</p>'''),
  ('Pozwolenie konserwatorskie a pozwolenie na budowę','''<p>To dwie osobne ścieżki w dwóch różnych urzędach. Pozwolenie konserwatorskie wydaje wojewódzki konserwator zabytków, pozwolenie na budowę - starosta albo prezydent miasta. Przy zabytku z rejestru Prawo budowlane wymaga, aby do wniosku o pozwolenie na budowę dołączyć pozwolenie konserwatorskie. Kolejność jest więc narzucona.</p>
<p>Nie każde prace wymagają pozwolenia na budowę. Część robót przy zabytku to remont w rozumieniu Prawa budowlanego i wystarcza zgłoszenie - ale pozwolenie konserwatorskie nadal jest potrzebne. To najczęstsze nieporozumienie: brak obowiązku budowlanego nie zwalnia z obowiązku konserwatorskiego.</p>'''),
  ('Najczęstsze powody wezwań i odmów','''<ul>
<li>Brak dokumentów potwierdzających kwalifikacje kierownika robót</li>
<li>Projekt zbyt ogólny, żeby ocenić wpływ prac na zabytek - brak detali, przekrojów, opisu technologii</li>
<li>Brak badań, które powinny poprzedzać decyzje projektowe</li>
<li>Rozwiązania materiałowe niezgodne z oryginałem, najczęściej zaprawy i tynki cementowe oraz stolarka z PVC</li>
<li>Zakres wniosku szerszy niż to, co obejmuje projekt</li>
<li>Brak programu prac przy pracach konserwatorskich</li>
</ul>
<p>Większość z nich to braki dokumentacyjne, nie merytoryczny spór. To dobra wiadomość, bo da się ich uniknąć na etapie przygotowania.</p>'''),
  ('Po otrzymaniu pozwolenia','''<p>Decyzja zwykle zawiera warunki: obowiązek zawiadomienia o rozpoczęciu i zakończeniu prac, zakres nadzoru, wymóg dokumentacji z przebiegu robót. Dokumentacja powykonawcza nie jest dodatkiem - bez niej nie zamyka się sprawy i nie rozlicza dotacji.</p>
<p>Jeśli w trakcie prac odkryjecie coś, czego nie było w projekcie - zamurowane okno, polichromię, starszy mur pod tynkiem - zakres trzeba uzgodnić ponownie. To normalny element remontu zabytku i warto mieć go wpisanego w harmonogram jako rezerwę, nie jako awarię.</p>
<p>Formalności prowadzimy w imieniu inwestora na każdym z tych etapów - zakres opisaliśmy w <a class="inl" href="uslugi.html">Usługach</a>.</p>'''),
 ],
 'faq':[
  ('Czy pozwolenie jest potrzebne na remont wnętrza?','Zależy od zakresu wpisu do rejestru. Jeśli ochrona obejmuje wnętrza, ich wystrój albo układ - tak. Jeśli wpis dotyczy tylko bryły i elewacji, część prac wewnętrznych może być poza zakresem, ale granicę trzeba ustalić na podstawie decyzji o wpisie, nie na wyczucie.'),
  ('Czy pozwolenie konserwatorskie wygasa?','Decyzja zwykle wskazuje termin wykonania prac. Po jego upływie trzeba wystąpić ponownie. Dlatego nie warto występować o pozwolenie, dopóki nie ma zapewnionego finansowania i wykonawcy.'),
  ('Czy można zmienić zakres prac w trakcie?','Tak, ale po uzgodnieniu. Zmiana wprowadzona samodzielnie oznacza prace bez pozwolenia w tym zakresie, z wszystkimi konsekwencjami.'),
  ('Czy wystarczy, że wykonawca ma doświadczenie w starych budynkach?','Nie. Ustawa wymaga udziału w robotach przy zabytkach wpisanych do rejestru albo do inwentarza muzeum, i to przez co najmniej 18 miesięcy. Remonty starych kamienic bez wpisu nie spełniają tego warunku.'),
 ],
 'zrodla':[('Rozporządzenie w sprawie prowadzenia prac przy zabytku wpisanym do rejestru','https://eli.gov.pl/eli/DU/2017/1265/ogl/pol/pdf'),
           ('Ustawa o ochronie zabytków - art. 37c','https://lexlege.pl/ustawa-o-ochronie-zabytkow-i-opiece-nad-zabytkami/art-37c/')],
})

ART.append({
 'slug':'kupno-domu-w-rejestrze-zabytkow',
 'h1':'Kupuję dom w rejestrze zabytków - na co patrzeć przed podpisaniem',
 'tyt':'Zakup domu wpisanego do rejestru zabytków · Arcada',
 'opis':'Jak sprawdzić status ochrony, o jakie dokumenty poprosić sprzedającego i które obowiązki przechodzą na nowego właściciela zabytku.',
 'czas':'10 min',
 'lead':'Dom w rejestrze zabytków kupuje się razem z obowiązkami, których nie widać w akcie notarialnym. Większość z nich da się sprawdzić przed podpisaniem, w ciągu dwóch tygodni.',
 'skrot':['Najpierw status: rejestr, ewidencja albo nic',
          'Poproście o decyzję o wpisie wraz z uzasadnieniem',
          'Zmianę właściciela zgłasza się konserwatorowi'],
 'sekcje':[
  ('Krok pierwszy: ustalcie formę ochrony','''<p>Ogłoszenia używają słowa „zabytkowy” swobodnie. Prawnie liczą się trzy sytuacje: wpis do rejestru zabytków, ujęcie w gminnej ewidencji zabytków albo brak jednego i drugiego, czasem przy jednoczesnym położeniu w strefie ochrony wyznaczonej w planie miejscowym.</p>
<p>Gdzie sprawdzić:</p>
<ul>
<li>wykazy zabytków wpisanych do rejestru publikują wojewódzcy konserwatorzy zabytków oraz <a class="inl" href="https://nid.pl/zasoby/rejestr-zabytkow-zasoby/" rel="noopener">Narodowy Instytut Dziedzictwa</a></li>
<li>mapa obiektów chronionych: <a class="inl" href="https://mapy.zabytek.gov.pl/nid/" rel="noopener">mapy.zabytek.gov.pl</a></li>
<li>gminna ewidencja zabytków: urząd gminy albo miasta</li>
<li>strefy ochrony: plan miejscowy, dostępny w urzędzie gminy</li>
</ul>
<p>Sam adres nie wystarcza - w wykazach obiekty bywają opisane przez numer działki albo obręb geodezyjny. Numer działki z księgi wieczystej rozstrzyga najpewniej.</p>'''),
  ('Krok drugi: decyzja o wpisie','''<p>Jeśli obiekt jest w rejestrze, najważniejszym dokumentem nie jest sam fakt wpisu, a jego zakres. Decyzja o wpisie wraz z uzasadnieniem mówi, co konkretnie jest chronione: budynek, jego wnętrza, stolarka, otoczenie, układ zieleni, ogrodzenie.</p>
<p>O kopię można poprosić sprzedającego albo wystąpić do wojewódzkiego urzędu ochrony zabytków. Warto też poprosić o kartę ewidencyjną obiektu - zawiera opis, historię i stan zachowania, często ze zdjęciami z lat, kiedy budynek wyglądał inaczej.</p>'''),
  ('Co przechodzi na nowego właściciela','''<p>Obowiązek opieki nad zabytkiem wiąże właściciela i posiadacza, nie konkretną osobę. Oznacza to w szczególności zabezpieczenie i utrzymanie zabytku oraz jego otoczenia w jak najlepszym stanie, prowadzenie prac konserwatorskich i robót budowlanych przy zabytku, korzystanie z niego w sposób zapewniający trwałe zachowanie wartości oraz popularyzowanie i upowszechnianie wiedzy o nim.</p>
<p>Dwie rzeczy, o których nowi właściciele dowiadują się zwykle za późno:</p>
<ul>
<li><strong>Zawiadomienie o zmianie stanu prawnego.</strong> O zmianach dotyczących stanu prawnego zabytku zawiadamia się wojewódzkiego konserwatora zabytków, nie później niż w terminie miesiąca.</li>
<li><strong>Zagospodarowanie na cele użytkowe.</strong> Zagospodarowanie zabytku wpisanego do rejestru na cele użytkowe wymaga posiadania dokumentacji konserwatorskiej określającej stan zachowania i możliwości adaptacji, uzgodnionego z konserwatorem programu prac konserwatorskich oraz uzgodnionego programu zagospodarowania obiektu z otoczeniem i dalszego korzystania z niego.</li>
</ul>'''),
  ('Czego nie pokaże akt notarialny','''<p>Stan prawny bywa czysty, a budynek nie. Przed podpisaniem warto wiedzieć:</p>
<ul>
<li>czy mur jest zawilgocony i skąd bierze się woda - brak izolacji, uszkodzone odwodnienie, podniesiony poziom terenu</li>
<li>w jakim stanie są belki stropowe i więźba, zwłaszcza w strefach przyściennych i w okolicy kominów</li>
<li>czy w drewnie są szkodniki i grzyby, i czy prowadzono już zabiegi</li>
<li>czy pod tynkiem nie ma dekoracji, która podniesie zakres prac</li>
<li>co zrobiono w ostatnich remontach i czy robiono to legalnie - cementowe tynki i wylewki z lat osiemdziesiątych to dziś osobna pozycja w kosztach</li>
<li>jaki jest stan instalacji i czy w ogóle da się je przeprowadzić bez naruszenia chronionych elementów</li>
</ul>'''),
  ('Co zrobić w dwa tygodnie przed podpisaniem','''<ol>
<li>Ustalić formę ochrony i uzyskać decyzję o wpisie</li>
<li>Zamówić oględziny z oceną stanu konstrukcji i zawilgocenia</li>
<li>Porozmawiać z wojewódzkim urzędem ochrony zabytków o planowanej funkcji - to rozmowa, nie wniosek, i zwykle wystarcza, żeby wiedzieć, czy pomysł jest realny</li>
<li>Sprawdzić plan miejscowy pod kątem funkcji i strefy ochrony</li>
<li>Oszacować pierwszy etap prac zabezpieczających, bo on zaczyna się niezależnie od planów</li>
</ol>
<p>Ekspertyza przed zakupem jest najtańszą pozycją w całym procesie i jedyną, która może zmienić decyzję o kupnie. Robimy ją jako osobną usługę - opis w <a class="inl" href="uslugi.html">Usługach</a>.</p>'''),
  ('Pieniądze','''<p>Właściciel obiektu wpisanego do rejestru, także osoba fizyczna, może wnioskować o dotacje: w programie ministra kultury, u wojewódzkiego konserwatora zabytków i w gminie. Szczegóły i terminy zebraliśmy na stronie <a class="inl" href="dofinansowania.html">Dofinansowania</a>.</p>
<p>Osobno działa ulga podatkowa w PIT na wydatki przy zabytku wpisanym do rejestru. Zasady i limity zmieniały się od jej wprowadzenia, a warunkiem jest między innymi posiadanie pozwolenia i zaświadczenia konserwatora, dlatego przed planowaniem wydatków pod ulgę warto sprawdzić aktualne brzmienie przepisów na <a class="inl" href="https://podatki.gov.pl/ulgi-i-odliczenia/ulga-na-zabytki-pit" rel="noopener">podatki.gov.pl</a> i skonsultować się z doradcą podatkowym. Nie doradzamy podatkowo.</p>'''),
  ('Czerwone flagi','''<ul>
<li>Sprzedający nie ma decyzji o wpisie i nie wie, co obejmuje ochrona</li>
<li>Świeży remont elewacji bez śladu pozwolenia konserwatorskiego</li>
<li>Nowa stolarka z PVC w obiekcie z rejestru - to zwykle oznacza niezalegalizowane prace</li>
<li>Dach po prowizorycznej naprawie przy widocznych zaciekach w środku</li>
<li>Oferta z argumentem „konserwator na wszystko się zgodzi, mamy ustalone”</li>
</ul>'''),
 ],
 'faq':[
  ('Czy można wykreślić budynek z rejestru zabytków?','Tylko wyjątkowo - gdy zabytek utracił wartości, które były podstawą wpisu, albo gdy wpis był oczywiście bezzasadny. To procedura na poziomie ministerialnym, nie element planowania remontu.'),
  ('Czy bank udzieli kredytu na zabytek?','Zdarza się, że tak, ale wycena bywa niższa od ceny ofertowej, a bank może pytać o zakres planowanych prac i o wymagane pozwolenia. Warto ustalić to równolegle z ekspertyzą techniczną.'),
  ('Czy muszę udostępniać obiekt do zwiedzania?','Obowiązek opieki obejmuje popularyzowanie i upowszechnianie wiedzy o zabytku, co nie jest tym samym co przymus wpuszczania zwiedzających do prywatnego domu. Szczególne warunki mogą wynikać z umowy dotacyjnej.'),
  ('Czy sprzedający musi mi powiedzieć, że dom jest w rejestrze?','Wpis do rejestru jest informacją publiczną i powinien być ujawniony w księdze wieczystej. Nie zwalnia to kupującego ze sprawdzenia - księgi bywają nieaktualne.'),
 ],
 'zrodla':[('Wykazy zabytków z rejestru - NID','https://nid.pl/zasoby/rejestr-zabytkow-zasoby/'),
           ('Mapa zabytków - mapy.zabytek.gov.pl','https://mapy.zabytek.gov.pl/nid/'),
           ('Ulga na zabytki w PIT - podatki.gov.pl','https://podatki.gov.pl/ulgi-i-odliczenia/ulga-na-zabytki-pit')],
})

ART.append({
 'slug':'okna-w-zabytku',
 'h1':'Czy można wymienić okna w zabytku',
 'tyt':'Wymiana okien w zabytku - zasady · Arcada Concept',
 'opis':'Rejestr, ewidencja, strefa ochrony - od tego zależy procedura. Kiedy konserwator dopuszcza wymianę stolarki, a kiedy wymaga odtworzenia.',
 'czas':'9 min',
 'lead':'Można, ale nie na dowolne okna i nie bez zgody. Procedura zależy od formy ochrony, a zakres dopuszczalnych zmian - od tego, co w stolarce uznano za wartościowe.',
 'skrot':['Rejestr: pozwolenie konserwatorskie przed wymianą',
          'Ewidencja: uzgodnienie w procedurze budowlanej, 30 dni',
          'Ciepło da się poprawić bez wymiany stolarki'],
 'sekcje':[
  ('Krótka odpowiedź','''<table><thead><tr><th scope="col">Sytuacja</th><th scope="col">Co jest wymagane</th></tr></thead><tbody>
<tr><td>Budynek wpisany do rejestru zabytków</td><td class="c">pozwolenie wojewódzkiego konserwatora zabytków</td></tr>
<tr><td>Budynek w gminnej ewidencji zabytków</td><td class="c">uzgodnienie z konserwatorem w postępowaniu budowlanym, 30 dni na stanowisko</td></tr>
<tr><td>Strefa ochrony w planie miejscowym, bez wpisu</td><td class="c">zgodność z zapisami planu, często dotyczącymi elewacji</td></tr>
<tr><td>Brak ochrony</td><td class="c">zasady ogólne Prawa budowlanego</td></tr>
</tbody></table>
<p>Do tego dochodzi Prawo budowlane: wymiana stolarki bez zmiany wielkości otworu to zwykle remont, natomiast zmiana wielkości albo kształtu otworu ingeruje w przegrodę i jest kwalifikowana jako przebudowa, z własnymi formalnościami.</p>'''),
  ('Dlaczego konserwator broni starej stolarki','''<p>Okno jest jednym z najbardziej czytelnych elementów datujących budynek. Decyduje o tym kilka cech naraz:</p>
<ul>
<li><strong>Podział.</strong> Liczba i rozkład kwater oraz szprosów - zmiana podziału zmienia wyraz całej elewacji.</li>
<li><strong>Profil.</strong> Szerokość i kształt profili ramy i skrzydła. Współczesne profile są grubsze, co pogrubia rysunek okna.</li>
<li><strong>Osadzenie w murze.</strong> Historyczne okna bywają cofnięte w glif albo osadzone w licu - przeniesienie okna w inną płaszczyznę zmienia światłocień elewacji.</li>
<li><strong>Szyba.</strong> Dawne szkło ciągnione ma nierówności, które widać w odbiciu. Nowa szyba zespolona daje płaskie, lustrzane odbicie.</li>
<li><strong>Okucia i detale.</strong> Zawiasy, zakrętki, okiennice, nadokienniki.</li>
</ul>'''),
  ('Trzy drogi','''<h3>Renowacja istniejącej stolarki</h3>
<p>Najczęściej preferowana. Stolarka z dobrego, wysezonowanego drewna po naprawie i uszczelnieniu działa dekady. Wymienia się uszkodzone fragmenty, nie całe skrzydła.</p>
<h3>Odtworzenie kopii</h3>
<p>Gdy oryginał jest zniszczony nieodwracalnie, wykonuje się kopię na podstawie inwentaryzacji: te same profile, podział, sposób osadzenia i wykończenie. To praca stolarska na zamówienie, nie zakup z katalogu.</p>
<h3>Nowa stolarka zgodna z charakterem</h3>
<p>Gdy pierwotnej stolarki nie ma i nie wiadomo, jak wyglądała, projektuje się nową, zgodną z epoką i z materiałem oryginału, na podstawie analogii z obiektów z tego samego okresu i regionu.</p>'''),
  ('PVC - dlaczego prawie nigdy','''<p>W obiektach objętych ochroną stolarka z PVC jest odrzucana niemal zawsze i nie chodzi tylko o estetykę. Profile są szersze, co zmienia proporcje. Materiał nie pozwala odwzorować profilowania. Szprosy międzyszybowe albo naklejane dają inny rysunek niż konstrukcyjne. Wreszcie PVC jest szczelny w sposób, który w starym murze zmienia bilans wilgoci - przy braku wentylacji skutkuje to zawilgoceniem ościeży i pleśnią.</p>
<p>To ostatnie zdarza się także w budynkach bez żadnej ochrony. Szczelne okna w murze bez izolacji i bez wentylacji mechanicznej przenoszą kondensację na najzimniejsze miejsca.</p>'''),
  ('Jak poprawić ciepło bez wymiany','''<p>Komfort cieplny da się podnieść znacząco, zachowując stolarkę:</p>
<ul>
<li>naprawa i doszczelnienie przylg oraz uzupełnienie kitów</li>
<li>przywrócenie albo odtworzenie okna skrzynkowego - dwie warstwy szklenia w jednej ościeżnicy to rozwiązanie historyczne i skuteczne</li>
<li>druga szyba albo szyba zespolona cienka, wstawiona w istniejące skrzydło, jeśli przekrój na to pozwala</li>
<li>okiennice i opaski zewnętrzne, tam gdzie występowały</li>
<li>zasłony i karnisze zamykające szczelinę przy ścianie - niedoceniany, a mierzalny efekt</li>
<li>uporządkowanie wentylacji, bez którego każda poprawa szczelności przenosi problem w inne miejsce</li>
</ul>'''),
  ('Co dołączyć do wniosku','''<ul>
<li>inwentaryzację istniejącej stolarki: wymiary, podziały, profile w skali, rodzaj drewna, okucia</li>
<li>dokumentację fotograficzną z zewnątrz i z wnętrza, z detalami osadzenia</li>
<li>rysunki projektowanego rozwiązania w skali detalu</li>
<li>opis materiału, rodzaju szkła i wykończenia powierzchni, z podaniem koloru</li>
<li>uzasadnienie wyboru drogi: renowacja, kopia albo nowa stolarka</li>
</ul>
<p>Wniosek bez rysunków detalu wraca do uzupełnienia niemal zawsze, bo bez nich nie da się ocenić, jak okno będzie wyglądać w murze.</p>'''),
  ('Czego nie robić','''<ul>
<li>Nie zamawiajcie okien przed uzyskaniem zgody. Zamówiona i opłacona stolarka nie jest argumentem w postępowaniu.</li>
<li>Nie wyrzucajcie starych skrzydeł, dopóki sprawa nie jest zamknięta. Czasem są dowodem, czasem materiałem do naprawy.</li>
<li>Nie wymieniajcie „na razie od podwórza”. Elewacja tylna też jest objęta wpisem, jeśli wpis nie mówi inaczej.</li>
</ul>'''),
 ],
 'faq':[
  ('Czy wymiana okna 1:1 wymaga zgłoszenia w prawie budowlanym?','Wymiana bez zmiany wielkości otworu jest zwykle traktowana jako remont. Zmiana wielkości albo kształtu otworu to przebudowa i wymaga formalności. Niezależnie od tego przy zabytku z rejestru potrzebne jest pozwolenie konserwatorskie.'),
  ('Czy mogę zmienić kolor stolarki?','Kolor jest częścią wyglądu zabytku, więc przy obiekcie z rejestru to element do uzgodnienia. Przy budynkach w ewidencji i w strefach ochrony kolor bywa określony w zapisach planu albo w wytycznych gminnego konserwatora.'),
  ('Czy mogę wstawić okna dachowe?','Czasem tak, jeśli nie zmieniają czytelności bryły i nie kolidują z więźbą. Zwykle negocjuje się ich liczbę, wielkość i położenie na połaci - łatwiej uzyskać zgodę na połaci niewidocznej z głównego kierunku widokowego.'),
  ('Czy okno skrzynkowe spełni dzisiejsze wymagania cieplne?','Przy remoncie zabytku przepisy dopuszczają odstępstwa od wymagań cieplnych tam, gdzie ich spełnienie naruszałoby wartości zabytkowe. Zakres odstępstwa ustala się w projekcie i uzgadnia z konserwatorem.'),
 ],
 'zrodla':[('Prawo budowlane - art. 39','https://sip.lex.pl/akty-prawne/dzu-dziennik-ustaw/prawo-budowlane-16796118/art-39')],
})

ART.append({
 'slug':'material-w-zabytku',
 'h1':'Cegła, tynk, gont: dlaczego materiał z marketu nie przejdzie',
 'tyt':'Materiały w remoncie zabytku · Arcada Concept',
 'opis':'Dobór cegły, zaprawy, tynku i drewna w obiekcie zabytkowym. Dlaczego cement niszczy stary mur i co znaczy odwracalność rozwiązania.',
 'czas':'10 min',
 'lead':'W zabytku materiał nie jest kwestią gustu ani ceny. Musi być zgodny z oryginałem pod względem fizyki, a rozwiązanie powinno być odwracalne - możliwe do usunięcia bez szkody dla substancji.',
 'skrot':['Zaprawa twardsza od cegły niszczy cegłę, nie odwrotnie',
          'Paroprzepuszczalność jest ważniejsza od współczynnika U',
          'Odwracalność: da się usunąć bez uszkodzenia oryginału'],
 'sekcje':[
  ('Dwie zasady, z których wynika wszystko','''<p><strong>Zgodność.</strong> Nowy materiał ma pracować tak jak stary: podobnie przyjmować i oddawać wilgoć, podobnie się odkształcać, mieć podobną wytrzymałość. Materiał mocniejszy od oryginału nie jest lepszy - przenosi naprężenia na element słabszy, czyli na zabytek.</p>
<p><strong>Odwracalność.</strong> Rozwiązanie powinno dać się usunąć bez niszczenia substancji zabytkowej. Dzięki temu błąd dzisiejszej generacji nie staje się trwałą stratą.</p>'''),
  ('Cegła','''<p>Dobiera się ją po kilku cechach naraz: wymiar, barwa, faktura, sposób wypału i nasiąkliwość. Wymiar jest najprostszy do sprawdzenia i zwykle najbardziej zdradliwy - cegła maszynowa współczesna rzadko zgadza się z formatem historycznym, a różnica kilku milimetrów zmienia rysunek wątku i grubość spoiny.</p>
<p>Dwie realne drogi:</p>
<ul>
<li><strong>Cegła rozbiórkowa z tego samego okresu.</strong> Najlepsza zgodność, ograniczona dostępność. Wymaga sortowania i oceny stanu, bo cegła przemarznięta albo zasolona nie nadaje się do wbudowania.</li>
<li><strong>Cegła formowana ręcznie na zamówienie.</strong> Produkowana w formatach historycznych. Dłuższy termin, wyższa cena jednostkowa, pełna kontrola nad parametrami.</li>
</ul>'''),
  ('Zaprawa, czyli najczęstszy błąd ostatnich dekad','''<p>Mur ceglany z XIX wieku był murowany na zaprawie wapiennej - miękkiej, paroprzepuszczalnej, słabszej niż cegła. To było zamierzone. Woda i sole wędrowały przez spoinę i odparowywały z niej, a nie z cegły. Spoina zużywała się pierwsza i była wymieniana - jak część serwisowa.</p>
<p>Zaprawa cementowa odwraca ten układ. Jest twardsza i szczelniejsza od cegły, więc wilgoć i sole szukają ujścia przez cegłę. Skutkiem jest łuszczenie powierzchni cegły, utrata lica i pęknięcia na styku spoiny z cegłą. Uszkodzenie postępuje od tego momentu szybciej niż przed „naprawą”.</p>
<div class="uwaga"><p>Dlatego przy zabytkach stosuje się zaprawy wapienne albo wapienno-cementowe o niskiej zawartości cementu, dobierane po badaniu zaprawy oryginalnej. Receptura jest częścią programu prac, nie decyzją majstra na budowie.</p></div>'''),
  ('Tynk','''<p>Ta sama logika. Tynk w starym murze ma odprowadzać wilgoć, a nie ją zamykać. Tynk cementowy na murze zawilgoconym działa jak folia: woda podnosi się wyżej, sole krystalizują pod warstwą tynku i odrywają go płatami.</p>
<p>W obiektach zawilgoconych i zasolonych stosuje się tynki renowacyjne o dużej porowatości, które pozwalają solom krystalizować wewnątrz warstwy, bez odspajania. To rozwiązanie techniczne, które wymaga wcześniejszego pomiaru zawilgocenia i zasolenia - bez badania jest zgadywaniem.</p>
<p>Przy warstwach malarskich obowiązuje dodatkowa ostrożność: pod farbą olejną albo akrylową z lat późniejszych często zachowały się starsze warstwy, w tym dekoracje. Dlatego badania stratygraficzne wykonuje się przed decyzją o skuciu, nie po.</p>'''),
  ('Drewno','''<p>Przy wymianie elementów konstrukcyjnych i pokryć liczy się gatunek, sposób obróbki i wilgotność. Drewno musi być wysezonowane - element z drewna mokrego skręci się i popęka po wbudowaniu.</p>
<p>Przy gontach różnica między wyrobem łupanym i ciętym jest zasadnicza. Gont łupany rozdziela się wzdłuż włókien, dzięki czemu woda spływa po nieprzerwanych włóknach. Gont cięty piłą ma przerwane włókna, chłonie wodę i żyje krócej. Konserwatorzy wymagają łupanego tam, gdzie takie było pierwotnie.</p>
<p>Elementy ciesielskie łączy się tak jak w oryginale - na zamki i kołki drewniane, nie na łączniki stalowe, o ile wpis nie dopuszcza inaczej. Wzmocnienia stalowe bywają akceptowane, ale jako czytelne i odwracalne uzupełnienie, nie jako zamiennik ciesiołki.</p>'''),
  ('Pokrycie dachu','''<p>Dach decyduje o sylwecie obiektu, więc jest pilnowany szczególnie. Przedmiotem uzgodnienia są rodzaj pokrycia, format i profil elementu, kolor oraz sposób wykończenia detali: okapu, kalenicy, obróbek, rynien.</p>
<p>Blacha trapezowa i dachówka o innym profilu niż historyczny są odrzucane rutynowo. Dachówka ceramiczna w profilu zgodnym z oryginałem, blacha na rąbek stojący tam, gdzie taka była, albo gont - to rozwiązania, które przechodzą.</p>'''),
  ('Co trzeba udokumentować','''<p>Każdy materiał wbudowany w zabytek powinien zostawić ślad w dokumentacji: skąd pochodzi, jakie ma parametry, gdzie został użyty i dlaczego wybrano właśnie ten. Dotyczy to zaprawy, tynku, cegły, drewna, pokrycia i farb.</p>
<p>To nie biurokracja. Przy kolejnym remoncie, za dwadzieścia lat, ta dokumentacja będzie jedynym źródłem wiedzy o tym, co jest oryginałem, a co uzupełnieniem. Jest też warunkiem rozliczenia pozwolenia i dotacji.</p>
<p>Jak prowadzimy dokumentację, pokazujemy na stronach obiektów w <a class="inl" href="realizacje.html">Realizacjach</a>.</p>'''),
 ],
 'faq':[
  ('Czy można użyć styropianu w budynku zabytkowym?','Na elewacji objętej ochroną praktycznie nie. Wewnątrz stosuje się materiały paroprzepuszczalne, na przykład płyty wapienno-krzemianowe albo lekkie zaprawy termoizolacyjne, dobierane po analizie wilgotnościowej przegrody.'),
  ('Czy tynk cementowy zawsze jest zły?','W nowym budynku nie. W starym murze ceglanym z zaprawą wapienną - tak, bo odwraca kierunek odparowania i przenosi niszczenie na cegłę.'),
  ('Skąd bierze się cegłę rozbiórkową?','Z rozbiórek obiektów z tego samego okresu i regionu. Materiał trzeba posortować i ocenić: cegła przemarznięta, zasolona albo wtórnie związana zaprawą cementową nie nadaje się do wbudowania.'),
  ('Czy można łączyć stare belki ze stalą?','Wzmocnienia stalowe bywają dopuszczane, jeśli są czytelne, odwracalne i nie zastępują ciesiołki. Rozwiązanie uzgadnia się z konserwatorem na etapie projektu.'),
 ],
 'zrodla':[],
})


# ---------------- render ----------------
def _plik(a): return f"poradnik-{a['slug']}.html"

def indeks():
    """Strona dzialu. Zwraca (zb, tresc) jak pozostale strony."""
    from b import blok
    poz=''
    for i,a in enumerate(ART):
        poz+=(f'<article class="por-poz"><div class="nr">{i+1:02d}</div>'
              f'<div><h2><a href="{_plik(a)}">{a["h1"]}</a></h2>'
              f'<p>{a["opis"]}</p></div>'
              f'<div class="czas">{a["czas"]} czytania</div></article>')
    return (blok('Poradnik','Co trzeba wiedzieć, zanim ruszy remont zabytku',
                 'Sześć tekstów o tym, co najczęściej decyduje o kosztach i o tym, '
                 'czy urząd wyda zgodę. Bez ogólników i bez obiecywania rzeczy, '
                 'których nie da się obiecać.',cta=False,maly=True),
f'''<section class="art-sekcja"><div class="w">
<div class="por-lista" style="margin-top:0">{poz}</div>
<p class="cicha" style="margin-top:26px;max-width:62ch">Stan prawny i stan programów dotacyjnych
opisujemy na {STAN}. Przepisy i terminy naborów się zmieniają - przy każdym tekście podajemy źródła,
w których można sprawdzić aktualny stan.</p>
<p style="margin-top:34px"><a class="btn" href="kontakt.html">Opiszcie swój obiekt</a></p>
</div></section>''')

def artykul(a,i):
    from b import blok
    sek=''; spis=''
    for k,(h2,html) in enumerate(a['sekcje']):
        sid=f's{k+1}'
        sek+=f'<h2 id="{sid}">{h2}</h2>{html}'
        spis+=f'<a href="#{sid}">{h2}</a>'
    faq=''
    if a.get('faq'):
        faq='<div class="art-faq"><h2 id="faq">Pytania, które dostajemy najczęściej</h2>'
        for q,odp in a['faq']:
            faq+=f'<details><summary>{q}</summary><p>{odp}</p></details>'
        faq+='</div>'
        spis+='<a href="#faq">Pytania i odpowiedzi</a>'
    zr=''
    if a.get('zrodla'):
        poz=''.join(f'<li><a class="inl" href="{u}" rel="noopener" target="_blank">{t}</a></li>'
                    for t,u in a['zrodla'])
        zr=(f'<div class="art-zrodla"><span class="m">Źródła</span><ul>{poz}</ul></div>')
    # poprzedni i nastepny tekst
    naw=''
    prev=ART[i-1] if i>0 else None
    nxt=ART[i+1] if i+1<len(ART) else None
    if prev or nxt:
        naw='<div class="g2" style="margin-top:46px">'
        if prev: naw+=(f'<div class="boks"><span class="m">Poprzedni tekst</span>'
                       f'<p style="margin-top:7px"><a class="inl" href="{_plik(prev)}">{prev["h1"]}</a></p></div>')
        if nxt: naw+=(f'<div class="boks"><span class="m">Następny tekst</span>'
                      f'<p style="margin-top:7px"><a class="inl" href="{_plik(nxt)}">{nxt["h1"]}</a></p></div>')
        naw+='</div>'
    skrot=''.join(f'<li>{s}</li>' for s in a.get('skrot',[]))
    return (blok('Poradnik',a['h1'],None,cta=False,maly=True),
f'''<section class="art-sekcja"><div class="w">
<nav class="ob-okruchy" aria-label="Ścieżka">
<a class="inl" href="index.html">Start</a><span>/</span>
<a class="inl" href="poradnik.html">Poradnik</a><span>/</span><span>{a['h1']}</span></nav>
<div class="ob-ukl">
<div class="ob-tresc art">
<p class="lead">{a['lead']}</p>
{sek}
{faq}
{zr}
{naw}
</div>
<aside class="ob-dane">
<span class="m">W skrócie</span>
<ul style="margin:10px 0 0;padding-left:18px;display:flex;flex-direction:column;gap:8px;font-size:14.5px;line-height:1.45">{skrot}</ul>
<div style="margin-top:22px;border-top:1px solid #DDE5E0;padding-top:18px">
<span class="m">W tekście</span><nav class="spis" aria-label="Spis treści">{spis}</nav></div>
<div style="margin-top:22px;border-top:1px solid #DDE5E0;padding-top:18px">
<span class="m">Macie taki obiekt?</span>
<p class="cicha" style="margin-top:7px;font-size:14.5px">Napiszcie, co to za budynek i co chcecie zrobić. Odpowiadamy w ciągu dwóch dni roboczych.</p>
<p style="margin-top:14px"><a class="btn" href="kontakt.html">Opiszcie obiekt</a></p></div>
<p class="m" style="margin-top:20px">Stan na {STAN}</p>
</aside>
</div></div></section>''')

def dane_artykulu(a,domena):
    """JSON-LD: Article + FAQPage + BreadcrumbList."""
    import json
    url=domena+_plik(a)
    art={"@context":"https://schema.org","@type":"Article",
         "headline":a['h1'],"description":a['opis'],"inLanguage":"pl-PL",
         "mainEntityOfPage":{"@type":"WebPage","@id":url},
         "author":{"@type":"Organization","name":"Arcada Concept sp. z o.o.","url":domena},
         "publisher":{"@type":"Organization","name":"Arcada Concept sp. z o.o.","url":domena},
         "about":[{"@type":"Thing","name":"konserwacja zabytków"},
                  {"@type":"Thing","name":"remont zabytku"}],
         "isAccessibleForFree":True}
    okr={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
         {"@type":"ListItem","position":1,"name":"Start","item":domena+"index.html"},
         {"@type":"ListItem","position":2,"name":"Poradnik","item":domena+"poradnik.html"},
         {"@type":"ListItem","position":3,"name":a['h1'],"item":url}]}
    out=[art,okr]
    if a.get('faq'):
        out.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
            {"@type":"Question","name":q,
             "acceptedAnswer":{"@type":"Answer","text":odp}} for q,odp in a['faq']]})
    return ''.join('<script type="application/ld+json">'
                   +json.dumps(d,ensure_ascii=False)+'</script>' for d in out)

def dane_indeksu(domena):
    import json
    d={"@context":"https://schema.org","@type":"ItemList",
       "name":"Poradnik: remonty i konserwacja zabytków",
       "numberOfItems":len(ART),
       "itemListElement":[{"@type":"ListItem","position":k+1,"name":a['h1'],
                           "url":domena+_plik(a)} for k,a in enumerate(ART)]}
    return '<script type="application/ld+json">'+json.dumps(d,ensure_ascii=False)+'</script>'
