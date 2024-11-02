import sqlite3


def initiate_db():
    connection = sqlite3.connect("Users.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL)
    ''')
    connection.commit()
    connection.close()


def add_user(username, email, age):
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM Users")
    total_us = cursor.fetchone()[0] + 1
    cursor.execute(f'''
        INSERT INTO Users VALUES('{total_us}', '{username}', '{email}', '{age}', '1000')
        ''')

    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    user_in = True
    check_usnam = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    if check_usnam.fetchone() is None:
        user_in = False
    return user_in


    connection.commit()
    connection.close()
