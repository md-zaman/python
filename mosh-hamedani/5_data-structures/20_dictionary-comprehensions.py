value = []
for x in range(5):
    value.append(x*2)

value = [x * 2 for x in range(5)] #This is identical to the one above

#This can also be converted to sets

value = {x * 2 for x in range(5)}

#----
print("\n----Separator\n")

values = {x: x * 2 for x in range(5)}
print(values)

# We can use comprehensions for lists, sets and dictionaries















