# question:1
# Python Program to Check if a Key Exists in a Dictionary or Not
# solution:
# d={'A':1,'B':2,'C':3}
# key=raw_input("Enter key to check:")
# if key in d.keys():
#       print("Key is present and value of the key is:")
#       print(d[key])
# else:
#       print("Key isn't present!")

# question:2
# Python Program to Add a Key-Value Pair to the Dictionary
# solution:
# dict = {'key1':'geeks', 'key2':'for'}
# print("Current Dict is: ", dict)
# dict['key3'] = 'Geeks'
# dict['key4'] = 'is'
# dict['key5'] = 'portal'
# dict['key6'] = 'Computer'
# print("Updated Dict is: ", dict)

# question:3
# python Program to Multiply All the Items in a Dictionary
# solution:
# d={'A':10,'B':10,'C':239}
# tot=1
# for i in d:
#     tot=tot*d[i]
# print(tot)

# question:4
# Python Program to Remove a Key from a Dictionary
# solution:
# myDict = {'a':1,'b':2,'c':3,'d':4}
# print(myDict)
# if 'a' in myDict:
#     del myDict['a']
# print(myDict)

# question:5
# Python Program to Concatenate Two Dictionaries
# solution:
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
# for d in (dic1, dic2, dic3): dic4.update(d)
# print(dic4)

# question:6
# Python Program to Map Two Lists into a Dictionary
# solution:
# keys=[]
# values=[]
# n=int(input("Enter number of elements for dictionary:"))
# print("For keys:")
# for x in range(0,n):
#     element=int(input("Enter element" + str(x+1) + ":"))
#     keys.append(element)
# print("For values:")
# for x in range(0,n):
#     element=int(input("Enter element" + str(x+1) + ":"))
#     values.append(element)
# d=dict(zip(keys,values))
# print("The dictionary is:")
# print(d)

# question:7
# Python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character
# solution:
# my_string=input("Enter the string :")
# split_string = my_string.split()
# my_dict={}
# for elem in split_string:
#    if(elem[0] not in my_dict.keys()):
#       my_dict[elem[0]]=[]
#       my_dict[elem[0]].append(elem)
#    else:
#       if(elem not in my_dict[elem[0]]):
#          my_dict[elem[0]].append(elem)
# print("The dictionary created is")
# for k,v in my_dict.items():
#    print(k,":",v)

# question:8
# Python Program to Create Dictionary that Contains Number
# solution:
# d=dict()
# for x in range(1,16):
#     d[x]=x**2
# print(d)

# question:9
# Python Program to Count the Frequency of Each Word in a String using Dictionary
# solution:
# from nltk import FreqDist
# text = "Learn and practice and learn to practice"
# words = text.split()
# fdist1 = FreqDist(words)
# print(fdist1)
# print(fdist1.most_common())
