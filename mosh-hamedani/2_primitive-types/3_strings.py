course = "Python Programming" #Double Quotes Used

#We also use  triple quotes when we have a long strings

message = """
Hi Zaman,
This is Zaman from Mumbai
""" # Triple quotes used

#Getting the lenght of a string
len(course) #len() function is used to count the number of characters in that string
print(len(course))

print(course[0])
print(course[-1]) #this will print the last character of the string because nothing is before 0
print(course[0:3]) #slicing the characters from 0 to 3, 3 will not be included
print(course[0:]) #if we don't include anything, it will print till the end
print(course[:3]) #by default pythong will put 0 there
print(course[:]) #print start to end

