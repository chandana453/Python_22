'''
Define a function that can accept an integer number as input and print
the "It is an even number" if the number is even, otherwise print "It
is an odd number".
Hints:
Use % operator to check if a number is even or odd.
'''

def checkvalue(d):
    if  d%2 == 0:
        print("it is an even number")
    else:
        print("it is an odd number")
checkvalue(7)