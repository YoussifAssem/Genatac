#import pyrebase
import hashlib
from lib2to3 import refactor
from flask import Flask,  redirect, render_template, request, url_for
from sqlalchemy import true
from Models.User import User
from firebase_admin import credentials, firestore


app = Flask(__name__)  # Initialze flask constructor
user = User()
    
db = firestore.client()

email = ''
password = ''

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
        password = str(session['password'])
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        print(email)
        print(password)
       
        if(checkUser(email=email, password=password)):
            if(True):
                return redirect(url_for('welcomePage'))
        # else:
        #     return redirect(url_for('login'))

def checkUser(email, password):
    
    
    if(email == ''):
        return redirect(url_for('login'))
    else:
        docs = db.collection('Users').document(email)
        val = docs.get().to_dict()
        if(docs.get().exists):
            if(val['email'] == email and val['password'] == password):
                return True
        else:
            return False
        



def register():
    if request.method == "POST":  # Only listen to POST
        
        
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
