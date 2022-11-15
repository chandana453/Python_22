#9.Write a program to reverse a string word by word along with reverse the characters in each word.

str="My name is Mounika"
#reverse of a string
s=str[::-1]
s=str.split()[::-1]
l=[]
for word in s:
    # apending reversed words to l
    l.append(word)

#printing reverse words
print(" ".join(l))

#reversing the letters in a string
rev_list=[]
for word in l:
    rev_list.append(word[::-1])

print(" ".join(rev_list))
