# the concatenation function is also same as the append but we can add two arrays with respect to the row and column
# the syntax is np.concatenate((the variables),default the axis=0),this is column wise concatenation
# for the row wise concatenation the synatx np.concatenation((the arrays),axis=1)



import numpy as np
a=np.array([[10,20],[30,40]])
b=np.array([[50,60],[70,80]])

# row wise concatenation
c=np.concatenate((a,b))
print(c)

# column wise concatenation
d=np.concatenate((a,b),axis=1)
print(d)