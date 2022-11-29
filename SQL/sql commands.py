import psycopg2
hostname= "localhost"
username= "postgres"
pwd= "ravichandra"
port_id=5432
database= "sekhar"
try:
    conn=psycopg2.connect(
        host=hostname,
        user=username,
        password=pwd,
        port=port_id,
        dbname=database)
    cur=conn.cursor()
    # cur.execute("create table SQL_COMMANDS (DDL_Commands varchar(10),DML_Commands varchar(10))")
    # cur.execute("alter table sql_commands add DCL_Commands varchar(10)")
    # cur.execute("alter table sql_commands add TCL_Commands varchar(10)")
    # cur.execute("insert into sql_commands (ddl_commands,dml_commands,dcl_commands,tcl_commands) values ('create','insert','grant','commit');")
    # cur.execute("insert into sql_commands (ddl_commands,dml_commands,dcl_commands,tcl_commands) values ('alter','update','revoke','rollback');")
    # cur.execute("insert into sql_commands (ddl_commands,dml_commands,dcl_commands,tcl_commands) values ('drop','delete','none','save_print')")
    cur.execute("select * from SQL_COMMANDS")
    conn.commit()
    print(cur.fetchall())
    cur.close()
    conn.close()
except Exception as error:
    print(error)

print(conn)
#
# psycopg2.connect(
#         host=hostname,
#         dbname=database,
#         user=username,
#         password=pwd,
#         port=port_id,)