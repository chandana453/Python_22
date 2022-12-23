import json
from flask import Flask,jsonify,request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import os
from sqlalchemy import create_engine as ce
import pandas as pd
import timeit
from datetime import datetime

mysetup = "from math import sqrt"
mycode = '''
def example():
    mylist = []
    for x in range(100):
        mylist.append(sqrt(x))
'''

app = Flask(__name__)
@app.route('/mail',methods=['POST'])
def sendmail():
        # loading dataframe to sql
        postgres_str = f'postgresql://postgres:m@localhost:5432/users'
        conn = ce(postgres_str)
        df = pd.read_excel('/Users/mounika/PycharmProjects/TASKS/example.xlsx')
        df.to_sql('example', con=conn, index=False)
        exec_time = timeit.timeit(stmt=mycode,setup=mysetup,number=1000000) * 10 ** 3
        if exec_time:
          #return jsonify({ "message": "Success"})

          try:
            file = request.args.get('file_name')
            path=request.args.get('file_path')
            file="example.xlsx"
            msg = MIMEMultipart()
            msg['From'] = os.environ["from_addr"]
            msg['To'] = os.environ['to_addr']
            msg['Subject'] = os.environ['subject']
            body = MIMEText(os.environ['content'], 'plain')
            msg.attach(body)
            filename = file
            part = MIMEBase('application', "octet-stream")
            os.chdir(path)
            part.set_payload(open(filename, "rb").read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename={}'.format(filename))
            msg.attach(part)

            smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            smtp.login(os.environ["from_addr"], os.environ["Password"])
            smtp.sendmail(os.environ["from_addr"], os.environ["to_addr"], msg.as_string())
            smtp.quit()

            return jsonify(({"filename":file , "message": "Success","response_cose":200}))
          except Exception as e:
            return jsonify({"filename":file , "message": "Failed","error":repr(e)})



#print(sendmail())
if __name__=='__main__':
    app.run()


