import sqlite3


def with_connection(fn):
    def wrapped(*args, **kwargs): #*args[] and **kwargs{:} allow you to pass multiple arguments or keyword arguments to a function
        conn = sqlite3.connect("getion.db") # connection to the data base
        try:
            result = fn(*args, connection=conn, **kwargs)
        except:
            conn.roollback()
            print("Sqlite failed")