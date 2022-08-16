# Generating Random Values
import random

for i in range(3):
    # print(random.random())
    print(random.randint(10, 20))
    
members = ['Torch', 'Pyre', 'Kawatta', 'Kinder']
leader = random.choice(members)
print(leader)

# Exercise
class Dice():
    def roll(dice = 1):
        output = []
        for times in range(dice):
            rolled_number = random.randint(1, 6)
            output.append(rolled_number)
        return tuple(output)
        
        
dice1 = Dice.roll(2)
dice2 = Dice.roll(2)
dice3 = Dice.roll(5)
print(dice1)
print(dice2)
print(dice3)