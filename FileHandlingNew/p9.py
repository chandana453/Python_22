#9. A text file named "matter.txt" contains some text, which needs to be displayed such that every next character is separated by a symbol "#". Write a function definition for hash_display() in Python that would display the entire content of the file matter.txt in the desired format.
import os.path

file_path='/Users/mounika/Desktop/matter.txt.rtf'
file_size=os.path.getsize(file_path)
print("FILE SIZE:",file_size,"bytes")

def hash_display():
    try:
        with open("/Users/mounika/Desktop/matter.txt.rtf") as f:
            data = f.read()
            for letter in data:
                print(letter,end='#')

    except Exception as e:
        print("Error:",e)

hash_display()
