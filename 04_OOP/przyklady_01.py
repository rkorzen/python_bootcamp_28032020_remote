class Monitor:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"<Monitor {self.brand} | {self.model}>"

    def wlacz(self):
        print(self, "włącza się")

    def wylacz(self):
        print(self, "wyłączony ...")

lista = list()
lista.append("cos")

m = Monitor("Philips", "M01x1")
m2 = Monitor("Sony", "BV02")
print(m)
print(m)
print(m2.brand)

m.wlacz()
m.wylacz()
