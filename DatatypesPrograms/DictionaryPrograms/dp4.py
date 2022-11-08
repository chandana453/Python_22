#4.Python Program to Multiply All the Items in a Dictionary
def MultiplyKeys(dict):
    val=1
    for i in dict:
        val=val*dict[i]

    return val

d={"a":10,"b":20,"c":100}
print(MultiplyKeys(d))