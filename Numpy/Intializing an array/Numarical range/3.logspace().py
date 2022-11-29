# This is also one of the range method to initialise the values to the variables or array.
# we have to use the np.logspace(),in this parameter we have to pass the parameters
# (start,stop) and the remaining are the optional,those are the step in the sense of no of intervals,and the base value



import numpy as np

a=np.logspace(1,10,10,base=2)
print(a)