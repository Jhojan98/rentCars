from flask import Flask, render_template, request
from access.signup import handle_signup
from access.login import handle_login

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('test.html')

@app.route('/SignUp')
def render_singup():
    return render_template('signUp.html')

@app.route('/signup', methods=['POST'])
def signup():
    return handle_signup(request.form)

@app.route('/login', methods=['POST'])
def login():
    return handle_login(request.form)



if __name__ == '__main__':
    app.run()    