napis = "ala ma kota"
zliczenia = dict() # {}

for znak in napis:
    if znak in zliczenia:
        zliczenia[znak] = zliczenia[znak] + 1
    else:
        zliczenia[znak] = 1


for znak in napis:
    zliczenia[znak] = zliczenia.get(znak, 0) + 1

for znak in napis:
    zliczenia[znak] = napis.count(znak)

print(zliczenia)

from collections import defaultdict

zliczenia = defaultdict(int)

for znak in napis:
    zliczenia[znak] += 1

print("333: ", zliczenia)