#8.Write a function in Python to count uppercase character in a text file.
import os.path

file_path='/Users/mounika/Desktop/poem.txt'
file_size=os.path.getsize(file_path)
print("FILE SIZE:",file_size,"bytes")

def countUppercase():
    try:
        with open("/Users/mounika/Desktop/poem.txt") as f:
            count = 0
            data = f.read()
            for letter in data:
                if letter.isupper():
                    count+=1

        print("Count:",count)

    except Exception as e:
        print("Error:",e)

countUppercase()
