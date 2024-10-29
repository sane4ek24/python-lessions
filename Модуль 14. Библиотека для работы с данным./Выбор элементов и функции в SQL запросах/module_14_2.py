import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")
cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

cursor.execute("DELETE FROM Users WHERE username = ?", ("User6",))

cursor.execute("SELECT COUNT (*) FROM Users")
count = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
sum = cursor.fetchone()[0]

print(sum / count)

connection.commit()
connection.close()
