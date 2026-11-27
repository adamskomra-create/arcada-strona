# -*- coding: utf-8 -*-
"""Model danych panelu Arcada Concept. SQLite, bez ORM."""
import sqlite3, os, json, datetime

SCIEZKA = os.environ.get('ARCADA_DB', '/home/claude/panel/dane/arcada.db')

SCHEMA = """
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS realizacja (
  id          INTEGER PRIMARY KEY,
  slug        TEXT NOT NULL UNIQUE,
  tytul       TEXT NOT NULL,
  podtytul    TEXT NOT NULL DEFAULT '',
  status      TEXT NOT NULL DEFAULT 'w toku',      -- 'odebrana' | 'w toku' | 'w przygotowaniu'
  material    TEXT NOT NULL DEFAULT '',            -- material wiodacy, np. 'cegła i wapno'
  lead        TEXT NOT NULL DEFAULT '',
  -- lokalizacja
  adres       TEXT NOT NULL DEFAULT '',
  dojazd      TEXT NOT NULL DEFAULT '',
  lat         REAL,
  lon         REAL,
  cel_mapy    TEXT NOT NULL DEFAULT '',            -- nazwa do wyszukania w mapach zamiast wspolrzednych
  epoka_mapy  TEXT NOT NULL DEFAULT 'XIX wieku',
  -- dane formalne; puste = pole ukryte na stronie
  inwestor    TEXT NOT NULL DEFAULT '',
  tryb        TEXT NOT NULL DEFAULT '',
  rejestr     TEXT NOT NULL DEFAULT '',
  pozwolenie  TEXT NOT NULL DEFAULT '',
  finansowanie TEXT NOT NULL DEFAULT '',
  wartosc     TEXT NOT NULL DEFAULT '',
  pokaz_wartosc INTEGER NOT NULL DEFAULT 0,        -- wartosc kontraktu bywa poufna
  nadzor      TEXT NOT NULL DEFAULT '',
  kolejnosc   INTEGER NOT NULL DEFAULT 0,
  opublikowana INTEGER NOT NULL DEFAULT 0,
  demo        INTEGER NOT NULL DEFAULT 0,
  utworzono   TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS wpis (
  id          INTEGER PRIMARY KEY,
  realizacja_id INTEGER NOT NULL REFERENCES realizacja(id) ON DELETE CASCADE,
  data        TEXT NOT NULL,                       -- '1766', 'ok. 1906', '30.10.2024', 'Dalej'
  tytul       TEXT NOT NULL,
  opis        TEXT NOT NULL DEFAULT '',
  rece        TEXT NOT NULL DEFAULT '',            -- czyje rece: 'cieśla, nieznany z nazwiska', 'Arcada Concept'
  rodzaj      TEXT NOT NULL DEFAULT 'historia',    -- 'historia' | 'my' | 'pusty' | 'dalej'
  blok        TEXT NOT NULL DEFAULT '',            -- '' | 'lokalizacja' | 'tabela' | 'porownanie' | 'galeria'
  kolejnosc   INTEGER NOT NULL DEFAULT 0,
  demo        INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS zdjecie (
  id          INTEGER PRIMARY KEY,
  realizacja_id INTEGER REFERENCES realizacja(id) ON DELETE CASCADE,
  wpis_id     INTEGER REFERENCES wpis(id) ON DELETE SET NULL,
  plik        TEXT NOT NULL,
  podpis      TEXT NOT NULL DEFAULT '',
  alt         TEXT NOT NULL DEFAULT '',
  rola        TEXT NOT NULL DEFAULT 'detal',       -- 'przed' | 'po' | 'detal' | 'rysunek' | 'dokument' | 'portret'
  kadr        TEXT NOT NULL DEFAULT '50% 50%',
  kolejnosc   INTEGER NOT NULL DEFAULT 0,
  demo        INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS osoba (
  id          INTEGER PRIMARY KEY,
  imie        TEXT NOT NULL,
  rola        TEXT NOT NULL DEFAULT 'Architekt',
  opis        TEXT NOT NULL DEFAULT '',
  wyksztalcenie TEXT NOT NULL DEFAULT '',
  uprawnienia TEXT NOT NULL DEFAULT '',
  portret     TEXT NOT NULL DEFAULT '',
  kolejnosc   INTEGER NOT NULL DEFAULT 0,
  demo        INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS ustawienie (
  klucz       TEXT PRIMARY KEY,
  wartosc     TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS dziennik (
  id          INTEGER PRIMARY KEY,
  kiedy       TEXT NOT NULL DEFAULT (datetime('now')),
  co          TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_wpis_real ON wpis(realizacja_id, kolejnosc);
CREATE INDEX IF NOT EXISTS idx_zdj_real  ON zdjecie(realizacja_id, kolejnosc);
"""

def polacz():
    os.makedirs(os.path.dirname(SCIEZKA), exist_ok=True)
    db = sqlite3.connect(SCIEZKA)
    db.row_factory = sqlite3.Row
    db.execute('PRAGMA foreign_keys=ON')
    return db

def zaloz():
    db = polacz()
    db.executescript(SCHEMA)
    # migracje dokladane po fakcie - bezpieczne przy istniejacej bazie
    kol = {r[1] for r in db.execute('PRAGMA table_info(realizacja)')}
    if 'nadzor' not in kol:
        db.execute("ALTER TABLE realizacja ADD COLUMN nadzor TEXT NOT NULL DEFAULT ''")
    db.commit()
    return db

def log(db, co):
    db.execute('INSERT INTO dziennik(co) VALUES(?)', (co,))

def ile_demo(db):
    """Ile rekordow demo siedzi w bazie - panel pokazuje to na banerze."""
    w = {}
    for t in ('realizacja','wpis','zdjecie','osoba'):
        w[t] = db.execute(f'SELECT COUNT(*) FROM {t} WHERE demo=1').fetchone()[0]
    w['razem'] = sum(w.values())
    return w

def usun_demo(db, katalog_zdjec=None):
    """Kasuje wszystkie rekordy demo razem z plikami zdjec. Nie rusza danych wlasnych."""
    pliki = [r[0] for r in db.execute('SELECT plik FROM zdjecie WHERE demo=1').fetchall()]
    # kasacja kaskadowa: realizacja pociaga wpisy i zdjecia
    db.execute('DELETE FROM realizacja WHERE demo=1')
    for t in ('wpis','zdjecie','osoba'):
        db.execute(f'DELETE FROM {t} WHERE demo=1')
    usuniete = 0
    if katalog_zdjec:
        for p in pliki:
            sc = os.path.join(katalog_zdjec, p)
            if os.path.isfile(sc):
                try: os.remove(sc); usuniete += 1
                except OSError: pass
    log(db, f'Usunięto dane demo: {len(pliki)} zdjęć w bazie, {usuniete} plików z dysku')
    db.commit()
    return {'zdjecia_w_bazie': len(pliki), 'pliki_usuniete': usuniete}

if __name__ == '__main__':
    db = zaloz()
    tab = [r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
    print('tabele:', ', '.join(tab))
    print('demo:', ile_demo(db))
