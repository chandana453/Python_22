import os.path
path = "C:\\Users\\Dell\\OneDrive\\Desktop\\poem.txt"
# path = "../text_file/poem.txt"

if os.path.exists(path) is True:

    f=open(path,'r')
    poem_list = f.readlines()
    for line in poem_list:
        if line[0] == "G":
            pass
        else:
            print(line,end=" ")
    f.close()


