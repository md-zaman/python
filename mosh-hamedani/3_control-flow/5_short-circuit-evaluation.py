high_income = True
good_credit = True
student = False

if high_income or good_credit and not student: #Boolean operators are short circuit i.e., when python interpreter wants to evaluate expression, it starts for first arguement. If the first arguement is true, it continues otherwise it stops there itself. So in Python, logical operators are short-circuit
    print("Eligible")
else:
    print("Not Eligible")
