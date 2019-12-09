class Triangle:
    def __init__(self,base,height):
        self.base = base;
        self.height = height;
        
    def t_area(self):
        return self.base * self.height/2

class Square:
    def __init__(self,side):
        self.side = side
    
    def s_area(self):
        return self.side**2

class Area(Triangle,Square):
    def __init__(self,a,b = 0):
        super().__init__(a,b)
    
    def areas(self):#returns area for triangle or square
        if(super().t_area() != 0):
            return super().t_area()
        self.side = self.base
        return super().s_area()

luas = Area(2,4)
print(luas.areas())
b = Area(8)
print(b.areas())
