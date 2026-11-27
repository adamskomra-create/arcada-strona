# -*- coding: utf-8 -*-
"""Strona do oglądania witryny na telefonie i tablecie bez wychodzenia z przeglądarki.
Nie jest linkowana z serwisu i ma noindex - to narzędzie robocze."""
from b import ZIE, ZIED, KREM, INK, MUT, LIN, SZA

STRONY = [
    ('index.html', 'Start'),
    ('realizacje.html', 'Realizacje'),
    ('uslugi.html', 'Usługi'),
    ('dofinansowania.html', 'Dofinansowania'),
    ('zespol.html', 'Architekci'),
    ('kontakt.html', 'Kontakt'),
]

URZADZENIA = [
    ('telefon',  'Telefon',   390,  844),
    ('tabletp',  'Tablet',    820, 1180),
    ('laptop',   'Laptop',   1280,  800),
    ('pelna',    'Pełna szerokość', 0, 0),
]

def zbuduj(obiekty=None):
    opcje = ''.join(f'<option value="{p}">{t}</option>' for p, t in STRONY)
    if obiekty:
        opcje += '<optgroup label="Obiekty">' + ''.join(
            f'<option value="obiekt-{o["slug"]}.html">{o["tytul"]}</option>' for o in obiekty
        ) + '</optgroup>'
    przyciski = ''.join(
        f'<button type="button" data-u="{k}" data-w="{w}" data-h="{h}"'
        f'{" class=\"akt\"" if k=="pelna" else ""}>{t}</button>'
        for k, t, w, h in URZADZENIA)
    return f"""<!doctype html><html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Podgląd na urządzeniach - Arcada Concept</title>
<style>
*{{box-sizing:border-box}}
html,body{{margin:0;height:100%}}
body{{background:{SZA};font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;color:{INK};
 display:flex;flex-direction:column}}
.pas{{flex:0 0 auto;background:{ZIED};color:{KREM};display:flex;align-items:center;gap:18px;
 padding:11px 20px;flex-wrap:wrap}}
.pas .tyt{{font-size:12px;letter-spacing:.14em;text-transform:uppercase;opacity:.72}}
.pas select{{font:inherit;font-size:14px;padding:7px 11px;border-radius:9px;border:1px solid rgba(242,245,243,.3);
 background:rgba(242,245,243,.08);color:{KREM};min-width:190px}}
.pas select optgroup,.pas select option{{color:{INK};background:#fff}}
.grupa{{display:flex;gap:6px;background:rgba(242,245,243,.08);padding:4px;border-radius:11px}}
.grupa button{{font:inherit;font-size:13.5px;padding:7px 14px;border:0;border-radius:8px;cursor:pointer;
 background:transparent;color:rgba(242,245,243,.82)}}
.grupa button:hover{{color:{KREM}}}
.grupa button.akt{{background:{KREM};color:{ZIED};font-weight:500}}
.pas .obrot{{font:inherit;font-size:13.5px;padding:8px 14px;border-radius:9px;cursor:pointer;
 border:1px solid rgba(242,245,243,.3);background:transparent;color:{KREM}}}
.pas .obrot[disabled]{{opacity:.35;cursor:default}}
.pas .miara{{margin-left:auto;font-size:12.5px;opacity:.75;font-variant-numeric:tabular-nums}}
.scena{{flex:1 1 auto;overflow:auto;display:flex;align-items:flex-start;justify-content:center;padding:26px}}
.scena.pelna{{padding:0}}
.ramka{{background:#fff;border-radius:22px;box-shadow:0 18px 50px rgba(18,22,21,.16);
 overflow:hidden;border:1px solid {LIN};flex:0 0 auto}}
.scena.pelna .ramka{{border-radius:0;box-shadow:none;border:0;width:100%;height:100%}}
iframe{{display:block;border:0;width:100%;height:100%;background:#fff}}
</style></head><body>
<div class="pas">
  <span class="tyt">Podgląd</span>
  <select id="str" aria-label="Strona">{opcje}</select>
  <div class="grupa" id="urz">{przyciski}</div>
  <button class="obrot" id="obrot" type="button" disabled>Obróć</button>
  <span class="miara" id="miara">pełna szerokość</span>
</div>
<div class="scena pelna" id="scena"><div class="ramka" id="ramka"><iframe id="pod" src="index.html"></iframe></div></div>
<script>
(function(){{
 var q=new URLSearchParams(location.search);
 var str=document.getElementById('str'), pod=document.getElementById('pod'),
     scena=document.getElementById('scena'), ramka=document.getElementById('ramka'),
     miara=document.getElementById('miara'), obrot=document.getElementById('obrot'),
     w=0,h=0,poziomo=false;
 function zastosuj(){{
  if(!w){{
   scena.classList.add('pelna'); ramka.style.width=''; ramka.style.height='';
   miara.textContent='pełna szerokość'; obrot.disabled=true; return;
  }}
  scena.classList.remove('pelna'); obrot.disabled=false;
  var a=poziomo?h:w, b=poziomo?w:h;
  ramka.style.width=a+'px'; ramka.style.height=b+'px';
  miara.textContent=a+' × '+b+' px';
 }}
 document.getElementById('urz').addEventListener('click',function(e){{
  var b=e.target.closest('button'); if(!b) return;
  [].forEach.call(this.querySelectorAll('button'),function(x){{x.classList.remove('akt')}});
  b.classList.add('akt');
  w=+b.dataset.w; h=+b.dataset.h; poziomo=false; zastosuj();
 }});
 obrot.addEventListener('click',function(){{poziomo=!poziomo; zastosuj()}});
 str.addEventListener('change',function(){{pod.src=this.value}});
 pod.addEventListener('load',function(){{
  try{{
   var a=pod.contentWindow.location.pathname.split('/').pop()||'index.html';
   if(str.value!==a){{ for(var i=0;i<str.options.length;i++) if(str.options[i].value===a) str.selectedIndex=i; }}
  }}catch(e){{}}
 }});
 // start z parametrow: ?p=strona.html&s=telefon
 var pp=q.get('p');
 if(pp){{ for(var i=0;i<str.options.length;i++) if(str.options[i].value===pp){{ str.selectedIndex=i; pod.src=pp; break; }} }}
 var ss=q.get('s');
 if(ss){{ var bt=document.querySelector('#urz button[data-u="'+ss+'"]'); if(bt) bt.click(); }}
 zastosuj();
}})();
</script></body></html>"""
