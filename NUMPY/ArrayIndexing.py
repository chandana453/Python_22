import numpy as np
a=np.array([1,2,3,4,5,6,7])
print(a[0])
print(a[5]+a[6]) # adding the elements at 5th and 6th index

#2-D array indexing
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("2nd row 2nd element",arr[1,1]) # o/p:7  #we can use comma separated integers representing the dimension and the index of the element.
print("1st row 4th element",arr[0,3]) #4

#3-D array Indexing
arr=np.array([[[10,9,8,7,6],[5,4,3,2,1]],[[1,2,3,4,5],[6,7,8,9,10]]])
print("3rd element from 2nd array(Index:1) in 2nd row(Index:1)",arr[1,1,2]) #o/p:8
print("4th element from 1st array in 1st row",arr[0,0,3]) #o/p:7


#Negative Indexing
ar=np.array([[1,2,3],[4,5,6]])
print("Accessing using negative indexing:",ar[1,-2]) #o/p:5