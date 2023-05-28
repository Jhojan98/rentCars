from db.connection import with_connection

class Vehicle():

    def data(self, model, plate, characteristics, aviailability, image):
        self._model = model
        self._plate = plate
        self._characteristics = characteristics
        self._aviailability = aviailability
        self._image_data = image

    
    @with_connection
    def insert_vehicle(self, *args, **kwargs):
        conn = kwargs.pop('connection')
        cursor = conn.cursor()
        query = f'''
        INSERT INTO vehiculo
            (model,
            plate,
            characteristics,
            aviailability,
            image_data)
            VALUES (?,?,?,?,?)
        '''
        cursor.execute(query,
                                (self._model,
                                self._plate,
                                self._characteristics,
                                self._aviailability,
                                self._image_data)
        )
        return cursor.lastrowid  


    @with_connection
    def select_vehicle(self, *args, **kwargs):
        conn = kwargs.pop('connection')
        cursor = conn.cursor()
        query = f'''
        SELECT model,
            plate,
            characteristics,
            aviailability,
            image_data
        FROM vehiculo
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    