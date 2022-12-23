#11.Write a Python program to count the number of characters (character frequency) in a string
# Sample String: google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}


st="google.com"
d={}
def CountCharacters(st):
    #words = [x for x in st]
    for word in st:
        if word in d:
            d[word]+=1
        else:
            d[word]=1
    return d
print(CountCharacters(st))

#2nd approach

from collections import Counter
st="Helloo!"
res=Counter(st)
print(res)


#3rd approach
st="Python Programming"
d={}
for word in st:
    d[word]=d.get(word,0)+1
print(d)
