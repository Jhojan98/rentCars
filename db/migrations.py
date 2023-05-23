import sqlite3
def create_table_cliente(*args,**kwargs):
    connection = kwargs.pop('connection')
    conn = kwargs.pop("database.db")
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
    conn = kwargs.pop("database.db")
    query  = '''
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha DATE;
        modelo TEXT NOT NULL;
    )
    '''
    cursor.execute(create_table_pago)
    result = cursor.fetchone()
    return result

def create_table_vehiculo(*args,**kwargs):
    connection = kwargs.pop('connection')
    conn = kwargs.pop("database.db")
    create_table_vehiculo  = '''
    CREATE TABLE IF NOT EXISTS vehiculo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        modelo TEXT NOT NULL;
        caracteristicas TEXT NOT NULL;
        disponibilidad BOOLEAN NOT NULL DEFAULT 1;
    )
    '''
    cursor.execute(create_table_vehiculo)
    result = cursor.fetchone()
    return result

def create_table_reserva(*args,**kwargs):
    conn = kwargs.pop("database.db")
    cursor = conn.cursor()
    query  = '''
        cliente_id INTEGER,
        FOREIGN KEY (vehiculo_id) REFERENCES vehiculo(id)
        fechaRecogida DATE,
        fechaEntrega DATE,
        pago_id INTEGER,
        FOREIGN KEY (pago_id) REFERENCES pago(id)
    )
    '''
    cursor.execute(query)
    result = cursor.fetchone()
    return result














