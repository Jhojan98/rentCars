from flask import request, render_template
from dao.vehiculo import Vehicle
import base64

def handle_cars(form):
    model = form['model']
    plate = form['plate']
    characteristics = form['characteristics']
    availability = form['availability']
  
    image_data = form['image_data']
    
    encoded_image = base64.b64encode(image_data.encode('utf-8')).decode('utf-8')
    print(model, plate, characteristics, availability)

    vehiculo = Vehicle()
    vehiculo.data(model, plate, characteristics, availability, encoded_image)
    vehiculo.insert_vehicle()

    return render_template('vehiculo.html')

    

