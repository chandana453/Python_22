##Python Program to Read the Contents of the File
#
# with open("my_file.txt","r") as file:
#     r = file.read()
#     print(r)


##Python Program to Copy One File to Another File
#
#
#
# with open("my_file.txt","r") as first, open("second.txt","w") as second:
#
#     for line in first:
#         second.write(line)


##Python Program to Count the Number of Lines in Text File
# count =0
# with open("my_file.txt","r") as file:
#
#     lines = file.readlines()
#     for i in lines:
#         count +=1
#     print("no.of lines are ",count)


##Python Program to Count the Number of Blank Spaces in a Text File
#
#
# with open("my_file.txt","r") as file:
#     count =0
#     while True:
#         char = file.read()
#         print(char)
#
#         if char == " ":
#
#             count+=1
#         if not char:
#             break
#
# print(count)
#


##Python Program to Count the Occurrences of a Word in a Text File
# word = "is"
# count = 0
# with open("my_file.txt","r") as file:
#
#     for line in file:
#         a = line.split(" ")
#         for i in a:
#             if i == word:
#                 count +=1
#             else:
#                 pass
#
#
#
# print(count)



##Python Program to Count the Number of Words in a Text File

# with open("my_file.txt","r") as file:
#     a= file.read()
#     b= a.split()
#     print(b,len(b))



##Python Program to Capitalize First Letter of Each Word in a File


# with open("my_file.txt","r") as file:
#     a= file.read()
#     print(a.title())



##Python Program to Counts the Number of Times a Letter Appears in the Text File
#
# with open("my_file.txt","r") as file:
#         lines = file.read()
#         print(lines.count("a"))



##Python Program to Extract Numbers from Text File
#
# with open("my_file.txt","r") as file:
#     lines = file.read()
#     for char in lines:
#         if char.isnumeric():
#             print(char)



##Python Program to Print the Contents of File in Reverse Order
# ##word reverse
# with open("my_file.txt","r") as file:
#     line = file.readlines()
#     data = line[::-1]
#     print(data)
# ##letter reverse
# with open("my_file.txt","r") as file:
#     line = file.read()
#     data = line[::-1]
#     print(data)



##Python Program to Append the Content of One File to the End of Another File
# with open("my_file.txt","r") as file:
#     a = file.read()
#     with open("second.txt","a+") as ext: # if we use w then it will clear the file and then write
#         #so by using a+ we are writing at the end
#         ext.write("\n")
#         ext.write(a)



##Python Program to Read a String from the User and Append it into a File
#
# with open("second.txt","w") as file:
#     str = input("enter a sentence: ")
#     file.write(str)






