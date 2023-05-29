from flask import request, render_template
from dao.vehiculo import Vehicle
import os
import base64


import time


def handle_cars(form, image):
    model = form['model']
    plate = form['plate']
    characteristics = form['characteristics']
    availability = form['availability']

    image_path = 'cars/' + image.filename
    image.save('static/'+image_path)


    vehiculo = Vehicle()
    vehiculo.data(model, plate, characteristics, availability, image_path)
    vehiculo.insert_vehicle()


    return render_template('vehiculo.html')

    


