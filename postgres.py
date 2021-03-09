import psycopg2
import os 

host = "localhost"
dbname = "postgres"
user = "tiphaineminguet"
password = "123"

conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS MaTable (ID INT);")
    conn.commit()

def insert_info(): 
    cursor.execute("INSERT INTO MaTable VALUES (%s)", ("1"))
    conn.commit()

create_table()
insert_info()


