#Python Program to Remove Odd Indexed Characters in a string

# def removeOddIndexChar(string1):
#     resultant_string=""
#     for i in range(len(string1)):
#         if i%2==0:
#             resultant_string+=string1[i]
#     return resultant_string
#
# a="programming"
# print(removeOddIndexChar(a))



#Python Program to Remove the nth Index Character from a Non-Empty String
# str="Programming language"
# index_to_remove=10
#
# def removeIndex(str):
#     modified_string=""
#     for i in range(len(str)):
#         if i!=index_to_remove:
#             modified_string+=str[i]
#     return modified_string
# print(removeIndex(str))


#Python Program to Replace All Occurrences of ‘a’ with $ in a String

# string1="Replace all in program"
# string1=string1.replace('a','$')
# print(string1)




#Python Program to Replace Every Blank Space with Hyphen in a String
# str="Python Program to Replace"
# str=str.replace(" ","-")
# print(str)


#Python Program to Reverse a String using Recursion
# def reverseString(str):
#     if len(str) == 0:
#         return str
#     else:
#         return reverseString(str[1:]) + str[0]
#
# string1="python"
# print(reverseString(string1))



#Python Program to Determine How Many Times a Given Letter Occurs in a String
# string1="procedural programming"
#
# def occuranceString(str,letter):
#     count = 0
#     for i in str:
#       if i==letter:
#          count=count+1
#     return count
#
# letter="r"
# print(occuranceString(string1,letter))



#python Program to Find the Length of a String without Library Function
# str="program"
# count=0
# for i in str:
#     count=count+1
# print(count)