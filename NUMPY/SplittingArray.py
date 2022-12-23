#array_split()
import numpy as np

a=np.array([1,2,3,4,5,6,7,8])
b=np.array_split(a,4)
print(b)

#splitting array and accessing it

a=np.array([1,2,3,4,5,6])
b=np.array_split(a,3)
print(b[0])
print(b[1])
print(b[2])

#SPLITTING 2D Arrays
print("SPLITTING 2D Arrays")
a=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
b=np.array_split(a,3)  #splits into 3 2D arrays with 2 arrays each
print(b)

aa=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
b=np.array_split(aa,3)
print(b)
newarr = np.array_split(aa, 3, axis=1)  #splitting using axis -they are split along the row (axis=1).
print(newarr)



aa= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr =np.vsplit(aa, 3)
print(newarr)

newarr =np.hsplit(aa, 3)
print(newarr)