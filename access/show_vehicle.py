from dao.vehiculo import Vehicle

def show_vehicle_db():
    vehicle = Vehicle()
    data = vehicle.select_vehicle()
    return data  