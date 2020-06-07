from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
Wynik: {wynik}
</body>
</html>"""

def div(request, a, b):
    tit = "Dzielenie"
    if b == 0:
        wyn = "Błąd dzielenia przez zero"
    else:
        wyn = a / b

    output = html_template.format(title=tit, wynik=wyn)
    return HttpResponse(output)


def add(request, a, b):
    tit = "Dodanie"
    wyn = a + b
    context = {"title": tit, "wynik":wyn}
    return render(
        request=request,
        template_name="maths/output.html",
        context=context
    )


def sub(request, a, b):
    return HttpResponse(f"Wynik {a - b}")


def mul(request, a, b):
    return HttpResponse(f"Wynik {a * b}")
