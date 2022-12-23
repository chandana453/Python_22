#8.Write a Python program to append 'El Niño' string to the text file using encoding.

with open("File5.txt","w+",encoding="utf-8") as f:
    f.write(u"El Niño")
    f.seek(0)
    print(f.read())
