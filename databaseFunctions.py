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

def add_user(conn, user_data):
    sql = ''' INSERT INTO user(username,password,gender)
              VALUES("{}","{}","{}") '''.format(user_data['username'],user_data['password'],user_data['gender'])
    cur = conn.cursor()
    cur.execute(sql, user_data)
    return cur.lastrowid

def get_user(conn, username,password):
    sql = ' SELECT * from `user` WHERE username = "{}" and password = "{}"'.format(username, password)
    cur = conn.cursor()
    record = cur.execute(sql)
    user = record.fetchone()
    if user is None:
        return False
    else:
        return user

def check_user(conn, username):
    sql = ' SELECT * from `user` WHERE username = "{}" '.format(username)
    cur = conn.cursor()
    record = cur.execute(sql)
    user = record.fetchone()
    if user is None:
        return False
    else:
        return user