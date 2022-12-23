#10.which should read each character of a text file STORY.TXT, should count and display the occurance of alphabets A and M (including small cases a and m too).
# For Example: If the file content is as follows:Updated information As simplified by official websites.
# The EUCount() function should display the output as:
# A or a:4 M or m :2

#8.Write a function in Python to count uppercase character in a text file.
import os.path

file_path='/Users/mounika/Desktop/story.txt.rtf'
file_size=os.path.getsize(file_path)
print("FILE SIZE:",file_size,"bytes")

def AMCount():
    try:
        with open("/Users/mounika/Desktop/story2.txt.rtf") as f:
            a_count = 0
            m_count=0
            data = f.read()
            for letter in data:
                if letter=='a' or letter=='A':
                    a_count+=1
                elif letter=='m' or letter=='M':
                    m_count+=1

        print("A_Count:",a_count,"M_Count:",m_count)

    except Exception as e:
        print("Error:",e)

AMCount()
