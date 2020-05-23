from obiekty import Polozenie, Postac, Przedmiot, Plansza
import sys
print(sys.path)

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
