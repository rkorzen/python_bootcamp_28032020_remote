# listy

elementy = [1, 2, 3, 4, 5, "xx", 2.0, 2]

print(type(elementy))
print(list())

print(dir(elementy))

#  'append', 'clear', 'copy', 'count',
#  'extend', 'index', 'insert', 'pop',
#  'remove', 'reverse', 'sort'

x = elementy.append("cos")
print(elementy)
print(x)
print(len(elementy))

while len(elementy) < 11:
    elementy.append("xx")
print(elementy)

# print(sum(elementy))
i = 0
while i < len(elementy):
    print(elementy[i])
    i += 1
print("-" * 40)

for xx in elementy:
    print(xx)

for y in "123":
    for x in "abc":
        if x == 'b':
            break
        print(x + y)

dane = [10, 20, 10, 40, 20, 50, -10, -20]


licznik = 0
for i in "123":
    licznik += 1

print("Licznik", licznik)

lista = ["A", 'B', 'C', 'D']
print(lista.index('C') - lista.index('A'))

i = 0
while i < 100:
    index = i % 4
    print(i, lista[index])
    i += 1