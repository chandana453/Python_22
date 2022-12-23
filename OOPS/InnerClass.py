class Student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()  #creating an object of inner class in outsr class

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    #Inner class
    class Laptop:
        def __init__(self):
         self.brand="HP"
         self.cpu="i5"
         self.ram=8
        def show(self):
            print(self.brand,self.cpu)


s1=Student("John",5)
s2=Student("Mary",7)

s1.show()

print(s1.lap.brand)
lap1=s1.lap
lap2=s2.lap
print(id(lap1))
print(id(lap2))

#lapt1=Student.Laptop()
#print(lapt1)

s1.show()