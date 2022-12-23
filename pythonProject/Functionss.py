def myfunc():
    print("my function")
myfunc()

def printFullName(fname):
    print(fname+" adam")

printFullName("emily")
printFullName("John")
printFullName("ces")

def Samplefunc(fname,lname):
    print(fname+" "+lname)

Samplefunc("emily","refnes")
#the below statement will result in error if we try to call the func with less or more parameters than the actual parameters
#Samplefunc("adams")

#If the number of arguments is unknown, add a * before the parameter name:

def my_func(*kids):
    print("Youngest child is:"+kids[2])

my_func("emil","tobias","lisa")

def my_func(child1,child2,child3):
    print("the youngest child is:"+child3)
my_func(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#my_func("abc","def","ghi")