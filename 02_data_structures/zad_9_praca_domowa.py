
cyfry_slownie = ["zero", "jeden", "dwa", "trzy"]
#                 0      1        2      3
text = "ala ma 3123"

out = []

for znak in text:
    if znak.isdigit():
        out.append(cyfry_slownie[int(znak)])

print(out)
print(" ".join(out))

#print(dir("1"))
#print(help("1".isdigit))
print(help(print))

print(1, 2, sep=";", end=";")
print(3, 4, sep=";")