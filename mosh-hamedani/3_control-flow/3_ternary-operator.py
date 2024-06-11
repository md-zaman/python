age = 22
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# A cleaner way of achieving the above result

age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

#Or even simpler

age = 12
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

#So, what we have in our last code is known as ternery 
# operator

