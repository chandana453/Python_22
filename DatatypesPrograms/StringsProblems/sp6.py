#6.Python Program to Reverse a String using Recursion
def reverseString(str):
    if len(str) == 0:
        return str
    else:
        return reverseString(str[1:]) + str[0]

string1="python"
print(reverseString(string1))