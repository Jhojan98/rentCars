from db.connection import with_connection

class reservasDAO():
    def data(self,
            cliente_id,
            vehiculo_id,
            pago_id,
            arrive_date,
            leave_date):
        self._cliente_id = cliente_id
        self._vehiculo_id = vehiculo_id
        self._pago_id = pago_id
        self._arrive_data = arrive_date
        self._leave_date = leave_date
    
@with_connection
def insert_reserva(self, *args, **kwargs):
    conn = kwargs.pop('connection')
    cursor = conn.cursor()
    query = f'''
        INSERT INTO reserva
        (cliente_id,
        vehiculo_id,
        pago_id,
        arrive_date,
        leave_date)
        VALUES (?, ?, ?, ?, ?)
    '''
    cursor.execute(query,
                    (self._cliente_id,
                        self._vehiculo_id,
                        self._pago_id,
                        self._arrive_data,
                        self._leave_date)
    )
    return cursor.lastrowid
