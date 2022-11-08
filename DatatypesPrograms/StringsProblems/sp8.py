#8.Python Program to Determine How Many Times a Given Letter Occurs in a String
string1="procedural programming"

def occuranceString(str,letter):
    count = 0
    for i in str:
      if i==letter:
         count=count+1
    return count

letter="r"
print(occuranceString(string1,letter))