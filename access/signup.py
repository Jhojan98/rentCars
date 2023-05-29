from flask import render_template, redirect,url_for
from dao.cliente import ClienteDAO


def handle_signup(form):
    identification = form['identification']
    username = form['username']
    name = form['name']
    last_name = form['last_name']
    address = form['address']
    phone = form['phone']
    email = form['email']
    password= form['password']
    
    cliente = ClienteDAO()
    cliente.data(identification, username, name, last_name, address, phone, email, password)
    cliente.insert_client();
    print(username,email,password)


    return redirect(url_for('home_vehicles'))