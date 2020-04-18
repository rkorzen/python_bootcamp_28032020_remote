
produkty = {
    "ziemniaki": 2.25,
    "pomiodory": 4.15,
    "cebula": 1.99,
    "kalafior": 3.20
}
magazyn = {
    "ziemniaki": 10,
    "pomiodory": 10,
    "cebula": 10,
    "kalafior": 10
}
# print(produkty.items())
#
# for item in produkty.items():
#     print(item)
#     a, b  = item
#     print(a, b)
#a, b = "k", "v"
#[("k", "v"), ()]

while True:
    komenda = input("Co chcesz zrobić? [k-kup] [z-zakończ] [m-magazyn]")

    if komenda == "z":
        break
    elif komenda == "k":
        print("Nasz zielnik oferuje: ")
        for nazwa, cena in produkty.items():
            print(f" - {nazwa} w cenie: {cena} PLN (stan: {magazyn[nazwa]})")

        produkt = input("Co chcesz kupić? ")

        if produkt in produkty:
            ile = input(f"Ile chcesz kupić [{produkt}]? ")
            ile = float(ile)
            if ile < magazyn[produkt]:
                print(f"Za {ile} kg {produkt} zapłacisz {ile * produkty[produkt]:.2f}")
                magazyn[produkt] = magazyn[produkt] - ile
            else:
                print("Nie mamy tyle produktu")
    elif komenda == "m":
        produkt = input("Co dodajemy? ")
        ile = int(input(f"Ile dodajemy [{produkt}]? "))
        magazyn[produkt] = magazyn.get(produkt, 0) + ile
        if produkt not in produkty:
            cena = float(input(f"Jaka cena za [{produkt}]"))
            produkty[produkt] = cena

    else:
        print("Niezrozumiała komenda")