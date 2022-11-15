# #10.Define a list and create a dictionary where the dictionary key is an index of the element and value
# is an element in the list.

l=[0,1,4,9,16,25]

d={}

for i in range(len(l)):
    d[i]=l[i]

for key, value in d.items():
    print(key,":",value)