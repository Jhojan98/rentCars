from flask import Flask, render_template, request, redirect, url_for
from access.signup import handle_signup
from access.login import handle_login
from access.itemcar import handle_itemcar
import sqlite3
import ast
from dao.cliente import ClienteDAO
from access.cars import handle_cars
from querys.querys_vehicle import show_vehicle_db, update_vehicle_db
from querys.query_client import update_client_db
import json
from ast import literal_eval

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

@app.route('/') #route
def home():
    return render_template('login.html')

@app.route('/SignUp')
def render_singup():
    return render_template('signUp.html')

# @app.route('/itemcar')
# def render_itemcar():
#     return render_template('itemcar.html')


@app.route('/itemcar', methods=['POST'])
def itemcar():
    vehicle = request.form.getlist('vehicle') # --> ["(admin,admin)"] - admin,admin -> data for example 
    client = request.form.getlist('client') # --> ["(admin,admin)"]

    vehicle_tuple = ast.literal_eval(vehicle[0])# vehicle[0] =  "(admin,admin)" -->  vehicle_tuple = (admin,admin)
    client_tuple = ast.literal_eval(client[0])

    context = {'vehicle': vehicle_tuple, 'client': client_tuple}
    return render_template('itemcar.html', **context)


@app.route('/signup', methods=['POST'])# When the user insert data make a peticion POTS for send that information to the server 
def signup():
    return handle_signup(request.form) # se resive la informacion con request.form


@app.route('/login', methods=['POST'])# When the user insert data make a peticion POTS for send that information to the server 
def login():
    return handle_login(request.form)


"""render de template html add card in the web"""
@app.route('/add/vehiculo')
def add_vehiculo():
    client = request.args.get('client', '')
    print(client)

    context = {'client':client}
    return render_template('vehiculo.html', **context)


"""When the user insert a form"""
@app.route('/add/vehiculo/added', methods=['POST']) # When the user insert data make a peticion POTS for send that information to the server 
def vehiculo():
    image = request.files['image_data']

    client = request.args.get('client', '')
    print(client)

    context = {'client':client}

    return handle_cars(request.form, image, **context)


@app.route('/home')
def home_vehicles():

    vehicles = show_vehicle_db()
    context = request.args.to_dict()
    client = request.args.get('data', '') #recoge del contexto todo lo que dice data

    try:
        client = json.loads(client)
        client = tuple(client)
    except:
        client = ast.literal_eval(client)  #cliente =  "(admin,admin)" --> cliente = (admin,admin)
        print("error")

    complete_context = {**context, 'vehicles': vehicles, 'client':client}# send information vehicle and client 


    return render_template('home.html', **complete_context)


@app.route('/reservar', methods=['POST'])
def reserva():
    # Obtener el vehículo que se muestra en pantalla
    vehicle = request.form.getlist('vehicle') # --> ["(admin,admin)"] - admin,admin -> data for example 
    client = request.form.getlist('client')
    vehicle_tuple = ast.literal_eval(vehicle[0])# vehicle[0] =  "(admin,admin)" -->  vehicle_tuple = (admin,admin)
    client_tuple = ast.literal_eval(client[0])
    update_vehicle_db(False, vehicle_tuple[1]) #call the funciotion update_vehicle_db from querys and vehicle_tuple[1] -- plate
    update_client_db(True, client_tuple[0]) # client_tuple[0] -- identification
    client_tuple = list(client_tuple) #(admin,admin) -->  [admin, admin]
    client_tuple[8] = 1 # i_rent

    context = {
        'data':json.dumps(tuple(client_tuple))
    }
    
    
    return redirect(url_for ('home_vehicles', **context))


if __name__ == '__main__':
    
    try:
        cliente = ClienteDAO()
        cliente.data(1, "ADMIN", "admin", "admin", "admin",321, "admin@google.com", 1234, False, True)
        cliente.insert_client()
    except sqlite3.IntegrityError:
        pass
    finally:
        app.run()    