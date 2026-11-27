# -*- coding: utf-8 -*-
NAV=[('Usługi','#uslugi'),('Dofinansowania','#dotacje'),('Realizacje','#realizacje'),('Zespół','#zespol'),('Pytania','#pytania'),('Kontakt','#kontakt')]
PERS=[('Parafia albo gmina','Kościół, kaplica, krypta do remontu, zwykle z dotacją do rozliczenia.','Zaczynamy od wizji lokalnej i sprawdzenia, z jakich programów możecie skorzystać.','#dotacje','Zobacz dofinansowania'),
      ('Właściciel zabytku','Dwór, pałac, kamienica pod ochroną konserwatora.','Zaczynamy od sprawdzenia statusu ochrony i inwentaryzacji budynku.','#uslugi','Zobacz zakres prac'),
      ('Inwestor przed zakupem','Budynek, który rozważacie kupić albo właśnie kupiliście.','Oglądamy obiekt i mówimy, ile realnie kosztuje doprowadzenie go do stanu używalności.','uslugi.html#ekspertyza','Ekspertyza przed zakupem')]
USL=[('Przed zakupem',[('Ekspertyza przed zakupem','Oględziny, ocena stanu technicznego, szacunek kosztów remontu i opinia, czy w ogóle warto kupować.'),
                      ('Inwentaryzacja i pomiar','Dron na zewnątrz, skaner laserowy w środku. Model całego obiektu, nie szkic na kolanie.')]),
     ('Papiery i pieniądze',[('Formalności z konserwatorem','Wnioski, pozwolenia, uzgodnienia i korespondencja z urzędem. Prowadzimy to za Was, od początku do końca.'),
                      ('Dofinansowania','Dokumentacja do wniosków o dotacje, pomoc przy rozliczeniu przyznanych środków.'),
                      ('Projekt budowlany i wykonawczy','Z rysunkami detali: profili, okuć, sposobu uzupełnienia muru i doboru cegły.')]),
     ('Budowa',[('Roboty budowlane','Mury, elewacje, tynki renowacyjne, stolarka, kamień, żeliwo i mosiądz. Własne ekipy i sprawdzeni podwykonawcy.'),
                      ('Obsługa inwestorska','Jedna osoba prowadzi całą sprawę: harmonogram, ekipy, odbiory, kontakt z urzędem.'),
                      ('Nadzór autorski','Do odbioru końcowego i rozliczenia dotacji.')])]
DOT=[('Program ministra „Ochrona zabytków”','Właściciel lub zarządca zabytku wpisanego do rejestru, także osoba prywatna i parafia','Prace planowane: nabór jesienią roku poprzedzającego. Refundacja prac z ostatnich trzech lat: nabór w pierwszym kwartale'),
     ('Dotacja wojewódzkiego konserwatora zabytków','Właściciel zabytku','Osobny nabór i budżet w każdym województwie'),
     ('Dotacja gminy albo miasta','Właściciel zabytku','Nabór ogłaszany przez gminę, zwykle na rok następny'),
     ('Rządowy Program Odbudowy Zabytków','Gmina, powiat albo województwo - także na obiekt innego właściciela','Dwie edycje w 2023 roku, nowego naboru nie ogłoszono')]
FAQ=[('Czy mogę dostać dofinansowanie na prywatny dom wpisany do rejestru?','Tak. W programie ministra „Ochrona zabytków” wnioski mogą składać także osoby fizyczne, o ile obiekt jest wpisany do rejestru zabytków. Równolegle działają dotacje wojewódzkiego konserwatora i dotacje gminne. Sprawdzamy wszystkie trzy ścieżki i mówimy, która w Waszym przypadku ma sens.'),
     ('Co wolno zmienić w budynku pod ochroną konserwatora?','To zależy od zakresu wpisu do rejestru. Czasem chroniona jest cała substancja budynku, czasem tylko bryła i elewacje. Zakres ustalamy na początku, na podstawie decyzji o wpisie, i dopiero wtedy planujemy prace.'),
     ('Jak dobiera się cegłę do uzupełnień?','Pod wymiar, kolor, nasiąkliwość i sposób wypału oryginału. Czasem da się odzyskać cegłę rozbiórkową z tego samego okresu, czasem trzeba zamówić cegłę formowaną ręcznie. Dobór uzgadniamy z konserwatorem przed rozpoczęciem prac.'),
     ('Czy robicie tylko projekt, czy także wykonawstwo?','Oba. Możemy poprowadzić całość, od pomiaru po odbiór, albo wejść tylko na wybranym etapie - na przykład przygotować dokumentację, a roboty zostawić Waszej ekipie.'),
     ('Ile trwa przygotowanie dokumentacji?','Zależy od obiektu i od tego, jak szybko uzyskamy wypisy i decyzje z urzędu. Termin podajemy po wizji lokalnej, razem z zakresem prac.')]
ZESPOL=[('Hubert Rybkowski','Architekt · współwłaściciel','[WYKSZTAŁCENIE]','[DOŚWIADCZENIE: lata pracy, rodzaje obiektów]','[UPRAWNIENIA: numer i izba]','+48 693 429 479'),
        ('Maciej Bartkowiak','Architekt · współwłaściciel','[WYKSZTAŁCENIE]','[DOŚWIADCZENIE: lata pracy, rodzaje obiektów]','[UPRAWNIENIA: numer i izba]','+48 609 103 397')]
# info rozwijane po kliknieciu w architekta; puste nawiasy czekaja na dane od nich
ZESPOL_INFO={
 'Hubert Rybkowski':{
   'zaint':'Kolekcjoner sztuki.',
   'foto':'hubert-kolekcja.webp',
   'podpis':'Z kolekcji Huberta',
   'prace':'[WYBRANE PRACE: obiekty, role, lata]'},
 'Maciej Bartkowiak':{
   'zaint':'[ZAINTERESOWANIA]',
   'foto':None,
   'podpis':'',
   'prace':'[WYBRANE PRACE: obiekty, role, lata]'},
}

KROKI=[('Wizja lokalna','Przyjeżdżamy, oglądamy obiekt i rozmawiamy o tym, co chcecie osiągnąć.'),
       ('Pomiar','Dron i skaner. Z pomiaru powstaje model, na którym opieramy projekt i kosztorys.'),
       ('Dokumentacja i pozwolenia','Projekt, wniosek do konserwatora, a jeśli trzeba - wniosek o dofinansowanie.'),
       ('Roboty','Prowadzimy budowę albo wchodzimy tylko na wybrany etap.'),
       ('Odbiór i rozliczenie','Odbiór z konserwatorem, komplet dokumentów do rozliczenia dotacji.')]
