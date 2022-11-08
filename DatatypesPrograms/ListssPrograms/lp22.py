#22.Python Program to Find the Total Sum of a Nested List Using Recursion
def sumOfNestedList(list1):
    total=0
    for i in range(len(list1)):
        if type(list1[i])==list:
            total +=sumOfNestedList(list1[i])
        else:
            total+=list1[i]

    return total

list1=[[4,5],[7,8,[20]],100]
print(sumOfNestedList(list1))


#source;https://www.geeksforgeeks.org/python-program-to-find-the-total-sum-of-a-nested-list-using-recursion/