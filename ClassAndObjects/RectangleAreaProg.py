#Python Program to Find the Area of a Rectangle using Classes

class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length * self.breadth

a=int(input("Enter length:"))
b=int(input("Enter breadth:"))
rect=Rectangle(a,b)
print("Area of rectangle is:",rect.area())