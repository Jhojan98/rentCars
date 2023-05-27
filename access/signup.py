from flask import render_template
from dao.cliente import ClienteDAO


def handle_signup(form):
    username = form['username']
    email = form['email']
    password = form['password']
    
    cliente = ClienteDAO()
    cliente.data(10,username,"asd","asd", 1234123, email)
    cliente.insert_estudiante()
    print(username,email,password)


    # Aquí puedes realizar acciones relacionadas con el registro del usuario,
    # como almacenar los datos en una base de datos

    return render_template('home.html')