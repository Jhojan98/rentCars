from flask import Flask, render_template, request
from access.signup import handle_signup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/SignUp')
def render_singup():
    return render_template('signUp.html')

@app.route('/signup', methods=['POST'])
def signup():
    return handle_signup(request.form)


if __name__ == '__main__':
    app.run()    