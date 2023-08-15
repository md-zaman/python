"""
lists can be of anything- letters, 
numbers or even list of lists
"""

letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]] #list of lists

# zeros = [0] * 100 #if you want to write list of 100 zeros
# print(zeros)

zeros = [0] * 5
combined = zeros + letters #we can concatenate number booleans or even strings
print(combined)

#---
numbers = list(range(20))# creating a list of 0 to 20
print(numbers)
chars = list("Hello World") # creating a list of a string
print(chars)

print(len(chars)) #printing the number of chars in a list










