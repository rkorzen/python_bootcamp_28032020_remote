x = list(range(1, 11))
print(x)

szesciany = []
for el in x:
    if el % 2 == 0:
        szesciany.append(el ** 3)

print(szesciany)

# zbior - set
{1, 2, 3}




print([[el, el**3] for el in range(-10, 10)])

print({el ** 3 for el in x if el % 2 == 0})


print({el: el ** 3 for el in x if el % 2 == 0})


print(tuple(el ** 3 for el in x if el % 2 == 0))



# 1

print([x/10 for x in range(11)])

# 2
print({(x, x**2, x**3) for x in range(-10, 11)})

# 3
napisy = {"xxx", "yyyyy", "xx", "xxxxxxxxxcxcxcxcxcx"}
print({napis:len(napis) for napis in napisy})
