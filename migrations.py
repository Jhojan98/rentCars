import sqlite3
def create_table_vehiculo(*args,**kwargs):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    create_table_users = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        nombre TEXT NOT NULL;
        dirección TEXT NOT NULL;
        teléfono TEXT NOT NULL;
        email TEXT NOT NULL;

    )
    '''
