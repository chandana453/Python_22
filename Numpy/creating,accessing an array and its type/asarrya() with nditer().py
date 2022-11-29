# here we can create an array by using asarray with nditer
# some parameters we have to pass to create an array,those are (input,datatype,order)
# input nothing but the variables to pass those may be list,tuple and any combination
# datatype:-here we can give the data type of the elements in the variables
# Order:-Order nothing but the row major or column major order
import numpy as np


import numpy as np

# Row major Order(C)
a=((1,2),(3,4))
b=np.asarray(a,dtype=float,order="C")
print(b)
for i in np.nditer(b):
    print(i)

# Column major order(f)

B=np.asarray(a,dtype=str,order="F")
print(B)
for i in np.nditer(B):
    print(i)