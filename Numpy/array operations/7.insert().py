# the function insert() is used to add the elements into the existing array with respect to the index position
# for this we need to give three parameters in the np.insert(the array,the index number,the values that we want to add either single element or
# multiple elements)
# if it multiple elements we have to that elements into the list or tuple format


import numpy as np
a=np.array((10,20,30,40))
b=np.insert(a,2,25)
print(b)
c=np.insert(b,3,(26,27,28,29))
print(c)