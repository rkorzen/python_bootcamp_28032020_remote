zbior = set()

while True:
    polecenie = input("Wpisz liczbę lub k by zakończyć: ")
    if polecenie == "k":
        break
    zbior.add(int(polecenie))

liczby_parzyste = set(range(0, 101, 2))

print(f"Unikalnych liczb: {len(zbior)}")
print(f"Parzystych z zakresu 1-100: {len(zbior & liczby_parzyste)}")







elementy = ["aaa", "aaaaa", "aba", "aba", "aaa", "ababa"]

elementy2 = {"aaa", "aba", "ccc"}

print(elementy2 & set(elementy))