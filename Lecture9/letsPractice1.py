'''
Define a Circle class to create a circle with radius r using the the constructor.
Define an Area() method of the class which calculates the ara of the circle.
Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
'''

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        print((22/7) * self.radius ** 2)

    def Perimeter(self):
        print(2 * (22/7) * self.radius)

obj1 = Circle(23)
obj1.Area()
obj1.Perimeter()