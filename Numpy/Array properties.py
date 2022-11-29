# an array can have the properties,thos are the listed below
# np.size(array)=it return the array size means no fo values in the array
# np.shape(array)=it return the shape of the array(ex-if the values are 9,then shape-3,3)
# array.dtype=it returns the data type of the values in the array



import numpy as np
a=np.array((1,2,3),dtype=float)
print(a)
print(np.size(a))
print(np.shape(a))
print(a.dtype)