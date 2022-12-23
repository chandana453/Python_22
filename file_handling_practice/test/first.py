from pathlib import Path

path_to_file = "C:\\Users\\Dell\\OneDrive\\Desktop\\poem.txt"


path = Path(path_to_file)

if path.is_file() is True:
    f = open(path,"r")
    list = f.readlines()
    for i in list:
        print(i,end=" ")
    f.close()