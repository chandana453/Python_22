from flask import Flask,request
#
# app =Flask(__name__)
#
# @app.route('/potato')
# def name():
#     return "HARSHITH"
#
# app.run()


#
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def root():
#     return "it's my roor page"
#
# @app.route('/potato')
# def name():
#     return 'my name is harshith'
#
# @app.route('/who')
# def made_by():
#     return "i did it!!!"
#
#
#
# app.run()


app=Flask(__name__)


@app.route('/method',methods=['GET','POST'])
def method():
    if request.method == 'POST':
        return "it's post!!"
    else:

        return "it's get"



app.run()











