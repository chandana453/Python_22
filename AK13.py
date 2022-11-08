'''
Define a function that can accept two strings as input and print the
string with maximum length in console. If two strings have the same
length, then the function should print al l strings line by line.
'''

def printvalue(a1,a2):
    len1=len(a1)
    len2=len(a2)
    if len1>len2:
        print(a1)
    elif len2>len1:
        print(a2)
    else:
        print(a1)
        print(a2)
printvalue("99","85")