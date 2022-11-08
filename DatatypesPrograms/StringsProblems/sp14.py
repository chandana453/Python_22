#14.Python Program to Count the Number of Digits and Letters in a String
def countDigLet(str):
    d={"Digits":0,"Letters":0}
    for i in str:
        if i.isdigit():
            d["Digits"]+=1
        elif i.isalpha():
            d["Letters"]+=1
        else:
            pass
    print("No of digits:",d["Digits"])
    print("No of letter:", d["Letters"])

countDigLet("str123ing34")