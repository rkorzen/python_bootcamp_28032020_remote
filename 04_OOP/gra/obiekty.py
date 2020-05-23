import random

class Postac:

    def __init__(self, nazwa: str, energia: int, sila: int):
        self.nazwa = nazwa
        self._energia = energia
        self._sila = sila
        self.ekwipunek = []

    def __str__(self):
        if self.czy_zyje():
            return f"{self.nazwa} (e:{self.energia}, s:{self.sila})"
        return f"{self.nazwa} nie żyje"

    def daj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    @property
    def energia(self):
        e = self._energia
        for przedmiot in self.ekwipunek:
            e += przedmiot.bonus_energia
        return e

    @property
    def sila(self):
        s = self._sila
        for przedmiot in self.ekwipunek:
            s += przedmiot.bonus_sila
        return s

    @staticmethod
    def walka(postac_1, postac_2):
        print("Rozpoczyna się pojedynek pomiędzy: ")
        print(postac_1)
        print("a: ")
        print(postac_2)
        while postac_1.czy_zyje() and postac_2.czy_zyje():
            postac_2.otrzymaj_obrazenia(postac_1.sila)
            if postac_2.czy_zyje():
                postac_1.otrzymaj_obrazenia(postac_2.sila)
        print("Pojedynek zakończył się: ")
        print(postac_1)
        print(postac_2)

    def otrzymaj_obrazenia(self, obrazenia):
        obr = int(obrazenia * random.random())
        print(f"{self.nazwa} otrzymuje {obr} obrażeń")
        self._energia -= obr

    def czy_zyje(self):
        if self.energia > 0:
            return True
        return False


class Przedmiot:

    def __init__(self, nazwa: str, bonus_energia: int = 0, bonus_sila: int = 0):
        self.nazwa = nazwa
        self.bonus_energia = bonus_energia
        self.bonus_sila = bonus_sila

    def __str__(self):
        return f"{self.nazwa} (e:+{self.bonus_energia} s:+{self.bonus_sila})"


class Plansza:
    def __init__(self, n=10, m=10):
        self.N = n
        self.M = m


class Polozenie:

    def __init__(self, x: int, y: int, plansza: Plansza):
        self.x = x
        self.y = y
        self.plansza = plansza

    def __eq__(self, other):
        # return self.x == other.x and self.y == other.y and self.plansza == other.plansza
        return all([
            self.x == other.x,
            self.y == other.y,
            self.plansza == other.plansza
        ])

    @property
    def czy_na_planszy(self):
        if 0 < self.x <= self.plansza.N and 0 < self.y <= self.plansza.M:
            return True
        return False

    def g(self):
        self.y += 1

    def d(self):
        self.y -= 1

    def l(self):
        self.x -= 1

    def p(self):
        self.x += 1

    def __str__(self):
        return f"x:{self.x}, y:{self.y}"

if __name__ == "__main__":
    print(__name__)
    print("To jest print z obiekty!!!!")