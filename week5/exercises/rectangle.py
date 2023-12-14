class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length*self.width
    
    def perimeter(self):
        return 2*(self.length+self.width)
    
rec1=Rectangle(4,5)
rec2=Rectangle(6,9)

print(f"Area1: {rec1.area()}\nPerimeter1: {rec1.perimeter()}")
print(f"Area2: {rec2.area()}\nPerimeter2: {rec2.perimeter()}")