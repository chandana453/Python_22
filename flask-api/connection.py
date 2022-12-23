import sqlalchemy
from sqlalchemy import create_engine as ce
import os




#create engine ("postgresql://user=postgres:password=postgre0207@host=localhost:port=5432/db_name = python")

s = ce("postgresql://postgres:postgre0207@localhost:5432/python")

conn = s.connect()


q = "select * from data"

# Connection.execute() method is called to execute a SQL statement and here result is an object
result = conn.execute(q)


data = result.fetchall()
for i in data:
    print(i)

conn.close()