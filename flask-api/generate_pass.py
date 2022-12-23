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