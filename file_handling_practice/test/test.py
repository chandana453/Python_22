data=["python","data","cream"]
#O/p: ["py","th","on","da","ta","cr","ea","am"]



def len_slice(data,slice_len):
    str = "".join(data)
    o_l = []
    str_len = len(str)

    for i in range(0, str_len, slice_len):
        # print(str[i : i + slice_len])
        o_l.append(str[i : i + slice_len])

    return o_l

slice_len = int(input("enter the len : "))

print(len_slice(data,slice_len))