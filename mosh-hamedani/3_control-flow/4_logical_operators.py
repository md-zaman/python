"""
In Python, we have three logical operators:
1. and (True, if both the coditions are true)
2. or (True, if either of the conditions are true)
3. not
"""

#--- and example

high_income = True
good_credit = True

if high_income and good_credit: #Here, we don't need to write "high_income = True" because it's already a boolean and and checking the same in the condition will be redundant and make it unprofessional
    print("Eligible")


#---- or example

high_income = False
good_credit = True

if high_income or good_credit:
    print("Eligible")
else:
    print("Not Eligible")

#---- not example

high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")






