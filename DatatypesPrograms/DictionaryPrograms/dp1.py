#1.Python Program to Check if a Key Exists in a Dictionary or Not
def checkKey(dict,key):
    if key in dict:
        print("Key is present",key," with value:",dict[key])
    else:
        print("key is not present")

d={"a":"john","b":"adams","c":"jos"}
key="c"
checkKey(d,key)