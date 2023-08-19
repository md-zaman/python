numbers = [1, 2, 3]
print(numbers)

#If you want to unpack and want to print it like 1 2 3 

print(*numbers)

#Another use is when creating list
values = list(range(5))
values = [*range(5), *"Hello"]
print(values)

#----
print("\n----Separator\n")


first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"]
print(values)

#Dictionaries
first = {"x": 1}
second = {"x": 10, "y":2}
combined = {**first, **second, "z": 1}
print(combined)


