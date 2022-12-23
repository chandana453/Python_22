import numpy as np

a=np.arange(1,9)   #creates an array with 1-8
print(a)

a=np.arange(9).reshape(3,3)
print(a)

b=np.arange(9,18).reshape(3,3)
print(b)

c=a+b
print(c)