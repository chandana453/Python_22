#Python Program to Create a Class which Performs Basic Calculator Operations

class Calculator:
    #the __init__() method is used to initialize values of that class.
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b

    def sub(self):
       return self.a - self.b

    def mul(self):
       return self.a * self.b

    def div(self):
       return self.a / self.b


a=int(input("Enter element1:"))
b=int(input("Enter element1:"))
calc=Calculator(a,b)

choice=1
while choice!=0:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    n=int(input("Enter choice:"))
    if n==1:
        print("Result: ",calc.add())
    elif n==2:
        print("Result: ",calc.sub())
    elif n==3:
        print("Result: ",calc.mul())
    elif n==4:
        print("Result: ",calc.div())
    elif n ==5:
        print("Exit!")
        break
    else:
        print("Invalid input")



