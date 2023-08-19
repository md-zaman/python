# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age #This will crash our program if we enter zero because we are only handling value error exceptions
# except ValueError: 
#     print("You haven't entered a valid age")
# except ZeroDivisionError:
#      print("Age cannot be Zero")
# else:
#     print("No exeptions were thrown")

#----
print("\n----Separator\n")

try:
    age = int(input("Age: "))
    xfactor = 10 / age #This will crash our program if we enter zero because we are only handling value error exceptions
except (ValueError, ZeroDivisionError): 
    print("You haven't entered a valid age")
else:
    print("No exeptions were thrown")








