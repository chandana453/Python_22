# def max_num_in_list(list):
#     max = list[0]
#     for i in list:
#         if i > max:
#              max = i
#     return max
# print(max_num_in_list([1,2,3,-8,0]))

# quetion 2:
# Python Program to Find Second Largest Number in a List
# solution:
# def findLargest(arr):
#     secondLargest = 0
#     largest = min(arr)
#     for i in range(len(arr)):
#         if arr[i] > largest:
#             secondLargest = largest
#             largest = arr[i]
#         else:
#             secondLargest = max(secondLargest, arr[i])
#     return secondLargest
# print(findLargest([10,20,30,4,50,99]))


# question:3
# Python Program to Print Largest Even and Largest Odd Number in a List
# solution:
# class LargestOddAndEven:
#      def largesteven(self,list):
#          crr = -1
#          for num in list:
#              num = int(num)
#              if(num % 2 == 0 and num > curr):
#                 curr = num
#          print("Largest even number is ",curr )
# def largestOdd(self,list):
#           curr = -1
#           for num in list:
#               num = int(num)
#               if(num % 2 == 1 and num > curr0):
#                   curr0 = num
#           print("largest odd number is ", curr0)
# list_num =  [1,2,3,5,8,7,10]
# obj = LargestOddAndEven()
# obj.largestEven(list_num)
# obj.largestOdd(list_num)

# question:4
# Python Program to Split Even and Odd Elements into Two Lists
# solution:
# def splitevenodd(A):
#    evenlist = []
#    oddlist = []
#    for i in A:
#       if (i % 2 ==0):
#          evenlist.append(i)
#       else:
#          oddlist.append(i)
#    print("Even lists:",evenlist)
#    print("Odd lists:",oddlist)

# question:5
# Python Program to Find Average of a List
# solution:
# def Average(list):
#     return sum(list) / len(list)
# list = [15,9,55,41,35,20,62,49]
# average = Average(list)
# print("Average of the list =", round(average,2))

# question:6
# Python Program to Print Sum of Negative Numbers, Positive Even & Odd Numbers in a List
# solution:
# def negSum(self,list):
#     neg_sum = 0
#     for num in list:
#         num = int(num)
#         if(num < 0):
#             neg_sum = num
#     print("sum of negative numbers is ", neg_sum)

# question:7
# Python Program to Count Occurrences of Element in list
# def countX(list,x):
#     count = 0
#     for ele in list:
#         if (ele == x):
#             count = count + 1
#     return count
# list = [8,6,8,10,8,20,10,8,8]
# x = 8
# print('{}has occured {} times'.format(x,countX(list,x)))

# question:8
# Python Program to Find the Sum of Elements in a List using Recursion
# solution:
# def getSum(piece):
#     if len(piece)==0:
#         return 0
#     else:
#         return piece[0] + getSum(piece[1:])
# print (getSum([1,3,4,5,6,2]))

# question:9
# Python Program to Find the Length of a List using Recursion
# solution:
# def list_length(my_list):
#     if not my_list:
#         return 0
#     return 1 + list_length(my_list[1::2]) + list_length(my_list[2::2])
# my_list = [1,2,3,4,11,34,52,78]
# print("the list is:")
# print(my_list)
# print("the length of the string is:")
# print(list_length(my_list))

# question:10
# Python Program to Merge Two Lists and Sort it
# solution:
# def merge_list(list_1, list_2):
#     merged_list = list_1 + list_2
#     merged_list.sort()
#     return(merged_list)
# list_1 = [20,28,9,51,46,35]
# list_2 = [29,34,4,26,18,32]
# print("the first list is :")
# print(list_1)
# print("the second list is :")
# print(list_2)
# print(merge_list(list_1, list_2))

# question:11
# Python Program to Remove Duplicates from a List
# solution
# def remove(duplicate):
#     final_list = []
#     for num in duplicate:
#         if num not in final_list:
#             final_list.append(num)
#             return final_list
#         duplicates = [2,4,10,20,5,2,20,4]
#         print(remove(duplicate))

# question:12
# Python Program to Swap the First and Last Element in a List
# solution:
# def swapList(newList):
#     size = len(newList)
#     temp = newList[0]
#     newList[0] = newList[size - 1]
#     newList[size - 1] = temp
#     return newList
# newList = [12,35,9,56,24]
# print(swapList(newList))

# question:13
# Python Program to Sort a List According to the Second Element in Sublist
# solution:
# def sort(sub_li):
#     l = len(sub_li)
#     for i in range(0,1):
#         for j in range(0, l-i-1):
#             if (sub_li)[j][1] > sub_li[j + 1][1]):
#                 tempo = sub_li[j]
#                 sub_li[j]= sub_li[j +  1]
#                 sub_li[j + 1]= tempo
#     return sub_li
# sub_li =[['rishav', 10],['akash', 5],['ram', 20],['gaurav',15]]
# print(sort(sub_li))

# question:14
# Python Program to Return the Length of the Longest Word from the List of Words
# solution:
# def find_longest_word(words_list):
#     word_len = []
#     for n in words_list:
#         word_len.append((len(n), n))
#         word_len.sort()
#         return word_len[-1][0], word_len[-1][1]
#     result = find_longest_word(["PHP", "Exercises", "Backend"])
#     print("\nLongest word: ",result[1])
#     print("Length of the longest word: ",result[0])


# question:15
# Python Program to Find the Number Occurring Odd Number of Times in a List
# solution:
# int getOddOccurence(int arr[], int arr_size)
# {
#     for (int i = 0; i < arr_size; i++){
#         int count = 0;
#     for (int j = 0; j < arr_size; j++)
#     {
#        if (arr[i]) == arr[j])
#          count++;
#     }
#     if (count % 2 !=0)
#     return arr[i];
#     }
#     return -1;
# }
# int main()
# {
# int arr[] = {2,3,4,5,2,4,3,5,2,4,4,2};
# int n = size of(arr) / sizeof(arr[0]);
# count << getOddOccurance(arr,n);
# returnGenerate Random Numbers from 1 to 20 and Append Them to the List

# question:16
# Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List
# solution:
# import random
# print("Random integers between 0 and 9:")
# for i in range(4,11):
#     y = random.uniform(4,10)
#     print(y)

# question:17
# Python Program to Remove the ith Occurrence of the Given Word in a List
# solution:
# def RemoveIthword(lst, word, n):
#     newList = []
#     count = 0
#     for i in lst:
#         if(i == word):
#             count = count + 1
#             if(count !=N):
#                 newList.append(i)
#             else:
#                 newList.append(i)
#                 lst = newList
#                 if count == 0:
#                     print("Item not found")
#                 else:
#                     print("updated list is: ",lst)
#                     return newList
#                 list = ["geeks", "for" "geeks",]
#                 word = "geeks"
#                 N = 2
#                 RemoveIthword(list,word,N)

# question:18
# Python Program to Find the Cumulative Sum of a List
# solution:
# def Cumulative(lists):
#     cu_list = []
#     length = len(lists)
#     cu_list = [sum(lists[0:x:1]) for x in range(0,length+1)]
#     lists = [10,20,30,40,50]
#     print (Cumulative(lists))

# question:19
# Python Program to Find the Union of Two Lists
# solution:
# l1 = []
# num =int(input('Enter size of list 1: '))
# numbers1 = int(input('Enter any number:'))
# l1.append(numbers1)
# l2 = []
# num2 = int(input('Enter size of list 2:'))
# for i in range (num2):
#     numbers2  = int(input('Enter any number:'))
#     l2.append(numbers2)
#     union = list(set().union(11,12))
#     print('The union of two lists is:',union)

# question :20
# Python Program to Find the Intersection of Two Lists
# solution:
# def intersection(a, b):
#     return list(set(a) & set(b))
# def main():
#     alist=[]
#     blist=[]
#     n1= int(input("Enter number of element for list1:"))
#     n2=int(input("Enter number of elements for list2:"))
#     print("For list1:")
#     for x in range(0,n1):
#         element=int(input("Enter element" + str(x+1) + ":"))
#         alist.append(element)
#     print("For list2:")
#     for x in range(0,n2):
#         element=int(input("Enter element" + str(x+1) + ":"))
#         blist.append(element)
#     print("the intersection is :")
#     print(intersection(alist,blist))
# main()

# question:21
# Python Program to Flatten a List without using Recursion
# solution:
# def flatten(input_list):
#     result = []
#     stack = [input_list]
#     while stack:
#         current = stack.pop(-1)
#         if isinstance(current,list):
#             stack.extend(current)
#             result.append(current)
# result.reverse()
# return result
# ans = flatten(1)
# print(ans)

# question:22
# Python Program to Find the Total Sum of a Nested List Using Recursion
# solution:
# def sum_nestedlist(1):
#     for j in range(len(1)):
#         if type(1[j]) == list :
#             total+=sum_nestedlist(l[j])
#         else:
#             total += l[j]
#             return total
#         print(sum_nestedlist([1,2,3],[4,[5,6]],7]))


# question:23
# Python Program to Flatten a Nested List using Recursion
# solution:
# def flattenList(nestedList):
#     if not(bool(nestedlist)):
#         return nestedList
#     if isinstance(nestedList[0], list)
#     return flattenList(*nestedList[:1]) + flattenList(nestedList[1:])
# return nestedList[:1] + flattenList(nestedList[1:])
# nestedList = [[8, 9]], [10,11, 'geeks'], [13]]
# print('Nested List:\n', nestedList)
# print("Flattend List:\n",flattenList(nestedList))
