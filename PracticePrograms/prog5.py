#5.Print the type of integer until the given index position in characters(Even or Odd) exclude index 0.
# Input: [0,1,2,3,4,6,7,8]
# index: 5
# Output: ['Odd','Even', 'Odd', 'Even', 'Even']

list1=[0,1,2,3,4,6,7,8]
new_list=[]

n=int(input("ENter index: "))

for i in range(1,n+1):
     if list1[i]%2==0:
         new_list.append("Even")
     else:
         new_list.append("Odd")

print(new_list)