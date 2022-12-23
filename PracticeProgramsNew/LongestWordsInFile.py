#6.Write a python program to find all the longest words(which have more than 10 characters) from the file.

with open("random.txt","w") as f:
    f.write("This program is to find the longestword in a file \n some of the words are : elephants1 rabbit crocodiles1")


f=open("random.txt","r")
length=10
longest=""
l=[]
file=f.read().split()
for word in file:
    if len(word) > length:
        l.append(word)

print(", ".join(l))  # to convert list to string

#2nd Approach (using list comprehension)

with open("random.txt","w") as f:
    f.write("\n Abbreviation Complicated Implicated Imply Comply Encapsulation abbreviated Imagination Explanation")
    f.close()


with open("random.txt",'r') as f1:
  wordsList=f1.read().split()
  #LongestWord=len(max(words List, key=len)) # key=len specifies that we must obtain the word depending on its length
  LongestWord=10
  result=[word for word in wordsList if len(word)>LongestWord]

print(result)

