#12.Python Program to Count the Number of Vowels in a String
def vowelCount(str):
    count=0
    vowels=set("aeiouAEIOU")
    for i in str:
        if i in vowels:
            count+=1
    return count

str="awesome"
print(vowelCount(str))