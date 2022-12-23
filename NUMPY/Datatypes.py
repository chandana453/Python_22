#To check the datatype of an array -> use dtype

import numpy as np
a=np.array([1,2,3,4])
print(a.dtype)

b=np.array(["a","bc","def"])
print(b.dtype)  #o/p:U3 -> U stands for UNICODE STRING

c=np.array(['apple','cherry','mango'])
print(c.dtype)

#We use the array() function to create arrays, this function can take an optional argument: dtype that allows us to define the expected data type of the array elements:

#Create an array with data type string
arr=np.array([1,2,3],dtype='S') #S -> string
print(arr)
print(arr.dtype)

a=np.array([1,2,3,4], dtype="i8") #i8 - integer with 8 bytes
print(a)
print(a.dtype)

#The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.
b=np.array([1.3,2.4,3.5])
new_b=b.astype('i')  #Change data type from float to integer by using 'i' as parameter value
print(new_b)
print(new_b.dtype)  #int32

new_bb=b.astype('int') #Change data type from float to integer by using int as parameter value:
print(new_bb)
print(new_bb.dtype)  #int64

c=np.array([0,1,2])
new_c=c.astype('bool')
print(new_c)   #[False  True  True]
print(new_c.dtype)


