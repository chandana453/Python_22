#2.Python Program to Remove Odd Indexed Characters in a string

def removeOddIndexChar(string1):
    resultant_string=""
    for i in range(len(string1)):
        if i%2==0:
            resultant_string+=string1[i]
    return resultant_string

a="programming"
print(removeOddIndexChar(a))