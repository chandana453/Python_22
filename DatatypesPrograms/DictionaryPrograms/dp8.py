#8.Python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character
str="create a dictionary"
words=str.split(" ")
dict={}
for word in words:
    if word[0] not in dict.keys():
        dict[word[0]]=[]
        dict[word[0]].append(word)
    else:
        if word not in dict[word[0]]:
            dict[word[0]].append(word)

print(dict)