from flask import Flask, request, render_template, redirect, url_for, flash
import os
import uuid
from datetime import datetime

app = Flask(__name__)
app.secret_key = "this_key_does_not_need_to_be_private_lmao"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
    return render_template("signup.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/account")
def account():
    return render_template("account.html")

if __name__ == "__main__":
    app.run(debug=True)