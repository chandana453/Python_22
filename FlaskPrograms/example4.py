from flask import Flask
app=Flask(__name__)

@app.route('/python')
def hello_python():
    return 'PYTHON'

@app.route('/flask/')
def hello_flask():
    return 'FLASK'

if __name__=='__main__':
    app.run()