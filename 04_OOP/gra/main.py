DEBUG = True

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
        self._energia -= obrazenia

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

def gra():
    bohater = Postac("John", 100, 100)
    wrog = Postac("Demon", 100, 100)
    przedmiot = Przedmiot("Krucyfix", 10, 10)

    plansza = Plansza()
    polozenie_bohater = Polozenie(1, 1, plansza)
    polozenie_wrog = Polozenie(5, 5, plansza)
    polozenie_przedmiot = Polozenie(3, 3, plansza)

    print("Rozpoczyna rozgrywkę: ")
    while True:
        if DEBUG:
            print(bohater, polozenie_bohater)
            print(wrog, polozenie_wrog)
            print(przedmiot, polozenie_przedmiot)

        komenda = input("W którą stronę idziesz? (g,d,l,p): ")

        # if komenda == "g":
        #     polozenie_bohater.g()
        # elif komenda == "d":
        #     polozenie_bohater.d()
        # elif komenda == "l":
        #     polozenie_bohater.l()
        # elif komenda == "p":
        #     polozenie_bohater.p()

        try:
            getattr(polozenie_bohater, komenda)()
        except AttributeError:
            print("Wpisz poprawną komendę: ")
            continue

        if not polozenie_bohater.czy_na_planszy:
            print("Wypadłeś za planszę! Koniec!")
            break

        if polozenie_bohater == polozenie_przedmiot:
            print("Znalazłeś przedmiot!!!")
            bohater.daj_przedmiot(przedmiot)
            polozenie_przedmiot.x == -100

        print("Bohater na pozycji: ", polozenie_bohater)



gra()

class TestPostac:

    def test_postac_init(self):
        postac = Postac("Zenek", 100, 100)
        assert postac.nazwa == "Zenek"
        assert postac.energia == 100
        assert postac.sila == 100
        assert postac.ekwipunek == []

    def test_daj_przedmiot(self):
        postac = Postac("Zenek", 110, 90)
        przedmiot = Przedmiot("Flaszka", bonus_energia=20, bonus_sila=15)

        assert postac.energia == 110
        assert postac.sila == 90

        postac.daj_przedmiot(przedmiot)

        assert postac.energia == 130
        assert postac.sila == 105

    def test_czy_zyje(self):
        postac = Postac("John", 10, 10)
        assert postac.czy_zyje() is True
        postac.otrzymaj_obrazenia(15)
        assert postac.czy_zyje() is False

    def test_walka(self):
        silna_postac = Postac("Adam", 1000, 1000)
        slaba_postac = Postac("Weak", 10, 10)
        Postac.walka(silna_postac, slaba_postac)
        silna_postac.czy_zyje() is True
        slaba_postac.czy_zyje() is False

    def test_str(self):
        postac = Postac("John", 123, 112)
        assert str(postac) == "John (e:123, s:112)"
        postac = Postac("John", -123, 112)
        assert str(postac) == "John nie żyje"


class TestPrzedmiot:

    def test_przedmiot_init(self):
        przedmiot = Przedmiot("Siekiera", bonus_sila=30)
        assert przedmiot.nazwa == "Siekiera"
        assert przedmiot.bonus_energia == 0
        assert przedmiot.bonus_sila == 30


class TestPlansza:

    def test_init(self):
        plansza = Plansza()
        assert plansza.N == 10
        assert plansza.M == 10

        plansza = Plansza(100, 200)
        assert plansza.N == 100
        assert plansza.M == 200


class TestPolozenie:

    def test_init(self):
        plansza = Plansza()
        polozenie = Polozenie(5, 6, plansza)
        assert polozenie.x == 5
        assert polozenie.y == 6

    def test_poza_plansza(self):
        plansza = Plansza()
        polozenie = Polozenie(5, 6, plansza)
        assert polozenie.czy_na_planszy is True
        polozenie = Polozenie(15, 6, plansza)
        assert polozenie.czy_na_planszy is False

    def test_porownanie_polozenia(self):
        plansza = Plansza()
        polozenie_1 = Polozenie(5, 6, plansza)
        polozenie_2 = Polozenie(6, 6, plansza)
        assert not (polozenie_1 == polozenie_2)

        polozenie_1 = Polozenie(5, 6, plansza)
        polozenie_2 = Polozenie(5, 6, plansza)

        assert polozenie_1 == polozenie_2

    def test_polozenie_ruch_gora(self):
        plansza = Plansza()
        polozenie = Polozenie(5, 6, plansza)
        assert polozenie.y == 6
        polozenie.g()
        assert polozenie.y == 7

    def test_polozenie_ruch_dol(self):
        plansza = Plansza()
        polozenie = Polozenie(5, 6, plansza)
        assert polozenie.y == 6
        polozenie.d()
        assert polozenie.y == 5

    def test_polozenie_ruch_lewo(self):
        plansza = Plansza()
        polozenie = Polozenie(5, 6, plansza)
        assert polozenie.x == 5
        polozenie.l()
        assert polozenie.x == 4

    def test_polozenie_ruch_prawo(self):
        plansza = Plansza()
        polozenie = Polozenie(5, 6, plansza)
        assert polozenie.x == 5
        polozenie.p()
        assert polozenie.x == 6
