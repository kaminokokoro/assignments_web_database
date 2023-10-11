import math

#class Rectangle:
class Rectangle:
    def __init__(self,a,b) :
        self.a=a
        self.b=b
    
    #method to calculate perimeter
    def perimeter(self):
        return (self.a+self.b)*2
    #method to calculate area
    def area(self):
        return self.a*self.b
    #method to print rectangle
    def __str__(self) -> str:
        return "Rectangle(%s, %s)" % (self.a, self.b)
    
#class Sqare extend from Rectangle
class Square(Rectangle):
    def __init__(self,a) :
        super().__init__(a,a)
    #method to print square
    def __str__(self) -> str:
        return "Square(%s)" % (self.a)
    #method to calculate perimeter
    def perimeter(self):
        return self.a*math.pi*2
    #method to calculate area
    def area(self):
        return self.a**2*math.pi
    
#test
print("Rectangle")
in_rectangle_a=input("Enter length of rectangle: ")
in_rectangle_b=input("Enter width of rectangle: ")
rectangle=Rectangle(int(in_rectangle_a),int(in_rectangle_b))
print(rectangle)
print("Perimeter of rectangle is:",rectangle.perimeter())
print("Area of rectangle is:",rectangle.area())
print("Square")
in_square_a=input("Enter radius of square: ")
square=Square(int(in_square_a))
print(square)
print("Perimeter of square is:",square.perimeter())
print("Area of square is:",square.area())
print("End of the program")