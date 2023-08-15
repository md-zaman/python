#while loop is used to repeat something as long a condition is true
number = 100
while number > 0:
    print(number)
#    number = number // 2 (or we can use augmented assignment operators to make this line shorter. We have used // to get an interger value)
    number //= 2

#---
command = ""
while command != "quit":
     command = input (">")
     print("ECHO", command)


#----Acceppt other forms of quit also to end the while loop

command = ""
while command.lower() != "quit":
     command = input (">")
     print("ECHO", command)

