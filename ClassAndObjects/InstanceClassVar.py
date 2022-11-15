#Instance variables are variables whose value is assigned inside a constructor or method with self whereas class variables are variables whose value is assigned in the class.


class Dog:
    #class variable
    animal="dog"

    def __init__(self,breed,color):
        # Instance Variables
        self.breed=breed
        self.color=color

# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

#class variables can be accessed using class name
print(Dog.animal)


#program to show that we can create instance variables inside methods

class Animal:
    animal="Dog"

    def __init__(self,breed):
        self.breed=breed

    def setColor(self,color):
        self.color=color

    def getColor(self):
        return self.color

ani= Animal("Shihtzu")
ani.setColor("brown")
print(ani.getColor())
