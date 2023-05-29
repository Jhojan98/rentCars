from flask import render_template, redirect,url_for
from dao.vehiculo import Vehicle

def handle_itemcar(form):
    model = form['model']
    plate = form['plate']
    characteristics = form['characteristics']
    aviailability = form['aviailability']
    image_data = form['image_data']
    



    return redirect(url_for('itemcar'))