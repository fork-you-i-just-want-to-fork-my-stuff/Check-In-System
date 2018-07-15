import sqlite3 as lite
import sys

clients = (
    ("James", 1),
    ("Dianne", 1),
    ("Mark", 3),
    ("Linda", 5)
)

con = lite.connect('clients.db')

with con:
    current = con.cursor()
    current.execute("DROP TABLE IF EXISTS clients")
    current.execute("CREATE TABLE clients(client_name TEXT, haircut_pref INT)")
    current.executemany("INSERT INTO clients VALUES(?,?)", clients)
