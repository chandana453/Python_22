#Python Program to Find Second Largest Number in a List
li=[70,11,20,4,100]
li.sort()
print(li[-2])

#2nd approach: Using enumerate function
lst = [30, 20, 4, 25, 99]
maximum_element=max(lst)
x=[x for i,x in enumerate(lst) if x<maximum_element]
# for i in x:
#     print(i)
print(max(x))


#3rd approach:using list comprehension
def max_element():
    sublist=[x for x in arr if x<max(arr)]
    return max(sublist)
arr=[20,15,9,7,12,30,27]
k=max_element()
print(k)

#4th approach:By removing the max element from the list
list1=[20,15,9,7,12,30,27]
#to remove the duplicates from the list
new_list=list(set(list1))
new_list.remove(max(new_list))
print(max(new_list))

#5th approach
# Traverse once to find the largest and then once again to find the second largest.
arr=[20,15,9,7,21,30,97,99]
largest=min(arr)
second_largest=0
n=len(arr)
for i in range(n):
    if(arr[i]>largest):
        second_largest=largest
        largest=arr[i]
    else:
        second_largest=max(second_largest,arr[i])

print(second_largest)


list=[120,15,9,7,21,30,97,99,190]
max1=list[0]
second_max=0
for i in range(len(list)):
     if list[i]>max1:
         second_max = max1
         max1=list[i]
     elif list[i]>second_max and list[i]!=max1:
         second_max = list[i]

print(second_max)
