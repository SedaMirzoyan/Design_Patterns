"""
Factory design pattern:
It provides a special class create objects based on input,
we don't need to know how they are built
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class for all animals
    """
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    """
    Implementation of a dog
    """
    def speak(self):
        """
        Returns the sound dog makes

        Return:
            string: Generic message
        """
        return "I am dog"


class Cat(Animal):
    """
    Implementation of a cat
    """
    def speak(self):
        """
        Returns the sound cat makes

        Return:
            string: Generic message
        """
        return "I am cat"


class AnimalFactory:
    """
    Factory class to create animal objects
    """
    def create_animal(self, animal):
        """
        create an animal object based on the provided type

        Args:
            animal (string): Type of an animal ("cat"/"dog")

        Return:
            An object of a cat or dog
        """
        if(animal == "dog"):
            return Dog()
        elif(animal == "cat"):
            return Cat()
        else:
            return None
        

#create objects of dog and cat using the factory
factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")

print(dog.speak())
print(cat.speak())



