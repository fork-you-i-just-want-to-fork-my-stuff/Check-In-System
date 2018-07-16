import sqlite3 as lite
import sys

# Creating test data for client db
clients = (
    ("James", 1),
    ("Dianne", 1),
    ("Mark", 3),
    ("Linda", 5)
)

#seting up client database

con = lite.connect('clients.db')
with con:
    current = con.cursor()
    current.execute("DROP TABLE IF EXISTS clients")
    current.execute("CREATE TABLE clients(client_name TEXT, haircut_pref INT)")
    current.executemany("INSERT INTO clients VALUES(?,?)", clients)

# Creating test data for queue db
queue = (
    ("James", 1),
    ("Dianne", 2),
    ("Mark", 3),
    ("Linda", 4)

#seting up queue database

)
con = lite.connect('queue.db')
with con:
    current = con.cursor()
    current.execute("DROP TABLE IF EXISTS queue")
    current.execute("CREATE TABLE queue(client_name TEXT, line_location INT)")
    current.executemany("INSERT INTO queue VALUES(?,?)", queue)
