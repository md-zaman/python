# A tupple is basically a read-only list
# We can use to to contain a sequence of objects but we cant modify it
# New object can't be added or removed

point = (1, 2) 
"""
In case you want to add only one item, you must add a 
comma (,) inorder to make python understand that it's 
not an integer.
Also if you want to define empty tuple, you must use a
parenthesis
"""
print(type(point))

#----
print("\n----Separator\n")


"""
Similar to lists, we can concatenate tuples

"""
point = (1, 2) + (3, 4)
print(point)

#----
print("\n----Separator\n")

#We can use a multiplication operator to reapeat a tuple

point = (1, 2) * 3
print(point)

















