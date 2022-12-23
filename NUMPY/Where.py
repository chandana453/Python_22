#where()
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
b=np.where(arr==4)  #Which means that the value 4 is present at index 3, 5, and 6.
print(b)

a=np.array([1,2,3,4,5,6,7,8,9,10])
b=np.where(a%2==0)  #returns indexes of the values which are even
print(b)
b=np.where(a%2!=0)  #returns indexes of the values which are odd
print(b)


#Search Sorted
# There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

a=np.array([1,3,5,7])
b=np.searchsorted(a,2,side='right')
print(b)

x = np.searchsorted(a, 7, side='right')
print(x)

a=np.array([1,3,5,7])
b=np.searchsorted(a,2)
print(b)

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)