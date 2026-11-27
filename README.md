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
- `strona/` - serwis wielostronicowy (sześć podstron), prawdziwe realizacje
- `podglad/` - ten sam serwis z pięcioma obiektami fikcyjnymi, do pokazania
  jak wygląda wypełnione portfolio; każdy obiekt ma widoczną plakietkę
  „wizualizacja poglądowa · obiekt fikcyjny"
- `ok/` - materiały pomocnicze
- `og.jpg`, `robots.txt`

## Dane demo

Pięć obiektów w `podglad/` nie istnieje. Służą wyłącznie do pokazania układu
portfolio, zanim przyjdą materiały z prawdziwych realizacji. Nie wolno ich
przedstawiać jako referencji. Wszystkie strony mają `noindex`.
