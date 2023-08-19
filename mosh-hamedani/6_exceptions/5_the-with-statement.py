try:
    with open("app.py") as file:
        print("file opened.")
        file.__exit
    age = int(input("Age: "))
    xfactor = 10 / age #This will crash our program if we enter zero because we are only handling value error exceptions
except (ValueError, ZeroDivisionError): 
    print("You haven't entered a valid age")
else:
    print("No exeptions were thrown")
