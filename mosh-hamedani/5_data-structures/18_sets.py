# Sets are collection with no duplicate
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
second = {1, 4} # Sets are defined in curly braces
#Similar to lists, we can add or remove items from a set
second.add(5)
second.remove(5)
len(second)
print(uniques)

#----
print("\n----Separator\n")

numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

print(first | second) #To make a union of two sets use '|'
print(first & second) #To make an intersection of two sets
print(first - second) #To print the different
print(first ^ second) #To print the symettric difference

# Sets are not in sequence unlike lists. Sets are unordered collections
# So we can't access them using index
# So this code will not work - print(first[0])
# If you waant to access the items in sets you need to make them a list

if 1 in first:
    print("Yes")













