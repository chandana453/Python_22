#9.Python Program to Find the Length of a List using Recursion
def lenOfList(list1):
    if not list1:
        return 0
    return 1+lenOfList(list1[1::2])+lenOfList(list1[2::2])

li1=[1,2,3,4,5,6,7,8,9,10,2,3,2,4,1]
k=lenOfList(li1)
print(k)

#source:https://www.tutorialspoint.com/python-program-to-find-the-length-of-a-list-using-recursion

