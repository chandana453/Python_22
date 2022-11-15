#3.Write a Python program to get the maximum and minimum value from a list without using any predefined function.

li=[4,7,5,17,8,3,288,1]
min=li[0]
max=li[0]

for i in range(len(li)):
    if li[i] > max:
        max=li[i]
    if li[i] < min:
        min=li[i]

print(max)
print(min)