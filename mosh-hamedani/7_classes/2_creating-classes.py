class Point: #We use Pascal Case for class names while defining
    def draw(self):
        print("draw")

point = Point()
print(type(point))
print(isinstance(point, Point)) #Sometimes we want to know if an object belongs to a class


