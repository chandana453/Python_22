
# # Python Program to Read the Contents of the File
# a=str(input("enter the name of the file with,txt extension:"))
# file2=open(a,'r')
# line=file2.readline()
# while(line:=""):
#     print(line)
#     line=file2.readline()
# file2.close()

# Python Program to Copy One File to Another File
#
# f1=open("sample file1.txt","r")
# f2=open("sample file2.txt","w")
# for line in f1:
#     f2.write(line.upper())





# # Python Program to Count the Number of Lines in Text File
# fname=input("enter file name:")
# num_lines=0
# with open(fname,'r') as f:
#     for line in f:
#         num_lines+=1
# print("number of lines:")
# print(num_lines)

# # Python Program to Count the Number of Blank Spaces in a Text File
# fname=input(" enter file name:")
# k=0
#
# with open(fname,'r') as f:
#      for line in f:
#          words=line.split()
#          for i in words:
#              for letter in i:
#                  if(letter,isspace):
#                     k=k+1
# print("0ccurances of blank spaces:")
# print(k)

# # Python Program to Count the Occurrences of a Word in a Text File
# fname=input("enter file name:")
# word=input("enter word to be searched:")
# k=0
#
# with open(fname,'r') as f:
#     for line in f:
#         words=line.split()
#         for i in words:
#             if(i==word):
#                 k=k+1
# print("occurances of the word:")
# priint(k)

# # Python Program to Count the Number of Words in a Text File
# fname=input("enter file name:")
# num_words=0
#
# with open(fname,'r') as f:
#     for line in f:
#         words=line.split()
#         num_words+=len(words)
# print("number of words:")
# print(num_words)

# # Python Program to Capitalize First Letter of Each Word in a File
# fname=input("enter file name:")
#
# with open(fname,'r') as f:
#     for line in f:
#         l=line,title()
#         print(l)

# # Python Program to Counts the Number of Times a Letter Appears in the Text File
# fname=input("enter file name:")
# l=input("enter letter to be searched:")
# k=0
#
# with open(fname,'r') as f:
#     for line in f:
#         words=line.split()
#         for i in words:
#             for letter in i:
#                 if (letter==l):
#                     k=k+1
# print("occurances of the letter:")
# printx
