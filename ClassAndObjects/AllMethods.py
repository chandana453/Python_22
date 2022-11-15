#python program to implement static method and class method and instance method

class Person:

    def __init__(self,name,age,can_vote):
        self.name=name
        self.age=age
        self.can_vote=can_vote

    @staticmethod
    def isEligible(age):
        if age>18:
            return True
        else:
            return False

    @classmethod
    def create(cls,name,age):
        if cls.isEligible(age)==True:
            return cls(name, age, "Yes")
        else:
            return cls(name,age,"No")

st1=Person.create("John",25)
st2=Person.create("Adam",17)

print("Can",st1.name,"vote?",st1.can_vote)
print("Can",st2.name,"vote?",st2.can_vote)