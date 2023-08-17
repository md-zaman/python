letters = ["a", "b", "c"]

#Adding items

letters.append("d")
print(letters)
#----

#If you want to add any items at a specific position use "insert" method
letters.insert(0, "-")
print(letters)

#---Remove an item at the end of the list, you can use "pop" method

letters.pop()
print(letters)

#We cal also pass an index here

letters.pop(0)
print(letters)

#When you want to remove an object but we don't know its index, we can use "remove"


letters.pop()
letters.remove("b") #This will only remove the first occurence of the letter 'b'
print(letters)

#If you want to remove all 'b's in the list, you have to look into the list and remove each b individually

#-----
#Another way to remove an item in the list is 'del' method. Here we can delete a range also
letters.pop()
# letters.remove("b") (comenting this line because removed earlier)
del letters[0:3]
#pop removes an individual items while delete removes range of items
print(letters)

#----

#If you want to remove all the objects from a list you can use 'clear' method
letters.clear()
print(letters)
#This list was already empty








