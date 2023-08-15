#Making a parameter optional
def increment(number, by=1): # By add by=1 we can make a parameter optional; just remeber the optional parameter should be after all required parametres
    return number + by


print(increment(number=2))


