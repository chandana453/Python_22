#4. Python Program to Split Even and Odd Elements into Two Lists
li=[1,2,3,4,5,67,7,8,9]
k=[x for x  in li if x%2==0]
print(k)

l=[y for y in li if y%2!=0]
print(l)

#2nd approach
li1=[]
li2=[]
for i in li:
    if i%2==0:
       li1.append(i)
    else:
        li2.append(i)

print(li1)
print(li2)