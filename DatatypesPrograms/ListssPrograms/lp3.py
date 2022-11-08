#3 Python Program to Print Largest Even and Largest Odd Number in a List
li=[1,2,3,4,5,6,7,8,9]
l=[x for x in li if x%2==0]
print(max(l))

m=[y for y in li if y%2!=0]
print(max(m))