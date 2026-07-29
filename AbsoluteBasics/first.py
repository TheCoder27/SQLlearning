import sqlite3

con = sqlite3.connect("people.db")

cur = con.cursor()

with open("first.sql", "r") as file:
    execution = file.read()

#if doing one command at a time, probably doesn't scale well.
execution = execution.split("-- break")

cur.execute(execution[0])
cur.execute(execution[1])

con.commit()
con.close()