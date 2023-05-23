import sqlite3
def create_table_cliente(*args,**kwargs):
    connection = kwargs.pop('connection')
    cursor = connection.cursor()
    query  = '''
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL;
        dirección TEXT NOT NULL;
        teléfono TEXT NOT NULL;
        email TEXT NOT NULL;

    )
    '''
    cursor.execute(query)
    result = cursor.fetchone()
    return result


def create_table_pago(*args,**kwargs):
    connection = kwargs.pop('connection')
    cursor = connection.cursor()
    query  = '''
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha DATE;
        modelo TEXT NOT NULL;
    )
    '''
    cursor.execute(query)
    result = cursor.fetchone()
    return result


def create_table_vehiculo(*args,**kwargs):
    connection = kwargs.pop('connection')
    cursor = connection.cursor()
    query  = '''
    CREATE TABLE IF NOT EXISTS vehiculo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        modelo TEXT NOT NULL;
        caracteristicas TEXT NOT NULL;
        disponibilidad BOOLEAN NOT NULL DEFAULT 1;
    )
    '''

    cursor.execute(query)
    result = cursor.fetchone()
    return result


