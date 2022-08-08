# Comparison Operators
temperature = 17

if temperature > 30:
    print("It's a hot day")
elif temperature < 10:
    print("It's a cold day")
else:
    print("It's not hot nor cold, perfect")
    
# "==" is used to compare if one thing is equal to another
# "!+" is used to compare if one thing isn't equal to another
# You can add "=" to the end of a greater than or less than sign. Ex. >=

# Exercise
name = input("What is your name? ")

if len(name) < 3:
    print("Name must be greater than 3 characters long")
elif len(name) > 50:
    print("Name cannot be over 50 characters long")
else:
    print(f"{name} fits right into the boundries")