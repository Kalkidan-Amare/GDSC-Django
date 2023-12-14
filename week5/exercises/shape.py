class Shape:
    def __init__(self,_color):
        self._color = _color
    
    def get_color(self):
        return self._color
    
    def area(self):
        return self.base*self.height*0.5
    
class Rectangle(Shape):
    def __init__(self,length,width,color):
        super().__init__(color)
        self.length =length
        self.width = width
    def area(self):
        return self.width*self.length

class Circle(Shape):
    def __init__(self,radius,color):
        super().__init__(color)
        self.radius =radius
    
    def area(self):
        return 3.14*self.radius*self.radius
    
class Triangle(Shape):
    def __init__(self,base,height,color):
        super().__init__(color)
        self.base = base
        self.height = height
    
rec=Rectangle(3,4,"RED")
circle=Circle(3,'White')
tri=Triangle(5,4,"Blue")


# rec._color="red"
# circle._color="white"

print(f"Area rec: {rec.area()} Color: {rec.get_color()}")
print(f"Area circle: {circle.area()} Color: {circle.get_color()}")
print(f"Area triagle: {tri.area()} Color: {tri.get_color()}")