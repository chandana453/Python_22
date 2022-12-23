hostname ='localhost'
database ='users'
username = 'postgres'
pwd = 'm'
port_id = 5432

import psycopg2
import psycopg2.extras

conn=psycopg2.connect(host=hostname,dbname=database,user=username,password=pwd,port=port_id,)

#CURSOR allows to execute statements
#cur=conn.cursor()   #creating a cursor by using connection

cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor) #returns the

#cur.execute("CREATE TABLE Student1 (ID SERIAL PRIMARY KEY, Name varchar);")

#cur.execute("INSERT INTO Student1(name) VALUES(%s)",("Jack",)) # %s is a placeholder that will take name..if you use %s%s%s it will sequence of strings 3 times

# cur.execute("SELECT * from Student1;")

# print(cur.fetchall()) #helps in viewing everything

cur.execute("SELECT * from Student1 where id = %s;",(2,))

#(IF i want to reference them by the name of the column then use diff cursor by importing psycopg2.extras

#make some changes in the connection object by passin cursor factory


print(cur.fetchone()['id'])  # helps in fetching only one value

conn.commit()  # this will comment whatever the statements we write

cur.close()

conn.close()