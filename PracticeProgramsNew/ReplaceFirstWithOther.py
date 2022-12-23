#19.Read two values using input() and find the first value position in the list and replace that with the second value in the list.

a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))

l=[1,3,5,3,4,6,4,3,7,8,5,9,3]

res=[b if x==a else x for x in l]
print(res)