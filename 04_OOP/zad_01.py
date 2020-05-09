
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        self.brutto = self.price * 1.23

    def __str__(self):
        return f"<Product: {self.id} | {self.name}>"

    def print_info(self):
        text = f"Produkt \"{self.name}\", id: {self.id}, cena: {self.price} PLN"
        print(text)
        return text

produkt = Product(1, "Woda", 10.99)
print(produkt)

produkt.print_info()



class TestProduct:
    def test_init(self):
        produkt = Product(1, "Woda", 10.99)
        assert produkt
        assert produkt.id == 1
        assert produkt.name == "Woda"
        assert produkt.price == 10.99

    def test_print_info(self):
        produkt = Product(1, "Woda", 10.99)
        assert produkt.print_info() == "Produkt \"Woda\", id: 1, cena: 10.99 PLN"
     #produkt.print_info()