from db.connection import with_connection

class ClienteDAO():
    def data(self,
            identification,
            username,
            name,
            last_name,
            address,
            phone,
            email,
            password):
        self._identificacion = identification
        self._username = username
        self._name= name
        self._last_name= last_name
        self._address= address
        self._phone= phone
        self._email= email
        self._password = password

    @with_connection
    def insert_client(self, *args, **kwargs):
        conn = kwargs.pop('connection')
        cursor = conn.cursor()
        query = f'''
            INSERT INTO cliente
            (identification,
            username,
            name,
            last_name,
            address,
            phone,
            email,
            password)
            VALUES(?,?,?,?,?,?,?,?)
        '''
        cursor.execute(query,
                                (self._identificacion,
                                self._username,
                                self._name,
                                self._last_name,
                                self._address,
                                self._phone,
                                self._email,
                                self._password)
        )
        return cursor.lastrowid
    

    @with_connection
    def select_client(self, username, password, *args, **kwargs):
        conn = kwargs.pop('connection')
        cursor = conn.cursor()
        query = f'''
            SELECT identification,
                username,
                name,
                last_name,
                address,
                phone,
                email,
                password
            FROM cliente
            WHERE username = ? AND password = ?
        '''
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        return result


