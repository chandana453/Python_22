import os.path

path = "C:\\Users\\Dell\\OneDrive\\Desktop\\fourth.txt"
# path = "../text_file/fourth.txt"

def word_counter_len4(path):
    if os.path.exists(path) is True:
        f = open(path,"r")
        list_of_lines = f.read()
        words = list_of_lines.split(" ")
        count = 0
        for word in words:
            if len(word) >= 4:
                count += 1
        f.close()
        return  count
    else:
        return "file not found"


val = word_counter_len4(path)
print(val)