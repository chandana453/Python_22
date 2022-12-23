class Student:
    def __init__(self,name,grades):
        self.name=name
        #self.name="adams"
        #self.grades=(90,90,100)
        self.grades=grades

    def average(self):
        return sum(self.grades)/len(self.grades)


student=Student("Bob",(100,100,95))
student2=Student("Bob",(100,100,100))
print(student.name)
print(student.average())
print(student2.average())


#__str()__ and __repr()__ method - used to represent an object

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # def __str__(self):   --- this method turns your object into a string
    #     return f" Person (Name:{self.name},age:{self.age})"

    def __repr__(self):
        return f"<Person (Name:{self.name},Age:{self.age})>"

person=Person("Bob",25)
print(person)

