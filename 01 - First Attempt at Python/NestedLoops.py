# Nested Loops
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")
        
# Challenge
numbers = [5, 2, 5, 2, 2]

for num in numbers:
    output = ''
    for a in range(num):
        output += "x"
    print(output)