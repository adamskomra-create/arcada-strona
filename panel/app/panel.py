# -*- coding: utf-8 -*-
import sys, os, re, io, secrets, functools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, request, redirect, session, url_for, send_from_directory, abort
from markupsafe import escape
from werkzeug.utils import secure_filename
import bcrypt
from PIL import Image, ImageOps
from baza import zaloz, polacz, log, ile_demo, usun_demo
from szablon import strona, ZIE, MUT

ZDJECIA = os.environ.get('ARCADA_ZDJECIA', '/home/claude/panel/dane/zdjecia')
os.makedirs(ZDJECIA, exist_ok=True)
app = Flask(__name__)
app.secret_key = os.environ.get('ARCADA_SECRET') or secrets.token_hex(32)
app.config['MAX_CONTENT_LENGTH'] = 40 * 1024 * 1024

STATUSY = ['odebrana', 'w toku', 'w przygotowaniu']
RODZAJE = [('historia','Historia obiektu'), ('my','Nasze wejście'),
           ('pusty','Puste - do uzupełnienia'), ('dalej','Co dalej')]
BLOKI   = [('','bez dodatków'), ('lokalizacja','mapka i nawigacja'), ('tabela','tabela danych'),
           ('porownanie','suwak przed i po'), ('galeria','galeria zdjęć')]
ROLE    = [('przed','przed'), ('po','po'), ('detal','detal'), ('rysunek','rysunek'),
           ('dokument','dokument'), ('portret','portret')]

def db():
    if 'db' not in session.__class__.__dict__:
        pass
    return zaloz()

def haslo_hash(d):
    r = d.execute("SELECT wartosc FROM ustawienie WHERE klucz='haslo'").fetchone()
    return r['wartosc'] if r else ''

def zalogowany(f):
    @functools.wraps(f)
    def g(*a, **k):
        if not session.get('ok'):
            return redirect(url_for('logowanie'))
        return f(*a, **k)
    return g

def pole(nazwa, etykieta, wartosc='', typ='text', pod='', opcje=None, wiersze=None):
    w = escape(wartosc or '')
    e = f'<em>{escape(pod)}</em>' if pod else ''
    if opcje is not None:
        o = ''.join(f'<option value="{escape(v)}"{" selected" if v==wartosc else ""}>{escape(t)}</option>'
                    for v, t in opcje)
        k = f'<select name="{nazwa}">{o}</select>'
    elif wiersze:
        k = f'<textarea name="{nazwa}" rows="{wiersze}">{w}</textarea>'
    else:
        k = f'<input type="{typ}" name="{nazwa}" value="{w}">'
    return f'<label><span>{escape(etykieta)}</span>{k}{e}</label>'

def slugify(s):
    s = s.lower()
    for a, b in zip('ąćęłńóśźż', 'acelnoszz'):
        s = s.replace(a, b)
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s or 'obiekt'

# ---------------- logowanie ----------------
@app.route('/logowanie', methods=['GET','POST'])
def logowanie():
    d = zaloz()
    h = haslo_hash(d)
    blad = ''
    if request.method == 'POST':
        p = request.form.get('haslo','').encode()
        if not h:
            d.execute("INSERT OR REPLACE INTO ustawienie(klucz,wartosc) VALUES('haslo',?)",
                      (bcrypt.hashpw(p, bcrypt.gensalt()).decode(),))
            log(d, 'Ustawiono hasło panelu'); d.commit()
            session['ok'] = True
            return redirect('/')
        if bcrypt.checkpw(p, h.encode()):
            session['ok'] = True
            return redirect('/')
        blad = 'Hasło nie pasuje.'
    tytul = 'Ustaw hasło' if not h else 'Zaloguj się'
    podp = ('Panel nie ma jeszcze hasła. To, które teraz wpiszesz, zostanie zapisane.'
            if not h else 'Podaj hasło do panelu.')
    b = f'<p style="color:#A33A2C;margin-bottom:12px">{blad}</p>' if blad else ''
    from szablon import CSS, sygnet
    return f"""<!doctype html><html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>{tytul} · Panel Arcada</title><style>{CSS}</style></head>
<body style="display:flex;align-items:center;justify-content:center;min-height:100vh">
<form method="post" class="karta" style="width:100%;max-width:380px;padding:30px">
{sygnet(ZIE,34)}<h1 style="margin-top:18px;font-size:22px">{tytul}</h1>
<p class="lead" style="margin-bottom:20px">{podp}</p>{b}
<label><span>Hasło</span><input type="password" name="haslo" autofocus required minlength="8"></label>
<button class="btn" style="width:100%;justify-content:center">{tytul}</button></form></body></html>"""

@app.route('/wyloguj')
def wyloguj():
    session.clear()
    return redirect(url_for('logowanie'))

# ---------------- lista realizacji ----------------
@app.route('/')
@zalogowany
def lista():
    d = zaloz()
    rz = d.execute('SELECT * FROM realizacja ORDER BY kolejnosc, id').fetchall()
    if rz:
        w = ''
        for r in rz:
            n = d.execute('SELECT COUNT(*) FROM wpis WHERE realizacja_id=?', (r['id'],)).fetchone()[0]
            z = d.execute('SELECT COUNT(*) FROM zdjecie WHERE realizacja_id=?', (r['id'],)).fetchone()[0]
            if r['demo']:
                pl = '<span class="plakietka">demo</span>'
                op = '<span class="plakietka szara">tylko podgląd</span>'
            else:
                pl = ''
                op = ('<span class="plakietka st">na stronie</span>' if r['opublikowana']
                      else '<span class="plakietka szara">szkic</span>')
            w += (f'<tr class="{"demo" if r["demo"] else ""}"><td><strong>{escape(r["tytul"])}</strong>'
                  f'<div class="cichy">{escape(r["podtytul"])}</div></td>'
                  f'<td>{escape(r["status"])}</td><td>{n} wpisów<br><span class="cichy">{z} zdjęć</span></td>'
                  f'<td>{op} {pl}</td>'
                  f'<td style="text-align:right"><a class="btn b2 maly" href="/obiekt/{r["id"]}">Edytuj</a></td></tr>')
        tresc = (f'<div class="rzad" style="margin-bottom:18px"><div><h1>Realizacje</h1>'
                 f'<p class="lead">Każdy obiekt ma własną oś czasu. Kolejność na stronie ustala pole „Kolejność”.</p></div>'
                 f'<form method="post" action="/obiekt/nowy" class="rozc"><button class="btn">Dodaj obiekt</button></form></div>'
                 f'<div class="karta"><table><thead><tr><th>Obiekt</th><th>Status</th><th>Zawartość</th>'
                 f'<th>Widoczność</th><th></th></tr></thead><tbody>{w}</tbody></table></div>'
                 f'<p style="margin-top:18px"><form method="post" action="/generuj">'
                 f'<button class="btn b2">Przebuduj stronę</button></form></p>')
    else:
        tresc = ('<h1>Realizacje</h1><div class="pusto" style="margin-top:18px">'
                 '<p>Nie ma jeszcze żadnego obiektu.</p>'
                 '<form method="post" action="/obiekt/nowy" style="margin-top:16px">'
                 '<button class="btn">Dodaj pierwszy obiekt</button></form></div>')
    return strona('Realizacje', tresc, '/', ile_demo(d)['razem'], session.pop('flash', None), ile_demo(d))

# ---------------- edycja obiektu ----------------
@app.route('/obiekt/nowy', methods=['POST'])
@zalogowany
def nowy():
    d = zaloz()
    k = d.execute('SELECT COALESCE(MAX(kolejnosc),0)+1 FROM realizacja').fetchone()[0]
    s = f'obiekt-{secrets.token_hex(3)}'
    cur = d.execute('INSERT INTO realizacja(slug,tytul,kolejnosc) VALUES(?,?,?)', (s, 'Nowy obiekt', k))
    d.commit()
    return redirect(f'/obiekt/{cur.lastrowid}')

@app.route('/obiekt/<int:rid>')
@zalogowany
def obiekt(rid):
    d = zaloz()
    r = d.execute('SELECT * FROM realizacja WHERE id=?', (rid,)).fetchone()
    if not r: abort(404)
    wp = d.execute('SELECT * FROM wpis WHERE realizacja_id=? ORDER BY kolejnosc, id', (rid,)).fetchall()
    zd = d.execute('SELECT * FROM zdjecie WHERE realizacja_id=? ORDER BY kolejnosc, id', (rid,)).fetchall()

    pl = '<span class="plakietka">obiekt demo</span>' if r['demo'] else ''
    glowa = (f'<div class="rzad" style="margin-bottom:18px"><div><h1>{escape(r["tytul"])} {pl}</h1>'
             f'<p class="lead">{escape(r["podtytul"] or "Bez podtytułu")}</p></div>'
             f'<a class="btn b2 rozc" href="/">Wróć do listy</a></div>')

    f1 = (f'<form method="post" action="/obiekt/{rid}/zapisz"><div class="karta"><h2>Obiekt</h2>'
          f'<p class="lead">To, co widać w nagłówku sekcji na stronie.</p><div style="margin-top:16px">'
          + pole('tytul','Nazwa obiektu',r['tytul'])
          + f'<div class="pola2">' + pole('podtytul','Podtytuł',r['podtytul'],pod='np. „Tynk wapienny i stolarka”')
          + pole('material','Materiał wiodący',r['material'],pod='do opisu i filtrowania') + '</div>'
          + pole('lead','Zdanie wprowadzające',r['lead'],wiersze=2)
          + f'<div class="pola3">' + pole('status','Status',r['status'],opcje=[(s,s) for s in STATUSY])
          + pole('kolejnosc','Kolejność',str(r['kolejnosc']),typ='number')
          + pole('opublikowana','Na stronie publicznej',str(r['opublikowana']),
                 opcje=[('1','tak, pokazuj'),('0','nie, zostaw jako szkic')]) + '</div></div></div>'
          f'<div class="karta"><h2>Gdzie to jest</h2>'
          f'<p class="lead">Mapka i przycisk „Nawiguj” pokazują się tylko, gdy wypełnisz adres.</p><div style="margin-top:16px">'
          + pole('adres','Adres',r['adres'],wiersze=2,pod='Można użyć &lt;br&gt; do łamania wierszy')
          + pole('dojazd','Jak dojechać',r['dojazd'],wiersze=2,pod='Odległości od większych miast, czy można obejrzeć z zewnątrz')
          + '<div class="pola3">' + pole('lat','Szerokość geogr.',('' if r['lat'] is None else str(r['lat'])),pod='np. 52.17444')
          + pole('lon','Długość geogr.',('' if r['lon'] is None else str(r['lon'])),pod='np. 18.57')
          + pole('epoka_mapy','Mapa z epoki',r['epoka_mapy'],pod='opis okresu w ramce') + '</div>'
          + pole('cel_mapy','Nazwa do wyszukania w mapach',r['cel_mapy'],
                 pod='Zostaw puste, żeby użyć współrzędnych. Wpisz nazwę, gdy współrzędne są niepewne.')
          + '</div></div>'
          f'<div class="karta"><h2>Dane formalne</h2>'
          f'<p class="lead">Puste pola nie pokazują się na stronie - nie zostawiamy tam kresek ani „brak danych”.</p>'
          f'<div style="margin-top:16px"><div class="pola2">'
          + pole('inwestor','Inwestor',r['inwestor']) + pole('tryb','Tryb',r['tryb'],pod='np. przetarg publiczny i numer')
          + pole('rejestr','Rejestr zabytków',r['rejestr']) + pole('pozwolenie','Pozwolenie konserwatorskie',r['pozwolenie'])
          + pole('nadzor','Nadzór',r['nadzor'],pod='np. Wielkopolski Wojewódzki Konserwator Zabytków')
          + pole('finansowanie','Finansowanie',r['finansowanie']) + pole('wartosc','Wartość kontraktu',r['wartosc'])
          + '</div>' + pole('pokaz_wartosc','Pokazywać wartość kontraktu',str(r['pokaz_wartosc']),
                 opcje=[('0','nie - domyślnie'),('1','tak, inwestor się zgodził')],
                 pod='Kwoty kontraktów bywają poufne. Pytaj inwestora, zanim włączysz.')
          + '</div></div><p><button class="btn">Zapisz obiekt</button></p></form>')

    # --- os czasu ---
    lw = ''
    for w in wp:
        kl = {'my':'my','pusty':'pusty'}.get(w['rodzaj'],'')
        rece = f'<span class="cichy"> · {escape(w["rece"])}</span>' if w['rece'] else ''
        blok = f'<span class="plakietka szara">{escape(dict(BLOKI).get(w["blok"],""))}</span>' if w['blok'] else ''
        lw += (f'<li class="wp {kl}"><div class="gl"><span class="dt">{escape(w["data"])}</span>'
               f'<span class="tt">{escape(w["tytul"])}</span>{rece}<span class="rozc">{blok}'
               f' <a class="btn b2 maly" href="/wpis/{w["id"]}">Edytuj</a></span></div>'
               f'<p class="cichy" style="margin-top:6px">{escape(w["opis"][:150])}{"…" if len(w["opis"])>150 else ""}</p></li>')
    if not lw:
        lw = '<li class="pusto">Oś czasu jest pusta. Dodaj pierwszy wpis - np. rok powstania obiektu.</li>'
    f2 = (f'<div class="karta"><div class="rzad"><div><h2>Oś czasu obiektu</h2>'
          f'<p class="lead">Pełny ciąg rąk, które dotykały budynku. Wasze wejście to jeden z wpisów, nie cała historia.</p></div>'
          f'<form method="post" action="/obiekt/{rid}/wpis/nowy" class="rozc"><button class="btn b2">Dodaj wpis</button></form></div>'
          f'<ul class="lista-wpisow" style="margin-top:16px">{lw}</ul></div>')

    # --- zdjecia ---
    mz = ''.join(f'<a href="/zdjecie/{z["id"]}" title="{escape(z["podpis"])}">'
                 f'<img src="/zdjecia/{escape(z["plik"])}" alt="{escape(z["alt"])}"></a>' for z in zd)
    f3 = (f'<div class="karta"><h2>Zdjęcia</h2>'
          f'<p class="lead">Wgrane pliki są zmniejszane i zapisywane jako WebP. Maksymalnie 40 MB na plik.</p>'
          f'<div class="mini">{mz or "<span class=cichy>Brak zdjęć.</span>"}</div>'
          f'<form method="post" action="/obiekt/{rid}/zdjecie" enctype="multipart/form-data" style="margin-top:16px">'
          f'<div class="pola2">'
          f'<label><span>Pliki</span><input type="file" name="pliki" accept="image/*" multiple required></label>'
          + pole('rola','Rola','detal',opcje=ROLE) + '</div>'
          f'<button class="btn b2">Wgraj</button></form></div>')

    usun = (f'<div class="karta" style="border-color:#E6C9C3"><h2>Usuń obiekt</h2>'
            f'<p class="lead">Kasuje obiekt razem z osią czasu i zdjęciami. Tego nie da się cofnąć.</p>'
            f'<form method="post" action="/obiekt/{rid}/usun" style="margin-top:14px" '
            f'onsubmit="return confirm(\'Usunąć ten obiekt na zawsze?\')">'
            f'<button class="btn zly">Usuń obiekt</button></form></div>')

    return strona(r['tytul'], glowa + f1 + f2 + f3 + usun, '/', ile_demo(d)['razem'], session.pop('flash', None), ile_demo(d))

@app.route('/obiekt/<int:rid>/zapisz', methods=['POST'])
@zalogowany
def zapisz(rid):
    d = zaloz(); f = request.form
    def licz(x):
        try: return float(f.get(x,'').replace(',','.'))
        except ValueError: return None
    d.execute("""UPDATE realizacja SET tytul=?,podtytul=?,material=?,lead=?,status=?,kolejnosc=?,
        opublikowana=?,adres=?,dojazd=?,lat=?,lon=?,epoka_mapy=?,cel_mapy=?,
        inwestor=?,tryb=?,rejestr=?,pozwolenie=?,nadzor=?,finansowanie=?,wartosc=?,pokaz_wartosc=?,slug=? WHERE id=?""",
        (f.get('tytul','').strip() or 'Bez nazwy', f.get('podtytul','').strip(), f.get('material','').strip(),
         f.get('lead','').strip(), f.get('status','w toku'), int(f.get('kolejnosc') or 0),
         int(f.get('opublikowana') or 0), f.get('adres','').strip(), f.get('dojazd','').strip(),
         licz('lat'), licz('lon'), f.get('epoka_mapy','').strip(), f.get('cel_mapy','').strip(),
         f.get('inwestor','').strip(), f.get('tryb','').strip(), f.get('rejestr','').strip(),
         f.get('pozwolenie','').strip(), f.get('nadzor','').strip(),
         f.get('finansowanie','').strip(), f.get('wartosc','').strip(),
         int(f.get('pokaz_wartosc') or 0), slugify(f.get('tytul','')), rid))
    log(d, f'Zapisano obiekt {rid}'); d.commit()
    session['flash'] = 'Zapisane.'
    return redirect(f'/obiekt/{rid}')

@app.route('/obiekt/<int:rid>/usun', methods=['POST'])
@zalogowany
def usun_obiekt(rid):
    d = zaloz()
    for z in d.execute('SELECT plik FROM zdjecie WHERE realizacja_id=?', (rid,)).fetchall():
        p = os.path.join(ZDJECIA, z['plik'])
        if os.path.isfile(p):
            try: os.remove(p)
            except OSError: pass
    d.execute('DELETE FROM realizacja WHERE id=?', (rid,))
    log(d, f'Usunięto obiekt {rid}'); d.commit()
    session['flash'] = 'Obiekt usunięty.'
    return redirect('/')

# ---------------- wpisy osi czasu ----------------
@app.route('/obiekt/<int:rid>/wpis/nowy', methods=['POST'])
@zalogowany
def wpis_nowy(rid):
    d = zaloz()
    k = d.execute('SELECT COALESCE(MAX(kolejnosc),0)+1 FROM wpis WHERE realizacja_id=?', (rid,)).fetchone()[0]
    cur = d.execute('INSERT INTO wpis(realizacja_id,data,tytul,kolejnosc) VALUES(?,?,?,?)',
                    (rid, '[rok]', 'Nowy wpis', k))
    d.commit()
    return redirect(f'/wpis/{cur.lastrowid}')

@app.route('/wpis/<int:wid>', methods=['GET','POST'])
@zalogowany
def wpis(wid):
    d = zaloz()
    w = d.execute('SELECT * FROM wpis WHERE id=?', (wid,)).fetchone()
    if not w: abort(404)
    if request.method == 'POST':
        f = request.form
        d.execute("""UPDATE wpis SET data=?,tytul=?,opis=?,rece=?,rodzaj=?,blok=?,kolejnosc=? WHERE id=?""",
                  (f.get('data','').strip() or '[rok]', f.get('tytul','').strip() or 'Bez tytułu',
                   f.get('opis','').strip(), f.get('rece','').strip(), f.get('rodzaj','historia'),
                   f.get('blok',''), int(f.get('kolejnosc') or 0), wid))
        log(d, f'Zapisano wpis {wid}'); d.commit()
        session['flash'] = 'Wpis zapisany.'
        return redirect(f'/obiekt/{w["realizacja_id"]}')
    r = d.execute('SELECT tytul FROM realizacja WHERE id=?', (w['realizacja_id'],)).fetchone()
    tresc = (f'<div class="rzad" style="margin-bottom:18px"><div><h1>Wpis na osi czasu</h1>'
             f'<p class="lead">{escape(r["tytul"])}</p></div>'
             f'<a class="btn b2 rozc" href="/obiekt/{w["realizacja_id"]}">Wróć do obiektu</a></div>'
             f'<form method="post"><div class="karta"><div class="pola3">'
             + pole('data','Data',w['data'],pod='„1766”, „ok. 1906”, „30.10.2024”, „Dalej”')
             + pole('rodzaj','Rodzaj wpisu',w['rodzaj'],opcje=RODZAJE)
             + pole('kolejnosc','Kolejność',str(w['kolejnosc']),typ='number') + '</div>'
             + pole('tytul','Tytuł',w['tytul'])
             + pole('opis','Opis',w['opis'],wiersze=5)
             + pole('rece','Czyje ręce',w['rece'],
                    pod='Kto wtedy dotykał budynku: „cieśla, nieznany z nazwiska”, „spółdzielnia”, „Arcada Concept”, „ktoś po nas”')
             + pole('blok','Dodatkowy blok pod wpisem',w['blok'],opcje=BLOKI)
             + '</div><p class="rzad"><button class="btn">Zapisz wpis</button>'
             f'<form method="post" action="/wpis/{wid}/usun" class="rozc" '
             f'onsubmit="return confirm(\'Usunąć ten wpis?\')"><button class="btn zly maly">Usuń wpis</button></form>'
             '</p></form>')
    return strona('Wpis', tresc, '/', ile_demo(d)['razem'], None, ile_demo(d))

@app.route('/wpis/<int:wid>/usun', methods=['POST'])
@zalogowany
def wpis_usun(wid):
    d = zaloz()
    w = d.execute('SELECT realizacja_id FROM wpis WHERE id=?', (wid,)).fetchone()
    if not w: abort(404)
    d.execute('DELETE FROM wpis WHERE id=?', (wid,)); log(d, f'Usunięto wpis {wid}'); d.commit()
    session['flash'] = 'Wpis usunięty.'
    return redirect(f'/obiekt/{w["realizacja_id"]}')

# ---------------- zdjecia ----------------
def przeskaluj(dane, szer=1600):
    im = Image.open(io.BytesIO(dane))
    im = ImageOps.exif_transpose(im)
    if im.mode not in ('RGB','L'): im = im.convert('RGB')
    if im.width > szer:
        im = im.resize((szer, round(im.height*szer/im.width)), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, 'WEBP', quality=82, method=5)
    return buf.getvalue(), im.size

@app.route('/obiekt/<int:rid>/zdjecie', methods=['POST'])
@zalogowany
def zdjecie_wgraj(rid):
    d = zaloz()
    rola = request.form.get('rola','detal')
    n = 0
    for f in request.files.getlist('pliki'):
        if not f or not f.filename: continue
        try:
            dane, rozm = przeskaluj(f.read())
        except Exception:
            continue
        nazwa = f'{secrets.token_hex(8)}.webp'
        with open(os.path.join(ZDJECIA, nazwa), 'wb') as g: g.write(dane)
        k = d.execute('SELECT COALESCE(MAX(kolejnosc),0)+1 FROM zdjecie WHERE realizacja_id=?',(rid,)).fetchone()[0]
        d.execute('INSERT INTO zdjecie(realizacja_id,plik,rola,kolejnosc,alt) VALUES(?,?,?,?,?)',
                  (rid, nazwa, rola, k, secure_filename(f.filename).rsplit('.',1)[0][:80]))
        n += 1
    log(d, f'Wgrano {n} zdjęć do obiektu {rid}'); d.commit()
    session['flash'] = f'Wgrano {n} {"zdjęcie" if n==1 else "zdjęć"}.' if n else 'Nie udało się wczytać żadnego pliku.'
    return redirect(f'/obiekt/{rid}')

@app.route('/zdjecie/<int:zid>', methods=['GET','POST'])
@zalogowany
def zdjecie(zid):
    d = zaloz()
    z = d.execute('SELECT * FROM zdjecie WHERE id=?', (zid,)).fetchone()
    if not z: abort(404)
    if request.method == 'POST':
        f = request.form
        d.execute('UPDATE zdjecie SET podpis=?,alt=?,rola=?,kadr=?,kolejnosc=? WHERE id=?',
                  (f.get('podpis','').strip(), f.get('alt','').strip(), f.get('rola','detal'),
                   f.get('kadr','50% 50%').strip() or '50% 50%', int(f.get('kolejnosc') or 0), zid))
        d.commit(); session['flash'] = 'Zdjęcie zapisane.'
        return redirect(f'/obiekt/{z["realizacja_id"]}')
    tresc = (f'<div class="rzad" style="margin-bottom:18px"><h1>Zdjęcie</h1>'
             f'<a class="btn b2 rozc" href="/obiekt/{z["realizacja_id"]}">Wróć do obiektu</a></div>'
             f'<div class="karta"><img src="/zdjecia/{escape(z["plik"])}" alt="" '
             f'style="max-width:100%;border-radius:6px;border:1px solid #DDE5E0"></div>'
             f'<form method="post"><div class="karta">'
             + pole('podpis','Podpis pod zdjęciem',z['podpis'],pod='Widoczny na stronie')
             + pole('alt','Opis dla czytników ekranu',z['alt'],pod='Co widać na zdjęciu. Potrzebne dla dostępności i SEO.')
             + '<div class="pola3">' + pole('rola','Rola',z['rola'],opcje=ROLE)
             + pole('kadr','Kadrowanie',z['kadr'],pod='np. 50% 42%')
             + pole('kolejnosc','Kolejność',str(z['kolejnosc']),typ='number') + '</div>'
             + '</div><p class="rzad"><button class="btn">Zapisz</button>'
             f'<form method="post" action="/zdjecie/{zid}/usun" class="rozc" '
             f'onsubmit="return confirm(\'Usunąć to zdjęcie?\')"><button class="btn zly maly">Usuń zdjęcie</button></form></p></form>')
    return strona('Zdjęcie', tresc, '/', ile_demo(d)['razem'], None, ile_demo(d))

@app.route('/zdjecie/<int:zid>/usun', methods=['POST'])
@zalogowany
def zdjecie_usun(zid):
    d = zaloz()
    z = d.execute('SELECT * FROM zdjecie WHERE id=?', (zid,)).fetchone()
    if not z: abort(404)
    p = os.path.join(ZDJECIA, z['plik'])
    if os.path.isfile(p):
        try: os.remove(p)
        except OSError: pass
    d.execute('DELETE FROM zdjecie WHERE id=?', (zid,)); d.commit()
    session['flash'] = 'Zdjęcie usunięte.'
    return redirect(f'/obiekt/{z["realizacja_id"]}')

@app.route('/zdjecia/<nazwa>')
@zalogowany
def plik_zdjecia(nazwa):
    return send_from_directory(ZDJECIA, secure_filename(nazwa))

# ---------------- dane demo ----------------
@app.route('/demo/usun', methods=['POST'])
@zalogowany
def demo_usun():
    d = zaloz()
    w = usun_demo(d, ZDJECIA)
    session['flash'] = (f'Dane demo usunięte: {w["zdjecia_w_bazie"]} zdjęć w bazie, '
                        f'{w["pliki_usuniete"]} plików z dysku. Pamiętaj o przebudowaniu strony.')
    return redirect('/')

# ---------------- zespol ----------------
@app.route('/zespol')
@zalogowany
def zespol():
    d = zaloz()
    os_ = d.execute('SELECT * FROM osoba ORDER BY kolejnosc, id').fetchall()
    w = ''
    for o in os_:
        brak = [n for n,v in (('wykształcenie',o['wyksztalcenie']),('uprawnienia',o['uprawnienia']),
                              ('opis',o['opis']),('portret',o['portret'])) if not v]
        ost = (f'<span class="plakietka">brak: {", ".join(brak)}</span>' if brak
               else '<span class="plakietka st">komplet</span>')
        w += (f'<tr><td><strong>{escape(o["imie"])}</strong><div class="cichy">{escape(o["rola"])}</div></td>'
              f'<td>{ost}</td><td style="text-align:right"><a class="btn b2 maly" href="/osoba/{o["id"]}">Edytuj</a></td></tr>')
    tresc = (f'<h1>Zespół</h1><p class="lead">Puste pola nie pokazują się na stronie. '
             f'Dopóki nie ma wykształcenia i uprawnień, sekcja na stronie jest skrócona.</p>'
             f'<div class="karta" style="margin-top:18px"><table><tbody>{w}</tbody></table></div>')
    return strona('Zespół', tresc, '/zespol', ile_demo(d)['razem'], session.pop('flash', None), ile_demo(d))

@app.route('/osoba/<int:oid>', methods=['GET','POST'])
@zalogowany
def osoba(oid):
    d = zaloz()
    o = d.execute('SELECT * FROM osoba WHERE id=?', (oid,)).fetchone()
    if not o: abort(404)
    if request.method == 'POST':
        f = request.form
        d.execute('UPDATE osoba SET imie=?,rola=?,opis=?,wyksztalcenie=?,uprawnienia=? WHERE id=?',
                  (f.get('imie','').strip(), f.get('rola','').strip(), f.get('opis','').strip(),
                   f.get('wyksztalcenie','').strip(), f.get('uprawnienia','').strip(), oid))
        d.commit(); session['flash'] = 'Zapisane.'
        return redirect('/zespol')
    tresc = (f'<div class="rzad" style="margin-bottom:18px"><h1>{escape(o["imie"])}</h1>'
             f'<a class="btn b2 rozc" href="/zespol">Wróć</a></div><form method="post"><div class="karta">'
             + '<div class="pola2">' + pole('imie','Imię i nazwisko',o['imie'])
             + pole('rola','Rola',o['rola'],pod='Na wizytówkach ustalone jako „Architekt”') + '</div>'
             + pole('opis','Krótki opis',o['opis'],wiersze=3)
             + pole('wyksztalcenie','Wykształcenie',o['wyksztalcenie'],wiersze=2,
                    pod='Uczelnia, kierunek, rok. Zostaw puste, jeśli nie masz pewnych danych.')
             + pole('uprawnienia','Uprawnienia',o['uprawnienia'],wiersze=2,
                    pod='Numer, izba, zakres. Nie wpisuj niczego niepotwierdzonego - to idzie do klientów publicznych.')
             + '</div><p><button class="btn">Zapisz</button></p></form>')
    return strona(o['imie'], tresc, '/zespol', ile_demo(d)['razem'], None, ile_demo(d))

# ---------------- ustawienia ----------------
@app.route('/ustawienia', methods=['GET','POST'])
@zalogowany
def ustawienia():
    d = zaloz()
    if request.method == 'POST':
        n = request.form.get('nowe','')
        if len(n) >= 8:
            d.execute("INSERT OR REPLACE INTO ustawienie(klucz,wartosc) VALUES('haslo',?)",
                      (bcrypt.hashpw(n.encode(), bcrypt.gensalt()).decode(),))
            log(d, 'Zmieniono hasło panelu'); d.commit()
            session['flash'] = 'Hasło zmienione.'
        else:
            session['flash'] = 'Hasło musi mieć co najmniej 8 znaków - nie zmieniłem.'
        return redirect('/ustawienia')
    dz = d.execute('SELECT kiedy,co FROM dziennik ORDER BY id DESC LIMIT 25').fetchall()
    lg = ''.join(f'<tr><td class="cichy" style="white-space:nowrap">{escape(r["kiedy"])}</td>'
                 f'<td>{escape(r["co"])}</td></tr>' for r in dz)
    tresc = ('<h1>Ustawienia</h1>'
             '<form method="post"><div class="karta" style="margin-top:18px"><h2>Hasło panelu</h2>'
             '<p class="lead">Co najmniej 8 znaków.</p><div style="margin-top:14px;max-width:360px">'
             + pole('nowe','Nowe hasło','',typ='password') + '</div>'
             '<button class="btn">Zmień hasło</button></div></form>'
             f'<div class="karta"><h2>Co się działo</h2><table style="margin-top:12px"><tbody>{lg or "<tr><td class=cichy>Pusto.</td></tr>"}</tbody></table></div>')
    return strona('Ustawienia', tresc, '/ustawienia', ile_demo(d)['razem'], session.pop('flash', None), ile_demo(d))

# ---------------- generowanie strony ----------------
@app.route('/generuj', methods=['POST'])
@zalogowany
def generuj():
    d = zaloz()
    try:
        from budowa import zbuduj
        ile = zbuduj(d)
        log(d, f'Przebudowano stronę: {ile} plików'); d.commit()
        session['flash'] = f'Strona przebudowana - {ile} plików.'
    except Exception as e:
        session['flash'] = f'Nie udało się przebudować strony: {e}'
    return redirect('/')

@app.route('/zdrowie')
def zdrowie():
    return {'ok': True}

if __name__ == '__main__':
    zaloz()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=False)
