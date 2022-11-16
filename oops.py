
#Python Program to Create a Class which Performs Basic Calculator Operations
class Calculator :
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add (self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mult(self):
        return self.a *self.b
    def div(self):
        return self.a/self.b
a = int(input("< "))
b = int(input("< "))
obj = Calculator(a,b)
choice = 1
while choice != 0:
        print("0.Exit")
        print("1.add")
        print("2.sub")
        print("3.mult")
        print("4.div")
        choice = int(input("entere your choice "))
        if choice ==1:
            print("add:",obj.add())
        elif choice ==2:
            print("sub:",obj.sub())
        elif choice ==3:
            print("mult:",obj.mult())
        elif choice ==4:
            print("div:",obj.div())
        else:
            print("invalid choice")
print()
#Python Program to Append, Delete and Display Elements of a List using Classes
class Perform :
    def __init__(self):
        self.list1 = []
    def append(self,a):
        return self.list1.append(a)
    def remove(self,b):
        return  self.list1.remove(b)
    def display(self):
        return self.list1

obj = Perform()
choice = 1
while choice != 0:
        print("0.Exit")
        print("1.add")
        print("2.remove")
        print("3.display")
        choice = int(input("entere your choice "))
        if choice ==1:
            list1=int(input("enter the numbers to append "))
            obj.append(list1)
            print("add:",obj.display())
        elif choice ==2:
            list1 = int(input("enter the numbers to remove "))
            obj.remove(list1)
            print("sub:",obj.display())
        elif choice ==3:
            print("mult:",obj.display())
        elif choice ==0:
            print("EXIT")
        else :
            print("invalid choice")
#Python Program to Find the Area of a Rectangle using Classes
class Area:
    def __init__(self,length,breadth):
        self.length =length
        self.breadth = breadth
    def rec(self):
        return self.length*self.breadth
obj = Area(23,12)
print("areaof rectangle:", obj.rec())
#python program to implement static method and class method and instance method
class Mobile :
    slot = "c-type"
    def __init__(self,company,cam):
        self.company=company
        self.cam = cam
    def calling (self,number):
        print("callling....{}".format(number))
    @classmethod
    def get_power(cls):
        return cls.slot
    @staticmethod
    def caution():
        print("use me in a proper way")
obj1 = Mobile("nokia","10")
obj1.calling(7094389972)
print(obj1.company,obj1.cam,obj1.get_power())
Mobile.caution()


