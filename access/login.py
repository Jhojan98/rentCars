from flask import render_template, redirect, url_for
import json

from dao.cliente import ClienteDAO


def handle_login(form):
    username = form['username'] # form = requets.form
    password = form['password']
    
    client = ClienteDAO()
    data = client.select_client(username,password)
        
    if(data != None):
        context = {
            'is_admin':data[-1] == 1, #data[-1] -- is_admin 1==1 true
            'data': json.dumps(data) #envia una tupla correctamente
        }

        return redirect(url_for('home_vehicles', **context))
    
    context = {
        'error': 'Incorrect fields',       
    }
    return render_template('login.html', **context) 