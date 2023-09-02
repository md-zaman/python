# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_int = int(age)
years_left = 90 - age_int
months_left = years_left * 12
weeks_left = months_left * 52
days_left = weeks_left * 7

print(f"You have {days_left} days , {weeks_left} weeks, {years_left} years left")
