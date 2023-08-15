letters = ["a", "b", "c", "d"]
print(letters[0]) #printing in a list


print(letters[-1]) #we get the last letter, similar to string

letters[0] = "A" #using square brackets, you can also change/replace something in a list, you have to mention the index and the value you want to replace

print(letters[0:3]) #slicing something from a list

print(letters[:3]) #if you don't specify the first arguement, 0 will be assigned by default

print(letters[0:]) #similarly if you specify the end index, it will print till the end

print(letters[:]) #anything not assigned.. you've got the point

print(letters[::2]) #known as step, helps us to print every 2nd or 3rd or whatever assigned step to print

#-----
number = list(range(20))
print(number[::2])

print(number[::-2]) #will print is reverse order





























