# By using range function also we can create the array,as we have seen the range before,as it is same we can create the array by using the range function
# Here we have to use the start,stop and step value as it is.Then we can get the values between the range.
# To covert that into the matrices we have to use one function is called the reshape(),in this reshape we have to pass the parameters as the dimensions
# the dimensions should be match with the no of values in the arrya,ex-10(2,5 &5,2)


import numpy as np

a=np.arange(10,20,1)
print(a)
b=a.reshape(2,5)
print(b)