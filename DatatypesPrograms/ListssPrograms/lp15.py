#15.Python Program to Find the Number Occurring Odd Number of Times in a List
def oddOccurence(a):
    res=0
    for i in a:
        res=res ^ i #xor operation
    return res

a=[1,1,5,4,3,4,3,9,5]
print(oddOccurence(a))