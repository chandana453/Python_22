#2.Write a function in python to count the number of lines from a text file "example.txt" which is not starting with an alphabet "G"
import os.path

file_path='/Users/mounika/Desktop/example.txt.rtf'
file_size=os.path.getsize(file_path)
print("FILE SIZE:",file_size,"bytes")

def CountNoOfLines():
    try:
        with open("/Users/mounika/Desktop/example.txt.rtf")as f:
            line=f.readline()
            count=0
            for line in f:
                if line[0]!='G':
                    count+=1

        print("Count",count)

    except Exception as e:
        print("Error:",e)

CountNoOfLines()