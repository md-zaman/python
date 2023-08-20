class Point:
    def draw(self):
        print("draw")

point = Point(1, 2) #Suppose we have a function like the one above and at times we want to pass two values like x and y co ordinates
# To achieve this, we need a constructor, which is a special method that is called when we create a new point object

#----
print("\n----Separator\n")

# How to create a constructor:

class Point:
    def __init__(self, x, y): # This is called the magic method. This magic method is called constructor and is executed when we create a new point object. The word 'self' is added by convention. Then we can added any additional parameters.
# Self is the reference to the current point object
# For all the methods that we define in a class, should have atleast one parameter which we call self by convention
        self.x = x
        self.y = y
        
    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
print.draw()










