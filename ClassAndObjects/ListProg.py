#2.Python Program to Append, Delete and Display Elements of a List using Classes

class ListOperations:
    def __init__(self):
        self.list1=[]

    def add(self,a):
        self.list1.append(a)

    def rem(self,b):
        self.list1.remove(b)

    def dis(self):
        return self.list1


list=ListOperations()
choice=1
while choice!=0:
    print("0: Exit")
    print("1. Append")
    print("2. Remove")
    print("3. Display")

    n=int(input("Enter choice of operation"))

    if n==0:
        print("Exiting")
        break

    elif n==1:
        k=int(input("Enter the element to append"))
        list.add(k)
        print("List: ", list.dis())


    elif n==2:
        k = int(input("Enter the element to remove"))
        list.rem(k)
        print("List: ", list.dis())

    elif n==3:
        print("Displaying the elements of a list:")
        print("List: ", list.dis())

    else:
        print("Invalid input")

print()