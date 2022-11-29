# this function is nothing but to find the average value fo an array,these two mean and median are same
# we can find the row and column wise mean and median values




import numpy as np

a=np.array(((10,20),(30,40),(50,60)))
b=np.mean(a)
c=np.median(a)
e=np.mean(a,axis=1)
f=np.mean(a,axis=0)
g=np.median(a,axis=1)
h=np.median(a,axis=0)
print(b)
print(c)
print(e)
print(f)
print(g)
print(h)