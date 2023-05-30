from flask import render_template, redirect,url_for
from dao.cliente import ClienteDAO
import sqlite3
import json


def handle_signup(form):
    identification = form['identification']
    username = form['username']
    name = form['name']
    last_name = form['last_name']
    address = form['address']
    phone = form['phone']
    email = form['email']
    password= form['password']
    i_rent = 0
    is_admin = 0
    
    cliente = ClienteDAO()

    try:
        cliente.data(identification, username, name, last_name, address, phone, email, password, i_rent, is_admin)
        cliente.insert_client();
        print(cliente)   
    except sqlite3.IntegrityError:
        return redirect(url_for('render_singup'))
    finally:
        data = (identification, username, name, last_name, address, phone,email,password, i_rent, is_admin)
        print(username, password)
    
    context = {
        'data': json.dumps(data)
    }


    return redirect(url_for('home_vehicles', **context))