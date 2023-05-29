from dao.vehiculo import Vehicle

def show_vehicle_db():
    vehicle = Vehicle()
    data = vehicle.select_vehicle()
    return data  

def update_vehicle_db(aviability,plate):
    vehicle = Vehicle()
    vehicle.update_vehicle(aviability,plate)
