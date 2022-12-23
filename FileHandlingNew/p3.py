#3.Write a function in Python to count and display the total number of words in a text file.
import os.path

file_path='/Users/mounika/Desktop/example.txt.rtf'
file_size=os.path.getsize(file_path)
print("FILE SIZE:",file_size,"bytes")

def NumOfWords():
        try:
            with open("/Users/mounika/Desktop/example.txt.rtf")as f:
                data = f.read()
                words = data.split() #Split the text using space separator
                print("Number of words in a file:",len(words))

        except Exception as e:
            print("Error:",e)

NumOfWords()