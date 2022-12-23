#4.Write a function in Python to read lines from a text file "notes.txt". Your function should find and display the occurrence of the word "the".

import os.path

file_path='/Users/mounika/Desktop/notes.txt.rtf'
file_size=os.path.getsize(file_path)
print("FILE SIZE:",file_size,"bytes")

def Occurrance():
    try:
        with open("/Users/mounika/Desktop/notes.txt.rtf") as f:
            data = f.read()
            count=0
            words = data.split() #Split the text using space separator
            for word in words:
                if word=="the" or word=="The":
                    count+=1
        print("Occurence of the word- the:",count,"times")

    except Exception as e:
        print("Error:",e)

Occurrance()