'''
python program to print sum of negative numbers,positive even numbers&odd numbers in a list
solution:
'''
x=[3,-1,7,-4,23,-3,2,-8]
sum=0
for i in range(len(x)):
    if x[i]<0:
        sum=sum+x[i]
print(sum)


evenl=0
oddl=0
for i in range(len(x)):
    if x[i]%2==0 and x[i]>0:
        evenl=evenl+x[i]
    else:
        oddl=oddl+x[i]
print(evenl)
print(oddl)

