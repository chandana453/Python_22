'''
Please write a binary search function which searches an item in a
sorted list. The function should return the index of element to be
searched in the list.
Hints:
solution:
'''
import math
def bin search(li,element):
      bottom =0
      top =len(li)-1
      index =-1
      while top>=bottom and index==-1:
          mid =int[mid]==element:
          if li[mid]=mid
              index = mid
          elif lil[mid]>element:
              top = mid-1
          else:
                 bottom =mid+1

      return index
li=[2,5,7,9,11,17,222]
print(bin search(li,11))
print(bin search(11,12))
