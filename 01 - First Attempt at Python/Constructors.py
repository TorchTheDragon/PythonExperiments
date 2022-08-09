# Contructors
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    
    def move(self):
        print("Move")
    
    
    def draw(self):
        print("Draw")
        

point = Point(10, 20)
point.x = 11
print(point.x)

# Exercise
class Person:
    def __init__(self, name):
        self.name = name
    
    
    def talk(self):
        print(f"Hello, I am {self.name}!")


torch = Person("Torch")
print(torch.name)
torch.talk()

pyre = Person("Pyre")
print(pyre.name)
pyre.talk()