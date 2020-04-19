def formatuj(*teksty, **znaczniki):
    text = "\n".join(teksty)
    for znacznik, wartosc in znaczniki.items():
        text = text.replace("$"+znacznik, str(wartosc))
    return text

def test_formatuj():
    assert formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10) == 'koszt 10 PLN\nkwota 10 brutto'
    assert formatuj('koszt $cena PLN', 'kwota $cena brutto') == 'koszt $cena PLN\nkwota $cena brutto'
    assert formatuj('koszt $cena PLN', 'kwota $cena brutto', podatek=15) == 'koszt $cena PLN\nkwota $cena brutto'
    assert formatuj('koszt $cena PLN', 'kwota podatku $podatek', podatek=15) == 'koszt $cena PLN\nkwota podatku 15'
    assert formatuj('koszt $cena PLN', podatek=15) == 'koszt $cena PLN'
