'''
python program to print largest even and
largest odd number in alist
solution:
'''
list=[765,75,434,978,547,321]
x=[i for i in list if i%2==0]
print(x)
y=[i for i in list if i%2!=0]
print(y)
largest_even =max(x)
largest_odd =max(y)
print("largest even number :",largest_even)
print("laregst odd number :",largest_odd)