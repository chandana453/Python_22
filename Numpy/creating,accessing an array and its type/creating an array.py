# Numpy is nothing but the numarcle python
# Numpy provides lot of functions to work in a domine of linear algebra,matrices and fourier transform,mainly it provides the functions related to the Array
# In python Numpy creates an array is called the ndarray(ndimensional array)
# The working of the of an array is faster than list in python
# Tpo get the present version of numpy we have to use numpy.__version__,
# Most of parts in the Numpy was create in the C,C++ and some of the portions only created in the python

# Array:- An array is a fundamental data structure used to store the no of elements at the same time.
# It is the important in the all programming languages.
# In python an array is a container which are used to store more than one element at the same time.

import numpy as np
# print(numpy.__version__)

# creating an array
a=np.array([1,2,3])
print(a)
print(type(a))
print(a.ndim)

# creating a 0 dimensional array
b=np.array(64)
print(b)
print(type(b))
print(b.ndim)

# creating an one dimensional array
c=np.array([1,2])
print(c)
print(type(c))
print(c.ndim)

# creaing a two dimensional array
d=np.array([[1,2],[3,4]])
print(d)
print(type(d))
print(d.ndim)

# creating a three dimensional array
e=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(e)
print(type(e))
print(e.ndim)
