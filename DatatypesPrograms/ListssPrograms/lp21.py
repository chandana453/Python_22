#21.Python Program to Flatten a List without using Recursion
mylist = [1,2,[3,4,[5,6],7],[[[8,9],10]],[11,[12,13]]]

def flatten(my_list):
    final_list=[]
    stack=[my_list]
    while stack:
        current=stack.pop(-1) # pops the last element
        if(isinstance(current,list)):
            stack.extend(current)
        else:
            final_list.append(current)
    final_list.reverse()
    return final_list
ans =flatten(mylist)
print(ans)