from flask import render_template, redirect, url_for

from dao.cliente import ClienteDAO


def handle_login(form):
    username = form['username']
    password = form['password']
    
    cliente = ClienteDAO()
    data = cliente.select_client(username,password)
    
    
    if(data != None):
        context = {
            'is_admin':data[-1] == 1,
        }

        print(context['is_admin'])
        return redirect(url_for('home_vehicles', **context))
    
    context = {
        'error': 'Incorrect fields',       
    }
    return render_template('login.html', **context) 