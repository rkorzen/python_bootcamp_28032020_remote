# pol_ang = dict()
pol_ang = {
    "kot": "cat",
    "ptak": "bird"
}

pol_ang["pies"] = "dog"
pol_ang["kot"] = "kitty"

dict_2 = dict(a=10, b=22, c=33)

dict_3 = dict([
    ["x", "ala"],
    ["y", "kot"]
])

print(dir(dict_3))

print(dict_3.keys())
print(dict_3.values())
print(dict_3.items())

print(dict_3.get("x"))
print(dict_3.get("z", "brak"))

if 'z' in dict_3:
    print(dict_3["z"])
else:
    print("brak")
