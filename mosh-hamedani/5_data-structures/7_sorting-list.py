numbers = [3, 51, 2, 8, 6]
numbers.sort() # this will print items in the list in ascending order
print(numbers)

#----
print("\n----Separator\n")


numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True) #In decending order
print(numbers)

#----
print("\n----Separator\n")

numbers = [3, 51, 2, 8, 6]
print(sorted(numbers)) #This will not modify the original list. This is make a new sorted list
print(numbers)
#This will print the sorted list first followed by the original list

#----
print("\n----Separator\n")

numbers = [3, 51, 2, 8, 6]
print(sorted(numbers, reverse=True)) #To reverese
print(numbers)

#----
print("\n----Separator\n")

items = [
    ("Product", 10),
    ("Product", 9),
    ("Product", 12),
] #When we have a tupple but Python won't be able to sort this list. So, we define a function
items.sort()
print(items)

#----
print("\n----Separator\n")

items = [
    ("Product", 10),
    ("Product", 9),
    ("Product", 12),
]
def sort_item(item):
    return item[1]

items.sort(key=sort_item) #Remember key from dictionary
print(items)


























