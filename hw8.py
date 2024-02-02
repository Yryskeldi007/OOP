import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = False
    try:
        conn = sqlite3.connect(db_file)
    except Error:
        print(Error)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error:
        print(Error)

def create_student(conn, student):
    sql = "INSERT INTO student (full_name, marks, hobby, age) VALUES (?,?,?,?)"
    try:
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error:
        print(Error)

def read(conn):
    try:
        sql = "SELECT * FROM student"
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for i in rows:
            print(i)
    except Error:
        print(Error)

def update_name_age(conn, student_id, name, age):
    sql = "UPDATE student SET full_name=?, age=? WHERE id=?"
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (name, age, student_id))
        conn.commit()
    except Error:
        print(Error, '104')

def delete_student(conn, student_id):
    sql = 'DELETE FROM student WHERE id=?'
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (student_id,))
        conn.commit()
    except Error:
        print(Error)

sql_create_table = '''CREATE TABLE IF NOT EXISTS student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR(50) NOT NULL,
marks INTEGER NOT NULL DEFAULT 0,
hobby TEXT DEFAULT NULL,
age DATE NOT NULL
);'''

database = r'user.db'
connection = create_connection(database)
if connection is not None:
    create_table(connection, sql_create_table)
    create_student(connection, ('beka3', 10, 'football', 20))
    create_student(connection, ('name', 19, 'reading', 10))
    create_student(connection, ('beka1', 100, 'drawing', 50))
    create_student(connection, ('beka2', 0, 'programming', 20))
    update_name_age(connection, 1, 'AMINE', 1000)

    print("Before Deletion:")
    read(connection)

    delete_student(connection, 2)

    print("\nAfter Deletion:")
    read(connection)

    print('всё работает')
