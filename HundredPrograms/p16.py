'''
Use a list comprehension to square each odd number in a list. The list
is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
Hints:
In case of input data being supplied to the question, it should be
assumed to be a console input.
'''
values="1,2,3,4"
# li=[]
# for i in values.split(","):
#     if int(i)%2 != 0:
#         li.append((int(i))**2)
# print(li)
# data=[str(i) for i in li]
# print(data)
# print(",".join(data))
# print(' '.join(li))
numbers = [int(x)**2 for x in values.split(",") if int(x)%2!=0]
print(numbers)
data=[str(i) for i in numbers]
print(data)
print(",".join(data))
#print(",".join(numbers))

