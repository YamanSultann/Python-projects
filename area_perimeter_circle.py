import math

class Circle:
    def __init__(self,rad):
        self.rad = rad
    
    def perimeter(self):
        return(math.pi*self.rad**2)

    def area(self):
         return(2*math.pi*self.rad)

circ = Circle(5)
circ.perimeter()
circ.area()
print(circ)