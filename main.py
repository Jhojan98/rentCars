from flask import Flask, render_template, request
from access.signup import handle_signup
from access.login import handle_login
import sqlite3
from dao.cliente import ClienteDAO
from access.cars import handle_cars

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/SignUp')
def render_singup():
    return render_template('signUp.html')

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
    return handle_cars(request.form)


if __name__ == '__main__':
    
    try:
        cliente = ClienteDAO()
        cliente.data(1, "ADMIN", "admin", "admin", "admin",321, "admin@google.com", 1234,True)
        cliente.insert_client()
    except sqlite3.IntegrityError:
        pass
    finally:
        app.run()    