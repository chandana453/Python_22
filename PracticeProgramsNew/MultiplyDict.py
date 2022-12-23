#16.Write a Python program to multiply all the items in a dictionary

d={'A':10,'B':20,'C':3,'D':4}
res=1
for i in d:
    res=res*d[i]

print(res)