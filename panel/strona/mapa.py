# -*- coding: utf-8 -*-
"""Schematyczna mapka Polski z punktem - do lokalizacji obiektu."""
import math
# przyblizony obrys granic Polski (lon, lat), uproszczony
PL=[(14.12,54.00),(14.28,53.70),(14.60,53.40),(14.42,53.27),(14.14,52.85),(14.44,52.68),(14.60,52.60),
    (14.71,52.10),(14.60,51.80),(14.95,51.45),(15.03,51.28),(15.35,51.00),(15.55,50.78),(16.00,50.63),
    (16.30,50.65),(16.65,50.10),(17.00,50.22),(17.35,50.27),(17.72,50.30),(18.05,50.02),(18.55,49.92),
    (18.85,49.52),(19.45,49.60),(19.80,49.20),(20.10,49.18),(20.70,49.40),(21.10,49.35),(21.80,49.35),
    (22.55,49.08),(22.70,49.05),(22.85,49.52),(23.65,50.40),(24.14,50.85),(23.95,51.50),(23.60,51.52),
    (23.20,52.22),(23.45,52.55),(23.90,52.70),(23.80,53.00),(23.50,53.95),(22.80,54.36),(22.00,54.36),
    (21.00,54.35),(19.80,54.44),(19.65,54.45),(19.30,54.35),(18.95,54.36),(18.60,54.70),(18.32,54.84),
    (18.10,54.72),(17.40,54.75),(16.70,54.55),(16.10,54.26),(15.30,54.12),(14.60,54.05),(14.12,54.00)]
def mapka(lon,lat,etykieta,szer=240,kol_lad='#E4EAE7',kol_lin='#CBD5CF',kol_pkt='#1F5C4A',tlo='none'):
    lons=[p[0] for p in PL];lats=[p[1] for p in PL]
    lo0,lo1=min(lons),max(lons);la0,la1=min(lats),max(lats)
    srL=(la0+la1)/2;k=math.cos(math.radians(srL))
    W=(lo1-lo0)*k;H=(la1-la0)
    sk=szer/W;wys=H*sk
    def xy(lo,la): return ((lo-lo0)*k*sk, (la1-la)*sk)
    d='M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in (xy(*p) for p in PL))+' Z'
    px,py=xy(lon,lat)
    return (f'<svg viewBox="0 0 {szer:.0f} {wys:.0f}" width="{szer:.0f}" height="{wys:.0f}" role="img" '
            f'aria-label="Mapa Polski z zaznaczonym położeniem: {etykieta}" style="display:block;max-width:100%;height:auto">'
            f'<path d="{d}" fill="{kol_lad}" stroke="{kol_lin}" stroke-width="1" stroke-linejoin="round"/>'
            f'<circle cx="{px:.1f}" cy="{py:.1f}" r="9" fill="{kol_pkt}" opacity=".18"/>'
            f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4.2" fill="{kol_pkt}"/>'
            f'</svg>')

def mapka_zbiorcza(punkty, szer=560, kol_lad='#E4EAE7', kol_lin='#CBD5CF', kol_pkt='#1F5C4A'):
    """punkty: [(lon, lat, etykieta, href)] - wszystkie obiekty na jednej mapie Polski."""
    lons=[p[0] for p in PL]; lats=[p[1] for p in PL]
    lo0,lo1=min(lons),max(lons); la0,la1=min(lats),max(lats)
    k=math.cos(math.radians((la0+la1)/2))
    W=(lo1-lo0)*k; H=(la1-la0); sk=szer/W; wys=H*sk
    def xy(lo,la): return ((lo-lo0)*k*sk, (la1-la)*sk)
    d='M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in (xy(*p) for p in PL))+' Z'
    s=(f'<svg viewBox="0 0 {szer:.0f} {wys:.0f}" width="{szer:.0f}" height="{wys:.0f}" role="img" '
       f'aria-label="Mapa Polski z położeniem wszystkich obiektów" '
       f'style="display:block;max-width:100%;height:auto;overflow:visible">'
       f'<path d="{d}" fill="{kol_lad}" stroke="{kol_lin}" stroke-width="1" stroke-linejoin="round"/>')
    # rozsuwanie etykiet, zeby nie siadaly na sobie
    uzyte=[]
    for i,(lo,la,et,hr) in enumerate(punkty):
        px,py=xy(lo,la)
        ty=py-14
        while any(abs(ty-u)<15 for u in uzyte): ty-=15
        uzyte.append(ty)
        s+=(f'<a href="{hr}" aria-label="{et}">'
            f'<circle cx="{px:.1f}" cy="{py:.1f}" r="11" fill="{kol_pkt}" opacity=".15"/>'
            f'<circle class="pkt" cx="{px:.1f}" cy="{py:.1f}" r="5.4" fill="{kol_pkt}"/>'
            f'<text class="numer" x="{px:.1f}" y="{ty:.1f}" text-anchor="middle" '
            f'font-size="12" font-weight="600" fill="{kol_pkt}">{i+1:02d}</text></a>')
    return s+'</svg>'
