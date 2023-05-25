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
            aviailability)
            VALUES (?,?,?,?)
        '''
        cursor.execute(query,
                                (self._model,
                                self._plate,
                                self._characteristics,
                                self._aviailability)
        )
        return cursor.lastrowid  
    
if __name__ == '__main__':
    ve = Vehicle()
    ve.data("hola", "123 fsd", "automatico",1)
    ve.insert_vehicle()
    # print("hola")