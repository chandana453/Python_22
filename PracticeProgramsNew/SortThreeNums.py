#18.Read 3 numbers and print them in sorted order.

a=int(input("Enter number:"))
b=int(input("Enter number:"))
c=int(input("Enter number:"))

a1=min(a,b,c)
a3=max(a,b,c)
a2=(a+b+c)-a1-a3 #Total-min-max
print("Numbers sorted are: ",a1,a2,a3)