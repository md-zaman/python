print("Welcome to the tip calculator")
bill = float(input("What was the total bill $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
total_tip = ((tip / 100) * bill) + bill
people_count = int(input("How many people to split the bill?"))
per_person = round(total_tip / people_count, 2)
print(f"Each person should pay: ${per_person}")
