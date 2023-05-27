from db.connection import with_connection

class ClienteDAO():
    def data(self,
            identification,
            name,
            last_name,
            address,
            phone,
            email):
        self._identificacion = identification
        self._name= name
        self._last_name= last_name
        self._address= address
        self._phone= phone
        self._email= email

    @with_connection
    def insert_estudiante(self, *args, **kwargs):
        conn = kwargs.pop('connection')
        cursor = conn.cursor()
        query = f'''
            INSERT INTO cliente
            (identification,
            name,
            last_name,
            address,
            phone,
            email)
            VALUES(?,?,?,?,?,?)
        '''
        cursor.execute(query,
                                (self._identificacion,
                                self._name,
                                self._last_name,
                                self._address,
                                self._phone,
                                self._email)
        )
        return cursor.lastrowid


