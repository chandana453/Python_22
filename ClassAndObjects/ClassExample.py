#Class creates a user-defined data structure, which holds its own data members and member functions, which can be accessed and used by creating an instance of that class. A class is like a blueprint for an object.
#A class is like a blueprint for an object.
#Object is an instance of a class

class Animal:
    attr1="Mammal" #attributes
    attr2="Dog"
    def func(self):
        print("I'm a ",self.attr1)
        print("I'm a ",self.attr2)

    #object instantiation

animal = Animal()   #animal is an object whereas Animal is a class

print(animal.attr1)
print(animal.attr2)
animal.func()
