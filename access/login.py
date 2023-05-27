from flask import render_template
from dao.cliente import ClienteDAO


def handle_login(form):
    username = form['username']
    password = form['password']
    
    cliente = ClienteDAO()
    data = cliente.select_client(username,password)
    
    if(data != None):
        context = {
            'is_admin':data[-1] == 1
        }
        return render_template('home.html', **context)
    
    context = {
        'error': 'Incorrect fields',       
    }
    return render_template('login.html', **context)    