
request - zapytanie robione przez użytkownika.

request wędruje do serwera HTTP

http://www.alx.pl -> serwer HTTP przekierowuje np do Django

http://www.alx.pl/kursy
Django w oparciu o mechnizm rouitingu przekierowuje request do
funkcji zwanych widokami
i te funkcje przygotowuja odpowiedź - response


Napisz roting i funkcje widoków, które obsłużą działania matematyczne:

http://locahost:8000/math/add/1/2
wynik: 3

http://locahost:8000/math/sub/1/2
wynik: -1

http://locahost:8000/math/div/1/2
wynik: 0.5

http://locahost:8000/math/div/1/0
wynik: Błąd dzielenia przez 0

http://locahost:8000/math/mul/1/2
wynik: 2



