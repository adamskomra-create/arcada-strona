# arcada-strona

Pliki publicznej części serwisu arcadaconcept.pl.

Serwer pobiera ten katalog automatycznie co 2 minuty i lustrzanie kopiuje
`www/` do `/opt/arcada/www/`. Kopia jest lustrzana (`rsync --delete`), więc
**plik usunięty stąd znika też z serwera**.

Katalog `demo/` celowo nie jest tu wersjonowany - treść pod `/demo`
pozostaje taka, jaka jest na serwerze, i nie podlega synchronizacji.

## Co jest w www

- `index.html` - strona główna (sam znak)
- `logo/` - wybór kroju napisu w logo
- `strona/` - serwis wielostronicowy; portfolio zawiera realizacje prawdziwe
  (Kościelec, Dębno) oraz pięć obiektów fikcyjnych, każdy z widoczną plakietką
  „wizualizacja poglądowa · obiekt fikcyjny"
- `ok/` - materiały pomocnicze
- `og.jpg`, `robots.txt`

## Dane demo

Pięć obiektów oznaczonych plakietką nie istnieje. Służą wyłącznie do pokazania układu
portfolio, zanim przyjdą materiały z prawdziwych realizacji. Nie wolno ich
przedstawiać jako referencji. Wszystkie strony mają `noindex`.

Znikają w całości po kliknięciu „Usuń dane demo” w panelu i przebudowaniu
strony. Realizacje prawdziwe zostają nietknięte.
