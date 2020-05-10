Stwórzmy grę.

Postać naszego bohatera bedzie poruszać się po zdefiniowanej planszy.
Na planszy w losowych miejsach znajdą się przedmioty oraz wrogowie
Wróg to też postać, ale nie sterowana przez nas

Klasy:

class Postac:
    def __init__(self, imie, atak, obrona, energia):
        self._atak = atak

    @property
    def atak(self):
        "wylicza moc ataku"
        atak = self._atak + # bonus od przedmiotow

    def __str__(self):
        "Opisuje postac - aktualny stan energii i posiadane przedmioty"

    def wylecz(self, ile):
        "Leczy - ale tylko żywe postaci - sprawdź czy_zyje()"

    def otrzymaj_obrazenia(self, ile):
        "Ile obrażeń - zależne od siły ataku i mocy obrony"

    def czy_zyje(self):
        return self.energia > 0

    def moc_ataku(self):
        wynik = randint(self.atak // 2, self.atak)
        return wynik

    def daj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    @staticmethod
    def walka(atakujacy, broniacy):
        "opis walki - walka do końca"


class Przedmiot:
    def __init__(...)

    def __str__(self):
        return f"{self.nazwa}, {self.bonus_atk} do ataku"


class Polozenie():
    "obsluga polozenia postaci, przedmiotow - metody zwiazane z ruchem powinny sprawdzic, czy jestem na planszy"
    def __init__(self, x, y, zasieg_x, zasieg_y):
        self.x = x
        self.y = y
        self.zasieg_x = zasieg_x
        self.zasieg_y = zasieg_y

    def __eq__(self, other):
        "Sprawdza czy polozenia takie same"

    def g(self):
        "Ruch w górę"


    def d(self):
        "Ruch w dół"

    def l(self):
        "Ruch w lewo"

    def p(self):
        "ruch w prawo"

    def __str__(self):
        return f"Twoja pozycja to: x={self.x}, y={self.y}"

class Plansza

    def __init__(self, gracz, wrog, skarb, x=10, y=10):


    def ruch(self):


    def gra(self):
        while True:
            self.ruch()


przydatne narzedzia

import random

print(random.randint(1, 10))


pip install faker

fake = Faker("pl_PL")

https://faker.readthedocs.io/en/master/locales/pl_PL.html

Przykładowe przedstawioenie postaci:




Jestem Rufus, mam 35 ataku i 100/100 życia.
EKWPIUNEK:
Zielony tuplian zniszczenia, 5 do ataku

walka odbywa się pomiędzy atakującym i broniącym, którzy uderzają się na przemian.
Przed każdym uderzeniem wyliczana jest moc_ataku, która jest losową liczbą z zakresu od 0.5 atak do atak



Przykłdowa walka:


Walka: Rufus vs Janusz
Jestem Rufus, mam 35 ataku i 100/100 życia.
EKWPIUNEK:
Zielony tuplian zniszczenia, 5 do ataku

Jestem Janusz, mam 40 ataku i 120/120 życia.
EKWPIUNEK:

Rufus uderza Janusz za 35 obrażeń.
Janusz oberwał za 35 obrażeń.
Janusz uderza Rufus za 30 obrażeń.
Rufus oberwał za 30 obrażeń.
Jestem Rufus, mam 35 ataku i 70/100 życia.
EKWPIUNEK:
Zielony tuplian zniszczenia, 5 do ataku

Jestem Janusz, mam 40 ataku i 85/120 życia.
EKWPIUNEK:

Rufus uderza Janusz za 18 obrażeń.
Janusz oberwał za 18 obrażeń.
Janusz uderza Rufus za 24 obrażeń.
Rufus oberwał za 24 obrażeń.
Jestem Rufus, mam 35 ataku i 46/100 życia.
EKWPIUNEK:
Zielony tuplian zniszczenia, 5 do ataku

Jestem Janusz, mam 40 ataku i 67/120 życia.
EKWPIUNEK:

Rufus uderza Janusz za 33 obrażeń.
Janusz oberwał za 33 obrażeń.
Janusz uderza Rufus za 35 obrażeń.
Rufus oberwał za 35 obrażeń.
Jestem Rufus, mam 35 ataku i 11/100 życia.
EKWPIUNEK:
Zielony tuplian zniszczenia, 5 do ataku

Jestem Janusz, mam 40 ataku i 34/120 życia.
EKWPIUNEK:

Rufus uderza Janusz za 34 obrażeń.
Janusz oberwał za 34 obrażeń.
Janusz uderza Rufus za 20 obrażeń.
Rufus oberwał za 20 obrażeń.
KONIEC WALKI
Jestem Rufus, miałem 35 i nie żyję.
Jestem Janusz, miałem 40 i nie żyję.


