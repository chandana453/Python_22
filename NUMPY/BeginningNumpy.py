import numpy as np
arr= np.array([1,2,3,4,5])  #create a ndarray using array() function
print(arr)
print(type(arr))
#The version string is stored under __version__ attribute.

print(np.__version__)


print("........MULTIDIMENSIONAL ARRAYS............")

#O_D array-> each element in an array is O-D array

ar=np.array(42)
print(ar)
print(type(ar))

#1-D array
import numpy
arr=numpy.array([1,2,3])
print(arr)

#2-D array
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(arr)

#3-D Arrays
arr=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr)

#Check Number of Dimensions - using "ndim"

import numpy as np

a=np.array(7)
b=np.array([1,2,3,4,5])
c=np.array([[1,2],[3,4]])
d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print("Getting dimensions of array using \"ndim\" attribute")
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


#Higher Dimensional Arrays
arr=np.array([1,2,3,4], ndmin=5)
print(arr)
print("Number of dimensions:", arr.ndim)

