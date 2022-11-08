#Lists:

#Python Program to Find Largest Number in a List
#solution:
#L=[1,2,4,8,15]
#print("Largest number is:",max(L))


#Python Program to Find Second Largest Number in a List
#solutiom:
# l=[2,4,5,7,9,1,3]
# l.sort()
# print(l)
# print(l[-1])
# print(l[-2])

#Method 2




# l=[1,2,4,6,9]
# max=l[0]
# second_last=l[0]
# for x in l:
#     if x>max:
#         max=x
#     if x>second_last and x!=max:
#         second_last=x
# print(second_last)
#




#Python Program to Split Even and Odd Elements into Two Lists
# l=[1,3,5,7,8,10]
# evenelement=[]
# oddelement=[]
# for i in range(len(l)):
#     if l[i]%2==0:
#         evenelement.append(l[i])
#     else:
#         oddelement.append(l[i])
# print(evenelement)




#Python Program to Find Average of a List
#solution:
# l=[1,3,5,3,7,8,9]
# print(sum(l)/len(l))



#Python Program to Print Sum of Negative Numbers, Positive Even & Odd Numbers in a List
#solutiom:
# l=[2,-4,-6,-7,9,10]
# sum=0
# for i in range(len(l)):
#     if l[i]<0:
#         sum=sum+l[i]
# print(sum)
#
# evenl=0
# oddl=0
# for i in range(len[l]):
#     if l[i]%2==0 and l[i]<0:
#         even1=even1+l[i]
#     else:
#         odd1=odd1+l[i]
# print(evenl)
# print(oddl)


#Python Program to Count Occurrences of Element in List
#solutiom:
# l=[1,4,5,6,4,7,9,4]
# x=4
# print(l.count(x))



#Python Program to Merge Two Lists and Sort it
#solution:de
# def append_lists():
#     list1=[1,2,4,8]
#     list2=[9,12,13,15]
#     for i in list2:
#         list1.append[i]
#     print(list1)
# append_lists()
def merge():
    list1=[1,2,3,4]
    List2=[6,8,9,10]
    List=list1+list2
print(list)