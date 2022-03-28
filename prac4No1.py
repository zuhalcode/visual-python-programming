# CLASS RECTANGLES
class Rectangle:
    def __init__(self, width):
        self.width = width

    def area(self):
        return pow(self.width, 2)
    
    def around(self):
        return 4 * self.width

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2
    
    def around(self):
        return self.base + self.height + (self.base * self.height)

class Parrallelogram:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

    def around(self):
        return self.base + self.height + (self.base * self.height)

rectangle = Rectangle(10)
triangle = Triangle(10, 5)
parrallelogram = Parrallelogram(10, 5)

print('Keliling Persegi = ',rectangle.around())
print('Luas Persegi = ',rectangle.area())
print('Keliling Segitiga = ',triangle.around())
print('Luas Segitiga = ',triangle.area())
print('Keliling Jajar Genjang = ',parrallelogram.around())
print('Luas Jajar Genjang = ',parrallelogram.area())
