# List Methods
numbers = [5, 2, 1, 7, 4]
# numbers.append(20) # Adds a list item to the end
numbers.insert(0, 10) # Adds a list item to a specific position
numbers.remove(5) # Removes a specific value from the list
# numbers.clear() # Clears a list of all values
numbers.pop() # Removes the last value in the list
# numbers.index(5) # Finds the index value of specified value
# numbers.count(5) # Counts how many of a specified value there is in a list
numbers.sort() # Sorts the values in a list
numbers.reverse() # Reverses a list

weh = numbers.copy()
numbers.append(40)

print(numbers)
print(3 in numbers) # Checks if specified value is in list
print(weh)

# Challenge
duplicates = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in duplicates:
    if number not in uniques:
        uniques.append(number)
print(uniques)