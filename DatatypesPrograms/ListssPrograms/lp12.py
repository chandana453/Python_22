#12.Python Program to Swap the First and Last Element in a List
def swapList(list1):
    length=len(list1)
    temp=list1[0]
    list1[0]=list1[length-1]
    list1[length-1]=temp
    return list1

list1=[1,2,3]
print(swapList(list1))

#2nd approach

def swaplists(li1):
    li1[0],li1[-1]=li1[-1],li1[0]
    return li1
li=[7,5,9,8,6,2,3,6]
print(swaplists(li))



#3rd approach using pop()
def swaplist1(list1):
    first=list1.pop(0)
    last=list1.pop() #pop(-1) and pop() are similar
    list1.insert(0,last)
    list1.append(first)
    return list1

list2=[99,12.3,56,7,35,92]
print(swaplist1(list2))