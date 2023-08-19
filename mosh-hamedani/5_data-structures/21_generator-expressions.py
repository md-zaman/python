from sys import getsizeof

values = (x * 2 for x in range(10))
print(values)
for x in values:
    print(x)

# If you have large data set

values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))


