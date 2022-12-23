'''
Define a function which can generate a dictionary where the keys are
numbers between 1 and 20 (both included) and the values are square of
keys. The function should just print the keys only.
Hints:
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item()
to get key/value pairs.
'''


def printDict():
    # d = dict()
    # for i in range(1, 21):
    #     d[i] = i ** 2
    # for k in d.keys():
    #     print(k)
    d={x: x**2 for x in range(1,21)}
    print(d)
printDict()