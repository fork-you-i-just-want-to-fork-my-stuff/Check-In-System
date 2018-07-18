import sqlite3 as lite
import sys

def get_client_db(user = None):
    #if you want the whole database returned
    client_db = lite.connect('clients.db')
    if user == None:
        current = client_db.execute('SELECT client_first_name, client_last_name, phone_number, postal_code, email from clients')
        clients = [dict(client_first_name=row[0], client_last_name=row[1],phone_number=row[2], postal_code=row[3], email=row[4]) for row in current.fetchall()]
        client_db.close()
        return clients

    if user != None:
        #TODO: Make this return user of a given name
        #return
        q = None

if __name__ == "__main__":
    # Creating test data for client db
    clients = (
        ("James","McTavish", "(403)123-1234", "T2Z 3l9", "bazinga@gmail.com"),
        ("Dianne", "Lawsorman", "(403)692-1234", "T2Z 5l9", "ww@gmail.com"),
        ("Mark", "Robertson", "(403)616-1234", "R3Z 3l9", "sdaklfj@gmail.com"),
        ("Linda", "Saursour", "(403)231-1234", "Y4P 3l9", "asdlfkyhqw@gmail.com")
    )

    #seting up client database

    con = lite.connect('clients.db')
    with con:
        current = con.cursor()
        current.execute("DROP TABLE IF EXISTS clients")
        current.execute("CREATE TABLE clients(client_first_name TEXT, client_last_name TEXT, phone_number TEXT, postal_code TEXT, email TEXT)")
        current.executemany("INSERT INTO clients VALUES(?,?,?,?,?)", clients)
