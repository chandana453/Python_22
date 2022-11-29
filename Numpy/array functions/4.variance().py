# here with this function we can find the variance of an array
# we can find the variance values w.r.to the row and column wise also



import numpy as np
a=np.array(((10,20),(30,40),(50,60)))
b=np.var(a)
c=np.var(a,axis=1)
d=np.var(a,axis=0)
print(b)
print(c)
print(d)