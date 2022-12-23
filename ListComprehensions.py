li=[(x,y) for x in [1,2,3] for y in (1,2,3) if x!=y]
print(li)

from math import pi  # import pi number from math module

li=[str(round(pi, i)) for i in range(1, 6)]
print(li)
#In Python, dictionary comprehensions are very similar to list comprehensions – only for dictionaries. They provide an
# elegant method of creating a dictionary from an iterable or transforming one dictionary into another.

print("Dict Comprehensions")
k=dict([(i,i+10) for i in range(4)])
print(k)

l=[2,3,4,5]
print("----list----")
m=[x for x in l if x%2!=0]
print(m)

k={x:x*x for x in l}
print(k)

m={i:i+10 for i in range(10) if i>5}
print(m)


#Similar to list comprehensions, dictionary comprehensions are also a powerful alternative to for-loops and lambda functions. For-loops, and nested for-loops in particular, can become complicated and confusing. Dictionary comprehensions offer a more compact way of writing the same code, making it easier to read and understand.
m={(k,v):k+v for k in range(2) for v in range(2)}
print(m)
#Class-based iterators in Python are often verbose and require a lot of overhead. Generators, on the other hand, are able to perform the same function while automatically reducing the overhead.
#Generators are relatively easy to create; a normal function is defined with a yield statement, rather than a return statement. The yield statement has the effect of pausing the function and saving its local state, so that successive calls continue from where it left off.
print("....Generators.....")
def gen():

   for x in range(10):
       yield x**2
       #print(k)

x=gen()
print(list(x))


# g=(x**2 for x in range(10))
# print(list(g))

#Another valuable feature of generators is their capability of filtering elements out with conditions.
gen_exp=(i**2 for i in range(10) if i>5)
for i in gen_exp:
    print(i)
