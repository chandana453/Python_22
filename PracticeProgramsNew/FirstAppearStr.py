#12.Write a Python program to find the first appearance of the substring 'not' and 'poor' from a
# given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string.
# Sample String: 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result: 'The lyrics is good!'
# 'The lyrics is poor!'

def FindAndReplace(st):

    notIndex=st.find("not")  #find() returns the index of a word
    poorIndex=st.find("poor")

    if poorIndex>notIndex and notIndex>0 and poorIndex>0:
        st=st.replace(st[notIndex:(poorIndex+4)],'good')
        return st
    else:
        return st

print(FindAndReplace("The lyrics is not that poor!"))
print(FindAndReplace("The lyrics is poor!"))
