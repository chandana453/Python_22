# here the function is useful for the delete of the element in a array
# for that we need to pass the parameters into the np.delete(the array,the index position number)


import numpy as np
a=np.array((10,20,30,40,50))
b=np.delete(a,4)
print(b)
print(a)