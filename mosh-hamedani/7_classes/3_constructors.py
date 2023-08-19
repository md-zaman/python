class Point:
    def __init__(self, x, y): # This is called the magic method. the word 'self' is added by convention. Then we can added any additional parameters.
# Self is the reference to the current point object
        self.x = x
        self.y = y
        
    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
point.draw()











