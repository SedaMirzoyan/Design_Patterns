#Factory

class Dog:
    def speak(self):
        return "I am dog"

class Cat:
    def speak(self):
        return "I am cat"

class AnimalFactory:
    def create_animal(self, animal):
        if(animal == "dog"):
            return Dog()
        elif(animal == "cat"):
            return Cat()
        else:
            return None
        

factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")

print(dog.speak())
print(cat.speak())



