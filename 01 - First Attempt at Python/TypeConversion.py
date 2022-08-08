from datetime import date # Not from tutorial, but I would like this to still be accurate later on

# Type Conversion
birth_year = input("Birth year: ")
print(type(birth_year))
cur_year = date.today().year # More advanced than the tutorial, but still works
age = cur_year - int(birth_year)
print(type(age))
print(age)

# Solution
weight_lbs = input("Weight (lbs): ")
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

# Actually useful, will have to remember