# -*- coding: utf-8 -*-
import os
from dane import *
ZIE='#1F5C4A';ZIED='#17493A';ZIEG='#143F33';KREM='#F2F5F3';INK='#15181A';MUT='#60666A';LIN='#E6E9E7';SZA='#F6F8F7'
DAS=[400,"62 7 300","30 6 90 6 300","120 7 300","48 6 70 6 300"]
def mark(c,w=4.6,style='',cls=''):
    p=''.join(f'<path d="M{60-r},112 V62 A{r},{r} 0 0 1 {60+r},62 V112" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-dasharray="{DAS[i]}"/>' for i,r in enumerate((10,19,28,37,46)))
    return f'<svg class="{cls}" viewBox="11 13 98 102" aria-hidden="true" style="{style}">{p}</svg>'
def logo(h=30,c=ZIE,sub='#3F7A66'):
    return ('<span style="display:inline-flex;align-items:center;gap:10px">'
      +mark(c,4.8,f'height:{h}px;width:auto;flex:none')
      +'<span style="display:flex;flex-direction:column;line-height:1;gap:3px">'
      +f'<span style="font-size:{round(h*.54)}px;font-weight:500;letter-spacing:.2em;color:{c}">ARCADA</span>'
      +f'<span style="font-size:{round(h*.29)}px;letter-spacing:.33em;color:{sub}">CONCEPT</span></span></span>')
def face(fam,pkg,w):
    return (f"@font-face{{font-family:'{fam}';font-weight:{w};font-display:swap;src:url('fonts/{pkg}-latin-ext-{w}-normal.woff2') format('woff2')}}"
            f"@font-face{{font-family:'{fam}';font-weight:{w};font-display:swap;src:url('fonts/{pkg}-latin-{w}-normal.woff2') format('woff2');unicode-range:U+0000-00FF}}")
F=''.join([face('AR','archivo',w) for w in (400,500,700)]+[face('PM','ibm-plex-mono',w) for w in (400,500)])

STRONY=[('Start','index.html'),('Realizacje','realizacje.html'),('Usługi','uslugi.html'),
        ('Dofinansowania','dofinansowania.html'),('Zespół','zespol.html'),('Kontakt','kontakt.html')]

CSS=F+f"""
@view-transition{{navigation:auto}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{margin:0;background:#fff;color:{INK};font-family:'AR',system-ui,sans-serif;font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}}
img{{display:block;width:100%;height:100%;object-fit:cover}}
h1,h2,h3,p,ul,ol,dl,dd,figure{{margin:0}}ul,ol{{padding:0;list-style:none}}
a{{color:inherit;text-decoration:none}}button,input,select,textarea{{font:inherit;color:inherit}}
.sr{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}}
.skip{{position:absolute;left:-9999px;top:0;background:{ZIE};color:#fff;padding:12px 18px;z-index:100}}
.skip:focus{{left:0}}
.w{{max-width:1240px;margin:0 auto;padding:0 40px}}
.m{{font-family:'PM';font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:{MUT}}}

/* --- menu --- */
header{{position:sticky;top:0;z-index:40;background:#fff;border-bottom:1px solid {LIN}}}
.hin{{display:flex;align-items:center;justify-content:space-between;gap:26px;padding:15px 0}}
nav.gl{{display:flex;gap:2px}}
nav.gl a{{font-size:14.5px;color:{MUT};min-height:44px;display:inline-flex;align-items:center;padding:0 13px;position:relative}}
nav.gl a:hover{{color:{ZIE}}}
nav.gl a[aria-current]{{color:{ZIE};font-weight:500}}
nav.gl a[aria-current]::after{{content:'';position:absolute;left:13px;right:13px;bottom:8px;height:2px;background:{ZIE}}}
.btn{{display:inline-flex;align-items:center;justify-content:center;min-height:46px;padding:0 22px;background:{ZIE};color:#fff;font-size:15px;font-weight:500}}
.btn:hover{{background:{ZIED}}}
.btn.jasny{{background:{KREM};color:{ZIEG}}}
.btn.obr{{background:transparent;color:{KREM};border:1px solid rgba(242,245,243,.45)}}
.btn.obr:hover{{background:rgba(242,245,243,.1)}}
.burger{{display:none;align-items:center;justify-content:center;width:46px;height:46px;border:1px solid {LIN};background:#fff;cursor:pointer}}
#mn{{display:none}}#mn.open{{display:block;padding-bottom:12px}}
#mn a{{display:flex;align-items:center;min-height:50px;border-top:1px solid {LIN};font-size:16px}}
#mn a[aria-current]{{color:{ZIE};font-weight:500}}
a:focus-visible,button:focus-visible,input:focus-visible,textarea:focus-visible,select:focus-visible,summary:focus-visible{{outline:2px solid {ZIE};outline-offset:3px}}

/* --- zielony blok pod menu --- */
.zb{{background:{ZIEG};color:{KREM};position:relative;overflow:hidden;view-transition-name:zb}}
.zb .w{{position:relative;z-index:1}}
.zb .in{{padding:92px 0 104px;max-width:30em}}
.zb.maly .in{{padding:56px 0 62px;max-width:34em}}
.zb .m{{color:rgba(242,245,243,.72)}}
.zb h1{{font-size:clamp(36px,5vw,66px);font-weight:400;letter-spacing:-.035em;line-height:1.04;margin-top:18px}}
.zb.maly h1{{font-size:clamp(28px,3.4vw,42px)}}
.zb p{{font-size:17px;color:rgba(242,245,243,.84);margin-top:20px;max-width:34em}}
.zb .cta{{display:flex;gap:12px;flex-wrap:wrap;margin-top:32px}}
.zb .znak{{position:absolute;right:-90px;top:-60px;width:560px;height:auto;pointer-events:none;z-index:0}}

/* --- biel i szarosci --- */
main section{{padding:84px 0}}
main section+section{{border-top:1px solid {LIN}}}
section.szara{{background:{SZA}}}
h2{{font-size:clamp(23px,2.5vw,31px);font-weight:400;letter-spacing:-.025em;line-height:1.2}}
h3{{font-size:17px;font-weight:500}}
.lead{{font-size:17px;color:{MUT};max-width:36em;margin-top:12px}}
.nag{{display:flex;flex-direction:column;gap:8px;max-width:38em}}
.g3{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:38px}}
.g2{{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:38px;align-items:start}}
.kar{{border:1px solid {LIN};background:#fff;padding:26px;display:flex;flex-direction:column;gap:8px;min-height:100%}}
a.kar:hover{{border-color:{ZIE}}}
.kar .nr{{font-family:'PM';font-size:11px;letter-spacing:.16em;color:{ZIE}}}
.kar p{{font-size:14.5px;color:{MUT};line-height:1.55}}
.kar .wiec{{margin-top:auto;padding-top:14px;font-size:14.5px;color:{ZIE};text-decoration:underline;text-underline-offset:4px}}
.cicha{{color:{MUT};font-size:14.5px}}
table{{width:100%;border-collapse:collapse;font-size:14.5px;margin-top:30px}}
th{{text-align:left;font-family:'PM';font-size:11px;letter-spacing:.13em;text-transform:uppercase;font-weight:400;color:{MUT};padding:0 14px 12px 0}}
td{{border-top:1px solid {LIN};padding:16px 14px 16px 0;vertical-align:top}}
td:first-child{{font-weight:500;width:32%}}
td.c{{color:{MUT}}}
.boks{{background:#fff;border:1px solid {LIN};padding:26px}}
.boks ul{{display:grid;gap:10px;margin-top:14px;font-size:14.5px;color:{MUT}}}
.boks li::before{{content:'';display:inline-block;width:13px;height:1px;background:{ZIE};vertical-align:middle;margin-right:10px}}
figure figcaption{{font-family:'PM';font-size:10.5px;letter-spacing:.13em;text-transform:uppercase;color:{MUT};margin-top:10px}}
.ba{{position:relative;aspect-ratio:3/4;overflow:hidden;background:{SZA}}}
.ba img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.ba .po{{clip-path:inset(0 0 0 var(--p,50%))}}
.ba .ln{{position:absolute;top:0;bottom:0;left:var(--p,50%);width:2px;margin-left:-1px;background:#fff;box-shadow:0 0 0 1px rgba(0,0,0,.22);pointer-events:none}}
.ba .gl{{position:absolute;top:50%;left:var(--p,50%);width:44px;height:44px;margin:-22px 0 0 -22px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;pointer-events:none;box-shadow:0 1px 6px rgba(0,0,0,.28);color:{INK}}}
.ba input{{position:absolute;inset:0;width:100%;height:100%;margin:0;opacity:0;cursor:ew-resize}}
.ba .et{{position:absolute;top:10px;background:rgba(21,24,26,.76);color:#fff;font-family:'PM';font-size:10px;letter-spacing:.1em;padding:5px 9px}}
form{{display:grid;gap:16px;max-width:30em}}
label{{display:flex;flex-direction:column;gap:7px;font-size:13px;color:{MUT}}}
input,textarea,select{{font-size:15px;padding:13px 14px;min-height:46px;border:1px solid {LIN};background:#fff}}
textarea{{min-height:120px;resize:vertical}}
.zle{{outline:2px solid #B4342A;outline-offset:1px}}
.blad{{color:#B4342A;font-size:14px}}
a.inl{{display:inline-flex;align-items:center;min-height:44px;color:{ZIE};text-decoration:underline;text-underline-offset:3px}}
.rece{{display:block;margin-top:10px;font-family:'PM';font-size:11px;letter-spacing:.13em;
 text-transform:uppercase;color:{MUT}}}
.wpis.my .rece{{color:{ZIE}}}
.plakietka-demo{{display:inline-block;margin-top:14px;font-family:'PM';font-size:11.5px;
 letter-spacing:.14em;text-transform:uppercase;color:#6B4310;background:#FDF6EC;
 border:1px solid #EBD5B3;border-radius:3px;padding:5px 10px}}
/* --- mapka obiektu --- */
.mapk{{display:block;border:1px solid {LIN};background:#fff;padding:18px;transition:border-color .2s}}
.mapk:hover{{border-color:{ZIE}}}
.mapk .m{{color:{ZIE}}}
.mapa-stara .ramka{{border:1px dashed #C6CFCA;background:{SZA};padding:18px;min-height:190px;display:flex;flex-direction:column;justify-content:center}}
@media(max-width:980px){{
 .wpis .g2{{grid-template-columns:1fr!important}}
}}
/* --- os czasu obiektu --- */
.os{{position:relative;margin-top:40px;padding-left:168px}}
.os::before{{content:'';position:absolute;left:84px;top:6px;bottom:6px;width:1px;background:{LIN}}}
.wpis{{position:relative;padding:26px 0 30px;border-top:1px solid {LIN}}}
.wpis:first-child{{border-top:0;padding-top:4px}}
.wpis .data{{position:absolute;left:-168px;top:27px;width:116px;text-align:right;font-family:'PM';font-size:17px;line-height:1.25;color:{INK};white-space:nowrap}}
.wpis .data.dl{{font-size:14px;top:29px}}
.wpis:first-child .data{{top:4px}}
.wpis .kr{{position:absolute;left:-41px;top:32px;width:11px;height:11px;border-radius:50%;background:#fff;border:2px solid #C6CFCA}}
.wpis:first-child .kr{{top:10px}}
.wpis.my .kr{{background:{ZIE};border-color:{ZIE};box-shadow:0 0 0 5px #E4EEE9}}
.wpis.my .data{{color:{ZIE};font-weight:500}}
.wpis.pusty .data,.wpis.pusty h3{{color:{MUT}}}
.wpis.pusty .kr{{border-style:dashed;border-color:#C6CFCA}}
.wpis h3{{font-size:19px;font-weight:400;letter-spacing:-.015em}}
.wpis p{{font-size:14.5px;color:{MUT};margin-top:7px;max-width:46em}}
.szara .wpis,.szara .os::before{{border-color:#E0E4E2}}
.szara .wpis .kr{{background:{SZA}}}
@media(max-width:980px){{
 .os{{padding-left:34px}}.os::before{{left:7px}}
 .wpis .data,.wpis:first-child .data{{position:static;width:auto;text-align:left;display:block;margin-bottom:5px}}
 .wpis .kr,.wpis:first-child .kr{{left:-32px;top:30px}}
}}
footer{{background:{ZIEG};color:{KREM};padding:52px 0 44px;position:relative;overflow:hidden}}
footer .w{{position:relative;z-index:1}}
footer .m{{color:rgba(242,245,243,.72)}}
.fgor{{display:flex;flex-wrap:wrap;gap:34px;justify-content:space-between;align-items:flex-start}}
.fdol{{display:flex;flex-wrap:wrap;gap:12px;justify-content:space-between;margin-top:40px;padding-top:18px;border-top:1px solid rgba(242,245,243,.2)}}
footer a.inl{{color:{KREM};min-height:40px}}
@media(max-width:980px){{
 nav.gl{{display:none}}.burger{{display:inline-flex}}.hin .btn{{display:none}}
 .w{{padding:0 22px}}.g3,.g2{{grid-template-columns:1fr}}
 main section{{padding:56px 0}}.zb .in{{padding:60px 0 66px}}
 .zb .znak{{right:-170px;width:420px;opacity:.9}}
}}
@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}@view-transition{{navigation:none}}}}
"""
JS=r"""
var b=document.getElementById('burger'),m=document.getElementById('mn');
if(b&&m)b.addEventListener('click',function(){var o=m.classList.toggle('open');b.setAttribute('aria-expanded',o)});
var ba=document.getElementById('ba');
if(ba){var r=ba.querySelector('input');r.addEventListener('input',function(){ba.style.setProperty('--p',r.value+'%')})}
var f=document.getElementById('kf');
if(f)f.addEventListener('submit',function(e){e.preventDefault();var ok=true,br=[],er=document.getElementById('ke');
 [['f1','imię'],['f2','e-mail'],['f3','opis obiektu']].forEach(function(p){var el=document.getElementById(p[0]);
  if(!el.value.trim()){ok=false;br.push(p[1]);el.classList.add('zle');el.setAttribute('aria-invalid','true')}
  else{el.classList.remove('zle');el.removeAttribute('aria-invalid')}});
 var em=document.getElementById('f2');
 if(em.value.trim()&&!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(em.value)){ok=false;br.push('poprawny e-mail');em.classList.add('zle')}
 if(!ok){er.hidden=false;er.textContent='Uzupełnijcie: '+br.join(', ')+'.';var p=f.querySelector('.zle');if(p)p.focus();return}
 er.hidden=true;f.hidden=true;var o=document.getElementById('kok');o.hidden=false;o.focus()});
"""
def strona(akt,tytul,opis,zb,tresc):
    nav=''.join(f'<a href="{h}"{" aria-current=\"page\"" if h==akt else ""}>{t}</a>' for t,h in STRONY)
    return ('<!doctype html><html lang="pl"><head><meta charset="utf-8">'
     '<meta name="viewport" content="width=device-width, initial-scale=1">'
     '<meta name="robots" content="noindex,nofollow">'
     f'<title>{tytul}</title><meta name="description" content="{opis}">'
     f'<style>{CSS}</style></head><body>'
     '<a class="skip" href="#main">Przejdź do treści</a>'
     f'<header><div class="w hin"><a href="index.html" aria-label="Arcada Concept, strona główna">{logo(30)}</a>'
     f'<nav class="gl" aria-label="Główne">{nav}</nav>'
     '<div style="display:flex;align-items:center;gap:10px">'
     '<a class="btn" href="kontakt.html">Opiszcie obiekt</a>'
     '<button class="burger" id="burger" aria-expanded="false" aria-controls="mn" aria-label="Menu"><span aria-hidden="true">&#9776;</span></button></div></div>'
     f'<div class="w"><nav id="mn" aria-label="Główne, wersja mobilna">{nav}</nav></div></header>'
     f'{zb}<main id="main">{tresc}</main>'
     f'<footer>{mark("rgba(242,245,243,.08)",6,"position:absolute;left:-120px;bottom:-220px;width:540px;height:auto;pointer-events:none")}'
     f'<div class="w"><div class="fgor">{logo(32,KREM,"rgba(242,245,243,.72)")}'
     '<div style="display:flex;flex-wrap:wrap;gap:46px">'
     '<div><div class="m">Kontakt</div><div style="margin-top:4px;display:flex;flex-direction:column;font-size:14.5px">'
     '<a class="inl" href="tel:+48693429479">693 429 479</a><a class="inl" href="mailto:arcada.concept@gmail.com">arcada.concept@gmail.com</a></div></div>'
     '<div><div class="m">Siedziba</div><div style="margin-top:10px;font-size:14.5px;line-height:1.55">ul. Wrzosowa 3<br>62-571 Żychlin</div></div>'
     '</div></div>'
     '<div class="fdol"><span class="m">Arcada Concept sp. z o.o. · remonty obiektów zabytkowych</span>'
     '<span class="m">NIP 665 305 91 60 · KRS 0001051640</span></div></div></footer>'
     f'<script>{JS}</script></body></html>')

def blok(nadt,h1,lead=None,cta=True,maly=False):
    s=f'<div class="zb{" maly" if maly else ""}">{mark("rgba(242,245,243,.07)",6,"","znak")}<div class="w"><div class="in">'
    s+=f'<div class="m">{nadt}</div><h1>{h1}</h1>'
    if lead: s+=f'<p>{lead}</p>'
    if cta: s+=('<div class="cta"><a class="btn jasny" href="kontakt.html">Opiszcie obiekt</a>'
                '<a class="btn obr" href="realizacje.html">Zobaczcie realizacje</a></div>')
    return s+'</div></div></div>'
