import sqlite3
def create_table_cliente(*args,**kwargs):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    create_table_cliente  = '''
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL;
        dirección TEXT NOT NULL;
        teléfono TEXT NOT NULL;
        email TEXT NOT NULL;

    )
    '''
def create_table_pago(*args,**kwargs):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    create_table_pago  = '''
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha DATE;
        modelo TEXT NOT NULL;
    )
    '''