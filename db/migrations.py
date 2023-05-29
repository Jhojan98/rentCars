from connection import with_connection

@with_connection
def create_table_cliente(*args,**kwargs):
    conn = kwargs.pop('connection')
    cursor = conn.cursor()
    query  = f'''
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            identification INTEGER PRIMARY_KEY UNIQUE,
            username TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            address TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            is_admin BOOLEAN DEFAULT FALSE
    )
    '''
    cursor.execute(query)
    result = cursor.fetchone()
    return result

@with_connection
def create_table_pago(*args,**kwargs):
    conn = kwargs.pop('connection')
    cursor = conn.cursor()
    query  = f'''
    CREATE TABLE IF NOT EXISTS pago (
        date DATE,
        model TEXT NOT NULL
    )
    '''
    cursor.execute(query)
    result = cursor.fetchone()
    return result

@with_connection
def create_table_vehiculo(*args,**kwargs):
    conn = kwargs.pop('connection')
    cursor = conn.cursor()
    query  = f'''
    CREATE TABLE IF NOT EXISTS vehiculo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT NOT NULL,
        plate TEXT NOT NULL UNIQUE,
        characteristics TEXT NOT NULL,
        price TEXT NOT NULL,
        aviailability BOOLEAN NOT NULL DEFAULT 1,
        image_data BLOB
    )
    '''
    cursor.execute(query)
    result = cursor.fetchone()
    return result

@with_connection
def create_table_reserva(*args,**kwargs):
     conn = kwargs.pop("connection")
     cursor = conn.cursor()
     query  = '''
     CREATE TABLE IF NOT EXISTS reserva (

         cliente_id INTEGER NOT NULL,
         vehiculo_id INTEGER NOT NULL,
         pago_id INTEGER NOT NULL,
         arrive_date DATE NOT NULL,
         leave_date DATE NOT NULL,
         FOREIGN KEY (cliente_id) REFERENCES cliente(id),
         FOREIGN KEY (vehiculo_id) REFERENCES vehiculo(id),
         FOREIGN KEY (pago_id) REFERENCES pago(id)
     )
     '''
     cursor.execute(query)
     result = cursor.fetchone()
     return result


if __name__ == "__main__":
    create_table_cliente()
    create_table_pago()
    create_table_vehiculo()
    create_table_reserva()
    