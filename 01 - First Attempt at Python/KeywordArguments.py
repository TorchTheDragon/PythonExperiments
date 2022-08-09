# Keyword Arguments
def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")

print("Start")
greet_user(last_name="Xentret", first_name="Torch") 
# A keyword argument is essentially just specifying what value in a function you want to edit.
# Can't have a positional agrument after a keyword argument
# WRONG: greet_user(first_name="Torch", "Xentret")
# RIGHT: greet_user("Torch", last_name="Xentret")
print("Finish")

# Example
# calc_cost(total=50, shipping=5, discount=0.1)