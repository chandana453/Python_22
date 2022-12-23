import numpy as np

ar=np.array([1,2,3,4,5,6,7,8,9,10])
print(ar[2:7])

print(ar[4:]) #specified index to end
print(ar[:4]) #beginning to specified index

print(ar[-4:-1])

print(ar[0:8:2]) #iterate until 8 with step 2 o/p:1,3,5,7

print(ar[1:9:3])

print(ar[::4])   #Return every other element from the entire array

#SLICING 2-D ARRAYS
print("*********2D ARRAYS********")
#From the second ROW, slice elements from index 2 to index 4 (not included)
ar=np.array([[1,2,3,4,5,6],[5,6,7,9,1,5]])
print(ar[1,2:5])  #1st row-> elements from index 2 to index 5(excluded)
#O/P: 7,9,1

#From both elements(EAch row is considered as an element), return index 2:
print(ar[0:2,2])

#From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
print(ar[0:2,1:4])