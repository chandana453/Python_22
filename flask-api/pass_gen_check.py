import random
from flask import Flask,request,jsonify
from test import pass_gen

app = Flask(__name__)


'''how to get the pass_list which is in pass_gen end point into the pass_check end_point'''
@app.route('/pass_check')
def char_check():
    len = int(request.args.get('length'))
    pass_list = pass_gen(len)
    list_case = {'is_upper': 0,
                'is_lower': 0,
                 'is_spl': 0}
    for char in pass_list:
        if char.isupper():
            list_case['is_upper'] += 1
        elif char.islower():
            list_case['is_lower'] += 1
        else:
            list_case['is_spl'] += 1

    output =[]
    for i in list_case:
        output.append(f"the new password has {list_case[i]} {i} case letters, ")
    output="\n".join(output)
    return jsonify({"output":output,"generated_password":pass_list})


app.run()
