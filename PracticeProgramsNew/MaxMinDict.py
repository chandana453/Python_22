#17.Write a Python program to get the maximum and minimum value in a dictionary

d={'a':5,'b':2,'c':7,'d':9,'e':5}
l=d.values()  #Dictionary values() Method -- The values() method returns a view object
#print(l)

print("Maximum value : ",max(l))
print("Minimum value : ",min(l))

