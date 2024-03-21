class Avto:
    def __init__(self ,brand ,model, god, price):
        self.brand = brand
        self.model = model
        self.god = god
        self.price = price

    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"God: {self.god}")
        print(f"Price: {self.price}")

mers = Avto("Mersedes |", "E63 |", "2020 |", "40.000$ - 80.000$ |")
cadillac = Avto("Cadillac |", "FLEEDWOOD |", "1983 |", "5.000$ - 10.000$ |")
dodge = Avto("Dodge  |", "challenger |", "2016 |", "15.000$ - 30.000$ |")

