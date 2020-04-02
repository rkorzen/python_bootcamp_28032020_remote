# Napisy

str()
'Ala "ma" kota'
"Ala \"ma\" kota"

print("1\n2\n3\n")

print("Programistar\tJunior")

x = """
1
2
3
"""

## łączenie napisów - konkatenacja
n1 = "Ala"
n2 = "kot"

print(n1 + " " + n2)
# ctrl + alt + L

print(f"{n1} {n2}")
print("{} {}".format(n1, n2))
print("{} {}".format(n2, n1))
print("{a} {b}".format(b=n2, a=n1))

print("%s %s" % (n1, n2))
print(f"{n1:>10} {n2:^20}")
x = 10/3
print(f"{x:.4f}")
print("{:>10} {:^20}".format(n2, n1))

napis = "Ala Ma kota"