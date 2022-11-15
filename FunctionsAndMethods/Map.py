l1=[1,2,3,4]
x=map(lambda a:a+a,l1)
print(list(x))

l2=[1,2,3,4,5]
y= map(lambda x:x*x , l2)
print(list(y))

list1=[1,3,5]
list2=[2,4,6]

result=map(lambda x,y: x+y,list1,list2)
print(list(result))

#map() can listify the list of strings individually
str=["abc","def","ghi"]
res=map(list,str)
print(list(res))

#squares of numbers
l1=[2,3,4,5]
result=map(lambda a:a*a,l1)
print(list(result))


#cubes
tup1=(3,4,2,5,6,3,7,5,2)
x=list(map(lambda a:a**a,tup1))
print(x)

#perfect squares
l=[1,2,3,4,5]
res=map(lambda x:x*x,l)
print(list(res))
