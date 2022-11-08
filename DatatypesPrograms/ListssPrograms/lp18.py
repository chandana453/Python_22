#18.Python Program to Find the Cumulative Sum of a List
def cumulativeSum(a):
    list_new=[]
    j=0
    for i in range(len(a)):
        j+=a[i]
        list_new.append(j)
    print(list_new)

list1=[2,3,4,5,6,10]
cumulativeSum(list1)

