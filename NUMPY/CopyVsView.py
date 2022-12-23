#COPY Vs View


print("****copy()******")
import numpy as np

arr=np.array([1,2,3,4])
new_arr=arr.copy()
new_arr[1]=5
print(arr)  #original array doesn't change
print(new_arr)

print("******view()*****")
b=np.array([1,2,3])
new_b=b.view()
new_b[0]=10
print(b)    #changes the original arrat as well
print(new_b)


#Check if Array Owns its Data -> using base attribute
a=np.array([1,2,3,4])
new_a=a.copy()
new_aa=a.view()

print(new_a.base)  # returns NONE as it copy() owns the data
print(new_aa.base) #the base  attribute refers to the original object (as it doesn't owns the data)


print("The copy returns None AND The view returns the original array.")
