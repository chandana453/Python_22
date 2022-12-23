#14.Write a Python program to count the number of strings where the string length is 2 or more and the first
# and the last characters are the same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result: 2

def CountStrings(list1):
    count=0
    for word in list1:
      if len(word)>=2 and word[0]==word[-1]:
         count+=1

    return count

List1=['xyz', 'aba','11','bob','929','sam']
print(CountStrings(List1))