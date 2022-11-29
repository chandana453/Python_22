# this reshape() we have already discussed,by using range we can initialise values to a variable,and again we can reshape that array
# to reshape that array the no of elements in that array should match with the dimensions we have given in the reshape function.


import numpy as np
a=np.arange(10,100,10)
b=a.reshape(3,3)
print(a)
print(b)

A=np.arange(10,130,10)
B=A.reshape(2,6)
print(B)