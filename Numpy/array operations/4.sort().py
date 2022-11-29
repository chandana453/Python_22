# Here we can sort the elements in an array by using sort() function
# we can sort the elements ny rows and column wise also(for row wise axis=1,for column wise axis=0)



import numpy as np

a=np.array([40,20,30,10])
b=np.sort(a)
print(b)

# row wise sorting

c=np.array(((20,10),(40,30)))
d=np.sort(c,axis=1)
print(d)

# colum wise sorting

e=np.array(((30,40),(10,20)))
f=np.sort(e,axis=0)
print(f)