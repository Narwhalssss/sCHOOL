from math import pi
class cirlce:
    
    def __init__(self,radius=1.0,color='red'):
        self.radius = radius
        self.color = color
        
        
    def getRadius(self):
        return self.radius
    
    def getColor(self):
        return self.color
    
    def setradius(self,radius):
        self.radius = radius
        
    def toString(self):
        print(f"Radius is {self.radius} and the color is {self.color}")
    
    def setColor(self,color):
        self.color = color
        
    def getArea(self,radius=10):
        area = pi*(radius**2)
        print('The area of the circle is %0.2f' %area)
        return area
    
    