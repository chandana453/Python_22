# question:1
# Python Program to Check if a String is a Pangram or Not
# solution:
# from string importascii_lowercase as asc_lower
# def checks(s):
#     return set(asc_lower) - set(s.lower()) == set([])
# string=input("Enter tring:")
# if(check(string))==True):
#     print("the string is a pangram")
# else:
#     print("The string isn't a pangram")

# quesion:2
# Python Program to Remove Odd Indexed Characters in a string
# solution:
# def odd_values_string(str):
#     result =""
#     for i in range(len(str)):
#         if i% 2 ==0:
#             result = result + str[i]
#             return result
#         print(odd_values_string('abcdef'))
#         print(odd_values_string('python'))
#

# question:3
# Python Program to Remove the nth Index Character from a Non-Empty String
# solution:
# def remove_char(str, n):
#     first_part = str[:n]
#     last_part = str[n+1:]
#     print(remove_char('Python',0))
#     print(remove_char('Python',3))
#     print(remove_char('python',5))

#  question:4
# Python Program to Replace Every Blank Space with Hyphen in a String
# solution:
# my_string = input("Enter a string :")
# print("The string entered by user is :")
# print(my_string)
# my_string = my_string.replace(' ', '_')
# print("The modified string:")
# print(my_string)

# # quetion:5
# Python Program to Reverse a String using Recursion
# solution:
# def reverse(string):
#     if len(string) == 0:
#         return string
#     else:
#         return reverse(string[1:]) + string[0]
#     a = str(input("Enter the stting to be reveresed: "))
#     print(reverse(a))

# question:6
# Python Program to Reverse a String Without using Recursion
# solution:
# my_string = str(input("Enter a string that needs to be reversed:"))
# print("The string after reversal is: ")
# print(my_string[::-1])


# question:7
# Python Program to Determine How Many Times a Given Letter Occurs in a String
# solution:
# def check(string,ch):
#     if not string:
#         return 0
#     elif string[0]==ch:
#         return 1+check(string[1:],ch)
#     else:
#         return check(string[1:],ch)
#     string=input("Enter string:")
#     ch=input(;"Enter character to check:")
#     print("count is:")
#     print(check(string,ch))

# question:8
# Python Program to Find the Length of a String without Library Function
# solution:
# string=input("Enter string:")
# count=0
# for i in string:
#     count=count+1
#     print("Length of the string is:")
#     print(count)

# question:9
# Python Program to Count the Number of Words and Characters in a String
# solution:
# string=input("Enter string")
# char=0
# word=1
# for i in string:
#     char=char+1
#     if(i==' '):
#         word=word+1
# print("Number of words in the string:")
# print(word)
# print("Number of charscters in the string:")
# print(char)

# question:10
# Python Program to Count Number of Lowercase Characters in a String
# solution:
# string=input("Enter string")
# count1=0
# count=2
# for i in string:
#     if(i.islower()):
#         count1=count1+1
#     elif(i.isupper()):
#         count=count2+1
#         print("The number of lowercase characters is:")
#         print(count1)
#         print("The number of uppercase characters is:")
#         print(count2)

# question:11
# Python Program to Count the Number of Vowels in a String
# solution:
# string=input("Enter string:")
# vowels=0
# for i in string:
#     if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='o' or i = 'u'):
#    print("Number of vowels are:")
#    print(vowels)

# quetion:12
# Python Program to Count Number of Uppercase and Lowercase Letters in a String
# solution:
# def string_test(s)
#     d={"UPPER_CASE":-, "LOWER_CASE":0}
#     for c in s:
#         if c.isupper():
#             d["UPPER_CASE"]+=1
#         elif c.islower():
#             d["LOWER_CASE"]+=1
#         else:
#             pass
#         print("original string : ", s)
#         print("No.of Upper case characters :",d["UPPER_CASE"])
#         print("No.of  Lower case Characters :", d["LOWER_CASE"])


# question:13
# Python Program to Count the Number of Digits and Letters in a String
# solution:
# string=input("Enter string:")
# count1=0
# count2=0
# for i in string:
#     if(i.isdigit())
#         count1=count1+1
#         count2=count2+1
#         print("The number of digits is:")
#         print(count1)
#         print("The number of characters is:")
#         print(count2)







