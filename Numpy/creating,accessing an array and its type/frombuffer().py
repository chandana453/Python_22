# Suppose if we take string,the we have to covert it into the array then the following are the syntax to follow
# In the variable before the value we need to mention one word "b"
# frombuffer we have to use(variable name,dtype="S1")
# the datatype we need to give must and should
# Count is the parameter that optional,if we gave count=2,then only two values exicutes.
# offset is also optional that from where the the values need to be print,ex.offset=2 from the 3rd position the values prints


import numpy as np

a=b"chandra"
b=np.frombuffer(a,dtype="S1",count=2,offset=2)
print(b[0:len(b)],type(b),b.ndim)