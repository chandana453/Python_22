# This is the function where we can find the min and max value in an array
# we can find the min and max element w.r.to the row and column also
# if it is the row wise finding then we can get the min or max elements in that array
# if it is the column wise finding then we can get min or max elements in that array




import numpy as np
a=np.array(((10,20),(30,40),(50,60)))
b=np.min(a)
c=np.max(a)
d=np.min(a,axis=1)
D=np.min(a,axis=0)
E=np.max(a,axis=1)
e=np.max(a,axis=0)
print(b)
print(c)
print(d)
print(D)
print(E)
print(e)