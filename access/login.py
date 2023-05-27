from flask import render_template
from dao.cliente import ClienteDAO


def handle_login(form):
    username = form['username']
    password = form['password']
    
    cliente = ClienteDAO()
    if(cliente.select_client(username,password) != None):
        return render_template('home.html')
    
    context = {
        'error': 'Incorrect fields'
    }
    return render_template('login.html', **context)    