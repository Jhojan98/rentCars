from connection import with_connection

@with_connection
def create_table_cliente(*args,**kwargs):
    conn = kwargs.pop('connection')
    cursor = conn.cursor()
    query  = f'''
        CREATE TABLE IF NOT EXISTS cliente (
            identification INTEGER PRIMARY_KEY UNIQUE,
            name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            address TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL
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
<<<<<<< HEAD
        fecha DATE NOT NULL,
        modelo TEXT NOT NULL
=======
        date DATE,
        model TEXT NOT NULL
>>>>>>> 83d885f19c3273d2ae7f8deb015c270d4ead2017
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
        model TEXT NOT NULL,
        plate TEXT NOT NULL,
        characteristics TEXT NOT NULL,
        aviailability BOOLEAN NOT NULL DEFAULT 1
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


def run_migration():
    # create_table_cliente()
    # create_table_pago()
    # create_table_vehiculo()
    # create_table_reserva()
    pass

if __name__ == "__main__":
    create_table_cliente()
    create_table_pago()
    create_table_vehiculo()
    create_table_reserva()
    