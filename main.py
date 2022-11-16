'''
python program to create a class which performs basic calcuator
operators
'''
class cal:
    def __int__(self,a,b):
        self.a=a
        self.b=b

    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b

A=int(input("enter the first number"))
B=int(input("enter the second number"))
obj1=cal()
print(obj1.add(A,B),obj1.sub(A,B),obj1.mul(A,B),obj1.div(A,B))