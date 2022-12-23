import numpy as np

#iterating 1-D array
a=np.array([1,2,3,4,5])
for i in a:
    print(i)

#Iterating 2-D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
for i in arr:
    print(i)

for i in arr:
    for j in i:
        print(j)

#Iterating 3-D arrays
a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for i in a:
    print(i)

for x in a:
    for y in x:
        for z in y:
            print(z)


#The function nditer() is a helping function that can be used from very basic to very advanced iterations.
b=np.array([[[1,2],[4,5]],[[7,8],[10,11]]])
for i in np.nditer(b):
    print(i)

#Iterating Array With Different Data Types
c=np.array([1,2,3])
for x in np.nditer(c, flags=['buffered'],op_dtypes='S'):
    print(x)

#iterating with diff step size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for i in np.nditer(arr[:,::2]):
    print(i)

a=np.array([1,2,3])

#Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.
for idx, i in np.ndenumerate(a):
    print(idx,i)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, i in np.ndenumerate(arr):
    print(idx,i)