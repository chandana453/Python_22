from flask import Flask, request
from datetime import date
import psycopg2
from encode_decode import encode

app = Flask(__name__)


@app.route("/user_data", methods=['GET', 'POST'])
def data():
    name = request.args.get("name")
    username = request.args.get("username")
    password = request.args.get("password")
    today = date.today()
    last_login = date.today()

    # send values to DB
    connection = psycopg2.connect(user="postgres",
                                  password="postgre0207",
                                  host="localhost",
                                  port="5432",
                                  database="python")

    cursor = connection.cursor()

    values = ("'" + username + "'")

    query = """SELECT USERNAME FROM DATA WHERE USERNAME LIKE (%s);""" % values

    cursor.execute(query)

    exist = cursor.fetchall()

    if exist:
        return f"user {username} already exists"

    else:

        encrypt_pass = encode(password)

        user_data = {"name": name, "username": username, 'password': encrypt_pass, 'created_date': today, 'last_login': last_login }

        values = ','.join("'" + str(x) + "'" for x in user_data.values())
        col = ','.join(str(x) for x in user_data.keys())

        sql = '''INSERT INTO DATA (%s)
               VALUES(%s);''' % (col, values)

        cursor.execute(sql)

    connection.commit()

    connection.close()
    cursor.close()
    return f"user {username} is added"


app.run()
