#7.Python Program to Reverse a String Without using Recursion
string1="python programming"
print(string1[::-1])

#2nd approach

def reverse(string1):
    str = ""
    for i in string1:
        str = i + str
    return str


string1 = "program"
# print("The reversed string is : ", end="")
print(reverse(string1))