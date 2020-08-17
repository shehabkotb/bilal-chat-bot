import os
import sqlite3


DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

def db_connect(db_path=DEFAULT_PATH):
    conn = sqlite3.connect(db_path)
    return conn

def create_table(conn):
    c = conn.cursor()
    sql = """ CREATE TABLE IF NOT EXISTS user (
                                     username text NOT NULL PRIMARY KEY,
                                     password text NOT NULL,
                                     gender char NOT NULL
                                 ); """
    c.execute(sql)

create_table(db_connect())
