#import pyrebase
import hashlib
from lib2to3 import refactor
from flask import Flask,  redirect, render_template, request, url_for
from Models.normalUser import User
from firebase_admin import credentials, firestore


app = Flask(__name__)  # Initialze flask constructor
user = User()
    

@app.route("/")


@app.route("/login")
def login():

    return render_template("login.html")


@app.route("/signup")
def signup():

    return render_template("signup.html")

@app.route("/welcomePage")
def welcomePage():
    return render_template('welcome.html')


@app.route("/welcome", methods=["POST", "GET"])
def welcome():
        

    if request.method == "POST":
        session = request.form
        email = str(session['email'])
        password = hashlib.sha256(str(session['password']).encode('utf-8')).hexdigest()
        if(user.logIn(email, password)):
                return redirect(url_for('welcomePage'))
        else:
            return redirect(url_for('login'))        
        # else:
        #     return redirect(url_for('login'))



def register():
    if request.method == "POST":  # Only listen to POST
        session = request.form
        email = str(session['email'])
        password = str(session['password'])
        
        
        try:
           if(user.logIn(email, password)):
               return redirect(url_for('welcome')) # mmkn aro7 ll el login
            
                
            
        except:
            # If there is any error, redirect to register
            return redirect(url_for('register'))

    else:
        if user.Registration(email, password):
            return redirect(url_for('welcome'))
        else:
            return redirect(url_for('register'))


if __name__ == "__main__":
    app.run(debug=True)
