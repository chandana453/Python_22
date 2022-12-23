# shape attribute
import numpy as np

a=np.array([[1,2,3],[4,5,6]])

#The shape of an array is the number of elements in each dimension.
print(a.shape)  #which means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 3.

# shape returns a tuple with each index having the number of corresponding elements.


#Create an array with 5 dimensions using ndmin
b=np.array([1,2,3],ndmin=5)
print(b)
print(b.shape) #Integers at every index tells about the number of elements the corresponding dimension has.
#O/P:(1, 1, 1, 1, 3)

#Array RESHAPING
#Reshaping means changing the shape of an array.
a=np.array([1,2,3,4,5,6,7,8,9,10])
b=a.reshape(5,2)   #this will reshape into 5 arrays each with 2 elements(1-D to 2-D)
print(b)

b=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_b=b.reshape(2,3,2)   # 2 2-D arrays ,each with 3 arrays with 2 elements each(1-D to 3-D)
print(new_b)

#to check if the reshaped array is copy or view - using base attribute
arr=np.array([1,2,3,4,5,6,7,8])
arr_new=arr.reshape(2,4)
print(arr_new)
print(arr_new.base)   # returns an original array , so it's a view


#pass -1 as the value(you do not have to specify an exact number for one of the dimensions in the reshape method.)

a=np.array([1,2,3,4,5,6,7,8])
a_new=a.reshape(2,2,-1)
print(a_new)


#Flattening arrays: Flattening array means converting a multidimensional array into a 1D array.

#We can use reshape(-1) to do this.

arr = np.array([[1, 2, 3], [4, 5, 6]])
arr_new1=arr.reshape(-1)
print(arr_new1)




