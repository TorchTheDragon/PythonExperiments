# Project: Weight Converter
weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
elif unit.upper() == 'K':
    converted = weight / 0.45
    print(f"You are {converted} pounds")
else:
    print("That is not a valid choice, please try again")