#Decorator

class Coffee:
    def price(self):
        return 5
    
class CoffeeDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def price(self):
        return self._coffee.price()


class Cappuccino(CoffeeDecorator):
    def __init__(self, coffee):
        self._coffee = coffee

    def price(self):
        return self._coffee.price() + 1.5

class Espresso(CoffeeDecorator):
    def __init__(self, coffee):
        self._coffee = coffee

    def price(self):
        return self._coffee.price() + 0.5
    


coffee = Coffee()
print("coffee price :", coffee.price())

cappuccino = Cappuccino(coffee)
print("cappuccino price :", cappuccino.price())

espresso = Espresso(coffee)
print("espresso price :", espresso.price())
