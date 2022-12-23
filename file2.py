from file1 import sample

def calculator(a,b):
    s=sample()
    add=s.add(a,b)
    mul=s.mul(a,b)
    return("Addition :",add,"Multiplication :", mul)

print(calculator(5,10))

