"""
We must always close a file before continuing because
otherwise our program or some other program might not
be able to access it.
In the example given below, the best part to close the
file would be to add 'finally:'. 'finally:' would be executed 
whether the other lines of codes worked or not
"""

try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age #This will crash our program if we enter zero because we are only handling value error exceptions
except (ValueError, ZeroDivisionError): 
    print("You haven't entered a valid age")
else:
    print("No exeptions were thrown")
finally:
    file.close()

