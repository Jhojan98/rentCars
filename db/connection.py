import sqlite3


def with_connection(fn):
    def wrapped(*args, **kwargs): #*args[] and **kwargs{:} allow you to pass multiple arguments or keyword arguments to a function
        conn = sqlite3.connect("gestion.db") # connection to the data base
        try:
            result = fn(*args, connection=conn, **kwargs) 
            """
            The function fn is called with the arguments and a connection 
            conn is passed to it using the named argument connection. 
            Depending on the implementation of the fn function, the 
            conn connection could be used within the function to perform 
            some operation on a database or other type of connection.
            """
        except:
            conn.roollback()
            """
            The call to conn.rollback() rolls back(retroceder) all operations performed in the current transaction, which means that 
            previously uncommitted (saved) changes to the database are rolled back and the previous state is restored.
            """
            print("Sqlite failed")
            raise
        else:
            conn.commit() #confirm changes
        finally:
            conn.close() #close connection
        return result
    return wrapped