# def przywitanie(name="World!"):
#     if name == "xxx":
#         return "Nie używamy brzydkich słów!"
#     return f"Hello {name}"
#
#
# print(przywitanie("Rafał"))
# przywitanie("Adam")
# przywitanie("Marcin")
# przywitanie("Paulina")
# przywitanie("Maria")
#
# przywitanie("xxx")
#
# #print(3, x)
# def incrementator(poczatek, krok=1):
#     return poczatek + krok
# print(incrementator(10))  # 11
# print(incrementator(14))  # 15
# print(incrementator(14, 4))  # 18
#

def zlacz_teksty(lista_textow):
    return " ".join(lista_textow)

lista = ["A", "B", "C"]

print(zlacz_teksty(lista))

t1 = "A"
t2 = "B"
t3 = "C"

def zlacz_teksty(*args, **kwargs):
    #print(args)
    #print(kwargs)
    text = "\n".join(args)
    for k, v in kwargs.items():
        text = text.replace(k, str(v))
    return text

slownik = dict(x=10, y=20)
print(slownik)

zlacz_teksty(t1, t2, t3, x=1, y=2, z=10)
zlacz_teksty(t1, t3)
print("-"*40)
print(zlacz_teksty(t1, "xxx", y=10))
print("-"*40)
print(zlacz_teksty(t1, "xxx", x=10))


def foo(a, *args, x=1, **kwargs):
    print("Argument a: ", a)
    print("*args", args)
    print("x", x)
    print("**kwargs", kwargs)
    print("-"*40)

foo(10)
foo(12, 23, "A",  x=20, y=30, z=10)


kolekcja = [(10, "z"), (5, "c"), (15, "a")]

def second(x):
    return x[1]

second = lambda x: x[1]

print(sorted(kolekcja, key=second))

print(sorted(kolekcja, key=lambda x: x[1]))

suma = lambda x, y: x + y
print((lambda x, y: x + y)(1, 2))
print(suma(1, 2))


lista_osob = ["Jan Nowak", "Anna Zagajska", "Mateusz Pospieszalski", "Piotr Baron"]

print(sorted(lista_osob, key=lambda x: x.split()[1]))

["Piotr Baron", "Jan Nowak",  "Mateusz Pospieszalski", "Anna Zagajska",]


def decrement(n):
    if n == 0:
        print(0)
        return
    print(n)
    decrement(n-1)

decrement(10)

# 5! = 5*4! = 5*4*3! = ... = 5*4*3*2*1*0! = 120
