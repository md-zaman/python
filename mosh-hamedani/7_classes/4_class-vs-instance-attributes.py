class Point:
    default_color = "red"
    def __init__(self, x, y): # This is called the magic method. the word 'self' is added by convention. Then we can added any additional parameters.
# Self is the reference to the current point object
        self.x = x
        self.y = y
        
    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
point.z = 10
point.draw()

another = Point(3, 4)
another.draw()











