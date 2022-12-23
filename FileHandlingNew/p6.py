#6.Write a function in Python to count the words "this" and "these" present in a text file "article.txt". [Note that the words "this" and "these" are complete words]

import os.path

file_path='/Users/mounika/Desktop/article.txt.rtf'
file_size=os.path.getsize(file_path)
print("FILE SIZE:",file_size,"bytes")

def countWords():
    try:
        with open("/Users/mounika/Desktop/article.txt.rtf") as f:
            count = 0
            data = f.read()
            words = data.split() #Split the text using space separator
            for word in words:
                if word=="this" or word=="these":
                    count+=1

        print("Count:",count)

    except Exception as e:
        print("Error:",e)

countWords()
