#The __init__ method is similar to constructors in C++ and Java. Constructors are used to initialize the object’s state. Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation. It runs as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.

class Person:

    # init method or constructor
    def __init__(self,name):
        self.name=name

    #sample method
    def say_hi(self):
        print("Hello, my name is:",self.name)

p=Person("Mounika")
p.say_hi()
