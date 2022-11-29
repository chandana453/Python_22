# This is also same as array function,we have to take some values and has to creat an array
# some perameters we have to pass(variable,dtype)
# dtype:we can give the str also like as "S1"
# we can giue the count also,that is optional
# we dont have to use Order parameter in the fromiter()


import numpy as np

a=[1,2,3,4]
b=np.fromiter(a,dtype="int",count=2)
print(b,type(b),b.ndim)