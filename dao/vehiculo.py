from db.connection import with_connection


class Vehicle():

    def __init__(self, model, plate, characteristics, aviailability):
        self._model = model
        self._plate = plate
        self._characteristics = characteristics
        self._aviailability = aviailability

    
    @with_connection
    def insert_vehicle(self, *args, **kwargs):
        conn = kwargs.pop('connoection')
        cursor = conn.cursor()
        query = f'''
            (model,
            plate,
            characteristics,
            aviailability)
            VALUES (?,?,?,?)
        '''
        cursor.execute(query,
                       (self._model,
                        self._plate,
                        self._characteristics,
                        self._aviailability,
                        )
        )
        return cursor.lastrowid   