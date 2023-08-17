numbers = [1, 2, 3]
first, second, third = numbers #This is same as below. Just remember, items on the left has to be equal to the list E.g.,
#first, second = numbers (this will not work because we have less variables to fit in)

first = numbers[0]
second = numbers[1]
third = numbers[2]

#----
number = [1, 2, 3, 4, 4, 4]

first, second, *other = number #This is to avoid the below error and we only want two of the items in the list
print(first)
print(other)

#----

number = [1, 2, 3, 4, 4, 4, 4, 94]
first, *other, last = number 
print(first, last)
print(other) 








