'''
Define a class with a generator which can iterate the numbers, which
Hints:
Consider use yield
solution:
'''
def putNumber(n):
    i=0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in reversed(100):
     print(i)

