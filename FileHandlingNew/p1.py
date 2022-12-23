#1.Write a function in python to read the content from a text file "poem.txt" line by line and display the same on screen.
import os.path

#To get size of the file
file_path="/Users/mounika/Desktop/poem.txt"
file_size=os.path.getsize(file_path)
print("SIZE OF THE FILE:",file_size,"bytes")

def display():
    try:
        with open("/Users/mounika/Desktop/poem.txt", "r") as f:
            f1=f.readline()
            for f1 in f:
                print(f1)

    except Exception as e:
            print("Error:",e)

display()



