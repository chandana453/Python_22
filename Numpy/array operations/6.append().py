# the function append(),use to to add two arrays into one array
# for this we have to use the function np.append(the arrays)
# but the result will displays in single dimensional array,again we can reshape that array according to the no of elements in that array.


import numpy as np
a=np.array((10,20,30))
b=np.array((40,50,60))
A=np.array((100,200,300))
c=np.append(a,b)
print(c)
d=c.reshape(2,3)
print(d)