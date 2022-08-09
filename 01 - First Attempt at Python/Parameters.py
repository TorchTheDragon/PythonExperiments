# Parameters
first_name = input("First Name: ")
last_name = input("Last Name: ")

def greet_user(name_first, name_last):
    print(f"Hi {name_first} {name_last}!")
    print("Welcome aboard")

print("Start")
greet_user(first_name, last_name)
print("Finish")