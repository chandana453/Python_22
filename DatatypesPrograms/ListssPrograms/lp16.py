#16.Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List

import random
list1=[]
n=int(input("Enter no of elements in list: "))
for i in range(n):
  list1.append(random.randint(1,20))
print(list1)