# Getting some elements out of an existing array and creating a new array out of them is called filtering.

# In NumPy, you filter an array using a boolean index list.

# If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.

import numpy as np

arr = np.array([1, 2, 3, 4])
b=[True,True,False,True]  #false at index 3 will remove the element at index 3 from arr array
new_Arr=arr[b]
print(new_Arr)

#creating the filter array

a=np.array([10,8,91,20,32,12,45,23,21,94])

filter_array=[]

for element in a:
    if element>30:
        filter_array.append(True)
    else:
        filter_array.append(False)

new_Arr=a[filter_array]
print(a)
print(new_Arr)

#creatng filter directly from array
import numpy as np

arr = np.array([9,10,12,8,4,7,19])
filter_arr=arr<10
new_arr=arr[filter_arr]
print(new_arr)


a=np.array([1,2,3,4,5,6,7,8,9,10])
fil_a = a%2==0
new_a=a[fil_a]
print(new_a)