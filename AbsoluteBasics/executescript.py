import sqlite3

con = sqlite3.connect("people.db")

cur = con.cursor()

with open("first.sql", "r") as file:
    execution = file.read()

cur.executescript(execution)

cur.execute("SELECT * from persons where age > 20")

result = cur.fetchall()
print(result)

con.commit()
con.close()