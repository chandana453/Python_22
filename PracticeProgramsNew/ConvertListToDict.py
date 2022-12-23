#15.Write a Python program to convert a list into a dictionary where keys are the unique elements of the list and the values are their frequency.
# Ex:
# Input: ['a', 'b', 'c', 'a', 'd', 'e']
# Output: {'a': 2, 'b': 1, 'c': 1, 'd': 1, 'e': 1}

#correct Approach
from collections import Counter

l = ['a', 'b', 'c', 'a', 'd', 'e']
l1=Counter(l)
print(l1)
#converting the counter object to dictionary
Output_dict=dict(l1)
print(l1)


#Some random approach
list1=['a', 'b', 'c', 'a', 'd', 'e']
dict={}

for ele in list1:
    dict[ele]=dict.get(ele,0)+1

print(dict)