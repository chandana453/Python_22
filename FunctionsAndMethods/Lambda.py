#lambda is small anonymous function which has single expression

x= lambda a:a+10
print(x(5))

x=lambda a,b : a*b
print(x(5,6))

x=lambda a,b,c : a+b+c
print(x(1,2,3))

def func(n):
    return lambda a:a*n

mydoubler = func(2)
mytripler = func(3)

print(mydoubler(11))
print(mytripler(11))

#string example

#reverse upper
str="python"
rev_upper=lambda x:x.upper() [::-1]
print(rev_upper(str))

#Reverse
str1="Program"
rev=lambda x:x [::-1]
print(rev(str1))

#upper
str1="execution"
rev=lambda x:x.upper() [::-1]
print(rev(str1))

#maximum
res=lambda a,b:a if (a>b) else b
print(res(5,7))

