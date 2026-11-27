# -*- coding: utf-8 -*-
"""Ciekawostki do obiektów DEMO. Tylko fikcyjne - przy Kościelcu i Dębnie
nic nie dopisujemy, bo to prawdziwe realizacje i treść musi przyjść od Arcady."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baza import zaloz, log

# slug -> [(po_dacie, data, tytul, opis)]
CIEK = {
'dwor-lipowiec':[
 ('2024','2024','Skan pokazał, że dwór się przechylił',
  'Chmura punktów wykazała, że zachodnia ściana odchyla się od pionu o cztery centymetry na wysokości kondygnacji. Odchylenie jest stare i ustabilizowane - widać to po tynku, który na styku nie pęka. Zamiast prostować, zostawiliśmy je i opisali w dokumentacji, a nowe tynki położyliśmy po istniejącym licu. Budynek ma prawo nosić ślad własnej historii.'),
 ('2025','2025','Okna, których nikt nie wyjął',
  'Dwa okna zamurowane w 1946 roku okazały się zamurowane dookoła ościeżnic - ekipa nie chciała ich wyjmować, więc obmurowała je od zewnątrz. Dzięki temu oryginalna stolarka z lat dwudziestych przeleżała w murze osiemdziesiąt lat bez dostępu wody. Po oczyszczeniu i uzupełnieniu czopów wróciła na miejsce; wymiany wymagały tylko dolne progi.'),
 ('2025','2025','Drzwi wróciły na swoje miejsce',
  'W 1891 roku ówczesny właściciel przebił nowe wejście od strony ogrodu, a oryginalne drzwi frontowe przeniósł tam razem z opaską. Pod wyprawą cementową znaleźliśmy ślad pierwotnego otworu - cegła była ułożona inaczej niż w reszcie ściany, bo zamurowano go w pośpiechu. Otwór odtworzyliśmy w dawnym wymiarze, a drzwi wróciły na front po 134 latach.'),
],
'kamienica-garbarska':[
 ('2025','2025','Sztukateria przetrwała w studni',
  'W 1971 roku całą sztukaterię skuto jako zagrażającą przechodniom - ale ekipa nie weszła do studni doświetlającej klatkę schodową, bo nie było tam ruchu. Zachowały się w niej cztery pełne kwiatony i fragment fryzu. To z nich zdjęliśmy formy silikonowe i odlaliśmy ornament na całą elewację frontową. Bez tej studni nie byłoby czego odtwarzać.'),
 ('2025','2025','Szkło dobierane na oko, nie z katalogu',
  'Do rekonstrukcji witraża nie da się kupić szkła z katalogu - współczesne jest zbyt równe i zbyt czyste. Zielenie i żółcie dobieraliśmy sztuka po sztuce z zapasów huty, która nadal ciągnie szkło walcowane, przykładając próbki do zachowanego fragmentu pod światło. Z szesnastu odcieni pasowały cztery.'),
 ('2025','2025','Balustrady wróciły z dwóch różnych odlewni',
  'Przy demontażu okazało się, że dwie z trzech balustrad mają inny rysunek spodu wspornika - zostały dorobione po wojnie w innej odlewni. Zostawiliśmy obie wersje i opisali, która jest pierwotna. Ujednolicenie wyglądałoby lepiej na zdjęciu, ale skasowałoby informację o tym, co się z domem działo.'),
],
'spichlerz-borowa':[
 ('2026','2026','Cieśla ponumerował ramę',
  'Na belkach są znaki ciesielskie - rzymskie cyfry wycinane dłutem, którymi cieśla oznaczył każde złącze, żeby po transporcie z placu obróbki złożyć ramę w tej samej kolejności. Przepisaliśmy je do inwentaryzacji i według nich wstawialiśmy nowe rygle, więc rama została złożona tak, jak chciał ją mieć ten, kto ją stawiał.'),
 ('2026','2026','Cegła z rozbiórek, nie z hurtowni',
  'Wypełnienia szachulca są z cegły ręcznie formowanej, mniejszej od dzisiejszej - około 26 na 12 na 6 centymetrów. Nowa cegła w tym wymiarze nie powstaje, a przycinanie współczesnej dałoby widoczną spoinę i inny kolor wypału. Zebraliśmy więc materiał z rozbiórek budynków z tego samego okresu w promieniu kilkudziesięciu kilometrów i przebraliśmy go sztuka po sztuce, osobno pod wymiar i osobno pod barwę.'),
 ('2026','2026','Jodełka układana od środka pola',
  'Wypełnienia szachulca muruje się od środka pola ku krawędziom, inaczej ostatnia cegła nie wchodzi bez przycinania, a przycięta pęka na mrozie. Tak samo robił cieśla w XIX wieku - widać to po tym, że docinki w starych polach siedzą przy słupach, nie na środku. Przemurowane pola ułożyliśmy tą samą metodą.'),
],
'wieza-cisnien-rudno':[
 ('2026','2026','Data w spoinie',
  'Przy przefugowaniu lica, dwa metry nad gruntem od strony dawnej bocznicy, znaleźliśmy w zaprawie wydrapany zapis: 14 VIII 1912 i trzy litery. To podpis murarza, zostawiony w świeżej spoinie w dniu, w którym kończył ten odcinek. Zaprawę wokół wymieniliśmy, ale ten fragment zostawiliśmy nietknięty.'),
 ('2026','2026','Miedź celowo bez patyny',
  'Nowe pokrycie sygnaturki i dachu jest z miedzi surowej, więc przez pierwsze lata będzie łososiowe, potem brązowe, a zielone dopiero po kilkunastu. Można kupić blachę wstępnie patynowaną, która od początku wygląda jak stara - nie użyliśmy jej. Nowy element ma być widoczny jako nowy, a nie udawać oryginału.'),
],
'oranzeria-zalesie':[
 ('2026','2026','Żebra mają numery odlewni',
  'Każde żeliwne żebro ma z tyłu odlany numer - odlewnia numerowała je kolejnością montażu, żeby na budowie nikt nie pomylił krzywizn. Przy inwentaryzacji spisaliśmy wszystkie i okazało się, że dwa numery się powtarzają, a jednego brakuje. To znaczy, że dwa żebra są późniejsze, dorobione po jakiejś awarii, i trzeba je naprawiać inaczej niż resztę.'),
 ('2026','2026','Szkło z huty, która ciągnie po staremu',
  'Oryginalne szyby mają lekko zielonkawy odcień i nierówną powierzchnię - to szkło ciągnione, nie float. Przy nim współczesna tafla wygląda jak plastik. Znaleźliśmy hutę, która nadal ciągnie szkło tą metodą i policzyliśmy, ile szyb trzeba zamówić, żeby wymiana nie rzucała się w oczy z poziomu ścieżki.'),
],
}

def dopisz(db):
    n=0
    for slug, lista in CIEK.items():
        r = db.execute('SELECT id FROM realizacja WHERE slug=? AND demo=1', (slug,)).fetchone()
        if not r:
            print('pomijam (brak obiektu demo):', slug); continue
        rid = r['id']
        for po, data, tyt, opis in lista:
            if db.execute('SELECT COUNT(*) FROM wpis WHERE realizacja_id=? AND tytul=?',
                          (rid, tyt)).fetchone()[0]:
                continue
            # tuz za ostatnim wpisem wlasnym o tej dacie
            k = db.execute("""SELECT kolejnosc FROM wpis WHERE realizacja_id=? AND data=?
                              AND rodzaj='my' ORDER BY kolejnosc DESC LIMIT 1""",
                           (rid, po)).fetchone()
            poz = (k['kolejnosc']+1) if k else 999
            db.execute('UPDATE wpis SET kolejnosc=kolejnosc+1 WHERE realizacja_id=? AND kolejnosc>=?',
                       (rid, poz))
            db.execute("""INSERT INTO wpis(realizacja_id,data,tytul,opis,rece,rodzaj,blok,kolejnosc,demo)
                          VALUES(?,?,?,?,'','ciekawostka','galeria',?,1)""", (rid, data, tyt, opis, poz))
            n+=1
    db.commit()
    return n

if __name__=='__main__':
    db=zaloz()
    n=dopisz(db)
    log(db,f'zasiew ciekawostek: {n}')
    db.commit()
    print('dopisano ciekawostek:',n)
    for r in db.execute("""SELECT r.tytul, COUNT(w.id) c FROM realizacja r
                           JOIN wpis w ON w.realizacja_id=r.id AND w.rodzaj='ciekawostka'
                           GROUP BY r.id ORDER BY r.kolejnosc"""):
        print(f'  {r[0]:42s} {r[1]}')
