#6.Python Program to Print Sum of Negative Numbers, Positive Even & Odd Numbers in a List
li=[1,2,3,7,-5,9,8,5,-3,-2,10]
x=[x for x in li if x%2==0]
y=[y for y in li if y%2!=0]
z=[x for x in li if x<0]
print("Sum of negative numbers: ",sum(z))
print("Sum of Positive even numbers: ",sum(x))
print("Sum of positive odd numbers: ",sum(y))

