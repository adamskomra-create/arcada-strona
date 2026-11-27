# -*- coding: utf-8 -*-
"""Cztery układy strony obiektu do wyboru. Każdy renderuje ten sam obiekt
z tych samych danych - różni się tylko rozmieszczeniem."""
from b import ZIE, ZIED, KREM, INK, MUT, LIN, SZA, blok

WARIANTY = [
 ('a','Dane z boku','Treść po lewej, lepka kolumna z danymi po prawej. Dane widoczne przez całą długość osi czasu.'),
 ('b','Pasek danych','Dane w poziomym pasku pod nagłówkiem, treść na pełnej szerokości. Najwięcej miejsca na zdjęcia.'),
 ('c','Okładka','Zdjęcie na całą szerokość, pod nim spis treści po lewej i dane w kafelku. Układ magazynowy.'),
 ('d','Karta ewidencyjna','Dane jako tabela u góry, jak metryczka w karcie zabytku. Oś czasu z latami na marginesie.'),
]

def css_wariantow():
    return f"""
/* ====== warianty układu ====== */
body.w-b .ob-ukl{{display:block}}
body.w-b .ob-dane{{position:static;background:{SZA};border:1px solid {LIN};border-radius:16px;
 padding:20px 24px;margin:0 0 36px}}
body.w-b .ob-dane dl{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));
 gap:18px 28px;margin:0}}
body.w-b .dane-tyt{{margin-bottom:14px}}
body.w-b .dane-nr{{display:none}}
body.w-b .ob-tresc .lead{{font-size:21px;max-width:34em}}
body.w-b .ob-foto img{{max-height:620px}}

body.w-c .ob-okruchy{{margin-bottom:18px}}
body.w-c .ob-ukl{{grid-template-columns:230px minmax(0,1fr);gap:46px}}
body.w-c .ob-spis{{position:sticky;top:18px;font-size:14.5px}}
body.w-c .ob-spis a{{display:block;padding:7px 0;border-bottom:1px solid {LIN};
 text-decoration:none;color:{MUT}}}
body.w-c .ob-spis a:hover{{color:{ZIE}}}
body.w-c .ob-dane{{position:static;border-radius:16px;margin-bottom:34px}}
body.w-c .ob-dane dl{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:16px 26px}}
body.w-c .okladka{{margin:0 0 30px}}
body.w-c .okladka img{{width:100%;aspect-ratio:21/9;object-fit:cover;display:block;border-radius:0}}

body.w-d .ob-ukl{{display:block}}
body.w-d .metryczka{{border:1px solid {INK};border-radius:4px;margin:0 0 40px;overflow:hidden}}
body.w-d .metryczka .mt-gl{{background:{INK};color:{KREM};padding:9px 16px;font-family:'PM';
 font-size:11px;letter-spacing:.14em;text-transform:uppercase}}
body.w-d .metryczka dl{{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));
 gap:0;margin:0}}
body.w-d .metryczka dl > div{{padding:13px 16px;border-right:1px solid {LIN};border-bottom:1px solid {LIN}}}
body.w-d .metryczka dt{{font-family:'PM';font-size:10.5px;letter-spacing:.1em;
 text-transform:uppercase;color:{MUT}}}
body.w-d .metryczka dd{{margin:5px 0 0;font-size:15px;line-height:1.4}}
body.w-d .dane-tyt,body.w-d .dane-nr{{display:none}}
body.w-d .ob-tresc .lead{{font-size:19px;max-width:36em}}

.wyb{{position:fixed;left:50%;transform:translateX(-50%);bottom:18px;z-index:70;
 background:{ZIED};color:{KREM};border-radius:999px;padding:7px 8px;display:flex;gap:5px;
 box-shadow:0 8px 24px rgba(18,22,21,.24);font-size:13px}}
.wyb a{{padding:7px 15px;border-radius:999px;text-decoration:none;color:rgba(242,245,243,.82)}}
.wyb a:hover{{background:rgba(242,245,243,.14);color:{KREM}}}
.wyb a.akt{{background:{KREM};color:{ZIED};font-weight:500}}
@media(max-width:700px){{.wyb{{font-size:12px;padding:6px}} .wyb a{{padding:6px 10px}}}}
"""

def pasek(akt):
    l=''.join(f'<a href="uklad-{k}.html"{" class=\"akt\"" if k==akt else ""}>{n}</a>'
              for k,n,_ in WARIANTY)
    return f'<div class="wyb">{l}</div>'
