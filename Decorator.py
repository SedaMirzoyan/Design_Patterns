"""
Decorator design pattern:
It adds new behaviour without changing its original class,
by wrapping it into another object.
"""

class Coffee:
    """
    Base Coffee class, for basic black coffee
    """
    def price(self):
        """
        Return basic coffee's price

        Return:
            float: basic black coffee price
        """
        return 5
    

class CoffeeDecorator(Coffee):
    """
    Base class for coffee decorators

    Attribute:
        coffee (string): coffee type
    """
    def __init__(self, coffee):
        """
        Add behaviour around coffee object

        Args:
            coffee (string): coffee type) 
        """
        self._coffee = coffee


    def price(self):
        """
        Returns coffee price

        Return:
            float: coffee object price
        """
        return self._coffee.price()


class MilkDecorator(CoffeeDecorator):
    """
    Adds milk to the coffee
    """
    def __init__(self, coffee):
        """
        Initialize milk decorator with a coffee instance

        Args:
            coffee (string): coffee type
        """
        self._coffee = coffee

    
    def price(self):
        """
        calculate total price of the coffee, after adding milk
        """
        return self._coffee.price() + 1.5


class SugarDecorator(CoffeeDecorator):
    """
    Adds sugar to the coffee
    """
    def __init__(self, coffee):
        """
        Initialize sugar decorator with a coffee instance

        Args:
            coffee (string): coffee type
        """
        self._coffee = coffee

    def price(self):
        """
        calculate total price of the coffee, after adding sugar
        """
        return self._coffee.price() + 0.5
    


#basic black coffee
coffee = Coffee()
print("coffee price :", coffee.price())

#add milk, make cappuccino
cappuccino = MilkDecorator(coffee)
print("cappuccino price :", cappuccino.price())

#add sugar
cappuccion = SugarDecorator(coffee)
print("cappuccino with sugar price :", cappuccion.price())
