#10.Python Program to Merge Two Lists and Sort it

list1=[]
list2=[]

m=int(input("Enter the number of elements in list1: "))
for i in range(0,m):
    a=int(input())
    list1.append(a)

n=int(input("Enter the number of elements in list2: "))
for i in range(0,n):
    b=int(input())
    list2.append(b)

new_list=list1+list2
print("Unsorted list: ",new_list)
new_list.sort()
print("Sorted list:",new_list)
