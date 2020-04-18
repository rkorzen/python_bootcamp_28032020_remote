

zbior = set()

zbior.add("x")
zbior.add(1)
print(zbior)

for el in zbior:
    print(el)

print(dir(zbior))

a = {1, 2, 3}
b = {2, 3, 4}

print(a | b)    

print(a)
print(b)

print(a & b)  # iloczyn

print(a - b)

print(a ^ b)

print(a.pop())
print(a)

list(range(100))
set(range(100))

