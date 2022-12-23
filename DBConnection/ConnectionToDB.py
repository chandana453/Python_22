import psycopg2.extras
import psycopg2

hostname ='localhost'
database ='users'
username = 'postgres'
pwd = 'm'
port_id = 5432
conn = None

try:
    with psycopg2.connect(
             host=hostname,
             dbname=database,
             user=username,
             password=pwd,
             port=port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("DROP TABLE IF EXISTS employee")

            create_script ="CREATE TABLE IF NOT EXISTS employee(id int PRIMARY KEY,name varchar(40) NOT NULL,Salary int,dept_id varchar(30))"

            cur.execute(create_script)

            insert_script ='INSERT INTO employee(id, name, salary, dept_id) VALUES( % s, % s. % s, % s)'


            insert_values = [(1,'John', 12000, 'D1'), (2,'Jos', 15000, 'D1'), (3,'Adam', 20000, 'D2')]

            for record in insert_values:
               cur.execute(insert_script, record)

            update_script ='UPDATE employee SET salary = salary + (salary * 0.5)'
            cur.execute(update_script)

            delete_script ='DELETE FROM employee where name ="%s"'
            delete_record = ('James')
            cur.execute(delete_script, delete_record)

            cur.execute('SELECT * FROM EMPLOYEE')

            for record in cur.fetchall():
                 print(record['name'], record['salary'])


except Exception as error:
    print(error)

finally:
    if conn is not None:
     conn.close()











# df1 = pd.read_csv("/Users/mounika/PycharmProjects/PANDAS/pokemon_data.txt")
#
# hostname = 'localhost'
# database = 'users'
# username = 'postgres'
# pwd = 'm'
# port_id = 5432

import psycopg2
# import psycopg2.extras
#
# conn = psycopg2.connect(host=hostname, dbname=database, user=username, password=pwd, port=port_id, )
#
# cur = conn.cursor()

# cur.execute("CREATE TABLE Pokemon (Num SERIAL PRIMARY KEY, Name varchar, Type1 varchar, Type2 varchar, HP varchar, Attack varchar,Defense varchar, Sp_Atk varchar, Sp_Def varchar, Speed int, Generation int, Legendary varchar);")

# cur.execute(" ALTER TABLE Pokemon RENAME COLUMN num to '#'; ")


# creating column list for insertion
# cols = "','".join([str(i) for i in df1.columns.tolist()])
# # Insert DataFrame records one by one.
# for i, row in df1.iterrows():
#     sql = "INSERT INTO Pokemon ('" + cols + "') VALUES (" + "%s," * (len(row) - 1) + "%s)"
#     cur.execute(sql, tuple(row))
#     # the connection is not autocommitted by default, so we must commit to save our # changes
#     conn.commit()

# cur.execute("SELECT * from Student1;")

# print(cur.fetchall()) #helps in viewing everything

# cur.execute("SELECT * from Student1 where id = %s;",(2,))

# (IF i want to reference them by the name of the column then use diff cursor by importing psycopg2.extras

# make some changes in the connection object by passin cursor factory


# print(cur.fetchone()['id'])  # helps in fetching only one value

# conn.commit()  # this will comment whatever the statements we write

# cur.close()
#
# conn.close()