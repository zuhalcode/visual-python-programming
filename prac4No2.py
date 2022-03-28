# volume tube
class Tube:
    def __init__(self, r, h):
        self.r = r
        self.h = h
    def volume(self):
        return 3.14*self.r*self.r*self.h

class Block:
    def __init__(self, w, l, h):
        self.w = w
        self.l = l
        self.h = h
    def volume(self):
        return self.w*self.l*self.h

class TriangularPrism:
    def __init__(self, w, l, h):
        self.w = w
        self.l = l
        self.h = h
    def volume(self):
        return self.w*self.l*self.h/2

tube = Tube(2, 3)
block = Block(2, 3, 4)
triangularPrism = TriangularPrism(2, 3, 4)

print('Tube Volume:', tube.volume())
print('Block Volume:', block.volume())
print('Triangular Prism Volume:', triangularPrism.volume())
