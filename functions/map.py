l=[1,2,3,4]
x=map(lambda a:a+a,l)
print(list(x))

squares
l=[2,3,4,5]
x=map(lambda a:a*a,l)
print(list(x))

cubes
l=[2,3,4,5]
x=map(lambda a:a**a,l)
print(list(x))

strings
str=["abc","def","ghi"]
res=map(list,str)
print(list(res))