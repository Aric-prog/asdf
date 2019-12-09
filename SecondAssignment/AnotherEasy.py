class Circle():
    def __init__(self, radius =1.0, color="red"):
        self.__radius = radius
        self.__color = color
    
    def getRadius(self):
        return self.__radius

    def setRadius(self,radius):
        self.__radius = radius
    
    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color
    
    def toString(self):
        print("The radius is ", self.__radius," and the color is ", self.__color)

class Cylinder(Circle):
    __height : float = 1.0

    def __init__(self,height,radius = 1.0,color = "red"):
        self.__height=height
        super().__init__(radius,color)

    def getHeight(self):
        return self.__height

    def setHeight(self , height):
        self.__height = height

    def toString(self):
        print("The radius is ", super().getRadius()," and the color is ", super().getColor(), " and the height is ", self.__height)
    
    def getVolume(self):

        return (3.14 * super().getRadius() * super().getRadius()) * self.__height
    
b = Circle()
a = Cylinder(3,2,"blue")
a.toString()
b.toString()
print(a.getVolume())
