#LIFO - Last In First Out - Example of a browser
browsing_session = []
browsing_session.append(1) #Append is to add an item on top of the stack
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop() #This will remove the last item from the list and return it ALSO
print(last)
print(browsing_session)
print("redirect", browsing_session[-1]) #We need take to user to the previous website he visited which is the last last website on top of the stack now. -1 returns the last item

# Here we need to check if the website is empty or not. If it's empty we need to disable the back button
# There are some empty value discussed earlier. So, we can do something like:
if not browsing_session: #This will return a boolean value to check if the stack is empty or not
    print("disable")










