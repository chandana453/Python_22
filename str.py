# li=[89,3,432,14,56,78,24,35]
# x=[i for i in li if i%2==0]
# print(x)
# y=[i for i in li if i%2!=0]
# print(y)
# largest_even=max(x)
# largest_odd=max(y)
# print("Largest even number:",largest_even)
# print("largest odd number:",largest_odd)
#
# Python Program to Find Average of a List
#  li=[1,2,3,4,5]
# sum_elements=sum(li)
# n=len(li)
# avg=sum_elements/n
# print(avg)


# # python Program to Find Largest Number in a List
# a=(1,2,3,4,5,9,12,14,16)
# max=0
# for i in a:
#     if i > max:
#         max=i
# print(max)

# # python Program to Find second Largest Number in a List
# list=(24,34,45,67,89,95)
# max=list[0]
# second_last=list[0]
# for x in list:
#     if x > max:
#         max = x
#     if x > second_last and x!=max:
#         second_last=x
# print(second_last)

#
# # Python Program to Split Even and Odd Elements into Two Lists
# li=[44,55,78,97,56]
# n=int(input("23,34,45,667,88,12,45:"))
# for i in range(1,n+1):
#     b=int(input("enter element:"))
# even=[]
# odd=[]
# for j in a:
#     if(j%2==0):
#         even.append(j)
#     else:
#         odd.append(j)
# print("the even list".even)
# print("the odd list".odd)

# # Python Program to Print Sum of Negative Numbers,positive even& 0dd numbers in a list
# list1=[3,5,7,-6,8,23,-5,-9,12]
# x=[x for x in list1 if x<0]
# y=[x for x in list1 if x%2==0 and x>0]
# z=[x for x in list1 if x%2!=0 and x>0]
# print("sum of negative numbers:",sum(x))
# print("sum of even numbers:",sum(y))
# print("{sum of odd numbers:",sum(z))

# # python Program to Count Occurrences of Element in List
# a=[]
# n=int(input("3,5,6,7,8,9,12,34"))
# for i in range(1,n+1):
#     b=int(input("3,5,6,7,8,9,12,34"))
#     a.append(b)
# k=0
# num=int(input("enter the number to be counted"))
# for j in a:
#     if(j==num):
#         k=k+1
# print("number of times",num,"appears is",k)

# # python Program to Find the Sum of Elements in a List using Recursion
# a = []
# n = int(input("1,2,3,4,5,6,7,8,9,10"))
# for i in range(0,n):
#     element = int(input("1,2,3,4,5,6,7,8,9,10"))
#     a.append(element)
# print("element")

# # Python Program to Find the Length of a List using Recursion
# def length(lst):
#     if not lst:
#         return 0
#     return 1 + length(lst[1::2])+length(lst[2::2])
# a=[1,2,3]
# print("length of the string is:")
# print(a)

# # python Program to Merge Two Lists and Sort it
# a=[]
# c=[]
# n1=int(input("enter number of elements:"))
# for i in range(1,n+1):
#     b=int(input("enter number of element:"))
#     a.append(b)
# n2=int(input("enter number of elements"))
# for i in range(1,n2+1):
#     d=int(input("enter element:"))
#     c.append(d)
# new=a+c
# new.sort()
# print("sorted list is:",new)

# # python Program to Remove Duplicates from a List
# a=[]
# n=int(input("enter the number of elements in list:"))
# for x in range(0,n):
#     elememt=int(input("enter element"+str(x+1)+":"))
#     a.append(element)
# b=set()
# unique=[]
# for x in a:
#     if x not in b:
#         unique.append(x)
#         b.add(x)
# print("non-duplicate items:")
# print(unique)

# # python Program to Swap the First and Last Element in a List
# a=[]
# n=int(input("2,3,4,56,78,97,54:"))
# for x in range(0,n):
#     element=int(input("2,3,4,56,78,97,54"+str(x+1)+":"))
#     a.append(element)
# temp=a[0]
# a[0]=a[n-1]
# a[n-1]=temp
# print("new list is:")
# print(a)

# # python Program to Sort a List According to the Second Element in Sublist
# a=[['A',34],['B',21],['C',26]]
# for i in range(0,len(a)):
#     for j in range(0,len(a)-i-1):
#         if(a[j][1]>a[j+1][1]):
#             temp=a[j]
#             a[j]=a[j+1]
#             a[j+1]=temp
# print(a)

# # Python Program to Return the Length of the Longest Word from the List of Words
# a=[]
# n=int(input("enter the number of elements in list:"))
# for x in range(0,n):
#     element=input("enter element"+str(x+1)+":")
#     a.append(element)
# max1=len(a[0])
# tempa[0]
# for i in a:
#     if(len(i)>max1):
#         max1=len(i)
#         temp=i
# print("the world with the longest length is:")
# print(temp)

# # Python Program to Find the Number Occurring Odd Number of Times in a List
# def oddnumber(array):
#     for i in arr:
#            d[a]+=1
#     for k,v in d.items():
#         if not(v%2==0):return k
#     return"the array doesn't fit the requirement"

# # Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List
# a=[]
# n=int(input("enter number of element:"))
# for j in range(n):
#     a.append(random.randit(1,20))
# print('randomised list is:',a)

# # Python Program to Remove the ith Occurrence of the Given Word in a List
# def remove_word(my_list,my_word,N):
#     count=0
#     for i in range(0,len(my_list)):
#         if(my_list[i]==my_word):
#             count=count+1
#         if(count==N) :
#             del(my_list[i])
#             return True
#     return false
# my_list=['harry','jane','will','rod','harry']
# print("the list is:")
# print(my_list)
# my_word='harry'
# N=2
# flag_val=remove_word(my_list,my_word,N)

# # python Program to Find the Cumulative Sum of a List
# a=[]
# n=int(input("enter the number of elements in list:"))
# for x in range(0,n):
#     element=int(input("enter element"+str(x+1)+"+"))
#     a.append(element)
# b=[sum(a[0:x+1])for x in range(0,len(a))]
# print("the original list is:",a)
# print("the new list is:",b)

# # Python Program to Find the Union of Two Lists
# li=[]
# num1=int(input('enter size of list 1:'))
# for i in range(num1):
#     numbers1=int(input('enter any number:'))
#     a.append(numbers1)
# li=[]
# num2=int(input('enter size of list 2:'))
# for i in range(num2):
#     numbers2=int(input('enter any number:'))
#     li.append(numbers2)
# union=list(set().union(11,12))
# print('the union of two lists is:',union)

# # Python Program to Find the Intersection of Two Lists
# def intersection_list(list1,list2):
#        return set(list1).intersection(list2)
# list1=[20,30,40,50,60,70]
# list2=[50,12,35,65,20,30]
# print(intersection_list(list1,list2))

# # Python Program to Flatten a List without using Recursion
# a=[[1,[[2]],[[[3]]]],[[4],5]]
# flatten=lambda l:sum(map(flatten,l),[]) if isinstance(l,list) else [l]
# print(flatten(a))
# # python Program to Find the Total Sum of a Nested List
# def column_sum(lst):
#     return[sum(i) for i in zip(*lst)]
# lst=[[2,4,6],[1,3,5],[8,9,7]]
# print(column_sum(lst))

# # Python Program to Find the Total Sum of a Nested List Uing recursion
# def sum1(lst):
#     total=0
#     for element in lst:
#         if (type(element)==type([])):
#             total=total=sum1(element)
#         else:
#             total=total+element
#     return total
# print("sum is:",sum1([[1,2],[3,4]]))

# # python Program to Flatten a Nested List using Recursion
# def flatten(s):
#     if s==[]:
#         return s
#     if isinstance(s[0],list):
#          return flatten(s[0]+flatten(s[1:]))
#     return s[:1]+flatten(s[1:])
# s=[[1,2],[3,4]]
# print("flatted list is:",flatten(s))

# string
# # Python Program to Check if a String is a Pangram or Not
# def check(s):
#     return set(asc_lower) - set(s.lower())==set([])
# strng=input("jimin:")
# if(check(strng)==true):
#     print("tne string is a pangram")
# else:
#     print("the string isn't a pangram")

# # python Program to Remove Odd Indexed Characters in a string
# def modify(string):
#     final - ""
#     for i in range(len(string)):
#         if i%2==0:
#             final=final+string[i]
#     return final
# string=input("enter string:")
# print("modified string is:")
# print(modify(string))


# # python Program to Remove the nth Index Character from a Non-Empty String
# def remove(string,n):
#     first=string[:n]
#     last=string[n+1:]
#     return first+last
# string=input("jin")
# n=int(input("enter the index of the character to remove:"))
# print("modified string:")
# print(remove(string,n))

# # Python Program to Replace All Occurrences of ‘a’ with $ in a String
# my_str="taehyung is most handsome"
# changed_str=''
# for char in range(0,len(my_str)):
#     if(my_str[char]=='a'):
#        changed_str+='$'
#     else:
#         changed_str+=my_str[char]
# print("the original string is :")
# print(my_str)
# print("the modified string is:")
# print(changed_str)

# # python Program to Replace Every Blank Space with Hyphen in a String
# str="best leader is kim namjoon"
# for i in range(0,len(str),1):
#     if(str[i]==' '):
#         str=str.replace(str[i],'-')
# print(str)

# #python program to Reverse a String using Recursion
# def reverse(string):
#     if len(string)==0:
#         return string
#     else:
#         return reverse(string[1:])+string[0]
# a=str(input("jin is wwh:"))
# print(reverse(a))

# # Python Program to Reverse a String Without using Recursion
# a=str(input("cat suga"))
# print("cat suga:")
# print(a[::-1])

# # python Program to Determine How Many Times a Given Letter Occurs in a String
# def check(string,ch):
#     if not string:
#         return 0
#     elif string[0]==ch:
#         return 1+check(string[1:],ch)
#     else:
#         return check(string[1:],ch)
# string=input("jung jungkook is the best:")
# ch=input("j:")
# print("check"+string(ch)+"is:")
# print(check(string,ch))

# # Python Program to Find the Length of a String without Library Function
# string=input("jhope is the best dancer:")
# count=0
# for i in string:
#     count=count+1
# print("the length of the string is:")
# print(count)

# # Python Program to Count the Number of Words and Characters in a String
# string=input("enter string:")
# char=0
# word=1
# for i in string:
#     char=char+1
#     if(i==' '):
#         word=word+1
# print("number of words in the string:")
# print(word)
# print("number of characters in the string:")
# print(char)

# # Python Program to Count Number of Lowercase Characters in a String
# my_string="hi there is busan concert"
# print("the string is")
# print(my_string)
# my_counter=0
# for i in my_string:
#     if(i.islower()):
#         my_counter=my_counter+1
# print("the number of lowercase characters in the string are: ")
# print(my_counter)

# # Python Program to Count the Number of Vowels in a String
# str1=input("how are you:")
# vowels=0
# str1.lower()
# for i in str1:
#     if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
#         vowels=vowels+1
# print("total number of vowels in the string =",vowels)


# # Python Program to Count Number of Uppercase and Lowercase Letters in a String
# str="hello world"
# lower=0
# upper=0
# for i in str:
#     if(i.islower()):
#         lower+=1
#     else:
#         upper+=1
# print("the number of lowercase character is:",lower)
# print("the number of uppercase characters is:",upper)


# # Python Program to Count the Number of Digits and Letters in a String
# str="army fandom"
# digit=letter=0
# for ch in str:
#     if ch.isdigit():
#         digit=digit+1
#     elif ch.isalpha():
#         letter=letter+1
#     else:
#         pass
# print("letters:",letter)
# print("digits:",digit)

# # python Program to Check if a Key Exists in a Dictionary or Not
# my_dict={1: 'a',2: 'b',3: 'c'}
# if 2 in my_dict:
#     print("present")

# # Python Program to Add a Key-Value Pair to the Dictionary
# key=int(input("enter the key (12)to be added:"))
# value=int(input("enter the value for the key to be added:"))
# d={}
# d.update({key:value})
# peint("updated dictionary is:")
# print(d)

# # Python Program to Find the Sum of All the Items in a Dictionary
# def returnsum(mydict):
#       list=[]
#       for i in mydict:
#          list.append(mydict[i])
#       final=sum(list)
#       return final
# dict={'a':100,'b':200,'c':300}
# print("sum:",returnsum(dict))

# # Python Program to Remove a Key from a Dictionary
# d={"jin":30,"suga":29,"jhope":28,'rm':28,'jimin':27,'v':27,'jk':25}
# print("initial dictionary")
# print(d)
# key=input("enter the key to delete(a-d):")
# if key in d:
#     del d[key]
# else:
#     print("key not found!")
#     exit(0)
# print("updated dictionary")
# print(d)

# # python Program to Concatenate Two Dictionaries
# d1={'s':1,'v':2}
# d2={'u':3}
# d1.update(d2)
# print("concatenated dictionary is:")
# print(d1)

# # python Program to Map Two Lists into a Dictionary
# fruits=['mango','pear','apple','papaya']
# price=[90,70,120,60]
# fruits_price=zip(fruits,price)
# fruits_dict={}
# for key,value in fruits_price:
#     if key in fruits_dict:
#         pass
#     else:
#         fruits_dict[key]=value
# print(fruits_dict)

# # python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character
# test_string=input("entr string:")
# l=test_string.split()
# d={}
# for word in l:
#     if(word[0] not in d.keys()):
#         d[word[0]]=[]
#         d[word[0]].append(word)
#     else:
#         if(word not in d[word[0]]):
#             d[word[0]].append(word)
# for k,v in d.items():
#     print(k,':',v)

# # Python Program to Create Dictionary that Contains Number
# n=int(input('10,1,2,3,4,5,6,7,8:'))
# d={x:x*x for x in range(1,n+1)}
# print(d)

# # # python Program to Count the Frequency of Each Word in a String using Dictionary
# test_string=input("hello world program word test:")
# l=[]
# l=test_string.split()
# wordfreq=[l.count(p) for p in l]
# print(dict(zip(l,wordfreq)))