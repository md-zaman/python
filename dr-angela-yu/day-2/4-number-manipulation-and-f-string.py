# To round numbers use 'round' function
print(round(8 / 3))

# We can also add upto how much decimal we need after comma inside bracket
# E.g., 
print(round(8 / 3, 4)) # ', 4' will round upto 4 Decimal places

# We can get flow division '//' i.e., We won't get decimal value after that
# This is prevent us from converting the number to an integer afterwards
# The datatype is also an integer in this case
# E.g., 
print(8 // 3)

# --
# We can do make calculations consecutively
# E.g., 
result = 4 / 2
result /= 2 # Doing the division by 2 again

# This manupulates value based on its previous value


#---
# Thus far we've seen that when we have different datatypes we 
# convert these datatypes when we what to print. The solution 
# to this is using f-string. Use f-string just before the quotes
# to merge different datatypes and put the datatypes in curly braces
# E.g., 
score = 0
height = 1.8
isWinning = True

print(f"Your score is {score}, your height is {height}, yar are winning is {isWinning}")




