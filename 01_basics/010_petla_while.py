x = 7
temp = 0
while x > 0:
    t = int(input("Podaj temperaturę: "))
    x = x - 1  # x -= 1
    temp = temp + t

print(f"Średnia: {temp/7:.2f}")








i = 10
while True:
    if i == 6:
        i -= 1
        continue
    print(i)
    i -= 1
    if i == 0:
        break
