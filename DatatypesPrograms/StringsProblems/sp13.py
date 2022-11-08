#13.Python Program to Count Number of Uppercase and Lowercase Letters in a String

def countCase(str):
    d={"Uppercase":0,"Lowercase":0}
    for i in str:
        if i.isupper():
            d["Uppercase"]+=1
        elif i.islower():
            d["Lowercase"]+=1
        else:
            pass
    print("No of uppercase letters:",d["Uppercase"])
    print("No of lowercase letters:",d["Lowercase"])

string1="abcdEFghIjK"
countCase(string1)