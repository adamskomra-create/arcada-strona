# -*- coding: utf-8 -*-
ZIE='#1F5C4A';ZIED='#143F33';KREM='#F2F5F3';INK='#121615';MUT='#5A625E';LIN='#DDE5E0';SZA='#F6F8F7'
OSTRZ='#9A5B16';CZERW='#A33A2C'

def sygnet(c=ZIE,h=30,w=4.6):
    ps=''.join(f'<path d="M{60-r},112 V62 A{r},{r} 0 0 1 {60+r},62 V112" fill="none" stroke="{c}" '
               f'stroke-width="{w}" stroke-linecap="round" stroke-dasharray="{d}"/>'
               for r,d in zip((10,19,28,37,46),("400","62 7 300","30 6 90 6 300","120 7 300","48 6 70 6 300")))
    return f'<svg viewBox="11 13 98 102" height="{h}" aria-hidden="true" style="display:block">{ps}</svg>'

CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:system-ui,-apple-system,'Segoe UI',sans-serif;background:{SZA};color:{INK};line-height:1.55;-webkit-font-smoothing:antialiased}}
a{{color:{ZIE}}}
.w{{max-width:1080px;margin:0 auto;padding:0 24px}}
header.g{{background:#fff;border-bottom:1px solid {LIN};position:sticky;top:0;z-index:30}}
header.g .w{{display:flex;align-items:center;gap:16px;height:64px}}
header.g nav{{margin-left:auto;display:flex;gap:4px;align-items:center}}
header.g nav a{{text-decoration:none;color:{MUT};font-size:14.5px;padding:8px 12px;border-radius:5px}}
header.g nav a:hover{{background:{SZA};color:{INK}}}
header.g nav a.akt{{color:{ZIE};font-weight:600;background:#EFF6F2}}
h1{{font-size:26px;font-weight:600;letter-spacing:-.015em}}
h2{{font-size:19px;font-weight:600;margin-top:4px}}
.lead{{color:{MUT};font-size:15px;margin-top:5px}}
main{{padding:30px 0 70px}}
.karta{{background:#fff;border:1px solid {LIN};border-radius:8px;padding:20px;margin-bottom:14px}}
.rzad{{display:flex;align-items:center;gap:14px;flex-wrap:wrap}}
.rozc{{margin-left:auto}}
label{{display:block;margin-bottom:14px}}
label>span{{display:block;font-size:12.5px;font-weight:600;color:{MUT};margin-bottom:5px;letter-spacing:.01em}}
label>em{{display:block;font-size:12px;color:{MUT};font-style:normal;margin-top:4px}}
input[type=text],input[type=password],input[type=number],textarea,select{{
 width:100%;font:inherit;font-size:15px;padding:9px 11px;border:1px solid {LIN};border-radius:6px;background:#fff;color:{INK}}}
textarea{{min-height:84px;resize:vertical;line-height:1.5}}
input:focus,textarea:focus,select:focus{{outline:none;border-color:{ZIE};box-shadow:0 0 0 3px rgba(31,92,74,.12)}}
.pola2{{display:grid;grid-template-columns:1fr 1fr;gap:0 16px}}
.pola3{{display:grid;grid-template-columns:repeat(3,1fr);gap:0 16px}}
.btn{{font:inherit;font-size:14.5px;font-weight:500;min-height:40px;padding:0 16px;border-radius:6px;
 border:1px solid {ZIE};background:{ZIE};color:#fff;cursor:pointer;display:inline-flex;align-items:center;gap:7px;text-decoration:none}}
.btn:hover{{background:{ZIED};border-color:{ZIED}}}
.btn.b2{{background:#fff;color:{ZIE}}}
.btn.b2:hover{{background:{KREM}}}
.btn.zly{{border-color:{CZERW};background:{CZERW};color:#fff}}
.btn.zly:hover{{background:#8C3125;border-color:#8C3125}}
.btn.maly{{min-height:32px;padding:0 11px;font-size:13px}}
.baner{{border-radius:8px;padding:16px 18px;margin-bottom:18px;display:flex;gap:14px;align-items:flex-start;flex-wrap:wrap}}
.baner.uwaga{{background:#FDF6EC;border:1px solid #EBD5B3;color:#6B4310}}
.baner.ok{{background:#EFF6F2;border:1px solid #CFE0D8;color:{ZIED}}}
.baner b{{display:block;margin-bottom:3px}}
.plakietka{{display:inline-flex;align-items:center;font-size:11.5px;font-weight:600;letter-spacing:.04em;
 text-transform:uppercase;padding:3px 8px;border-radius:4px;background:#FDF6EC;color:{OSTRZ};border:1px solid #EBD5B3}}
.plakietka.st{{background:#EFF6F2;color:{ZIE};border-color:#CFE0D8}}
.plakietka.szara{{background:{SZA};color:{MUT};border-color:{LIN}}}
table{{width:100%;border-collapse:collapse;font-size:14.5px}}
th{{text-align:left;font-size:12px;text-transform:uppercase;letter-spacing:.06em;color:{MUT};padding:0 10px 9px;font-weight:600}}
td{{padding:11px 10px;border-top:1px solid {LIN};vertical-align:middle}}
tr.demo td:first-child{{box-shadow:inset 3px 0 0 {OSTRZ}}}
.cichy{{color:{MUT};font-size:13.5px}}
.pusto{{text-align:center;padding:40px 20px;color:{MUT};border:1px dashed #C6CFCA;border-radius:8px;background:#fff}}
.lista-wpisow{{list-style:none}}
.wp{{border:1px solid {LIN};border-radius:7px;padding:14px;margin-bottom:10px;background:#fff}}
.wp.my{{border-left:3px solid {ZIE}}}
.wp.pusty{{border-style:dashed;background:{SZA}}}
.wp .gl{{display:flex;gap:12px;align-items:baseline;flex-wrap:wrap}}
.wp .dt{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13.5px;color:{ZIE};font-weight:600;min-width:92px}}
.wp .tt{{font-weight:600}}
.mini{{display:flex;gap:10px;flex-wrap:wrap;margin-top:10px}}
.mini img{{width:88px;height:62px;object-fit:cover;border-radius:5px;border:1px solid {LIN}}}
.stopka{{padding:26px 0;color:{MUT};font-size:13px;border-top:1px solid {LIN};margin-top:40px}}
@media(max-width:760px){{.pola2,.pola3{{grid-template-columns:1fr}}header.g nav a{{padding:8px}}}}
"""

def strona(tytul, tresc, akt='', demo=0, flash=None, demo_szczegoly=None):
    nav=''.join(f'<a href="{h}" class="{"akt" if h==akt else ""}">{n}</a>'
                for n,h in [('Realizacje','/'),('Zespół','/zespol'),('Ustawienia','/ustawienia')])
    pasek_demo=''
    if demo:
        d = demo_szczegoly or {}
        rozpis = ' · '.join(f'{v} {k}' for k, v in
                            (('obiektów', d.get('realizacja', 0)), ('wpisów', d.get('wpis', 0)),
                             ('zdjęć', d.get('zdjecie', 0))) if v)
        pyt = (f'Usunąć wszystkie dane demo?\\n\\n{rozpis}\\n\\n'
               f'Zdjęcia znikną też z dysku. Tego nie da się cofnąć.\\n'
               f'Realizacje prawdziwe zostaną nietknięte.')
        pasek_demo=(f'<div class="baner uwaga"><div><b>W bazie są dane demo: {rozpis or str(demo)+" rekordów"}</b>'
                    f'Pięć przykładowych obiektów pokazuje, jak wygląda wypełnione portfolio. '
                    f'Na stronie każdy z nich ma widoczną plakietkę „wizualizacja poglądowa · obiekt fikcyjny”. '
                    f'Usuń je jednym kliknięciem, gdy wprowadzisz własne - realizacje prawdziwe zostaną.</div>'
                    f'<form method="post" action="/demo/usun" class="rozc" '
                    f'onsubmit="return confirm(\'{pyt}\')">'
                    f'<button class="btn zly">Usuń wszystkie dane demo</button></form></div>')
    fl=f'<div class="baner ok">{flash}</div>' if flash else ''
    return f"""<!doctype html><html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>{tytul} · Panel Arcada</title>
<style>{CSS}</style></head><body>
<header class="g"><div class="w">{sygnet()}
<strong style="font-size:15px;letter-spacing:.02em">Panel Arcada</strong>
<nav>{nav}<a href="/wyloguj" style="color:{MUT}">Wyloguj</a></nav></div></header>
<main><div class="w">{pasek_demo}{fl}{tresc}</div></main>
<div class="stopka"><div class="w">Arcada Concept sp. z o.o. · panel redakcyjny</div></div>
</body></html>"""
