#5.Write a Python program to demonstrate different modes of a file open method.

f=open("Myfile.txt","w") #creates a file if it doesn't exist
f.write("Hello, Python programmer")
f.close()

#Read the Contents of the File

with open("Myfile.txt","a+") as f1:   #appending will not overwrite,adds the content to the existing file
     f1.write(" Welcome to the programming world!\n")  #a+ -> appending,reading and writing
     f1.write("The .readlines() method always gives a list of all the lines of our file as list elements.\n")
     f1.write("The .readline() method prints each line from our file, every time we execute this function, until the end of the file is reached.\n")
     f1.write("EXIT!\n")
     f1.seek(0)    # Now moves the cursor to the beginning of the file
     #print(f1.read())

     # print(f1.readline())
     # print(f1.readline())
     # print(f1.readline())

     #print(f1.readlines())
#
# #The .readline() method prints each line from our file, every time we execute this function, until the end of the file is reached. Let’s add some additional lines to our text file to illustrate this example.
#
# #The .readlines() method always gives a list of all the lines of our file as list elements.
#
with open("Myfile.txt","r+") as f:    #r+ reading and writing
    #f.write("Helloooooo!!")   #file pointer position is at the beginning of the file; if we write the file directly, it will overwrite the beginning content.
    print(f.read())  #f.read() to move the file pointer to the end of the file, and append a new line.
    f.write("Helloooooo!!\n")
    print(f.read())




with open('file.txt', 'w+') as f1:   # create a new file or truncates it (w+ for reading and writing)
    f1.write("test 1\n")
    f1.write("test 2\n")
    f1.write("test 3\n")   # now the file pointer is at the end
    f1.seek(0)              # move the file pointer to the beginning
    lines = f1.read()       # read it, now we can read!
    print(lines)     # print it


import os
os.rename('Myfile.txt', 'ourfile.txt')   # to rename we need to import os


with open('file1.txt', 'a+') as f2:
    f2.write("Python 1\n")
    f2.write("Python 2\n")
    f2.write("Python 3\n")
    f2.seek(0)                       # file pointer at end, move to beginning
    lines = f2.readlines()           # read all and file pointer at end again
    f2.write("\n" + str(len(lines)))  # append number of lines to a file
    f2.seek(0)
    print(f2.read())


file = open('Myfile.txt', 'w')
file.truncate(20)  #the file will get truncated up to the current cursor position of the file.
# .truncate() method is, the file must be opened in write mode to perform truncating task
file.close()



# If the file does not exist, r+ throws FileNotFoundError; the w+ creates the file.
# If the file exists, r+ opens it without truncating; the w+ truncates the file and opens it.

# If the file does not exist, r+ throws FileNotFoundError; the a+ creates the file.
# For r+ mode, the initial file pointer position at the beginning of the file; For a+ mode, the initial file pointer position at the end of the file.


# If the file exists, w+ truncates the file and opens it; a+ opens it without truncating.
# For w+ mode, the initial file pointer position at the beginning of the file; For a+ mode, the initial file pointer position at the end of the file.


file = open("SampleFile.txt", 'w')
file.write("This is the Practical ExamplenIt performs reading, writing and closing operations of filen")
file.close()
file = open("SampleFile.txt", 'r')
print(file.read(10))
file.seek(0)   #The .seek() method in Python is used to change the cursor to a specific position.
print(file.readlines())
file.seek(0)
print(file.readline())
file.close()

# The .tell() method in Python prints the current position of our cursor.

file = open("SampleFile.txt", 'r')
print(file.tell())