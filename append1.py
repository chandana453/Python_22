#Python Program to Append, Delete and Display Elements of
#a List using classes

a=[3,4,35,8]
class Method:
    # def __int__(self,x):
    #     self.x=x
    def add(self,x):
        a.append(x)
        return a
    def remove(self,x):
        a.remove(x)
        return a
    def dis(self):
        return a

obj1=Method()
print(obj1.add(10))