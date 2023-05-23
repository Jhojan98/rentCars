import sqlite3
def create_table_cliente(*args,**kwargs):
    connection = kwargs.pop('connection')
    cursor = connection.cursor()
<<<<<<< Updated upstream
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

=======
    create_table_cliente  = '''
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL;
            dirección TEXT NOT NULL;
            teléfono TEXT NOT NULL;
            email TEXT NOT NULL;
    )
    '''
    cursor.execute(create_table_cliente)
    result = cursor.fetchone()
    return result 
>>>>>>> Stashed changes

def create_table_pago(*args,**kwargs):
    connection = kwargs.pop('connection')
    cursor = connection.cursor()
<<<<<<< Updated upstream
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

=======
    create_table_pago  = '''
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha DATE;
            modelo TEXT NOT NULL;
    )
    '''
    cursor.execute(create_table_pago)
    result = cursor.fetchone()
    return result 
>>>>>>> Stashed changes

def create_table_vehiculo(*args,**kwargs):
    connection = kwargs.pop('connection')
    cursor = connection.cursor()
<<<<<<< Updated upstream
    query  = '''
    CREATE TABLE IF NOT EXISTS vehiculo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        modelo TEXT NOT NULL;
        caracteristicas TEXT NOT NULL;
        disponibilidad BOOLEAN NOT NULL DEFAULT 1;
=======
    create_table_vehiculo  = '''
        CREATE TABLE IF NOT EXISTS vehiculo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo TEXT NOT NULL;
            caracteristicas TEXT NOT NULL;
            disponibilidad BOOLEAN NOT NULL DEFAULT 1;
>>>>>>> Stashed changes
    )
    '''
    cursor.execute(create_table_vehiculo)
    result = cursor.fetchone()
    return result 

    cursor.execute(query)
    result = cursor.fetchone()
    return result


