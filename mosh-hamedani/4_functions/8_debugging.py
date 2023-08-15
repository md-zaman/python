def multiply(*numbers):
    total = 1
    for number in numbers:
        # total = total * number (or use an augmented assignment operator)
        total *= number
    return total

print("Start")
print(multiply(1, 2, 3))


"""
To debug click on debug
create the json wala file if this is the first time you're debugging
Go to the line until where you want to debug and press f9
Then press f5 to start debugging to go to the next line of debigging, press f10
Press f11 to start all over again

"""