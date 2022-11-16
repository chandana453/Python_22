#python program ro find the area of a rectangle
#using classes
class rec:
    def area(self,length,breadth):
        return length*breadth

A=int(input("enter the length of rectangle"))
B=int(input("enter the breadth of rectangle "))
obj1=rec()
print("the area of rectangle",obj1.area(A,B))
