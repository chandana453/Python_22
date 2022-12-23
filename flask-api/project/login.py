from flask import Flask, request, jsonify
import psycopg2
from encode_decode import decode
from datetime import date
from last_login import last_login

app = Flask(__name__)


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
