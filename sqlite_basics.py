import sqlite3
from sqlite3 import Error
import os


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return

def execute_query(conn, sql_query):
    try:
        c = conn.cursor()
        c.execute(sql_query)
        conn.commit()
    except Error as e:
        print(e)

 


sql_query = """
        CREATE TABLE IF NOT EXISTS Probes(
            pk_id integer PRIMARY KEY,
            msisdn text NOT NULL,
            success integer NOT NULL,
            dt datetime NOT NULL
        ); """
