# For Loops
for item in range(5, 10, 2):
    print(item)
    
# You can use a list instead of a normal variable after the "in." Ex. ['Python', 69, "Minecraft", "Lol"]

# Exercise
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total Cost: ${total}")