import psycopg2
from datetime import date


def last_login(username):
    connection = psycopg2.connect(user="postgres",
                                  password="postgre0207",
                                  host="localhost",
                                  port="5432",
                                  database="python")

    cursor = connection.cursor()

    today = date.today()

    value = ("'" + username + "'")

    to = ("'" + str(today) + "'")

    login = """UPDATE DATA SET last_login = %s  where username like %s;""" % (to, value)

    cursor.execute(login)
    connection.commit()

    connection.close()
    cursor.close()
