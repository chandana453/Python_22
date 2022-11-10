#5.Python Program to Count the Occurrences of a Word in a Text File
word="of"
f=open("First.txt","r")
count=0

fileRead=f.read()
words=fileRead.split(" ")
for i in words:
    if i==word:
        count+=1
print(count)

#2nd approach - finding occurances of each word in a file

f=open("myfile.txt","r")
dict={}
for line in f:
    line = line.lower()
    # Remove the leading spaces and newline character
    line = line.strip()
    # Splitting the data into separate lines using the split() function
    words = line.split()
    for word in words:
        if word in dict:
             dict[word]=dict[word]+1
        else:
             dict[word]=1

for key in list(dict.keys()):
    print(key,":",dict[key])


