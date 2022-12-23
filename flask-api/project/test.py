import psycopg2
import json
import pandas as pd
from encode_decode import decode
#
# connection = psycopg2.connect(user="postgres",
#                               password="postgre0207",
#                               host="localhost",
#                               port="5432",
#                               database="python")
#
# cursor = connection.cursor()
#
#
#
# values = ("'" + name + "'"  )
# query = """select name from data where name like (%s);""" %(values)
# cursor.execute(query)
#
#
# exist = cursor.fetchall()
#
# if exist:
#     print("user already exists")
# else:
#     print("ok")
#
# connection.commit()
#
#
# connection.close()
# cursor.close()
# #
#
#
# d = pd.read_json(json)
# df = pd.DataFrame(d)
# print(df)


# dict={
#     "created_date": "Wed, 07 Dec 2022 00:00:00 GMT",
#     "dob": "27-03-1999",
#     "name": "harshith",
#     "password": "idinene",
#     "username": "harshu1"
# }
#
#
# df =pd.DataFrame.from_dict(dict,orient='index')
# print(d)

# username = "harshu007"
#
# connection = psycopg2.connect(user="postgres",
#                               password="postgre0207",
#                               host="localhost",
#                               port="5432",
#                               database="python")
# cursor = connection.cursor()
#
# value = ("'" + username + "'")
#
# db_password = """SELECT PASSWORD,name FROM DATA WHERE USERNAME LIKE (%s) """ % (value)
#
# cursor.execute(db_password)
#
# en_password = cursor.fetchall()
# de_password = decode(en_password[0][0])
#
# connection.close()
# cursor.close()



#
# from flask import Flask, request
# from datetime import date
# import psycopg2
# from encode_decode import encode
#
# app = Flask(__name__)
#
#
# @app.route("/user_data", methods=['GET', 'POST'])
# def data():
#     name = request.args.get("name")
#     username = request.args.get("username")
#     password = request.args.get("password")
#     today = date.today()
#     last_login = date.today()
#
#     # send values to DB
#     connection = psycopg2.connect(user="postgres",
#                                   password="postgre0207",
#                                   host="localhost",
#                                   port="5432",
#                                   database="python")
#
#     cursor = connection.cursor()
#
#     values = ("'" + username + "'")
#
#     query = """SELECT USERNAME FROM DATA WHERE USERNAME LIKE (%s);""" % values
#
#     cursor.execute(query)
#
#     exist = cursor.fetchall()
#
#     if exist:
#         return f"user {username} already exists"
#
#     else:
#
#         encrypt_pass = encode(password)
#
#         user_data = {"name": name, "username": username, 'password': encrypt_pass, 'created_date': today, 'last_login': last_login }
#
#         values = ','.join("'" + str(x) + "'" for x in user_data.values())
#         col = ','.join(str(x) for x in user_data.keys())
#
#         sql = '''INSERT INTO DATA (%s)
#                VALUES(%s);''' % (col, values)
#
#         cursor.execute(sql)
#
#     connection.commit()
#
#     connection.close()
#     cursor.close()
#     return f"user {username} is added"
#
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def verification():
#     try:
#         username = request.args.get("username")
#         password = request.args.get("password")
#
#         connection = psycopg2.connect(user="postgres",
#                                       password="postgre0207",
#                                       host="localhost",
#                                       port="5432",
#                                       database="python")
#
#         cursor = connection.cursor()
#
#         value = ("'" + username + "'")
#
#         db_password = """SELECT PASSWORD,NAME FROM DATA WHERE USERNAME LIKE (%s) """ % value
#
#         cursor.execute(db_password)
#         connection.commit()
#
#         user_data = cursor.fetchall()
#
#         cursor.close()
#         connection.close()
#
#         de_password = decode(user_data[0][0])
#
#         if de_password != password:
#             return "incorrect password check again"
#         else:
#             # last_login(username)
#             cursor.close()
#             connection.close()
#
#
#             return f"welcome back {user_data[0][1]}"
#
#     except Exception as e:
#         print(e)
#
# app.run()
#
#
#
# list1 = ['ten','twenty','thirty']
# list2 = [10,20,30]
#
# x = dict(zip(list1,list2))
# print(x)


# t = ("orange",[10,20,30],(5,15,25))
#
# print(t[1][1])



# s = "hi my name is harshith".split()
#
# l = [len(x) for x in s ]
# print(dict(zip(s,l)))



class a():
    def f1(self,m1):
        print("hi")

    def f1(self,m,n):
        print("hello")

obj = a()

obj.f1(1)
# obj.f1(1,2)