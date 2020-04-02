# Podstawy

Przydatne w czasie poznawania Pythona funkcje to `help` i `dir`

#### `help` - pomoc

    help()  # by wyjść naciśnij q
    help(print)
    help(dir)
    help(20)

#### `dir`

Zwraca dostępne obiekty w bieżącym zasięgu jeśli jest wywołana bez argumentów.
Wywołana z argumentem zwraca atrybuty i metody danego obiektu.

    >>> dir()
    >>> dir("")
    >>> dir(<jakis obiekt>)

#### `type`

Pozwala sprawdzić typ obiektu, np:

    >>> type(10)
    >>> type("home")
    >>> type(10.1)

#### `id`

Zwraca id obiektu. W standardowej edycji Pythona można o tym pomyśleć jako o
adresie w pamięci

    >>> x = 1
    >>> id(x)

## Liczby

W Pythonie mamy 3 typy liczbowe: `int`, `float`, `complex` odpowiadają one
liczbom całkowitym, zmiennoprzecinkowym i zespolonym

### int

Funkcja wbudowana `int` pozwala rzutować na typ int - gdy jest to możliwe.
Wywołana bez argumentu zwraca 0.

    int()
    int("10")

 Przykładowe liczby:

    10
    -11
    123123123123

Możliwy jest też zapis w systemie binarnym

    0b010010010

ósemkowym:

    0o1234567

szesnastkowym

    0x123456789abcdef

Liczby całkowite mogą teoretycznie być dowolnie duże.
Nie ma w Pythonie ograniczeń na ich wielkość.

### float

Analogicznie jak dla int tu mamy funkcję `float`. Tak też nazywa się typ
Typ ten pozwala na przechowywanie liczb zmiennoprzecinkowych.

    0.1
    0.125

Tu sprawa się nieco komplikuje. Ze względu na to, że liczby we współczesnych
komputerach są zapisywane w systemie binarnym.. niektóre liczby - jak choćby te 0.1
nie mogą być zapisane w sposób dokładny. Zobaczmy:

    >>> 0.1 + 0.1 + 0.1 == 0.3

Jaki będzie wynik? True? False? Dlaczego?

https://docs.python.org/3/tutorial/floatingpoint.html

### complex

Liczby zespolone

    1 + 3j

### operatory matematyczne

    + - * / // % **

### Operatory porównania

    < > <= >= != ==

### Operatory przypisana

    = += -= *= /=

## Typ bool

    True
    False

### Spójniki logiczne

#### and

| A     | B     | A and B |
|:------|:------|:-------- |
| False | False | False   |
| False | True  | False   |
| True  | False | False   |
| True  | True  | True    |

Example:

    x = 10
    print(x < 5 and x % 2 == 0)

#### or

| A     | B     | A or B |
|:------|:------|:-------|
| False | False | False  |
| False | True  | True   |
| True  | False | True   |
| True  | True  | True   |


Example:

    x = 10
    print(x < 5 or x % 2 == 0)

#### not

| A     | not A |
|:------|:------|
| False | False |
| False | True  |

Example:

    x = 10
    print(not x % 5 == 0)

## Napisy

    >>> "To jest napis"
    >>> 'To też jest napis'
    >>> 'to \
    jest \
    napos'

    >>> '''to
    też jest
    napis'''

    >>> """i to
    też"""

    >>> ("To"
    "jest"
    "napis")

Napisy mają też szereg użytecznych metod. `dir("")`

### Łączenie napisów

    >>> x = "Ala"
    >>> y = "Kot"
    >>> x + y
    >>> "%s %s" % (x, y)
    >>> "{} {}".format(x, y)
    >>> "{a} {b}".format(a=x, b=y)
    >>> f"{x} {y}"

## instrukcja warunkowa

    if a > b:
        print("tu blok kodu")
        x = 10
    elif a < b:
        x = 20
    else:
        print("a i b są równe")

## pętla while

    while cos_jest_prawda:
        robimy_to_w_srodku

    while x > 10:
        print(x ** 2)
        x -= 1