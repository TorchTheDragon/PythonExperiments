# Modules
import converters # Imports entire module
from converters import kg_to_lbs # Imports a specific module part so you wont have to use the module name
# from converters import * # Imports all functions from a module

kg_to_lbs(80)
print(converters.kg_to_lbs(70))

# Exercise
# import custom_math
from custom_math import *

numbers = [10, 7, 2, 9, 123, 54, 128, 54, 287, 23, 573, 89, 43]
numbers2 = [234, 345, 5, 63, 2, 644, 23, 674]

max_num = maximum_number(numbers, False)
print(max_num)

maximum_number(numbers2, True)