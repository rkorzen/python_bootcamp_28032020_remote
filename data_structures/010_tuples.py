# krotka, tupla
x = (1, 2, 3, 10, 12, "ala", "mmm", 2.0, 12)
#    0  1  2  3   4   5      6      7
print(x)
print(type(x))
print(dir(x))

print(x.index("ala"))
if 'xxxxx' in x:
    print(x.index('xxxxx'))

print(len(x))
print(len("Ala"))
print(x.count(12))

print("b" in "Olaf")
print(3 in x)
y = "ala ma kota kot ma ale"
print(x[0])
print(x[-3])
print(x[0:6])
print(x[:6])

print(x[::2])
print(y[::-1])

print(tuple("123"))

x = tuple()
x = ()
print(type(x))

x = ("ala"
     "ma"
     "kota")

x = "ala" + \
    "ma" + \
    "kota"

x = (1,)
print(x)
print(type(x))

x = (1, 2)
y = (3, 4)
print(x + y)

a, b = 1, 2
wynik = (a, b) == (1, 2)
print("xxx", wynik)

print(a, b)
