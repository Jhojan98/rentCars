from db.connection import with_connection

class Vehicle():

    def data(self, model, plate, characteristics, aviailability):
        self._model = model
        self._plate = plate
        self._characteristics = characteristics
        self._aviailability = aviailability

    
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
    