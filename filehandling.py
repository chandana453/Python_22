#Python Program to Read the Contents of the File
f = open(r"C:\Users\pmr\Desktop\programming test books\list of courses.txt" ,"r")
print(f.readline())
f.close()
#Python Program to Copy One File to Another File
first_file = open(r"C:\Users\pmr\Desktop\programming test books\list of courses.txt" ,"r")
second_file= open(r"C:\Users\pmr\Desktop\gitam\sample.txt" ,"r+")
for line in first_file :
    second_file.write(line)
print(second_file.readline())
#Python Program to Count the Number of Lines in Text File
file= open(r"C:\Users\pmr\Desktop\gitam\sample.txt" ,"r+")
lines = len(file.readlines())
print("the number of lines in file:",lines )
#Python Program to Count the Number of Blank Spaces in a Text File
file1= open(r"C:\Users\pmr\Desktop\gitam\sample.txt" ,"r+")
count = 0
while True:
    char = file1.read(1)
    if char.isspace() :
        count+=1
    if not char :
        break
print("the number of spaces in file:" , count)
#Python Program to Count the Occurrences of a Word in a Text File
file1= open(r"C:\Users\pmr\Desktop\gitam\sample.txt" ,"r+")
d = dict()
for line in file1:
    line = line.strip()
    line = line.lower()
    values = line.split(" ")
    for word in values:
        if word in d:
            d[word] += + 1
        else :
            d[word] =1
for key in list(d.keys()) :
    print(key,":",d[key])
#Python Program to Capitalize First Letter of Each Word in a File
file1= open(r"C:\Users\pmr\Desktop\gitam\sample.txt" ,"r+")
for line in file1:
 word_change = line.title()
 print(word_change)
#Python Program to Counts the Number of Times a Letter Appears in the Text File
file1= open(r"C:\Users\pmr\Desktop\gitam\sample.txt" ,"r+")
for