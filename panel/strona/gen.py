# -*- coding: utf-8 -*-
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from b import *
from mapa import mapka
OUT=os.environ.get('ARCADA_OUT','/home/claude/panel/wynik')

def lokalizacja(lon,lat,nazwa,adres,dojazd,cel=None,epoka=None):
    from urllib.parse import quote
    pkt=quote(cel) if cel else f'{lat}%2C{lon}'
    pokaz=f'https://www.google.com/maps/search/?api=1&query={pkt}'
    nawig=f'https://www.google.com/maps/dir/?api=1&destination={pkt}'
    return (f'<div class="g2" style="margin-top:26px;grid-template-columns:250px 1fr 250px;gap:24px;align-items:start">'
            f'<a class="mapk" href="{pokaz}" target="_blank" rel="noopener" aria-label="Otwórz mapę: {nazwa}">'
            f'{mapka(lon,lat,nazwa,210)}<span class="m" style="display:block;margin-top:12px">Pokaż na mapie</span></a>'
            f'<div><span class="m">Gdzie to jest</span>'
            f'<p style="font-size:17px;margin-top:8px">{adres}</p>'
            f'<p class="cicha" style="margin-top:10px">{dojazd}</p>'
            f'<p style="margin-top:14px;display:flex;gap:10px;flex-wrap:wrap">'
            f'<a class="btn" style="min-height:44px;padding:0 18px;font-size:14.5px" href="{nawig}" target="_blank" rel="noopener">Nawiguj</a>'
            f'<a class="inl" href="{pokaz}" target="_blank" rel="noopener">Otwórz w mapach</a></p>'
            f'</div>'
            f'<div class="mapa-stara"><div class="ramka"><span class="m">[MAPA Z EPOKI]</span>'
            f'<p class="cicha" style="margin-top:8px;font-size:13px">Wycinek mapy topograficznej z {epoka or "XIX wieku"}, z zaznaczonym tym samym miejscem. '
            f'Wstawimy, gdy ustalimy arkusz i prawa do publikacji skanu.</p></div></div>'
            f'</div>')

def wpis(data,tyt,opis,kl='',tresc=''):
    dl=' dl' if len(data)>8 else ''
    if kl=='ciek':
        srodek=(f'<div class="ciek-k"><span class="et">Ciekawostka</span>'
                f'<h4>{tyt}</h4><p>{opis}</p>{tresc}</div>')
    else:
        srodek=f'<h3>{tyt}</h3><p>{opis}</p>{tresc}'
    return (f'<div class="wpis {kl}"><span class="data{dl}">{data}</span><span class="kr"></span>'
            f'{srodek}</div>')

def fig(f,cap,alt,ratio='3 / 4',pos='50% 50%'):
    return (f'<figure><div style="aspect-ratio:{ratio};overflow:hidden;background:{SZA}">'
            f'<img src="img/{f}" alt="{alt}" loading="lazy" style="object-position:{pos}"></div>'
            f'<figcaption>{cap}</figcaption></figure>')

# ---------------- START ----------------
def p_start():
    kar=''.join(f'<a class="kar" href="{h if h.startswith("uslugi") else "kontakt.html"}"><span class="nr">{i+1:02d}</span><h3>{t}</h3><p>{d}</p><p>{s}</p><span class="wiec">{c}</span></a>'
                for i,(t,d,s,h,c) in enumerate(PERS))
    return (blok('Remonty obiektów zabytkowych · cała Polska','Remontujemy tylko zabytki. Nic innego.',
                 'Kościoły, kaplice, dwory, pałace i kamienice pod ochroną konserwatora. Pomiar, dokumentacja, pozwolenia i roboty w jednej firmie.'),
f'''<section><div class="w">
<div class="nag"><span class="m">Z czym do nas przychodzą</span><h2>Trzy sytuacje, od których zaczynamy</h2>
<p class="lead">Każda prowadzi do innego pierwszego kroku.</p></div>
<div class="g3">{kar}</div></div></section>

<section class="szara"><div class="w">
<div class="nag"><span class="m">Realizacja</span><h2>Kaplica cmentarna z kryptą w Kościelcu</h2>
<p class="lead">Prace pod nadzorem Wielkopolskiego Wojewódzkiego Konserwatora Zabytków, odebrane w terminie umownym.</p></div>
<div class="g2">
<div><div class="ba" id="ba">
<img src="img/kaplica-koscielec-krypta-przed-kadr-938.webp" alt="Kaplica od strony krypty przed remontem" loading="lazy">
<img class="po" src="img/kaplica-koscielec-krypta-po-kadr-938.webp" alt="Ten sam widok po remoncie" loading="lazy">
<span class="et" style="left:10px">PRZED</span><span class="et" style="right:10px">PO</span><span class="ln"></span>
<span class="gl" aria-hidden="true">&#8596;</span>
<input type="range" min="0" max="100" value="50" aria-label="Porównanie przed i po, przesuń suwak"></div>
<p class="cicha" style="margin-top:12px">Przesuń suwak, żeby porównać</p></div>
<div><dl style="display:grid;gap:18px">
<div><dt class="m">Inwestor</dt><dd style="font-size:17px;margin-top:5px">Gmina Kościelec</dd></div>
<div><dt class="m">Tryb</dt><dd style="font-size:17px;margin-top:5px">Przetarg publiczny, 2024/BZP 00090607</dd></div>
<div><dt class="m">Wartość kontraktu</dt><dd style="font-size:17px;margin-top:5px">1 017 210 zł</dd></div></dl>
<p style="margin-top:26px"><a class="inl" href="realizacje.html">Zobaczcie całe portfolio</a></p></div></div>
</div></section>

<section><div class="w">
<div class="nag"><span class="m">Pomiar</span><h2>Każdy wymiar jest zmierzony, żaden nie jest zgadnięty</h2>
<p class="lead">Elewacje, dach i teren mierzymy dronem DJI Matrice 4E. Wnętrza, krypty i sklepienia skanerem FARO Focus 70. Z obu źródeł powstaje jeden model obiektu, na którym opieramy projekt i kosztorys.</p></div>
<div class="g2" style="max-width:860px">
<div class="boks"><div style="aspect-ratio:4/3"><img src="img/ilustracja-dron-pomiarowy-izometria-1024.webp" alt="Dron pomiarowy nad obiektem" loading="lazy" style="object-fit:contain"></div><p class="m" style="margin-top:12px">Dron · elewacje, dach, teren</p></div>
<div class="boks"><div style="aspect-ratio:4/3"><img src="img/ilustracja-skaner-laserowy-na-statywie-1024.webp" alt="Skaner laserowy na statywie" loading="lazy" style="object-fit:contain"></div><p class="m" style="margin-top:12px">Skaner · wnętrza, krypty, sklepienia</p></div></div>
</div></section>

<section class="szara"><div class="w" style="text-align:center">
<h2 style="max-width:18em;margin:0 auto">Macie obiekt pod ochroną konserwatora?</h2>
<p class="lead" style="margin:14px auto 0">Napiszcie, co to za budynek i co chcecie zrobić. Odpowiadamy w ciągu dwóch dni roboczych.</p>
<p style="margin-top:28px"><a class="btn" href="kontakt.html">Opiszcie obiekt</a></p>
</div></section>''')

# ---------------- PORTFOLIO ----------------
OBIEKTY_Z_BAZY=None   # ustawiane przez budowa.py; None = stara, wpisana na sztywno zawartosc

def p_realizacje():
    if OBIEKTY_Z_BAZY is not None:
        return p_realizacje_z_bazy(OBIEKTY_Z_BAZY)
    return _p_realizacje_wbudowane()

def _p_realizacje_wbudowane():
    det=''.join(fig(f,c,a,'4 / 5',p) for f,c,a,p in [
      ('kolatka-mosiadz-1280.webp','Kołatka · rekonstrukcja mosiądzu','Mosiężna kołatka po rekonstrukcji','50% 42%'),
      ('luk-portalu-cegla-1280.webp','Łuk portalu · uzupełnienia muru','Ceglany łuk portalu po uzupełnieniach','55% 50%'),
      ('drzwi-krypty-1280.webp','Drzwi krypty · renowacja z okuciami','Drewniane drzwi krypty po renowacji','50% 50%')]) 
    porown = f'''<div class="g2" style="margin-top:26px">
<div><div class="ba" id="ba">
<img src="img/kaplica-koscielec-krypta-przed-kadr-938.webp" alt="Kaplica od strony krypty przed remontem" loading="lazy">
<img class="po" src="img/kaplica-koscielec-krypta-po-kadr-938.webp" alt="Ten sam widok po remoncie" loading="lazy">
<span class="et" style="left:10px">PRZED</span><span class="et" style="right:10px">PO</span><span class="ln"></span>
<span class="gl" aria-hidden="true">&#8596;</span>
<input type="range" min="0" max="100" value="50" aria-label="Porównanie przed i po, przesuń suwak"></div>
<p class="cicha" style="margin-top:12px">Przesuń suwak, żeby porównać</p></div>
<div class="boks"><div style="aspect-ratio:3/4"><img src="img/elewacja-a04-rysunek-1280.webp" alt="Rysunek elewacji, arkusz A-04" loading="lazy" style="object-fit:contain"></div>
<p class="m" style="margin-top:12px">Elewacja · arkusz A-04</p></div></div>
<div class="g3" style="margin-top:20px">{det}</div>'''
    tabela = f'''<table style="margin-top:26px"><caption class="sr">Dane realizacji w Kościelcu</caption><tbody>
<tr><td>Inwestor</td><td class="c">Gmina Kościelec</td></tr>
<tr><td>Tryb</td><td class="c">Przetarg publiczny, 2024/BZP 00090607</td></tr>
<tr><td>Wartość kontraktu</td><td class="c">1 017 210 zł</td></tr>
<tr><td>Nadzór</td><td class="c">Wielkopolski Wojewódzki Konserwator Zabytków</td></tr></tbody></table>
<div class="boks" style="margin-top:22px;max-width:320px"><div><img src="img/poswiadczenie-gmina-koscielec-600.webp" alt="Poświadczenie realizacji wystawione przez Gminę Kościelec" loading="lazy" style="object-fit:contain;max-height:380px"></div>
<p class="m" style="margin-top:12px">Poświadczenie odbioru</p></div>'''
    os1 = (wpis('XIX w.','Obiekt powstaje','Kaplica cmentarna w Kościelcu figuruje w Gminnej Ewidencji Zabytków jako obiekt z XIX wieku. Dokładną datę i materiał uzupełnimy z karty ewidencyjnej.','')
         + wpis('[rok]','Wpis do rejestru zabytków','Numer i data decyzji. Od tego momentu każda zmiana wymaga zgody konserwatora.','pusty')
         + wpis('2024','Przetarg i umowa','Postępowanie 2024/BZP 00090607. Inwestorem jest Gmina Kościelec, nadzór sprawuje Wielkopolski Wojewódzki Konserwator Zabytków.','my',
                 lokalizacja(18.57,52.17444,'Kościelec, powiat kolski',
                   'Cmentarz parafialny, ul. Długa<br>Kościelec, gm. Kościelec<br>pow. kolski, woj. wielkopolskie',
                   'Około 6 km na południowy zachód od Koła, 116 km na wschód od Poznania. Kaplica stoi na cmentarzu parafialnym - można podejść i obejrzeć z zewnątrz o każdej porze.'))
         + wpis('2024','Prace','Osuszenie i odsolenie muru, uzupełnienia cegłą dobraną pod wymiar i wypał, tynki wapienne, renowacja stolarki i okuć, uporządkowanie otoczenia.','my',porown)
         + wpis('12.06','Odbiór','Odebrane w terminie umownym, z poświadczeniem wystawionym przez inwestora.','my',tabela)
         + wpis('Dalej','Obiekt ma przetrwać kolejne sto lat','Dokumentacja powykonawcza, zalecenia do przeglądów, kontakt na wypadek, gdyby coś zaczęło się dziać.',''))
    tab2 = '''<table style="margin-top:26px"><caption class="sr">Dane realizacji w Dębnie</caption><tbody>
<tr><td>Inwestor</td><td class="c">Parafia św. Michała Archanioła w Dębnie Królewskim</td></tr>
<tr><td>Rejestr zabytków</td><td class="c">nr 107/692/A</td></tr>
<tr><td>Pozwolenie konserwatorskie</td><td class="c">WWKZ Delegatura w Koninie, nr 171/2024/A</td></tr>
<tr><td>Finansowanie</td><td class="c">Rządowy Program Odbudowy Zabytków</td></tr></tbody></table>'''
    os2 = (wpis('1766','Kościół powstaje','Drewniany kościół parafialny pod wezwaniem świętego Michała Archanioła. Konstrukcja zrębowa, szalowana deskami, dach kryty gontem.','')
         + wpis('ok. 1906','Rozbudowa','Kościół zostaje powiększony. To z tego etapu pochodzi znaczna część dzisiejszej bryły.','')
         + wpis('[rok]','Wpis do rejestru zabytków','Numer decyzji to 107/692/A. Datę wpisu uzupełnimy z karty ewidencyjnej.','pusty')
         + wpis('08.2024','Umowa z parafią','Inwestorem jest parafia, prace finansowane z Rządowego Programu Odbudowy Zabytków. Umowa podpisana 2 sierpnia 2024.','my',
                 lokalizacja(18.675278,52.303889,'Dębno, gmina Babiak',
                   'Kościół św. Michała Archanioła<br>Dębno Poproboszczowskie, gm. Babiak<br>pow. kolski, woj. wielkopolskie',
                   'Około 5 km na południe od Babiaka, 12 km na północ od Koła i 120 km na wschód od Poznania. Parafia nosi nazwę „w Dębnie Królewskim”, ale sam kościół stoi w sąsiednim Dębnie Poproboszczowskim, tuż przy zachodniej granicy wsi.',
                   cel='Kościół św. Michała Archanioła, Dębno Poproboszczowskie, gmina Babiak',
                   epoka='przełomu XIX i XX wieku'))
         + wpis('2024','Prace przy drewnie','Dezynfekcja, usunięcie starych powłok, wymiana uszkodzonych elementów szalowania i impregnacja. Nowe pokrycie dachu gontem.','my',tab2)
         + wpis('30.10.2024','Odbiór pierwszego etapu','Pierwszy etap odebrany w terminie.','my')
         + wpis('04.2025','Sygnaturka i zakończenie','Nowe miedziane pokrycie sygnaturki. Umowny termin zakończenia całości to 1 kwietnia 2025 - potwierdzimy odbiór końcowy.','my')
         + wpis('Dalej','Drewno wymaga nadzoru','Gont i szalowanie trzeba oglądać regularnie. Zostaje zestaw zaleceń i kontakt.',''))

    return (blok('Portfolio','Każdy obiekt opisujemy jego własną osią czasu',
                 'Remont to jeden datowany punkt w życiu budynku. Pokazujemy, co było przed nim i co zostaje po nim - z inwestorem, trybem i wartością kontraktu, bez zaokrągleń.',
                 cta=False,maly=True),
f'''<section><div class="w">
<div class="nag"><span class="m">01 · Odebrana</span><h2>Kaplica cmentarna z kryptą w Kościelcu</h2>
<p class="lead">Remont kaplicy wraz z kryptą, prowadzony w całości przez nas.</p></div>
<div class="os">{os1}</div>
<p class="cicha" style="margin-top:10px">Pola w nawiasach uzupełnimy po otrzymaniu karty ewidencyjnej obiektu.</p>
</div></section>

<section class="szara"><div class="w">
<div class="nag"><span class="m">02 · W toku</span><h2>Drewniany kościół św. Michała Archanioła w Dębnie</h2>
<p class="lead">Szalowanie ścian, gontowe pokrycie dachu i miedziana sygnaturka. Obiekt z 1766 roku.</p></div>
<div class="os">''' + os2 + '''</div>
<p class="cicha" style="margin-top:10px">Zdjęcia z tej realizacji uzupełnimy po przekazaniu materiałów.</p>
</div></section>

<section><div class="w">
<div class="nag"><span class="m">W przygotowaniu</span><h2>Kolejne obiekty</h2>
<p class="lead">Każdy dostanie taką samą oś: powstanie, wpis do rejestru, nasze wejście, odbiór i to, co zostaje po nas.</p></div>
<div class="os">'''
+ wpis('[rok]','Miejsce na kolejną realizację','Nazwa obiektu, zakres prac, inwestor, tryb, zdjęcia przed i po.','pusty')
+ '''</div>
<p style="margin-top:34px"><a class="btn" href="kontakt.html">Opiszcie swój obiekt</a></p>
</div></section>''')

# ---------------- USLUGI ----------------
def p_uslugi():
    gr=''
    for g,items in USL:
        poz=''.join(f'<div style="border-top:1px solid {LIN};padding:22px 0"><h3>{t}</h3><p class="cicha" style="margin-top:6px;max-width:46em">{d}</p></div>' for t,d in items)
        gr+=f'<div style="margin-top:46px"><span class="m">{g}</span>{poz}<div style="border-top:1px solid {LIN}"></div></div>'
    return (blok('Zakres','Od oględzin przed zakupem po rozliczenie dotacji',
                 'Możemy poprowadzić całość albo wejść tylko na wybranym etapie.',cta=False,maly=True),
f'''<section><div class="w">{gr}
<p style="margin-top:40px"><a class="btn" href="kontakt.html">Opiszcie obiekt</a></p></div></section>

<section class="szara"><div class="w">
<div class="nag"><span class="m">Jak pracujemy</span><h2>Pięć kroków, zawsze w tej samej kolejności</h2></div>
<ol style="margin-top:34px;max-width:52em">'''
+''.join(f'<li style="display:grid;grid-template-columns:46px 1fr;gap:20px;border-top:1px solid {LIN};padding:22px 0"><span class="m">{i+1:02d}</span><div><h3>{t}</h3><p class="cicha" style="margin-top:5px">{d}</p></div></li>' for i,(t,d) in enumerate(KROKI))
+'</ol></div></section>')

# ---------------- DOFINANSOWANIA ----------------
def p_dot():
    rows=''.join(f'<tr><td>{a}</td><td class="c">{b}</td><td class="c">{c}</td></tr>' for a,b,c in DOT)
    return (blok('Dofinansowania','Remont zabytku rzadko płaci się z własnej kieszeni',
                 'Trzy ścieżki, z których korzystają nasi klienci. Sprawdzamy wszystkie i mówimy, która w Waszym przypadku ma sens.',cta=False,maly=True),
f'''<section><div class="w">
<table><thead><tr><th scope="col">Źródło</th><th scope="col">Kto składa wniosek</th><th scope="col">Kiedy</th></tr></thead><tbody>{rows}</tbody></table>
<div class="g2">
<div class="boks"><h3>Co robimy my</h3><ul>
<li>Sprawdzamy status ochrony i to, czy obiekt kwalifikuje się do programu</li>
<li>Kompletujemy dokumentację techniczną do wniosku</li>
<li>Pilnujemy terminów naborów</li>
<li>Przygotowujemy dokumenty do rozliczenia przyznanych środków</li></ul></div>
<div class="boks"><h3>Czego potrzebujemy od Was</h3><ul>
<li>Decyzję o wpisie do rejestru zabytków</li>
<li>Dokument własności obiektu</li>
<li>Zgodę na kontakt z urzędem w Waszym imieniu</li>
<li>Czas: wnioski na prace planowane składa się jesienią roku poprzedzającego</li></ul></div></div>
<p class="cicha" style="margin-top:22px;max-width:62ch">Nie obiecujemy przyznania dotacji. Decyzję podejmuje urząd, my odpowiadamy za kompletność i terminowość dokumentów.</p>
<p style="margin-top:34px"><a class="btn" href="kontakt.html">Sprawdźmy Wasz obiekt</a></p>
</div></section>''')

# ---------------- ZESPOL ----------------
def p_zespol():
    import json
    FOTO={'Hubert Rybkowski':'hubert'}
    def _kadr(n,maly=False):
        k=FOTO.get(n)
        if not k:
            return (f'<div class="portret pusty"><span class="m">[ZDJĘCIE]</span></div>')
        return (f'<div class="portret"><img class="foto" src="img/{k}-foto2.webp" alt="{n}" loading="lazy">'
                f'<img class="szkic" src="img/{k}-szkic.webp" alt="" aria-hidden="true" loading="lazy"></div>')
    kar=''
    dane=[]
    for i,(n,rola,w,d,u,tel) in enumerate(ZESPOL):
        inf=ZESPOL_INFO.get(n,{})
        kar+=(f'<button class="arch" type="button" data-k="{i}" aria-expanded="false" aria-controls="zinfo">'
              f'{_kadr(n)}<div class="arch-tr"><h3>{n}</h3><p class="m">{rola}</p>'
              f'<dl class="arch-dl"><dt>Wykształcenie</dt><dd>{w}</dd>'
              f'<dt>Doświadczenie</dt><dd>{d}</dd><dt>Uprawnienia</dt><dd>{u}</dd></dl>'
              f'<span class="inl arch-wiecej">Zobacz więcej</span></div></button>')
        dane.append({'imie':n,'rola':rola,'wyk':w,'dosw':d,'upr':u,'tel':tel,
                     'zaint':inf.get('zaint',''),'foto':inf.get('foto'),
                     'podpis':inf.get('podpis',''),'prace':inf.get('prace','')})
    faq=''.join(f'<div style="border-top:1px solid {LIN};padding:22px 0"><h3>{q}</h3>'
                f'<p class="cicha" style="margin-top:7px;max-width:46em">{a}</p></div>' for q,a in FAQ)
    return (blok('Architekci','Projekt prowadzi osoba, z którą rozmawiacie',
                 'Dwóch architektów, obaj współwłaściciele. Nie przekazujemy sprawy dalej.',cta=False,maly=True),
f"""<section><div class="w">
<div class="zesp" id="zesp"><div class="zesp-karty">{kar}</div>
<div class="zesp-info" id="zinfo" hidden></div></div>
<p class="cicha" style="margin-top:20px">Pola w nawiasach uzupełniamy po otrzymaniu danych od Was.</p>
<script type="application/json" id="zdane">{json.dumps(dane,ensure_ascii=False)}</script>
</div></section>
<section class="szara"><div class="w">
<div class="nag"><span class="m">Pytania</span><h2>O co pytają najczęściej</h2></div>
<div style="margin-top:30px">{faq}<div style="border-top:1px solid {LIN}"></div></div></div></section>""")

# ---------------- KONTAKT ----------------
def p_kontakt():
    return (blok('Kontakt','Macie obiekt pod ochroną konserwatora?',
                 'Napiszcie, co to za budynek i co chcecie zrobić. Odpowiadamy w ciągu dwóch dni roboczych.',cta=False,maly=True),
f'''<section><div class="w"><div class="g2" style="margin-top:0;max-width:980px">
<form id="kf" novalidate>
<label for="f1">Imię i nazwisko<input id="f1" name="imie" autocomplete="name" required></label>
<label for="f2">E-mail<input id="f2" name="email" type="email" autocomplete="email" required></label>
<label for="f4">Telefon<input id="f4" name="tel" type="tel" autocomplete="tel"></label>
<label for="f5">Rodzaj obiektu<select id="f5" name="rodzaj"><option>Kościół albo kaplica</option><option>Dwór albo pałac</option><option>Kamienica</option><option>Inny obiekt zabytkowy</option></select></label>
<label for="f3">Opis obiektu i prac<textarea id="f3" name="opis" placeholder="Gdzie jest budynek, czy jest wpisany do rejestru, co chcecie zrobić" required></textarea></label>
<p id="ke" hidden class="blad" role="alert" aria-live="polite"></p>
<button class="btn" type="submit">Wyślij opis obiektu</button>
<p class="cicha" style="font-size:13px">Dane z formularza służą tylko do odpowiedzi na wiadomość.</p>
</form>
<div id="kok" hidden tabindex="-1" class="boks"><h3>Wiadomość przygotowana</h3>
<p class="cicha" style="margin-top:9px">Formularz zacznie wysyłać wiadomości po uruchomieniu skrzynki w domenie. Na razie napiszcie na arcada.concept@gmail.com albo zadzwońcie.</p></div>
<div class="boks">
<span class="m">Adres</span><p style="margin-top:6px">Arcada Concept sp. z o.o.<br>ul. Wrzosowa 3, 62-571 Żychlin</p>
<span class="m" style="display:block;margin-top:22px">E-mail</span><p style="margin-top:2px"><a class="inl" href="mailto:arcada.concept@gmail.com">arcada.concept@gmail.com</a></p>
<span class="m" style="display:block;margin-top:14px">Telefon</span><p style="margin-top:2px"><a class="inl" href="tel:+48693429479">+48 693 429 479</a></p>
<span class="m" style="display:block;margin-top:22px">Odpowiadamy</span><p class="cicha" style="margin-top:6px">W ciągu dwóch dni roboczych.</p>
</div></div></div></section>''')

def zbuduj_pliki(out=None):
  out=out or OUT
  os.makedirs(out,exist_ok=True)
  PG=[('index.html','Arcada Concept - remonty zabytków w całej Polsce','Remontujemy tylko zabytki. Pomiar, dokumentacja, pozwolenia konserwatorskie, dofinansowania i roboty budowlane. Cała Polska.',p_start),
      ('realizacje.html','Realizacje - Arcada Concept','Portfolio: kaplica cmentarna z kryptą w Kościelcu, zakres prac, inwestor, wartość kontraktu i poświadczenie odbioru.',p_realizacje),
      ('uslugi.html','Usługi - Arcada Concept','Ekspertyza przed zakupem, inwentaryzacja, formalności z konserwatorem, projekt, roboty budowlane i nadzór autorski.',p_uslugi),
      ('dofinansowania.html','Dofinansowania - Arcada Concept','Program ministra, dotacja wojewódzkiego konserwatora, środki gminy. Co robimy my, czego potrzebujemy od Was.',p_dot),
      ('zespol.html','Architekci - Arcada Concept','Dwóch architektów, obaj współwłaściciele. Projekt prowadzi osoba, z którą rozmawiacie.',p_zespol),
      ('kontakt.html','Kontakt - Arcada Concept','Napiszcie, co to za budynek i co chcecie zrobić. Odpowiadamy w ciągu dwóch dni roboczych.',p_kontakt)]
  import shutil
  n=0
  for fn,t,d,f in PG:
    zb,tr=f()
    open(f'{out}/{fn}','w',encoding='utf-8').write(strona(fn,t,d,zb,tr))
    n+=1
  # osobna strona dla kazdego obiektu z bazy
  if OBIEKTY_Z_BAZY:
    ile=len(OBIEKTY_Z_BAZY)
    for i,o in enumerate(OBIEKTY_Z_BAZY):
      zb,tr=p_obiekt(o,i,ile)
      tyt=f"{o['tytul']} - Arcada Concept"
      op=(o.get('lead') or o.get('podtytul') or '')[:155]
      open(f"{out}/{_plik_obiektu(o)}",'w',encoding='utf-8').write(
          strona('realizacje.html',tyt,op,zb,tr))
      n+=1
  # narzedzie robocze: podglad na telefonie i tablecie
  try:
    from podglad import zbuduj as _podglad
    open(f'{out}/podglad.html','w',encoding='utf-8').write(_podglad(OBIEKTY_Z_BAZY))
    n+=1
  except Exception as e:
    print('podglad pominiety:',e)
  here=os.path.dirname(os.path.abspath(__file__))
  for k in ('img','fonts'):
    zrodlo=os.path.join(here,k)
    if os.path.isdir(zrodlo) and not os.path.exists(f'{out}/{k}'):
        shutil.copytree(zrodlo,f'{out}/{k}')
  return n

if __name__=='__main__':
    print('zbudowano',zbuduj_pliki(),'plikow w',OUT)


# ================= portfolio budowane z bazy =================
def _tabela(o):
    w=[]
    for et,kl in (('Inwestor','inwestor'),('Tryb','tryb'),('Rejestr zabytków','rejestr'),
                  ('Pozwolenie konserwatorskie','pozwolenie'),('Nadzór','nadzor'),
                  ('Finansowanie','finansowanie')):
        if o.get(kl): w.append(f'<tr><td>{et}</td><td class="c">{o[kl]}</td></tr>')
    if o.get('wartosc') and o.get('pokaz_wartosc'):
        w.append(f'<tr><td>Wartość kontraktu</td><td class="c">{o["wartosc"]}</td></tr>')
    if not w: return ''
    return (f'<table style="margin-top:26px"><caption class="sr">Dane realizacji: {o["tytul"]}</caption>'
            f'<tbody>{"".join(w)}</tbody></table>')

def _galeria(o,wid=None,scisle=False):
    """Zdjęcia przypięte do wpisu. scisle=True - bez podmiany na nieprzypisane detale,
    żeby ciekawostka nie pokazywała cudzych zdjęć, gdy jeszcze nie ma własnych."""
    z=[x for x in o['zdjecia'] if x['wpis_id']==wid and x['rola'] in ('detal','rysunek','dokument')]
    if not z and not scisle:
        z=[x for x in o['zdjecia'] if x['wpis_id'] is None and x['rola'] in ('detal','rysunek','dokument')]
    if not z: return ''
    def _ar(x): return '4 / 3' if x['rola'] in ('rysunek','dokument') else '4 / 5'
    k=''.join(f'<figure><div style="aspect-ratio:{_ar(x)};overflow:hidden;background:{SZA}">'
              f'<img src="img/{x["plik"]}" alt="{x["alt"]}" loading="lazy" '
              f'style="object-position:{x["kadr"]}"></div>'
              f'<figcaption>{x["podpis"]}</figcaption></figure>' for x in z[:6])
    return f'<div class="g3{" ciek-g" if scisle else ""}" style="margin-top:20px">{k}</div>'

def _porownanie(o):
    p=[x for x in o['zdjecia'] if x['rola']=='przed']
    q=[x for x in o['zdjecia'] if x['rola']=='po']
    if not (p and q): return ''
    pion = 'aspect-ratio:3/4' if True else ''
    return (f'<div class="g2" style="margin-top:26px"><div><div class="ba">'
            f'<img src="img/{p[0]["plik"]}" alt="{p[0]["alt"] or "Stan przed remontem"}" loading="lazy">'
            f'<img class="po" src="img/{q[0]["plik"]}" alt="{q[0]["alt"] or "Stan po remoncie"}" loading="lazy">'
            f'<span class="et" style="left:10px">PRZED</span><span class="et" style="right:10px">PO</span>'
            f'<span class="ln"></span><span class="gl" aria-hidden="true">&#8596;</span>'
            f'<input type="range" min="0" max="100" value="50" aria-label="Porównanie przed i po, przesuń suwak">'
            f'</div><p class="cicha" style="margin-top:12px">Przesuń suwak, żeby porównać</p></div></div>')

def _zakres(ws):
    a,b=ws[0]['data'],ws[-1]['data']
    return a if a==b else f'{a} - {b}'

def _os(o):
    s=''
    bufor=[]                      # ciagly blok wpisow wlasnych -> jedna ramka
    def domknij():
        nonlocal s,bufor
        if not bufor: return
        tr=''.join(bufor)
        s+=(f'<div class="nasze"><span class="nasze-tag">Nasz remont · {_zakres(_bufdane)}</span>'
            f'{tr}</div>')
        bufor=[]
    _bufdane=[]
    for w in o['wpisy']:
        kl={'my':'my','pusty':'pusty','ciekawostka':'ciek'}.get(w['rodzaj'],'')
        opis=w['opis']
        dod=f'<span class="rece">{w["rece"]}</span>' if w['rece'] else ''
        if w['blok']=='lokalizacja' and o.get('adres'):
            dod=lokalizacja(o.get('lon'),o.get('lat'),o['tytul'],o['adres'],o.get('dojazd',''),
                            cel=o.get('cel_mapy') or None, epoka=o.get('epoka_mapy') or None)
        elif w['blok']=='tabela':  dod=_tabela(o)
        elif w['blok']=='porownanie': dod=_porownanie(o)+_galeria(o)
        elif w['blok']=='galeria': dod=_galeria(o,w['id'],scisle=(kl=='ciek'))
        kawalek=wpis(w['data'],w['tytul'],opis,kl,dod)
        if kl=='my':
            bufor.append(kawalek); _bufdane.append(w)
        elif kl=='ciek' and bufor:
            bufor.append(kawalek)          # ciekawostka nie rozbija ramki remontu
        else:
            domknij(); _bufdane=[]; s+=kawalek
    domknij()
    return s

ETYKIETY={'odebrana':'Odebrana','w toku':'W toku','w przygotowaniu':'W przygotowaniu'}

def _oklad(o):
    """Zdjecie na karte: najpierw 'po', potem cokolwiek."""
    z=o.get('zdjecia') or []
    for rola in ('po','detal','przed','rysunek'):
        for x in z:
            if x.get('rola')==rola: return x['plik']
    return z[0]['plik'] if z else None

def _plik_obiektu(o): return f"obiekt-{o['slug']}.html"

def _miejsce(o):
    a=(o.get('adres') or '').replace('<br>',', ')
    return a

def p_realizacje_z_bazy(obiekty):
    from mapa import mapka_zbiorcza
    pkt=[(float(o['lon']),float(o['lat']),o['tytul'],_plik_obiektu(o))
         for o in obiekty if o.get('lon') and o.get('lat')]
    mapa=(f'<section><div class="w"><div class="mapa-wszystko">'
          f'<div>{mapka_zbiorcza(pkt,560)}</div>'
          f'<div><span class="m">Gdzie pracujemy</span>'
          f'<p class="lead" style="margin-top:10px">Każdy punkt to jeden obiekt. '
          f'Kliknij, żeby przejść do jego historii.</p>'
          f'<ol class="spis">' +
          ''.join(f'<li><a href="{_plik_obiektu(o)}"><span class="nr">{i+1:02d}</span>'
                  f'<span><strong>{o["tytul"]}</strong>'
                  f'<span class="cicha">{_miejsce(o)}</span></span></a></li>'
                  for i,o in enumerate(obiekty))
          + f'</ol></div></div></div></section>') if pkt else ''

    kar=''
    for i,o in enumerate(obiekty):
        f=_oklad(o)
        obraz=(f'<div class="kar-foto"><img src="img/{f}" alt="{o["tytul"]}" loading="lazy"></div>'
               if f else f'<div class="kar-foto pusta"><span class="m">zdjęcia w przygotowaniu</span></div>')
        plak=('<span class="plakietka-demo">obiekt fikcyjny</span>' if o.get('demo') else '')
        lead=o.get('lead') or ''
        if len(lead)>140: lead=lead[:137].rsplit(' ',1)[0]+'…'
        kar+=(f'<a class="kar-ob" href="{_plik_obiektu(o)}">{obraz}'
              f'<div class="kar-tr"><span class="m">{i+1:02d} · {ETYKIETY.get(o["status"],o["status"])}</span>'
              f'<h3>{o["tytul"]}</h3><p class="cicha">{lead}</p>{plak}'
              f'<span class="inl">Zobacz obiekt</span></div></a>')
    siatka=(f'<section class="szara"><div class="w"><div class="nag" style="margin-bottom:26px">'
            f'<h2>Obiekty</h2></div><div class="siatka-ob">{kar}</div></div></section>'
            if kar else
            '<section><div class="w"><div class="nag"><h2>Portfolio w budowie</h2>'
            '<p class="lead">Obiekty pojawią się tu, gdy tylko zostaną wprowadzone.</p></div></div></section>')

    return (blok('Portfolio','Każdy obiekt opisujemy jego własną osią czasu',
                 'Budynek stoi dłużej niż my. Remont to jeden datowany punkt w jego życiu - '
                 'pokazujemy, co było przed nim, co zrobiliśmy i co zostaje po nas.',
                 cta=False,maly=True), mapa+siatka)

def _wpisow(n):
    if n==1: return '1 wpis'
    r=n%10; rr=n%100
    return f'{n} wpisy' if (2<=r<=4 and not 12<=rr<=14) else f'{n} wpisów'

def _rysunek(o):
    """Rysunek techniczny obiektu, jesli jest."""
    for x in (o.get('zdjecia') or []):
        if x.get('rola')=='rysunek': return x['plik'], (x.get('podpis') or 'Rysunek inwentaryzacyjny')
    return None,''

def p_obiekt(o,i,ile):
    rys,podp=_rysunek(o)
    f=_oklad(o)                       # zdjecie idzie w naglowek
    drugi=rys                         # rysunek schodzi nizej, zeby sie nie powtarzac
    hero=(f'<figure class="ob-foto"><img src="img/{drugi}" alt="{podp or o["tytul"]}">'
          f'<figcaption>{podp}</figcaption></figure>' if drugi else '')
    pola=[('Status',ETYKIETY.get(o['status'],o['status'])),
          ('Zakres',o.get('material') or ''),
          ('Gdzie',_miejsce(o)),
          ('Inwestor',o.get('inwestor') or ''),
          ('Nadzór',o.get('nadzor') or ''),
          ('Rejestr zabytków',o.get('rejestr') or ''),
          ('Finansowanie',o.get('finansowanie') or '')]
    fakty=''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k,v in pola if v)
    plak=('<span class="plakietka-demo">wizualizacja poglądowa · obiekt fikcyjny</span>'
          if o.get('demo') else '')
    lead=f'<p class="lead">{o["lead"]}</p>' if o.get('lead') else ''
    n=len(o.get('wpisy') or [])
    hist=(f'<details class="historia"><summary><span class="hist-tyt">Historia obiektu</span>'
          f'<span class="hist-ile">{_wpisow(n)} · od {o["wpisy"][0]["data"]} do {o["wpisy"][-1]["data"]}</span>'
          f'<span class="hist-strz" aria-hidden="true"></span></summary>'
          f'<div class="os">{_os(o)}</div></details>') if n else ''
    sek=(f'<section><div class="w"><p style="margin-bottom:22px">'
         f'<a class="inl" href="realizacje.html">← Wszystkie realizacje</a></p>'
         f'<div class="nag"><span class="m">{i+1:02d} z {ile:02d} · '
         f'{ETYKIETY.get(o["status"],o["status"])}</span>'
         f'<h2>{o["tytul"]}</h2>{lead}{plak}</div>'
         f'{hero}'
         f'<dl class="ob-fakty">{fakty}</dl>'
         f'{hist}</div></section>')
    return (blok('Realizacja',o['tytul'],o.get('podtytul') or '',cta=False,maly=True,
                 obraz=f,podpis=''), sek)
