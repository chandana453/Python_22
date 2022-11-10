#8.Python Program to Counts the Number of Times a Letter Appears in the Text File

def freqOfLetter(file1,letter):
    f=open(file1,"r")
    count=0
    data=f.read()
    for char in data:
        if char==letter:
            count+=1
    return count

k=freqOfLetter("myfile.txt","t")
print("No of times a letter appeared in a file :",k)