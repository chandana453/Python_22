# this function is nothing but adding fo the elements in the array
# we can adda the elements w.r.to the rwo and column wise also
# syntax=np.sum(the array,axis=0,axis=1)



import numpy as np
a=np.array(((10,20),(30,40),(50,60)))
b=np.sum(a)
c=np.sum(a,axis=1)
d=np.sum(a,axis=0)
print(b)
print(c)
print(d)