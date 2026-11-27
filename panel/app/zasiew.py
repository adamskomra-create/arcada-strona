# -*- coding: utf-8 -*-
"""Pięć obiektów fikcyjnych jako dane demo. Każdy rekord ma demo=1 i znika
po kliknięciu 'Usuń dane demo' w panelu."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baza import zaloz, log, ile_demo

# (slug, tytul, podtytul, status, material, lead, adres, dojazd, lat, lon, cel_mapy, epoka_mapy)
OBIEKTY = [
 ('dwor-lipowiec','Dwór w Lipowcu Starym','Tynk wapienny i stolarka','odebrana','tynk wapienny, stolarka',
  'Klasycystyczny dwór z około 1820 roku. Po wojnie dom kultury, potem dwadzieścia lat pustki.',
  'Lipowiec Stary 4<br>woj. wielkopolskie','Obiekt fikcyjny - dane poglądowe.',52.22,17.40,'','XIX wieku'),
 ('kamienica-garbarska','Kamienica przy Garbarskiej 14','Sztukateria i witraż','odebrana','sztukateria, witraż',
  'Secesyjna kamienica czynszowa z 1904 roku. W 1971 sztukaterię skuto, my ją odtworzyliśmy.',
  'ul. Garbarska 14<br>woj. wielkopolskie','Obiekt fikcyjny - dane poglądowe.',52.40,16.92,'','przełomu XIX i XX wieku'),
 ('spichlerz-borowa','Spichlerz szachulcowy w Borowej','Drewno i cegła','w toku','mur pruski, dąb, cegła',
  'Spichlerz zbożowy z pierwszej połowy XIX wieku, konstrukcja szachulcowa.',
  'Borowa 11<br>woj. wielkopolskie','Obiekt fikcyjny - dane poglądowe.',52.05,17.75,'','XIX wieku'),
 ('wieza-cisnien-rudno','Wieża ciśnień w Rudnie','Cegła i żeliwo','w toku','klinkier, żeliwo, miedź',
  'Ceglana wieża ciśnień z 1912 roku przy dawnej bocznicy kolejowej.',
  'ul. Kolejowa, Rudno<br>woj. wielkopolskie','Obiekt fikcyjny - dane poglądowe.',52.55,17.20,'','początku XX wieku'),
 ('oranzeria-zalesie','Oranżeria pałacowa w Zalesiu','Żeliwo i szkło','w przygotowaniu','żeliwo, szkło, terakota',
  'Żeliwno-szklana oranżeria z około 1880 roku w zespole pałacowo-parkowym.',
  'Park pałacowy, Zalesie<br>woj. wielkopolskie','Obiekt fikcyjny - dane poglądowe.',51.95,17.05,'','XIX wieku'),
]

# slug -> [(data, tytul, opis, rece, rodzaj, blok)]
OSIE = {
'dwor-lipowiec':[
 ('ok. 1820','Dwór powstaje','Mur ceglany na kamiennym cokole, tynki wapienne, portyk z czterema kolumnami, dach naczółkowy.','murarz, nieznany z nazwiska','historia',''),
 ('1891','Przebudowa kuchni','Dobudowa ganku od strony ogrodu, przebicie nowego wejścia.','ówczesny właściciel majątku','historia',''),
 ('1946','Świetlica','Majątek przejęty, dwór zamieniony na świetlicę. Zamurowano dwa okna, portyk otynkowano cementem.','państwo','historia',''),
 ('1998','Pustka','Dom kultury się wyprowadza. Dach przecieka, zaczyna się dwadzieścia lat bez gospodarza.','nikt','historia',''),
 ('2025','Remont konserwatorski','Osuszenie murów, zdjęcie wyprawy cementowej, tynki wapienne, odtworzenie dwóch zamurowanych okien, renowacja stolarki.','Arcada Concept','my','lokalizacja'),
 ('Dalej','Obiekt ma przetrwać kolejne sto lat','Dokumentacja powykonawcza, zalecenia do przeglądów co dwa lata, kontakt na wypadek gdyby coś zaczęło się dziać.','ktoś po nas','dalej','')],
'kamienica-garbarska':[
 ('1904','Kamienica staje','Elewacja ze sztukaterią roślinną, witraż na półpiętrze, balkony na żeliwnych wspornikach.','budowniczy miejski','historia',''),
 ('1944','Wybity witraż','Podmuch wybija witraż klatki schodowej. Otwór zabito dyktą.','wojna','historia',''),
 ('1971','Skucie sztukaterii','Remont. Sztukaterię skuto jako niebezpieczną, elewację pokryto szarą wyprawą cementową.','spółdzielnia','historia',''),
 ('2025','Odtworzenie elewacji','Odlewy sztukaterii z form zdjętych z zachowanych fragmentów, rekonstrukcja witraża, renowacja żeliwnych balustrad.','Arcada Concept','my','lokalizacja'),
 ('Dalej','Elewacja pod dokumentacją','Szczegółowa dokumentacja ornamentu, formy odlewnicze zostają u właściciela, przegląd co trzy lata.','ktoś po nas','dalej','')],
'spichlerz-borowa':[
 ('1. poł. XIX w.','Spichlerz powstaje','Konstrukcja szachulcowa: dębowa kratownica słupów i rygli, wypełnienia z cegły układanej w jodełkę.','cieśla wiejski','historia',''),
 ('[rok]','Wpis do rejestru zabytków','Numer i data decyzji. Do uzupełnienia z karty ewidencyjnej.','konserwator','pusty',''),
 ('lata 60.','Magazyn nawozów','Zmiana funkcji. Wnętrze przedzielone, część wypełnień wybita pod wjazd.','spółdzielnia rolnicza','historia',''),
 ('2026','Naprawa konstrukcji','Wymiana spróchniałych rygli na nowe dębowe, wpuszczane na jaskółczy ogon. Przemurowania wypełnień, nowe pokrycie z esówki.','Arcada Concept','my','lokalizacja'),
 ('Dalej','Drewno wymaga oglądania','Zestaw zaleceń dla właściciela, miejsca naprawy opisane i udokumentowane, żeby następny wiedział co jest oryginałem.','ktoś po nas','dalej','')],
'wieza-cisnien-rudno':[
 ('1912','Wieża powstaje','Trzon ośmioboczny z ciemnego klinkieru, fryz arkadkowy, zbiornik na wspornikach, dach stożkowy kryty miedzią.','budowniczy kolejowy','historia',''),
 ('1987','Koniec pracy','Bocznica zlikwidowana, wieża odcięta od sieci. Zbiornik opróżniony, drzwi zamknięte na trzydzieści lat.','kolej','historia',''),
 ('2026','Mur, blacha, stolarka','Oczyszczenie lica, przefugowanie spoin zaprawą dobraną do oryginału, uzupełnienia cegłą pod wymiar i wypał, nowe pokrycie miedziane.','Arcada Concept','my','lokalizacja'),
 ('Dalej','Nowa funkcja do ustalenia','Konstrukcja zabezpieczona, obiekt gotowy na decyzję właściciela co dalej.','ktoś po nas','dalej','')],
'oranzeria-zalesie':[
 ('ok. 1880','Oranżeria powstaje','Konstrukcja z żeliwnych żeber wypełnionych szkłem, murowany cokół z cegły licowej, posadzka z terakoty.','odlewnia i ogrodnik dworski','historia',''),
 ('1945','Opuszczenie','Zespół pałacowy przechodzi w inne ręce, oranżeria przestaje być ogrzewana. Szkło zaczyna wypadać.','nikt','historia',''),
 ('[rok]','Wpis do rejestru zabytków','Numer i data decyzji. Do uzupełnienia.','konserwator','pusty',''),
 ('2026','Inwentaryzacja i projekt','Skan całej konstrukcji, inwentaryzacja żeber sztuka po sztuce, projekt naprawy odlewów i nowego przeszklenia.','Arcada Concept','my','lokalizacja'),
 ('Dalej','Prace przed nami','Harmonogram i pozwolenie w toku.','ktoś po nas','dalej','')],
}

def zasiej(db):
    if db.execute('SELECT COUNT(*) FROM realizacja WHERE demo=1').fetchone()[0]:
        return 'Dane demo już są w bazie - pomijam.'
    for k,(slug,tyt,pod,st,mat,lead,adres,dojazd,lat,lon,cel,ep) in enumerate(OBIEKTY):
        cur = db.execute("""INSERT INTO realizacja
            (slug,tytul,podtytul,status,material,lead,adres,dojazd,lat,lon,cel_mapy,epoka_mapy,
             kolejnosc,opublikowana,demo)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,1,1)""",
            (slug,tyt,pod,st,mat,lead,adres,dojazd,lat,lon,cel,ep,k))
        rid = cur.lastrowid
        for i,(data,t,o,rece,rodz,blok) in enumerate(OSIE[slug]):
            db.execute("""INSERT INTO wpis(realizacja_id,data,tytul,opis,rece,rodzaj,blok,kolejnosc,demo)
                          VALUES(?,?,?,?,?,?,?,?,1)""",(rid,data,t,o,rece,rodz,blok,i))
    log(db,'Zasiano 5 obiektów demo')
    db.commit()
    return f"Zasiano. {ile_demo(db)}"

def zespol(db):
    """Hubert i Maciej to dane prawdziwe (KRS), nie demo - pola puste do uzupełnienia."""
    if db.execute('SELECT COUNT(*) FROM osoba').fetchone()[0]:
        return 'Zespół już jest.'
    for i,(imie,rola) in enumerate([('Hubert Rybkowski','Architekt'),('Maciej Bartkowiak','Architekt')]):
        db.execute('INSERT INTO osoba(imie,rola,kolejnosc,demo) VALUES(?,?,?,0)',(imie,rola,i))
    db.commit()
    return 'Dodano dwie osoby (bez wykształcenia i uprawnień - do uzupełnienia przez Huberta).'

if __name__ == '__main__':
    db = zaloz()
    print(zasiej(db))
    print(zespol(db))
    print('--- obiekty ---')
    for r in db.execute('SELECT slug,tytul,status,demo FROM realizacja ORDER BY kolejnosc'):
        n = db.execute('SELECT COUNT(*) FROM wpis WHERE realizacja_id=(SELECT id FROM realizacja WHERE slug=?)',(r['slug'],)).fetchone()[0]
        print(f"  {r['tytul']:38} {r['status']:16} wpisów: {n}  demo={r['demo']}")
