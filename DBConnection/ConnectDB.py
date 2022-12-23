import psycopg2
from config import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()



# hostname ='localhost'
# database ='users'
# username = 'postgres'
# pwd = 'm'
# port_id = 5432
#
# import psycopg2
# import psycopg2.extras
#
# conn=psycopg2.connect(host=hostname,dbname=database,user=username,password=pwd,port=port_id,)
#
# #CURSOR allows to execute statements
# #cur=conn.cursor()   #creating a cursor by using connection
#
# cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor) #returns the
#
# #cur.execute("CREATE TABLE Student1 (ID SERIAL PRIMARY KEY, Name varchar);")
#
# #cur.execute("INSERT INTO Student1(name) VALUES(%s)",("Jack",)) # %s is a placeholder that will take name..if you use %s%s%s it will sequence of strings 3 times
#
# # cur.execute("SELECT * from Student1;")
#
# # print(cur.fetchall()) #helps in viewing everything
#
# cur.execute("SELECT * from Student1 where id = %s;",(2,))
#
# #(IF i want to reference them by the name of the column then use diff cursor by importing psycopg2.extras
#
# #make some changes in the connection object by passin cursor factory
#
#
# print(cur.fetchone()['id'])  # helps in fetching only one value
#
# conn.commit()  # this will comment whatever the statements we write
#
# cur.close()
#
# conn.close()






































# import psycopg2
#
#
# hostname= "localhost"
# username= "postgres"
# pwd= "m"
# port_id=5432
# database= "users"
#
# try:
#     conn=psycopg2.connect(
#         host=hostname,
#         dbname=database,
#         user=username,
#         password=pwd,
#         port=port_id,)
#     cur=conn.cursor()
#     # cur.execute("create table fruits(fruit_name varchar(10),fruit_color varchar(10));")
#     # cur.execute("alter table fruits add fruit_size int;")
#     cur.execute("alter table fruits rename to fruits_details;")
#     # cur.execute("select * from fruits;")
#     # print(cur.fetchall())
#     conn.commit()
#     # cur.close()
#     # conn.close()
# except Exception as error:
#     print(error)
# print(conn)