# This copy() is the operation where we want to copy the values in one array into the another array.
# the array that we have mentioned in the copy()parenthesis,the values in that array copy to the another array


import numpy as np
a=np.array(((1,2,3),(4,5,6)))
print(a)
b=np.copy(a)
print(b)