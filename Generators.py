# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)


#2nd example
list1=[2,3,4,5]

x=[x**2 for x in list1]
print(x)

# same thing can be done using a generator expression and generator expressions are surrounded by parenthesis ()
generator=(x**2 for x in list1)
print(list(generator))


#3rd example

list2=[1,2,3,4,5]

gen=(x**2 for x in list2)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#4th example

def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1


#5th example

def all_even():
    n = 0
    while True:
        yield n
        n += 2

#6th example

def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)

#7th example

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))

#8th example

def oddNumbers(num):
    for i in range(num):
        if i%2!=0:
            yield i

result=oddNumbers(20)
for i in result:
    print(i)


#9th example

#find perfect squares of a number

def perfectSquares():
    num=1
    while num<=10:
        sq=num*num
        yield sq
        num+=1

for i in perfectSquares():
    print(i)
