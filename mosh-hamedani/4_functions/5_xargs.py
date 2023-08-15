def multiply(*numbers): #Instead of putting number of parametres we have put *numbers so that we can accept n number of arguements
    print (numbers)

multiply(2, 3, 4, 5)

#The output is a tupple in brackets. it's similar to a list as in it's a collection of objects. These tuples, just like lists are iterable



def multiply(*numbers):
    total = 1
    for number in numbers:
        # total = total * number (or use an augmented assignment operator)
        total *= number
    return total

print(multiply(2, 3, 4, 5))