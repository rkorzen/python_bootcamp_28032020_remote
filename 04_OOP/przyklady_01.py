class Monitor:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"<Monitor {self.brand} | {self.model}>"

    def wlacz(self):
        print(self, "włącza się")

    def wylacz(self):
        print(self, "wyłączony ...")


lista = list()
lista.append("cos")

m = Monitor("Philips", "M01x1")
m2 = Monitor("Sony", "BV02")
print(m)
print(m)
print(m2.brand)

m.wlacz()
m.wylacz()

# przeciażanie operatorów
import math


class Kwadrat:

    def __init__(self, bok):
        self.bok = bok

    def __add__(self, other):
        "Kwadrat + Kwadrat"
        bok = math.sqrt(self.pole + other.pole)
        return Kwadrat(bok)

    def __radd__(self, other):
        "int + Kwadrat"
        bok = self.bok + other
        return Kwadrat(bok)

    def __gt__(self, other):
        return self.bok > other.bok

    def __gte__(self, other):
        return self.bok >= other.bok

    def __eq__(self, other):
        return self.bok == other.bok

    def __mul__(self, other):
        if isinstance(other, int):
            return Kwadrat(self.bok * other)
        elif isinstance(other, Kwadrat):
            return Kwadrat(self.bok * other.bok)
        else:
            raise NotImplementedError()

    def __str__(self):
        return f"<Kwadrat: {self.bok}>"

    @property
    def obowd(self):
        return self.bok * 4

    @property
    def pole(self):
        return self.bok ** 2

    def porownaj(self, other):
        return self.bok == other.bok


kw1 = Kwadrat(4)
kw2 = Kwadrat(5)
kw3 = Kwadrat(4)
print(kw1.pole)
print(kw2.pole)

# self + other
# wynik = kw1 + kw2

print(kw1 < kw2)

print(kw1 + kw3)
print(kw1.__add__(kw3))
print(kw1 == kw3)
print(kw1.__eq__(kw3))
print(kw1.porownaj(kw3))

print(kw1 * 3)
print(kw1 * kw2)
# print(kw1 * "ala")

# kw1 + 2
# kw1.__add__(2)

print(2 + kw1)
# 2.__add__(kw1)
kw1.__radd__(2)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


Vector(1, 2)
Vector(x=1, y=2)
Vector(y=2, x=1)

print(pow(4, 0.5))


class Zwierze:
    def __init__(self, name):
        self.name = name
        self.krolestwo = "Zwierzęta"

    def przedstaw_sie(self):
        print(f"Cześć jestem, {self.name}")


zw = Zwierze("Bugs")

zw.przedstaw_sie()

class Pies(Zwierze):
    def __init__(self, name, rasa):
        super().__init__(name)
        self.rasa = rasa

pies = Pies("Pluto", "Owczarek Podhalański")
pies.przedstaw_sie()
print(pies.rasa)
print(pies.krolestwo)

class ExceptionFull(Exception):
    pass

class Pojemnik:

    def __init__(self, capacity):
        self.elements = []
        self.capacity = capacity

    def add_element(self, element):
        # if 5 in self.elements:
        #     raise ValueError("Nie możemy tu mieć 5-ki")
        if len(self.elements) == self.capacity:
            raise ExceptionFull("Capacity przekroczone")
        self.elements.append(element)


p = Pojemnik(3)
p.add_element(1)
p.add_element(1)
p.add_element(1)
p.add_element(1)


# try:
#     for i in range(20):
#         p.add_element(i)
# except ExceptionFull:
#     print("Więcej nie można dodać")
# except ValueError:
#     print("Ktoś tam znowu wrzucił 5-kę")

print(p.elements)

import pytest

def test_pojemnik():
    p = Pojemnik(3)
    p.add_element(1)
    p.add_element(1)
    p.add_element(1)

    with pytest.raises(ExceptionFull):
        p.add_element(4)