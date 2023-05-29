from flask import render_template
from dao.cliente import ClienteDAO

def handle_itemcar(form):
    card_title = form['cart-title']
    