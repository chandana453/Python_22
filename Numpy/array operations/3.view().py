# the view function also same as the copy function,but the small diff is there
# in the below i have taken one "a" array,copied the values in a into the "b",the values in "a" copied to the array "b",
# and again i have taken another array "c",i have used view function with array "b",then the values in b view to the "c"
# but the differance,when i want to change the value in "b",then the value in the "c " also changed,but when i changed value in "a",the value in the
# "b" not changed





import numpy as np
a=np.array(((10,20),(30,40)))
print(a)
b=np.copy(a)
print(b)
c=b.view()
print(c)
b[0][0]=100
print(b)
print(c)
a[1][0]=1000
print(a)
print(b)
print(c)
