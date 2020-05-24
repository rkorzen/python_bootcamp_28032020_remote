

def foo():
    print(a)

def foo2():
    # zasieg lokalny
    global a
    a = 20
    print(locals())
    print(globals())

    print(a)

def foo3():
    def foo4():
        print("Jestem foo4")

    print("wywoluje foo4 ze srdoka foo3")
    foo4()

# zasieg globalny
a = 10

print(locals())
print(globals())

foo()
foo2()
foo()

foo3()
foo4()

