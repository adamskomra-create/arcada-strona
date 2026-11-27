# -*- coding: utf-8 -*-
"""Wczytuje wygenerowane zdjęcia demo do bazy i dopisuje fikcyjne historie."""
import sys, os, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baza import zaloz, log

ZRODLA = os.environ.get('ARCADA_ZRODLA', '/home/claude/panel/zrodla')
ZDJECIA = os.environ.get('ARCADA_ZDJECIA', '/home/claude/panel/dane/zdjecia')
os.makedirs(ZDJECIA, exist_ok=True)

# slug obiektu -> [(plik, rola, podpis, alt, wpis_po_dacie)]
ZDJ = {
'dwor-lipowiec':[
 ('dwor-przed','przed','','Dwór przed remontem: odpadły tynk, zamurowane okna, dziury w dachu','2025'),
 ('dwor-po','po','','Dwór po remoncie: nowe tynki wapienne, odtworzone okna, naprawiony dach','2025'),
 ('dwor-kolumna','detal','Kolumna portyku · tynk wapienny','Narożnik kolumny toskańskiej po konserwacji','2025'),
 ('dwor-rysunek','rysunek','Elewacja frontowa · arkusz A-04','Rysunek inwentaryzacyjny elewacji frontowej dworu','2025'),
 ('dwor-chmura','detal','Chmura punktów ze skanu','Model punktowy dworu z pomiaru','2025')],
'kamienica-garbarska':[
 ('kamienica-przed','przed','','Elewacja przed remontem: szara wyprawa, skuta sztukateria','2025'),
 ('kamienica-po','po','','Elewacja po remoncie: odtworzona sztukateria i balustrady','2025'),
 ('kamienica-witraz','detal','Witraż klatki schodowej · rekonstrukcja','Secesyjny witraż z motywem irysów, widok od wewnątrz','2025')],
'spichlerz-borowa':[
 ('spichlerz-po','po','','Spichlerz po naprawie konstrukcji szachulcowej','2026'),
 ('spichlerz-zlacze','detal','Złącze ciesielskie · nowy dąb w starym słupie','Nowy rygiel wpuszczony na jaskółczy ogon, widoczna różnica drewna','2026')],
'wieza-cisnien-rudno':[
 ('wieza-przed','przed','','Wieża przed remontem: ubytki cegły, dziurawa blacha, brzozy na gzymsie','2026'),
 ('wieza-po','po','','Wieża po remoncie: przefugowane lico, nowe pokrycie miedziane','2026'),
 ('wieza-fryz','detal','Fryz arkadkowy · uzupełnienia cegłą','Ceglany fryz arkadkowy po konserwacji','2026')],
'oranzeria-zalesie':[
 ('oranzeria-przed','przed','','Oranżeria przed pracami: wybite szyby, zawalony fragment dachu','2026'),
 ('oranzeria-po','po','','Oranżeria po renowacji żeliwa i przeszkleniu','2026')],
}

# dopisywane wpisy: slug -> [(po_jakiej_dacie, data, tytul, opis, rece, rodzaj, blok)]
DOPISKI = {
'dwor-lipowiec':[
 ('2025','2024','Pomiar i dokumentacja','Skan laserowy całej bryły i wnętrz. Z chmury punktów powstał komplet rysunków inwentaryzacyjnych - pierwszy w historii tego dworu.','Arcada Concept','my','galeria')],
'wieza-cisnien-rudno':[
 ('2026','2026','Brzozy z dachu','Na gzymsie i wokół zbiornika wyrosło dziewięć brzóz. Zamiast je wyciąć, zdjęliśmy je z bryłami korzeniowymi i przesadziliśmy u podnóża wieży. Siedem się przyjęło. Rosną teraz tam, gdzie nie rozsadzają muru.','Arcada Concept','my','')],
}

def wczytaj(db):
    n = 0
    for slug, lista in ZDJ.items():
        r = db.execute('SELECT id FROM realizacja WHERE slug=?', (slug,)).fetchone()
        if not r: print('brak obiektu', slug); continue
        rid = r['id']
        if db.execute('SELECT COUNT(*) FROM zdjecie WHERE realizacja_id=?', (rid,)).fetchone()[0]:
            continue
        for k, (plik, rola, podpis, alt, _d) in enumerate(lista):
            zr = os.path.join(ZRODLA, plik + '.webp')
            if not os.path.isfile(zr): print('brak pliku', zr); continue
            nazwa = f'demo-{plik}.webp'
            shutil.copy2(zr, os.path.join(ZDJECIA, nazwa))
            db.execute("""INSERT INTO zdjecie(realizacja_id,plik,podpis,alt,rola,kolejnosc,demo)
                          VALUES(?,?,?,?,?,?,1)""", (rid, nazwa, podpis, alt, rola, k))
            n += 1
    return n

def dopisz(db):
    n = 0
    for slug, lista in DOPISKI.items():
        r = db.execute('SELECT id FROM realizacja WHERE slug=?', (slug,)).fetchone()
        if not r: continue
        rid = r['id']
        for po, data, tyt, opis, rece, rodz, blok in lista:
            if db.execute('SELECT COUNT(*) FROM wpis WHERE realizacja_id=? AND tytul=?',(rid,tyt)).fetchone()[0]:
                continue
            k = db.execute('SELECT kolejnosc FROM wpis WHERE realizacja_id=? AND data=? ORDER BY kolejnosc LIMIT 1',
                           (rid, po)).fetchone()
            poz = (k['kolejnosc'] if k else 0)
            db.execute('UPDATE wpis SET kolejnosc=kolejnosc+1 WHERE realizacja_id=? AND kolejnosc>=?', (rid, poz))
            db.execute("""INSERT INTO wpis(realizacja_id,data,tytul,opis,rece,rodzaj,blok,kolejnosc,demo)
                          VALUES(?,?,?,?,?,?,?,?,1)""", (rid, data, tyt, opis, rece, rodz, blok, poz))
            n += 1
    return n

def bloki(db):
    """Wpisom z pracami nadaje blok porównania i galerii, żeby zdjęcia miały gdzie usiąść."""
    par = [('dwor-lipowiec','Remont konserwatorski','porownanie'),
           ('kamienica-garbarska','Odtworzenie elewacji','porownanie'),
           ('spichlerz-borowa','Naprawa konstrukcji','porownanie'),
           ('wieza-cisnien-rudno','Mur, blacha, stolarka','porownanie'),
           ('oranzeria-zalesie','Inwentaryzacja i projekt','porownanie')]
    for slug, tyt, blok in par:
        db.execute("""UPDATE wpis SET blok=? WHERE tytul=? AND realizacja_id=
                      (SELECT id FROM realizacja WHERE slug=?)""", (blok, tyt, slug))

if __name__ == '__main__':
    db = zaloz()
    z = wczytaj(db); w = dopisz(db); bloki(db)
    log(db, f'Wczytano {z} zdjęć demo, dopisano {w} wpisów'); db.commit()
    print(f'zdjęć: {z}, nowych wpisów: {w}')
    for r in db.execute('SELECT slug,tytul FROM realizacja ORDER BY kolejnosc'):
        nz = db.execute('SELECT COUNT(*) FROM zdjecie WHERE realizacja_id=(SELECT id FROM realizacja WHERE slug=?)',(r['slug'],)).fetchone()[0]
        nw = db.execute('SELECT COUNT(*) FROM wpis WHERE realizacja_id=(SELECT id FROM realizacja WHERE slug=?)',(r['slug'],)).fetchone()[0]
        print(f"  {r['tytul']:38} zdjęć {nz}  wpisów {nw}")
