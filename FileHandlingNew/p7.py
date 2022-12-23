#7.Write a function in Python to count words in a text file those are ending with alphabet "e"

import os.path

file_path='/Users/mounika/Desktop/article.txt.rtf'
file_size=os.path.getsize(file_path)
print("FILE SIZE:",file_size,"bytes")

def countWordEndingWithE():
    try:
        with open("/Users/mounika/Desktop/article.txt.rtf") as f:
            count = 0
            data = f.read()
            words = data.split() #Split the text using space separator
            for word in words:
                if word[-1]=='e':
                    count+=1

        print("Count:",count)

    except Exception as e:
        print("Error:",e)

countWordEndingWithE()

