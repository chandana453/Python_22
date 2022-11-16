 # b.add(x)
# print("non-duplicate item:")
# print(unique)
"""Python Program to Swap the First and Last Element in a List."""
# a=[]
# n=int(input("2,5,6,28,26:"))
# for x in r# def sum_arr(arr,size):
#      if (size == 0):
#          return 0
#      else:
#          return arr[size-1]+sum_arr(arr,size-1)
#  n=int(input("Enter the number of element for list:"))
#  a=[]
#  for i in range(0,n):
#      element=int(input("enter element:"))
#      a.append(element)
#  print("The list is:")
#  print(a)
#  print("sum of items in list:")
#  b=sum_arr(a,n)
#  print(b)
"""python Program to Find the Length of a List using Recursion."""
#  def length(lst):
#      if not lst:
#          return 0
#      return 1+length('lst'''[1::2])+length('lst'[2::2])
#  a=[1,2,3]
#  print("Length of the string is:")
#  print(a)
"""python Program to Merge Two Lists and Sort it."""
#  a=[]
# c=[]
#  n1=int(input("Enter number of elements:"))
#  for i in range(1,n1=1):
#      b=int(input("Enter element:"))
#      a.append(b)
#  n2=int(input("Enter number of elements:"))
#  for i in range(1,n2+1):
#       d=int (input("Enter element:"))
#       c.append(d)
#  new=a+c
#  new.sort()
#  print("sorted list is:",new)
"""Python Program to Remove Duplicates from a List."""
#  a=[]
#  n=int(input("enter the number of element in list:"))
#  for x in range(0,n):
#      element=int(input("enter element"+str(x+1)+":"))
#     a.append(element)
# b=set()
#  unique=[]
#  for x in 'a':
#     if x not in b:
#          unique.append(x)
#      ange(0,n):
#     element=int(input("2,3,44,56,53,7,"+str(x+1)+":"))
#     a.append(element)
# temp=a[0]
# a[0]=a[n-1]a[n-1]=temp


"""Python Program to Find Largest Number in a List."""
# # # s=(10,20,25,30,3,6)
#  max=0
#  for i in s:
#      if i > max:
#          max=i
#  print(max)
"""Python Program to Find Second Largest Number in a List."""
#  list=(15,20,3,14,16,4,99,100)
#  max=list[0]
#  second_last=list[0]
#  for x in list:
#     if x > max:
#         second_last=max
#         max = x
#     elif x > second_last and x!=max:
#         second_last=x
#  print(second_last)
"""Python Program to Print Largest Even and Largest Odd Number in a List."""
#  li=[78,5,68,14,56,78,35]
#  x=[i for i in li if i%2!=0]
#  print(x)
#  y=[i for i in li if i%2!=0]
#  print(y)
#  largest_even=max(x)
# largest_odd=max(y)
#  print("largest even number:",largest_even)
#  print("largest odd number :",largest_odd)
"""Python Program to Split Even and Odd Elements into Two Lists."""
#  a=[2,4,57,88,39]
#  n=input("7,39,10,2,7,")
#  for i in range(1,n+1):
#      b=int(input("8,11,14,2,20:"))
#      a.append(b)
#  even=[]
#  odd=[]
#  for j in a:
#     if(j%2==0):
#          even.append(j)
#     else:
#          odd.append(j)
#  print("The even list",even)
#  print("The odd list",odd)
"""Python Program to Find Average of a List."""
#  li=[1,2,3,4,5,6]
#  sum_elements=sum(li)
#  n=len(li)
#  avg=sum_elements/n
#  print(avg)
"""Python Program to Print Sum of Negative Numbers, Positive Even & Odd Numbers in a List."""
#  list1=[1,3,2,4,-2,-1,5,6,4,-4]
# x=[x for x in list1 if x<0]
#  y=[x for x in list1 if x%2==0 and x>0]
# z=[x for x in list1 if x%2!=0 and x>0]
#  print("Sum of negative numbers:",sum(x))
#  print("Sum of even numbers:",sum(y))
#  print("Sum of odd numbers:",sum(z))
"""Python Program to Count Occurrences of Element in List."""
#  li=[]
#  n=int(input("5"))
#  for i in range(0,n):
#     e=int(input("8"))j
#     li.append(e)
#  print("Oringal list:",li)
#  n=int(input("Enter element to be checked list:",))
#  print(n,"has occurred",li.count(n),"times")
"""Python Program to Find the Sum of Elements in a List using Recursion."""
# print("new list is:")
# print(a)
"""Python Program to Sort a List According to the Second Element in Sublist."""
# a=[['A',24],['B',27],['C',38]]
# for i in range(0,len(a)):
#     for j in range(0,len(a)-i-1):
#         if(a[j][1]>a[j+1][1]):
#             temp=a[j+1]
#             a[j]=a[j+1]
#             a[j+1]=temp
# print(a)
"""Python Program to Return the Length of the Longest Word from the List of Words."""
# a=[]
# n=int(input("enter the number the length of list:"))
# for x in range(0):
#     element=input("element element"+str(x+1)+":")
#     a.append(element)
# max1=len(a[0])
# tempa[0]
# for i in a:
#     if(len(i)>max1):
#         max1=len(i)
#         temp=i
# print("the world writh the longest length is:")
# print(temp)
"""Python Program to Find the Number Occurring Odd Number of Times in a List."""
# def oddnumber(array):
#     for i in 'arr':
#            'd'['a']+=1
#     for k,v in 'd'.items():
#         if not(v%2==0): return k
#     return"the array doesn't fit the requirement"
"""Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List."""
# a=[]
# n=int(input("Enter number of elements:"))
# for j in range(n):
#     a.append(random.randint(1,20))
# print('Randomised list is:',a)
"""Python Program to Remove the ith Occurrence of the Given Word in a List."""
# def remove_word(my_list,my_word,N):
#     count=0
#     for i in range(0,len(my_list)):#         if(my_list[i]==my_world):
#             count=count+1
#         if(count==N):
#             del(my_list[i])
#             return True
#     return 'false'
# my_list=['harry','jane','will','rod','harry']
# print("the list is:")
# print(my_list)
# my_world='harry'
# N=2
# flag_val=remove_word(my_list,my_world,N)
"""Python Program to Find the Cumulative Sum of a List."""
# def cumulative(lists):
#     cu_list=[]
#     length = len(lists)
#     cu_list=[sum(lists[0:x:1]) for x in range(0,length+1)]
#     return cu_list[1:]
# lists=[20,40,30,10]
# print(cumulative(lists))
"""Python Program to Find the Union of Two Lists."""
# l1 =[]
# num1= int(input('Enter any of list 1:'))
# for n in range(num1):
#     numbers1 = int(input('Enter any number :'))
#     l1.append(numbers1)
# l2=[]
# num2=int(input('Enter size of list 2:'))
# for n in range(num2):
#     numbers2=int(input('Enter any number:'))
#     l2.append(numbers2)
# union=list(set().union(11,12))
# print('The union of two lists is:',union)
"""Python Program to Find the Intersection of Two Lists"""
# list_x=[11,23,11,2,3,4,5]
# list_y=[3,11,5,2,7,23]
# set1=set(list_x)
# set2=set(list_y)
# intersect=set1.intersection(set2)
# result=list(intersect)
# print(result)
"""Python Program to Flatten a List without using Recursion."""
# a=[[1,[[2]],[[[3]]]],[[4],5]]
# flatten=lambda l:sum(map(flatten,l),[])if isinstance(l,list)else[l]
# print(flatten(a))
"""Python Program to Find the Total Sum of a Nested List Using Recursion."""
# def sum1(lst):
#     total=0
#     for element in lst:
#         if(type(element)==type([])):
#             total=total=sum1(element)
#         else:
#             total=total+element
#     return total
# print("sum is:",sum1([[1,2],[3,4]]))
"""Python Program to Flatten a Nested List using Recursion."""
# def flatten(s):
#     if s==[]:
#         return s
#     if isinstance(s[0],list):
#         return flatten(s[0]+flatten(s[1:]))
#     return s[:1]+flatten(s[1:])
# s=[[1,2],[3,4]]
# print("flatted list is:",flatten(s))


"""Python Program to Check if a String is a Pangram or Not."""
# def check(s):
#     return set(asc_lower)-set(s.lower())==set([])
# strng=input("Enter string:")
# if(check(strng)==True):
#     print("The string is a pangram")
# else:
#     print("The string isn't a pangram")
"""Python Program to Remove Odd Indexed Characters in a string."""
# def modify(string):
#     final=""
#     for i in range (len(string)):
#       if i % 2==0:
#           final = final+string[i]
#     return fi)nal
# string=input("Enter string:")
# print("modified string is:")
# print(modify(string)
"""Python Program to Remove the nth Index Character from a Non-Empty String"""
# def remove_char(str,n):
#       first_part=str[:n]
#       last_part=str[n+1:]
#       return first_part+last_part
# print(remove_char('python',0))
# print(remove_char('python',3))
# print(remove_char('python',5))
"""Python Program to Replace All Occurrences of ‘a’ with $ in a String."""
# string=input("Enter string:")
# string=string.replace('a','$')
# print("modified string:")
# print(string)
"""Python Program to Replace Every Blank Space with Hyphen in a String."""
# string=input("Enter string:")
# string=string.replace('','_')
# print("modified string:")
# print(string)
"""Python Program to Reverse a String using Recursion."""
# def reverse(string):
#     if len(string)==0:
#         return string
#     else:
#         return reverse(string[1:])+string[0]
#     a=str(inout("Enter the string to be reversed:"))
"""Python Program to Reverse a String Without using Recursion."""
# a=str(input("Enter a string:"))
# print("Reverse of the string is:")
# print(a[::-1])
"""Python Program to Determine How Many Times a Given Letter Occurs in a String."""
# def check(string,ch):
#     if not string:
#       return 0
#     elif string[0]==ch:
#           return 1+check(string[1:],ch)
#     else:
#              return check(string[1:],ch)
# string=input("Enter string:")
# ch=input("Enter character to check:")
# print("count is:")
# print(check(string,ch))
"""Python Program to Find the Length of a String without Library Function."""
# string=input("Enter string:")
# coutn=0
# for i in string:
#     count=count+1
# print("Length of the string is:")
# print(count)
"""Python Program to Count the Number of Words and Characters in a String."""
# string=input("Enter string:")
# char=0
# word=0
# for i in string:
#     char=char+1
#     if(i==''):
#         word=word+1
# print("Number of words in the string:")
# print(word)
# print("Number of characters in the string:")
# print(char)
"""Python Program to Count Number of Lowercase Characters in a String."""
# sting=input("Enter string:")
# count=0
# for i in 'string':
#     if(i.islower()):
#         count=count+1
# print("The number of lowercase characters is:")
# print(count)
"""Python Program to Count the Number of Vowels in a String."""
# string=input("Enter string:")
# vowels=0
# for i in string:
#     if(i=='a' or i=='e' or i=='i' or i=='0'):
#           vowels=vowels+1
# print("Number of vowels are:")
# print(vowels)
"""Python Program to Count Number of Uppercase and Lowercase Letters in a String."""
# string=input("Enter string:")
# count1=0
# count2=0
# for i in string:
#     if(i.islower()):
#         count1=count1+1
#     elif(i.isupper()):
#         count2=count2+1
# print("The number of lowercase characters is:")
# print(count1)
# print("The number of uppercase characters is:")
# print(count2)
"""Python Program to Count the Number of Digits and Letters in a String."""
# string=input("Enter string:")
# count=0
# count=0
# for i in string:
#       if(i.isdigit()):
#            count1=count1+1
#       count2=count2+1
# print("The number of digits is:")
# print(count1)
# print("The number of characters is:")
# print(count2)


"""Python Program to Check if a Key Exists in a Dictionary or Not."""
# d={'A':2,'B':4,'C':5}
# Key=input("Enter key to check:")
# if 'key' in d.keys():
#     print("key is print and value of the key is:")
#     print(d['Key'])
# else:
#     print("key isn't present!")
"""Python Program to Add a Key-Value Pair to the Dictionary."""
# key=int(input("Enter the key(int) to be added:"))
# value=int(input("Enter the value for the key to be added:"))
# d={}
# d.update({key:'values'})
# print("updated dictionary is:")
# print(d)
"""Python Program to Find the Sum of All the Items in a Dictionary."""
# d={'A':100,'B':540,'C':239}
# print("Total sum of values in the dictionary:")
# print(sum(d.values()))
"""Python Program to Multiply All the Items in a Dictionary"""
# d={'A':10,'B':10,'C':239}
# tot=1
# for i in d:
#     tot=tot*d[i]
# print(tot)
"""Python Program to Remove a Key from a Dictionary."""
# a={'a':1,'b':2,'c':3,'d':4}
# print("Initial dictionary")
# print('d')
# key=input("Enter the key to delete(a-d):")
# if key in 'd':
#     del 'd'[key]
# else:
#     print("key not found!")
#     exit(0)
# print("updated dictionary")
# print('d')
"""Python Program to Concatenate Two Dictionaries."""
# d1={'A':1,'B':2}
# d2={'c':3}
# d1.update(d2)
# print("concatenated dictionary is:")
# print(d1)
"""Python Program to Map Two Lists into a Dictionary."""
# keys=['green','pink','blue']
# values=['#FF0000','#00800','#000FF']
# color_dictionary=dict(zip(keys,values))
# print(color_dictionary)
"""Python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Characte."""
# test_string=input("Enter string:")
# l=test_string.split()
# for word in l:
#     if(word[0]not in 'd'.keys()):
#         'd'[word[0]]=[]
#         'd'[word[0]]=[].append(word)
#     else:
#         if(word not in 'd'[word[0]]):
#             'd'[word[0]].append(word)
# for k,v in 'd'.item():
#          print(k,":",v)

"""Python Program to Create Dictionary that Contains Number."""
# n=int(input("Enter a number:"))
# d={x:x*x for x in range(1,n+1)}
# print(d)

Function:

"""Python Program to Read the Contents of the File."""
# a=str(input("Enter the number of the file with.txt extension:"))
# file2=open(a,'r')
# line=file2.readline()
# while(line!=""):
#     print(line)
#     line=file2.readline()
# file2.close()
"""Python Program to Copy One File to Another File."""
# with open("test.txt") as f:
#     with open("out.txt","w")as f1:
#         for line in f:
#             f1.write(line)
"""Python Program to Count the Number of Lines in Text File."""
# fname=input("Enter file name:")
# num_lines=0
# with open(fname,'r') as f:
#     for line in f:
#         num_lines+=1
# print("Number of lines:")
# print(num_lines)
"""Python Program to Count the Number of Lines in Text File."""
# fname=input("Enter file name:")
# num_lines=0
# with open(fname,'r')as f:
#     for line in f:
#         num_lines+=1
# print("Number of lines:")
# print(num_lines)
"""Python Program to Count the Number of Blank Spaces in a Tex File."""
# fname=input("Enter file name:")
# k=0
# with open (fname,'r')as f:
#     for line in f:
#         words = line.split()
#         for i in words:
#             for letter in i:
#                 if(letter.isspace):
#                     k=k+1
# print("occurrences of blank spaces:")
# print(k)
"""Python Program to Count the Occurrences of a Word in a Text File."""
# fname=input("Enter file name:")
# word=input("Enter word to be searched:")
# k=0
# with open(fname,'r')as f:
#     for line in f:
#         word=line.split()
#         for i in 'words':
#             if(i==word):
#                 k=k+1
# print("occurrences of the word:")
# print(k)
"""Python Program to Count the Number of Words in a Text File."""
# fname=input("Enter file name:")
# num_words=0
# with open(fname,'r')as f:
#     for line in f:
#         word=line.split()
#         num_words+=len(word)
# print("Numbe of words:")
# print(num_words)
"""Python Program to Capitalize First Letter of Each Word in a File."""
# fname=input("Enter file name:")
# with open(fname,'r') as f:
#     for line in f:
#         l=line.title()
#         print(1)
"""Python Program to Counts the Number of Times a Letter Appears in the Text File."""
# fname ='inpit'("Enter file name:")
# l=input("Enter letter to be searched:")
# k=0
# with open(fname,'r') as f:
#     for line in f:
#         words=line.split()
#         for i in words:
#             for letter in i:
#                 if(letter==1):
#                     k=k+1
# print("occurrences of the letter:")
# print(k)
"""Python Program to Extract Numbers from Text File."""
# fname =input("Enter file name:")
# with open(fname,'r') as f:
#     for line in f:
#         words= line.split()
#         for i in words:
#             for letter in i:
#                 if(letter.isdigit()):
#                     print(letter)
"""Python Program to Print the Contents of File in Reverse Order."""
# filename=input("Enter file name:")
# for line in reversed(list(open(filename))):
#     print(line.rstrip())
"""Python Program to Append the Content of One File to the End of Another File"""
# name1=input("Enter file to be read from:")
# name2=input("Enter file to be append to:")
# fin=open(name1,'r')
# data2=fin.read()
# fin.close()
# fout=open(name2,"a")
# fout.write(data2)
# fout.close()
"""Python Program to Read a String from the User and Append it into a File."""
# fname=input("Enter file name:")
# file3=open(fname,"a")
# c=input("Enter string to append:\n")
# file3.write("\n")
# file3.write(c)
# file3.close()
# print("contents of append file:")
# file4=open(fname,'r')
# line1=file4.readline()
# while(line1!=""):
#      print(line1)
#      line1=file4.readline()
# file4 .close()