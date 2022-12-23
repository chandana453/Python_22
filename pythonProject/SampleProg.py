l=[1,2,3,4,3,4,2,3,2,4,9,8]
list1=[[]] #initializing empty 2d array
element=4
count=0
list1=[-1,-1]
length=len(l)-1
for i in range(len(l)):
    if element==l[i] and count==0:
        list1[0]=i
        count+=1
    elif element==l[i] and count!=0:
        list1[1]=i

print(list1)

