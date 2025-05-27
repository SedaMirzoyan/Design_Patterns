#Builder design pattern

class Burger:
    def __init__(self):
        self.cheese = None
        self.meat = None
        self.green = None
        self.topping = None

    def __str__(self):
        return f"Burger with {self.cheese} cheese, with {self.meat}, with {self.green} and with {self.topping}"
    

class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def add_meat(self, meat_type):
        self.burger.meat = meat_type
        return self

    def add_cheese(self, cheese_type):
        self.burger.cheese = cheese_type
        return self

    def add_green(self, green_type):
        self.burger.green = green_type
        return self

    def add_topping(self, topping_type):
        self.burger.topping = topping_type
        return self

    def build(self):
        return self.burger

    

builder = BurgerBuilder()
burger = builder.add_meat("beef")
burger = builder.add_cheese("cheddar")
burger = builder.add_green("lettuce")
burger = builder.add_topping("ketchup")
print(burger.build())



