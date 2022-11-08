#14.Python Program to Return the Length of the Longest Word from the List of Words
def lenOfLongestWord(list1):
    max_length=len(list1[0]) #stores the length of first value
    temp=list1[0]   #stores the first value
    for i in list1:
       if len(i) > max_length:
           max_length=len(i)
           temp=i
    print("The longest word is",temp,"with length",max_length)

list1=["one","nine","two","three"]
lenOfLongestWord(list1)

#2nd approach

def longestwords(list1):
    final_list=[]
    for i in list1:
        final_list.append((len(i),i))
    final_list.sort()
    print("The word with the longest length is:", final_list[-1][1],
          " and length is ", len(final_list[-1][1]))


list1 = ["one", "two", "third", "four"]
longestwords(list1)


