from flask import Flask
import logging

logging.basicConfig(filename='debug.log',level=logging.DEBUG)

# logging.DEBUG('This is a DEBUG message')
# logging.INFO('This is a INFO message')
# logging.WARNING('This is a WARNING message')
# logging.ERROR('This is a error message')
# logging.CRITICAL('This is a critical message')

app=Flask(__name__)
@app.route('/login/<name>',methods=['POST', 'GET'])
def login(name):
    if(len(name)<2):
        logging.debug('Checking for name length')
        return 'Invalid name'
    elif name.isspace():
        logging.debug('Checking if name has a space')
        return 'Valid Name'
    elif name.isalpha():
        logging.debug('checking if name is a alphabet')
        return 'Valid Name'
    elif name.replace(' ','').isalpha():
        logging.debug('Checking for full name...')
        return 'Valid Name'
    else:
        logging.debug('Failed all checks..')
        return 'Invalid Name'

if __name__=='__main__':
    app.run()



    # app = Flask(__name__)
    #
    #
    # @app.route('/success/<name>')
    # def success(name):
    #     return 'welcome %s' % name
    #
    #
    # @app.route('/login', methods=['POST', 'GET'])
    # def login():
    #     if request.method == 'POST':
    #         user = request.form['nm']
    #         return redirect(url_for('success', name=user))
    #     else:
    #         user = request.args.get('nm')
    #         return redirect(url_for('success', name=user))
    #
    #
    # if __name__ == '__main__':
    #     app.run()
