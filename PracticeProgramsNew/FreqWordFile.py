#7.Write a Python program to count the frequency of words in a file.
from DatatypesPrograms.StringsProblems.sp1 import string

dict={}
with open("Sample.txt","w+") as f:
    f.write("Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis. Python is a general-purpose language")

f=open("Sample.txt","r")
file=f.read().split()
for word in file:
  if word in dict:
    dict[word]+=1
  else:
     dict[word]=1


for k,v in dict.items():
    print(k,":",v)

# for i in dict:
#     print(i,dict[i])







#2nd approach

# Open the file in read mode
text = open("sample.txt", "r")

# Create an empty dictionary
d = {}

# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()

    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()

    # Remove the punctuation marks from the line
    # line = line.translate(line.maketrans("", "", string.punctuation))

    # Split the line into words
    words = line.split(" ")

    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

# Print the contents of dictionary
for key in list(d.keys()):
    print(key, " ", d[key])
