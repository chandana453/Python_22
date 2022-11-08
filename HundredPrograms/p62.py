'''
Write a program to read an ASCII string and to convert it to a unicode
string encoded by utf-8.
Hints:
Use unicode() function to convert.
Solution:
'''
s=input()
utf=s.encode()
print("Encode string is",utf)


# o/p:Dejan ŹivkoviČ
# Encode string is b'Dejan \xc5\xb9ivkovi\xc4\x8c'