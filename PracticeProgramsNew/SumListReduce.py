#13.Write a Python program to sum all the items in a list using reduce.


#reduce() function to reduce a list into a single value.
from functools import reduce
list1=[1,2,3,4,5,6,7]
result = reduce(lambda a, b: a + b, list1)
print(result)