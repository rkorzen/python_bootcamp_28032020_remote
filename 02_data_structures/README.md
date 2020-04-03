# Struktury danych, kolekcje

Omówiliśmy na zajęciach kolekcje takie jak tuple (krotki) i listy

## tupla

funkcja wbudowana `tuple` pozwala na utworzenie pustej tupli, lub zrzutowanie
czegoś na tuplę.Np:

    >>> tuple()  # pusta tupla
    ()
    >>> tuple("123")
    ('1', '2', '3')

tupla ma dwie publiczne metody:

* `count` - zliczna ile razy dany obiekt występuje w tupli
* `index` - zwraca index pierwszego wystąpienia danego elementu, lub wyjątek, gdy danego elementu nie ma w tupli

Do tworzenia tupli możemy też użyć nawiasów ()

    >>> elements = (1, 2, 3, 'a', 'b', 'a')
    >>> elements.count(1)
    1
    >>> elements.count('a')
    2
    >>> elements.count("c")
    0
    >>> elements.index('a')
    3

Tupla jest strukturą niemutowalną. Podobnie jak napisy, czy typu numeryczne.
Tzn. nie można zmienić takiego obiektu. Można natomiast utworzyć nowy

    >>> x = (1, 2, 3)
    >>> id(x)
    <jakieś id>
    >>> x = x + (4, 5)
    <inne id>
    >>> x
    (1, 2, 3, 4, 5)

jednoelementowa tupla to np:

    >>> (1, )


## Lista

Do tworzenia listy używamy nawiasów []. Lub funkcji `list`

    >>> list("123")
    ['1', '2', '3']

    >>> [1, 2, 3]
    [1, 2, 3]

oprócz znanych z tupli metod takich jak `count` i `index` mamy też szereg
metod zmieniających stan tupli.

Zadanie:

Przy pomocy dir i help znajdzi i przeczytaj jak działają metody listy


