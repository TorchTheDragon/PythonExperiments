# Logical Operators
has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Uneligible for loan")

# "and" is used to combine conditions
# "or" is used to check between conditions
# "and not" makes sure one condition is true and the other is false