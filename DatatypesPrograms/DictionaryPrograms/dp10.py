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







