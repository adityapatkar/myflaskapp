from flask import Flask, render_template, redirect

app = Flask(__name__)


#--- routes start ---
from user import routes

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login/")
def login_page():
    return render_template('login.html')

@app.route("/dashboard/")
def dashboard():
    return redirect("http://www.google.com")
