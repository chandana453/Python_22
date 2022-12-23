#CONNECTING TO DATABASE AND LOADING EXCEL FILE TO DB
import pandas as pd
import self as self
# from sqlalchemy import create_engine
#
# username = 'postgres'
# password = 'm'
# hostname = 'localhost'
# port = 5432
# dbname = 'users'
#
# # A long string that contains the necessary Postgres login information
# try:
#  postgres_str = f'postgresql://{username}:{password}@{hostname}:{port}/{dbname}'
# except Exception as e:
#     print("Some Error OCCURED",e)
# #Create the connection
# conn = create_engine(postgres_str)

#Loading your pandas dataframe into your SQL db as a table
# df= pd.read_excel("/Users/mounika/Desktop/Sample.xlsx")
# df.to_sql('Sample', con=conn, index=False)

#
# def File_to_SQL():
#     df = pd.read_excel("input_data.xlsx")
#     df.to_sql('NEW_TABLE', con=conn, index=False)
#     return True
#
#
# File_to_SQL()


import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders


def sendmail(file):

        from_addr = 'mounika.adams@gmail.com'
        to_addr = 'aguypro@gmail.com'
        subject = 'I just sent this attachment from Python!'
        content = 'How neat is that?'

        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = subject
        body = MIMEText(content, 'plain')
        msg.attach(body)

        #filename = 'input_data.xlsx'
        filename=file
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(filename, "rb").read())
        #print(part)
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="data.xlsx"')
        msg.attach(part)

        smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
        smtp.login("mounika.adams@gmail.com", "ngcpsoqcpzzfdmei")
        smtp.sendmail(from_addr, to_addr, msg.as_string())
        smtp.quit()


sendmail('../PANDAS/input_data.xlsx')





