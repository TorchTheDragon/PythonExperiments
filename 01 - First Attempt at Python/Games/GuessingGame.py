# Game: Guessing Game
from random import randint

# secret_number = 9
secret_number = randint(1, 10)
guess_count = 0 # Guesses Taken
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You Won")    
        break
else:
    print("You Lose")