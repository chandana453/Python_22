# with this function we can find the standard values of an array
# we can find the standard values w.r.to the row and column wise also



import numpy as np
a=np.array(((10,20),(30,40),(50,60)))
b=np.std(a)
c=np.std(a,axis=1)
d=np.std(a,axis=0)
print(b)
print(c)
print(d)