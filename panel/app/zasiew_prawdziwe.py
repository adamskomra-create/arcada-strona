# -*- coding: utf-8 -*-
"""Kościelec i Dębno - realizacje prawdziwe, demo=0. Nie znikają przy czyszczeniu demo."""
import sys, os, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baza import zaloz, log

ZRODLO_IMG = '/home/claude/w4/img'
ZDJECIA = os.environ.get('ARCADA_ZDJECIA', '/home/claude/panel/dane/zdjecia')

OBIEKTY = [
 dict(slug='kaplica-koscielec', tytul='Kaplica cmentarna z kryptą w Kościelcu',
      podtytul='Cegła, wapno i okucia', status='odebrana', material='cegła, wapno, mosiądz',
      lead='Remont kaplicy wraz z kryptą, prowadzony w całości przez nas.',
      adres='Cmentarz parafialny, ul. Długa<br>Kościelec, gm. Kościelec<br>pow. kolski, woj. wielkopolskie',
      dojazd='Około 6 km na południowy zachód od Koła, 116 km na wschód od Poznania. '
             'Kaplica stoi na cmentarzu parafialnym - można podejść i obejrzeć z zewnątrz o każdej porze.',
      lat=52.17444, lon=18.57, cel_mapy='', epoka_mapy='XIX wieku',
      inwestor='Gmina Kościelec', tryb='Przetarg publiczny, 2024/BZP 00090607',
      nadzor='Wielkopolski Wojewódzki Konserwator Zabytków',
      wartosc='1 017 210 zł', pokaz_wartosc=0, kolejnosc=-20),
 dict(slug='kosciol-debno', tytul='Drewniany kościół św. Michała Archanioła w Dębnie',
      podtytul='Drewno, gont i miedź', status='w toku', material='drewno, gont, miedź',
      lead='Szalowanie ścian, gontowe pokrycie dachu i miedziana sygnaturka. Obiekt z 1766 roku.',
      adres='Kościół św. Michała Archanioła<br>Dębno Poproboszczowskie, gm. Babiak<br>pow. kolski, woj. wielkopolskie',
      dojazd='Około 5 km na południe od Babiaka, 12 km na północ od Koła i 120 km na wschód od Poznania. '
             'Parafia nosi nazwę „w Dębnie Królewskim”, ale sam kościół stoi w sąsiednim Dębnie '
             'Poproboszczowskim, tuż przy zachodniej granicy wsi.',
      lat=52.303889, lon=18.675278,
      cel_mapy='Kościół św. Michała Archanioła, Dębno Poproboszczowskie, gmina Babiak',
      epoka_mapy='przełomu XIX i XX wieku',
      inwestor='Parafia św. Michała Archanioła w Dębnie Królewskim', rejestr='nr 107/692/A',
      pozwolenie='WWKZ Delegatura w Koninie, nr 171/2024/A',
      finansowanie='Rządowy Program Odbudowy Zabytków',
      wartosc='', pokaz_wartosc=0, kolejnosc=-10),
]

OSIE = {
'kaplica-koscielec':[
 ('XIX w.','Obiekt powstaje','Kaplica cmentarna figuruje w Gminnej Ewidencji Zabytków jako obiekt z XIX wieku. Dokładną datę i materiał uzupełnimy z karty ewidencyjnej.','budowniczy, nieznany z nazwiska','historia',''),
 ('[rok]','Wpis do rejestru zabytków','Numer i data decyzji. Od tego momentu każda zmiana wymaga zgody konserwatora.','konserwator','pusty',''),
 ('2024','Przetarg i umowa','Postępowanie 2024/BZP 00090607. Inwestorem jest Gmina Kościelec, nadzór sprawuje Wielkopolski Wojewódzki Konserwator Zabytków.','Arcada Concept','my','lokalizacja'),
 ('2024','Prace','Osuszenie i odsolenie muru, uzupełnienia cegłą dobraną pod wymiar i wypał, tynki wapienne, renowacja stolarki i okuć, uporządkowanie otoczenia.','Arcada Concept','my','porownanie'),
 ('12.06.2025','Odbiór','Odebrane w terminie umownym, z poświadczeniem wystawionym przez inwestora.','Arcada Concept','my','tabela'),
 ('Dalej','Obiekt ma przetrwać kolejne sto lat','Dokumentacja powykonawcza, zalecenia do przeglądów, kontakt na wypadek gdyby coś zaczęło się dziać.','ktoś po nas','dalej','')],
'kosciol-debno':[
 ('1766','Kościół powstaje','Drewniany kościół parafialny pod wezwaniem świętego Michała Archanioła. Konstrukcja zrębowa, szalowana deskami, dach kryty gontem.','cieśla, nieznany z nazwiska','historia',''),
 ('ok. 1906','Rozbudowa','Kościół zostaje powiększony. Z tego etapu pochodzi znaczna część dzisiejszej bryły.','ówczesna parafia','historia',''),
 ('[rok]','Wpis do rejestru zabytków','Numer decyzji to 107/692/A. Datę wpisu uzupełnimy z karty ewidencyjnej.','konserwator','pusty',''),
 ('08.2024','Umowa z parafią','Inwestorem jest parafia, prace finansowane z Rządowego Programu Odbudowy Zabytków. Umowa podpisana 2 sierpnia 2024.','Arcada Concept','my','lokalizacja'),
 ('2024','Prace przy drewnie','Dezynfekcja, usunięcie starych powłok, wymiana uszkodzonych elementów szalowania i impregnacja. Nowe pokrycie dachu gontem.','Arcada Concept','my','tabela'),
 ('30.10.2024','Odbiór pierwszego etapu','Pierwszy etap odebrany w terminie.','Arcada Concept','my',''),
 ('04.2025','Sygnaturka i zakończenie','Nowe miedziane pokrycie sygnaturki. Umowny termin zakończenia całości to 1 kwietnia 2025 - potwierdzimy odbiór końcowy.','Arcada Concept','my',''),
 ('Dalej','Drewno wymaga nadzoru','Gont i szalowanie trzeba oglądać regularnie. Zostaje zestaw zaleceń i kontakt.','ktoś po nas','dalej','')],
}

ZDJ = {
'kaplica-koscielec':[
 ('kaplica-koscielec-krypta-przed-kadr-938.webp','przed','','Kaplica od strony krypty przed remontem'),
 ('kaplica-koscielec-krypta-po-kadr-938.webp','po','','Ten sam widok po remoncie'),
 ('kolatka-mosiadz-1280.webp','detal','Kołatka · rekonstrukcja mosiądzu','Mosiężna kołatka po rekonstrukcji'),
 ('luk-portalu-cegla-1280.webp','detal','Łuk portalu · uzupełnienia muru','Ceglany łuk portalu po uzupełnieniach'),
 ('drzwi-krypty-1280.webp','detal','Drzwi krypty · renowacja z okuciami','Drewniane drzwi krypty po renowacji'),
 ('elewacja-a04-rysunek-1280.webp','rysunek','Elewacja · arkusz A-04','Rysunek elewacji, arkusz A-04'),
 ('poswiadczenie-gmina-koscielec-600.webp','dokument','Poświadczenie odbioru','Poświadczenie realizacji wystawione przez Gminę Kościelec')],
}

def zasiej(db):
    os.makedirs(ZDJECIA, exist_ok=True)
    n = z = 0
    for o in OBIEKTY:
        if db.execute('SELECT COUNT(*) FROM realizacja WHERE slug=?', (o['slug'],)).fetchone()[0]:
            continue
        kol = ','.join(o.keys()); pyt = ','.join('?' * len(o))
        cur = db.execute(f'INSERT INTO realizacja({kol},opublikowana,demo) VALUES({pyt},1,0)', tuple(o.values()))
        rid = cur.lastrowid; n += 1
        for i, (d, t, op, r, rodz, bl) in enumerate(OSIE[o['slug']]):
            db.execute("""INSERT INTO wpis(realizacja_id,data,tytul,opis,rece,rodzaj,blok,kolejnosc,demo)
                          VALUES(?,?,?,?,?,?,?,?,0)""", (rid, d, t, op, r, rodz, bl, i))
        for i, (plik, rola, podpis, alt) in enumerate(ZDJ.get(o['slug'], [])):
            zr = os.path.join(ZRODLO_IMG, plik)
            if not os.path.isfile(zr): print('brak', plik); continue
            shutil.copy2(zr, os.path.join(ZDJECIA, plik))
            db.execute("""INSERT INTO zdjecie(realizacja_id,plik,podpis,alt,rola,kolejnosc,demo)
                          VALUES(?,?,?,?,?,?,0)""", (rid, plik, podpis, alt, rola, i))
            z += 1
    log(db, f'Dodano {n} realizacji prawdziwych, {z} zdjęć'); db.commit()
    return n, z

if __name__ == '__main__':
    db = zaloz()
    n, z = zasiej(db)
    print(f'obiektów: {n}, zdjęć: {z}')
    print(f"{'OBIEKT':40} {'DEMO':5} WPISY ZDJ")
    for r in db.execute('SELECT * FROM realizacja ORDER BY kolejnosc, id'):
        w = db.execute('SELECT COUNT(*) FROM wpis WHERE realizacja_id=?', (r['id'],)).fetchone()[0]
        zz = db.execute('SELECT COUNT(*) FROM zdjecie WHERE realizacja_id=?', (r['id'],)).fetchone()[0]
        print(f"{r['tytul'][:39]:40} {'tak' if r['demo'] else 'nie':5} {w:5} {zz:3}")
