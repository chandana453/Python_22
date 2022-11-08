l=[1,2,3,4,5,5,5,6]
a=0
l_add=[]
for i in range(len(l)):
    if l[i]==5:
        a = a+1
        l_add.append(i)
print(a)
print(l_add)