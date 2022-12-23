#in NumPy we join arrays by axes.
import numpy as np

a=np.array([1,2,3])
b=np.array([4,5,6])

c=np.concatenate((a,b))
print(c)

#2D arrays
d=np.array([[1,2],[3,4]])
e=np.array([[5,6],[7,8]])

f=np.concatenate((d,e), axis=1)

print(f)


#Arrays Joining using stacks
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.stack((a,b),axis=1)  #We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
print(c)

#STACKING ALONG ROWS
#hstack() to stack along rows.
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.hstack((a,b))
print(c)

#STACKING ALONG COLUMNS
#vstack()  to stack along columns.
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.vstack((a,b))
print(c)

#Stacking Along Height (depth)
#NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.dstack((a,b))
print(c)

