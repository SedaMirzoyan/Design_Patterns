"""
Builder design pattern:
The goal of this design pattern is to separate 
the construction of an object of its representation
"""

class Burger:
    """
    Class represents final burger product

    Attributes:
        cheese (string): cheese type attribute
        meat (string): meat type
        green (string): green type
        topping (string): topping type
    """
    def __init__(self):
        """
        Initialize ingredients with None
        """
        self.cheese = None
        self.meat = None
        self.green = None
        self.topping = None


    def __str__(self):
        """
        Overloading of __str__ magic method, print burger ingredients 
        """
        return f"Burger with {self.cheese} cheese, with {self.meat}, with {self.green} and with {self.topping}"
    

class BurgerBuilder:
    """
    class to construct a burger
    """
    def __init__(self):
        """
        Initializes a new Burger object
        """
        self.burger = Burger()


    def add_meat(self, meat_type):
        """
        adds meat to a burger

        Args:
            meat_type (string): meat type (beef, pork, chicken)
        Return:
            The builder instance 
        """
        self.burger.meat = meat_type
        return self


    def add_cheese(self, cheese_type):
        """
        adds cheese to a burger

        Args:
            cheese_type (string): cheese type (cheddar, mozzarella, parmesan)
        Return:
            The builder instance 
        """
        self.burger.cheese = cheese_type
        return self
    

    def add_green(self, green_type):
        """
        adds green to a burger

        Args:
            green_type (string): green type (lettuce, rucola, parsley)
        Return:
            The builder instance 
        """
        self.burger.green = green_type
        return self


    def add_topping(self, topping_type):
        """
        adds topping to a burger

        Args:
            topping_type (string): topping type (ketchup, cheese sauce, mayonnaise)
        Return:
            The builder instance 
        """
        self.burger.topping = topping_type
        return self


    def build(self):
        """
        constructs a completed burger

        Return:
            The burger instance 
        """
        return self.burger

    


builder = BurgerBuilder()
burger = builder.add_meat("beef")
burger = builder.add_cheese("cheddar")
burger = builder.add_green("lettuce")
burger = builder.add_topping("ketchup")
print(burger.build())



