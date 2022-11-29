import psycopg2

# Psycopg is a PostgreSQL adapter for the Python programming language


hostname= "localhost"
username= "postgres"
pwd= "ravichandra"
port_id=5432
database= "chandra"

try:
    conn=psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id,)
    cur=conn.cursor()
    # cur.execute("create table fruits(fruit_name varchar(10),fruit_color varchar(10));")
    # cur.execute("alter table fruits add fruit_size int;")
    # cur.execute("RENAME table fruits TO fruits_details;")
    cur.execute("select * from fruits;")
    print(cur.fetchall())
    conn.commit()
    # cur.close()
    # conn.close()
except Exception as error:
    print(error)
print(conn)