#5.Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.

import os.path

file_path='/Users/mounika/Desktop/story.txt.rtf'
file_size=os.path.getsize(file_path)
print("FILE SIZE:",file_size,"bytes")

def displaywords(length):
    try:
        with open("/Users/mounika/Desktop/story.txt.rtf") as f:
            data = f.read()
            count=0
            words = data.split() #Split the text using space separator
            for word in words:
                if len(word)<length:
                    count+=1
                    print(word,end=", ")
        print("Total Words of letters less than 4 in file are:",count)

    except Exception as e:
        print("Error:",e)

displaywords(4)
