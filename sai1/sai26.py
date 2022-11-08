'''
 Define a class, which have a class parameter and have a same
instance parameter.
Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value
later
solution:
'''
class person:
    #Define the class parameter "name"
    name="person"



    def init (self,name=none):
        #self.name is the instance parameter
        self.name=name


 jeffrey=person("Jeffrey")
print("%s name is %s"%(person.name,jefferey.name))


nico=person()
nico.name="Nico"
PRINT("%s name is %s"%(person.name,nico.name))

