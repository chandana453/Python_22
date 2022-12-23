import os.path

path = "C:\\Users\\Dell\\OneDrive\\Desktop\\fourth.txt"
# path = "../text_file/fourth.txt"

def count(path,word1,word2):
    if os.path.exists(path) is True:
        f = open(path,"r")
        list_of_lines = f.read()
        words = list_of_lines.split(" ")
        print(f"'{word1}' has been repaeted {words.count(word1)} times" )
        print(f"'{word2}' has been repaeted {words.count(word2)} times" )
        f.close()
    else:
        return "file not found"


count(path,"the","an")