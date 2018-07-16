import sqlite3 as lite
import sys

def get_client_db(user = None):
    #if you want the whole database returned
    client_db = lite.connect('clients.db')
    if user == None:
        current = client_db.execute('SELECT client_name, haircut_pref from clients')
        clients = [dict(client_name=row[0], haircut_pref=row[1]) for row in current.fetchall()]
        client_db.close()
        return clients

    if user != None:
        #TODO: Make this return user of a given name
        #return
        q = None

def get_queue_db():
    queue_db = lite.connect('queue.db')
    current = queue_db.execute('SELECT client_name, line_location from queue')
    clients = [dict(client_name=row[0], line_location=row[1]) for row in current.fetchall()]
    queue_db.close()
    return clients


if __name__ == "__main__":
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
