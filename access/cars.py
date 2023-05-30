from flask import render_template, redirect, url_for
from dao.vehiculo import Vehicle
import sqlite3


import time


def handle_cars(form, image, **context):
    model = form['model']
    plate = form['plate']
    characteristics = form['characteristics']
    price = form['price']
    aviailability = True

    image_path = 'cars/' + image.filename
    image.save('static/'+image_path)

    print(model, plate, characteristics, price, aviailability, image_path)

    vehiculo = Vehicle()
    try:
        vehiculo.data(model, plate, characteristics, price, aviailability, image_path)
        vehiculo.insert_vehicle()
    except sqlite3.IntegrityError:
        return redirect(url_for('add_vehiculo', **context))


    return render_template('vehiculo.html', **context)

    


