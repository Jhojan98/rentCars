import base64
from flask import render_template
from dao.vehiculo import Vehicle

def handle_cars(form):
    image_file = form['image_file']
    #with open(image_file, 'rb') as file:
        #image_data = file.read()
        # = base64.b64encode(image_data)
    model = form['model']
    plate = form['plate']
    characteristics = form['characteristics']
    aviailability = form['aviailability']
    email = form['email']
    password= form['password']
    encoded_data = "hola"

    #vehiculo = Vehicle()
    #vehiculo.data(model, plate, characteristics,aviailability, encoded_data)
    #vehiculo.insert_vehicle();
    print(model, plate, characteristics,aviailability, encoded_data)

    return render_template('home.html')
    

