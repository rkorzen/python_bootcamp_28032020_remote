"""
if <warunek>:
    <blok kodu>
elif <warunek 2>:
    ...
elif <warunek 2>:
    ...
elif <warunek 2>:
    ...
else:
    ...

"""

# if (x>10)
# {
#
# }
# else
# {
#
# }

x = 7
if x > 10:
    print("Większy")
    print("!!!")
elif x % 2 == 0:
    print("Parzysty")
elif x % 3 == 0:
    print("Podzielny przez 3")
else:
    print("Żaden z warunków nie jest spełniony")
print("Koniec")
