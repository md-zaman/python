# Collection of key value pair
# E.g., Phonebook. In a phonebook, a name is connected to a number
point = {"x":1, "y": 2}

# We can also use the 'dict' function like list(), tuple(), etc.

point = dict(x=1, y=2) #This is a better approach because we don't have to use a quote ("")

#Since dictionaries are collection of key value pairs we cannot print it using its numeric value index

point["x"] = 10 # We can also change the value of x here
point["z"] = 20
print(point)
#----
print("\n----Separator\n")

# point["a"]
# print(point["a"]) #This would be invalid because doesn't comply the above key value pairs
# So, we can use
if "a" in point:
    print(["a"])
else:
    print("Not Found")

# The other solution is to use the get method

print(point.get("a"))
print(point.get("a", 0))

del point["x"]
print(point)

# Loop over dictionaries

for key in point:
    print(key, point[key])

#Another way
for x in point.items():
    print(x)

for key, value in point.items():
    print(x)












