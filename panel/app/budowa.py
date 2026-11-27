# -*- coding: utf-8 -*-
"""Buduje statyczne pliki strony z danych w bazie.

Dwa wyjścia:
  publiczne/  - bez rekordów demo, to idzie na arcadaconcept.pl
  podglad/    - z rekordami demo, to idzie za hasło
"""
import os, sys, shutil

TU = os.path.dirname(os.path.abspath(__file__))
STRONA = os.environ.get('ARCADA_STRONA', os.path.join(os.path.dirname(TU), 'strona'))
WYNIK  = os.environ.get('ARCADA_WYNIK',  os.path.join(os.path.dirname(TU), 'wynik'))
ZDJECIA = os.environ.get('ARCADA_ZDJECIA', os.path.join(os.path.dirname(TU), 'dane', 'zdjecia'))

def _obiekty(db, z_demo):
    war = '' if z_demo else ' AND demo=0'
    rz = db.execute(f'SELECT * FROM realizacja WHERE opublikowana=1{war} ORDER BY kolejnosc, id').fetchall()
    out = []
    for r in rz:
        o = dict(r)
        o['wpisy'] = [dict(x) for x in db.execute(
            'SELECT * FROM wpis WHERE realizacja_id=? ORDER BY kolejnosc, id', (r['id'],)).fetchall()]
        o['zdjecia'] = [dict(x) for x in db.execute(
            'SELECT * FROM zdjecie WHERE realizacja_id=? ORDER BY kolejnosc, id', (r['id'],)).fetchall()]
        out.append(o)
    return out

def _kopiuj_zdjecia(out):
    """Zdjęcia z panelu lądują w img/ obok tych wbudowanych."""
    cel = os.path.join(out, 'img')
    os.makedirs(cel, exist_ok=True)
    n = 0
    if os.path.isdir(ZDJECIA):
        for f in os.listdir(ZDJECIA):
            z = os.path.join(ZDJECIA, f)
            if os.path.isfile(z):
                shutil.copy2(z, os.path.join(cel, f)); n += 1
    return n

def _jedno(db, katalog, z_demo):
    if STRONA not in sys.path:
        sys.path.insert(0, STRONA)
    for m in ('gen', 'b', 'mapa', 'dane'):
        sys.modules.pop(m, None)
    import gen
    gen.OBIEKTY_Z_BAZY = _obiekty(db, z_demo)
    n = gen.zbuduj_pliki(katalog)
    _kopiuj_zdjecia(katalog)
    return n

def zbuduj(db, z_demo=True):
    """Jedno wyjście. Domyślnie z obiektami demo - każdy ma widoczną plakietkę
    'wizualizacja poglądowa · obiekt fikcyjny'. Po wyczyszczeniu danych demo
    w panelu znikają same, bez żadnego przełącznika."""
    return _jedno(db, os.path.join(WYNIK, 'strona'), z_demo=z_demo)

if __name__ == '__main__':
    sys.path.insert(0, TU)
    from baza import zaloz
    d = zaloz()
    print('zbudowano', zbuduj(d), 'plików w', WYNIK)
