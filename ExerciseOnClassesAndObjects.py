from math import* 
class Point():
    x = 0 
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distanceFromOrigin(self):
        return sqrt(self.x**2 + self.y**2)
    
    def distanceWithOtherPoint(self , other):
        x = self.x - other.x
        y = self.y - other.y
        return sqrt(x**2 + y**2)

p1 = Point(1,1)
p2 = Point(5,1)
print(p1.distanceWithOtherPoint(p2))







