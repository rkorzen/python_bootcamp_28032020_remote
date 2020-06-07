from django.shortcuts import render


class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __repr__(self):
        return f"{self.imie} {self.nazwisko}"

def div(request, a, b):
    tit = "Dzielenie"
    if b == 0:
        wyn = "Błąd dzielenia przez zero"
    else:
        wyn = a / b

    context = {"title": tit, "wynik": wyn}
    return render(
        request=request,
        template_name="maths/output.html",
        context=context
    )


def add(request, a, b):
    tit = "Dodanie"
    wyn = a + b
    context = {"title": tit, "wynik": wyn}
    return render(
        request=request,
        template_name="maths/output.html",
        context=context
    )


def sub(request, a, b):
    tit = "Odejmowanie"
    wyn = a - b
    context = {"title": tit, "wynik": wyn}
    return render(
        request=request,
        template_name="maths/output.html",
        context=context
    )


def mul(request, a, b):
    tit = "Mnożenie"
    wyn = a * b
    context = {"title": tit, "wynik": wyn}
    return render(
        request=request,
        template_name="maths/output.html",
        context=context
    )


def list_example(request):
    dane = [1, 2, 'a', 'b']

    slowa = {"dog": "pies", "cat": "kot"}

    osoba = Osoba("Adam", "Korzeniewski")

    context = {"dane": dane, "slowa": slowa, "osoba": osoba}

    return render(
        request,
        "maths/list_example.html",
        context
    )
