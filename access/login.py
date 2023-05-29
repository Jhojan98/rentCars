from flask import render_template, redirect, url_for
from .show_vehicle import show_vehicle_db
from dao.cliente import ClienteDAO


def handle_login(form):
    username = form['username']
    password = form['password']
    
    cliente = ClienteDAO()
    data = cliente.select_client(username,password)
    # vehicle = show_vehicle_db()
    
    if(data != None):
        context = {
            'is_admin':data[-1] == 1,
            # 'vehicles': vehicle,
        }
        return redirect(url_for('home_vehicles', **context))
    
    context = {
        'error': 'Incorrect fields',       
    }
    return render_template('login.html', **context) 