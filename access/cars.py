from base64 import b64encode
from flask import render_template
from dao.vehiculo import Vehicle

def handle_cars(form):
    
    image_data = form['image_data']
    with open(image_data.filename, 'rb') as file:
        image_data = file.read()
        encoded_image = b64encode(image_data).decode('utf-8')

       
    model = form['model']
    plate = form['plate']
    characteristics = form['characteristics']
    availability = form['availability']
  

    #vehiculo = Vehicle()
    # vehiculo.data(model, plate, characteristics,aviailability, encoded_data)
    #vehiculo.insert_vehicle();
    print(model, plate, characteristics,availability)

    return render_template('vehiculo.html')
    

