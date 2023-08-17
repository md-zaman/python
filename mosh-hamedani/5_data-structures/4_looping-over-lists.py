letters = ["a", "b", "c"]
for letter in letters: 
    print(letter)

print("---") # Just a separation
#------

letters = ["a", "b", "c"]
for letter in enumerate(letters): #enumerate is a built-in function this will return an enumerate object, which is iterable- this will return a tupple
    print(letter[0], letter[1])

print("---") # Just a separation
#-------

letters = ["a", "b", "c"]
for letter in enumerate(letters): #enumerate is a built-in function this will return an enumerate object, which is iterable- this will return a tupple
    print(letter[0], letter[1])


print("---") # Just a separation

letters = ["a", "b", "c"]

for index, letter in enumerate(letters):
    print(index, letter)





