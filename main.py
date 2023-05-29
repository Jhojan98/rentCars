from flask import Flask, render_template, request, redirect, url_for
from access.signup import handle_signup
from access.login import handle_login
from access.itemcar import handle_itemcar
import sqlite3
import ast
from dao.cliente import ClienteDAO
from access.cars import handle_cars
from access.querys_vehicle import show_vehicle_db, update_vehicle_db

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/SignUp')
def render_singup():
    return render_template('signUp.html')

@app.route('/itemcar')
def render_itemcar():
    return render_template('itemcar.html')

@app.route('/itemcar', methods=['POST'])
def itemcar():
    vehicle = request.form.getlist('vehicle')
    vehicle_tuple = ast.literal_eval(vehicle[0])
    print(type(vehicle_tuple))
    print(vehicle_tuple)
    context = {'vehicle': vehicle_tuple}
    return render_template('itemcar.html', **context)

@app.route('/signup', methods=['POST'])# When de user insert data make a peticion POTS for send that information to the server 
def signup():
    return handle_signup(request.form)

@app.route('/login', methods=['POST'])# When de user insert data make a peticion POTS for send that information to the server 
def login():
    return handle_login(request.form)

"""render de template html add card in the web"""
@app.route('/add/vehiculo')
def render_vehiculo():
    return render_template('vehiculo.html')



"""When the user insert a form"""
@app.route('/add/vehiculo/added', methods=['POST']) # When de user insert data make a peticion POTS for send that information to the server 
def vehiculo():
    image = request.files['image_data']
    print("this:",type(image))

    return handle_cars(request.form, image)

@app.route('/home')
def home_vehicles():

    vehicles = show_vehicle_db()
    context = request.args.to_dict()
    for vehicle in vehicles:
        print(vehicle)

    complete_context = {**context, 'vehicles': vehicles}

    return render_template('home.html', **complete_context)

@app.route('/reservar', methods=['POST'])
def reserva():
    # Obtener el vehículo que se muestra en pantalla
    vehicle = request.form.getlist('vehicle')
    vehicle_tuple = ast.literal_eval(vehicle[0])
    update_vehicle_db(False, vehicle_tuple[1])
    
    
    return redirect(url_for ('home_vehicles'))


if __name__ == '__main__':
    
    try:
        cliente = ClienteDAO()
        cliente.data(1, "ADMIN", "admin", "admin", "admin",321, "admin@google.com", 1234,True)
        cliente.insert_client()
    except sqlite3.IntegrityError:
        pass
    finally:
        app.run()    