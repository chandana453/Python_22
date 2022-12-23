import random
def pass_gen(len):
    try:
        alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
                      ,'A','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                      '~','!','@','#','$','%','^','&','*','|','>','<']
        pass_list =[]



        for num in range(len):
            char = random.choice(alpha_list)
            pass_list += char



        a = ("".join(pass_list))

        return a


    except Exception as e:
        return repr(e)

#
# import base64
#
# sample_string = "Harshith2234"
# sample_string_bytes = sample_string.encode("ascii")
#
# base64_bytes = base64.b64encode(sample_string_bytes)
# base64_string = base64_bytes.decode("ascii")
#
# print(f"Encoded string: {base64_string}")
#
# import base64
#
# base64_string = "SGFyc2hpdGgyMjM0"
# base64_bytes = base64_string.encode("ascii")
#
# sample_string_bytes = base64.b64decode(base64_bytes)
# sample_string = sample_string_bytes.decode("ascii")
#
# print(f"Decoded string: {sample_string}")