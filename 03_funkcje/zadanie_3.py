# def policz_znaki(text,):
#     return text.index(">") - text.index("<") - 1




def policz_znaki(text, start="<", stop=">"):
    poziom = 0
    licznik = 0

    for znak in text:
        if znak == start:
            poziom += 1
            continue
        elif znak == stop:
            poziom -= 1
            continue

        licznik += poziom

    return licznik

def test_policz_znaki():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4
    assert policz_znaki('ala ma <ko>ta a kot ma ale') == 2
    assert policz_znaki('ala ma <kota> a <kot> ma ale') == 7
    assert policz_znaki('ala ma [kota] a [kot] ma ale', "[", "]") == 7
    assert policz_znaki('a <a<a<a>>>') == 6
    assert policz_znaki('a') == 0
    assert policz_znaki('<a>') == 1
    assert policz_znaki('<<a<a>>>') == 5
