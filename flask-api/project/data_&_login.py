from flask import Flask, request
from datetime import date
import psycopg2
from encode_decode import encode, decode
from last_login import last_login
import os

app = Flask(__name__)


@app.route("/user_data", methods=['GET', 'POST'])
def data():
    name = request.args.get("name")
    username = request.args.get("username")
    password = request.args.get("password")
    today = date.today()
    pre_login = date.today()

    # send values to DB
    connection = psycopg2.connect(user="postgres",
                                  password= os.environ['password'],
                                  host="localhost",
                                  port="5432",
                                  database="python")

    cursor = connection.cursor()

    values = ("'" + username + "'")

    query = """SELECT USERNAME FROM DATA WHERE USERNAME LIKE (%s);""" % values

    cursor.execute(query)

    exist = cursor.fetchall()

    if exist:
        return f"{username} already exists, please enter a different username"

    else:

        encrypt_pass = encode(password)

        user_data = {"name": name, "username": username, 'password': encrypt_pass, 'created_date': today,
                     'last_login': pre_login}

        values = ','.join("'" + str(x) + "'" for x in user_data.values())
        col = ','.join(str(x) for x in user_data.keys())

        sql = '''INSERT INTO DATA (%s)
               VALUES(%s);''' % (col, values)

        cursor.execute(sql)

    connection.commit()

    connection.close()
    cursor.close()

    return f"user {username} is added"


@app.route('/login', methods=['GET', 'POST'])
def verification():
    try:
        username = request.args.get("username")
        password = request.args.get("password")

        connection = psycopg2.connect(user="postgres",
                                      password="postgre0207",
                                      host="localhost",
                                      port="5432",
                                      database="python")

        cursor = connection.cursor()

        value = ("'" + username + "'")

        db_password = """SELECT PASSWORD,NAME FROM DATA WHERE USERNAME LIKE (%s) """ % value

        cursor.execute(db_password)
        connection.commit()

        user_data = cursor.fetchall()

        cursor.close()
        connection.close()

        de_password = decode(user_data[0][0])

        if de_password != password:
            return "incorrect password check again"
        else:
            last_login(username)
            return f"welcome back {user_data[0][1]}"

    except Exception as e:
        print(e)


app.run()
