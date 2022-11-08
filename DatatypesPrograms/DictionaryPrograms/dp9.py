#9.Python Program to Create Dictionary that Contains Number

n=int(input("Enter number:"))
dict={x:x*x for x in range(1,n+1)}
print(dict)


#2nd approach
n=int(input())
dict = {}
for i in range(1,n+1):
    dict[i]=i*i

print(dict)