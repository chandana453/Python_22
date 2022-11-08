'''
RIGHT 2
Then, the output of the program should be:
2
Hints:
In case of input data being supplied to the question, it should be
assumed to be a console input.
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
Hints
In case of input data being supplied to the question, it should be
assumed to be a console input.
solution:
'''
freq ={}   #frequency of words in text
line =input()
for word in line.split():
    freq[word]=freq.get(word,0)+1

words =freq.keys()
words.sort()
for w in words:
    print("%s:%d"%(w,freq[w]))

