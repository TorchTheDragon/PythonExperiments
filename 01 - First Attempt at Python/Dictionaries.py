# Dictopnaries
customer = {
    "name" : "Torch Xentret",
    "age" : 18,
    "is_verified" : True
}
customer["favorite_color"] = "Red"
print(customer.get("birthday", "June 30th"))

# Exercise
phone = input("Phone ")
digits_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "0" : "Zero"
}
output = ""
for number in phone:
    output += digits_mapping.get(number, "Unknown") + " "
print(output)