li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
result=(filter(lambda x:(x%2!=0),li))
print(list(result))

ages = [13, 90, 17, 59, 21, 60, 5]
youngest=list(filter(lambda x: (x<18),ages))
print(youngest)