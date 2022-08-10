# Inheritance
class Mammal:
    def walk(self):
            print("Walk")


class Dog(Mammal): # Inheritance allows a class to grab the same methods that other classes have
    def bark(self):
        print("Bark")


class Cat(Mammal):
    def be_annoying(self):
        print("Annoying")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.be_annoying()