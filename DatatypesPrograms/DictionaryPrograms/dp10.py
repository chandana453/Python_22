#10.Python Program to Count the Frequency of Each Word in a String using Dictionary
str ='apple mango apple orange orange apple guava mango mango'
str_list=str.split(' ')
unique_words=set(str_list)

for i in unique_words:
    print("Frequency of", i,"is:",str_list.count(i))

str ='apple mango apple orange orange apple guava mango mango'
words = str.split()
wfreq=[words.count(w) for w in words]
print(dict(zip(words,wfreq)))

str="apple"
d={}
for i in str:
    d[i]=d.get(i,0)+1
print(d)

from collections import Counter
str="banana"
print(Counter(str))





