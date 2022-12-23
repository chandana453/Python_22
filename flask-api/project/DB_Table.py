import psycopg2


try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="postgre0207",
                                  host="localhost",
                                  port="5432",
                                  database="python")

    # Create a cursor to perform database operations
    cursor = connection.cursor()

    # SQL query to create a new table
    create_table = '''CREATE TABLE DATA 
        (ID SERIAL PRIMARY KEY,
        NAME VARCHAR(30),
        USERNAME VARCHAR(30),
        PASSWORD VARCHAR(60),
        CREATED_DATE VARCHAR(50),
        LAST_LOGIN VARCHAR(60))'''

    # Execute a command: this creates a new table
    cursor.execute(create_table)
    connection.commit()


except Exception as error:
    print("failed to connect to DB, ", error)


else:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
