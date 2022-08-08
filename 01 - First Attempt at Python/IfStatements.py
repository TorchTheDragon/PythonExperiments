# If Statements
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day.")
    print("Drink plenty of water.")
elif is_cold: # Else If
    print("It's a cold day.")
    print("Wear warm clothes.")
else:
    print("It's a lovely day!")
print("Enjoy your day!")

# If statements appear to only run the tabbed lines, not the coding in line with the statement itself

# Exercise
price = 1000000
good_credit = True

if good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f"Down Payment: ${int(down_payment)}")