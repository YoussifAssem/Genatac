#import pyrebase
import email
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
'''
@app.route("/edit")
def edit():
    return render_template("editprofile.html")


@app.route("/signup")
def signup():

    return render_template("signup.html")

@app.route("/Home")
def home():
     return render_template('menu.html')
'''

@app.route("/Results", methods=["POST", "GET"])
def Results():
        if request.method == 'POST':
            result = request.form
            check = user.getResults(result['adminName'], result['caseNumber'], result['nationalNumber'])[0]
            print(check)
            probFather = user.getResults(result['adminName'], result['caseNumber'], result['nationalNumber'])[1]
            probNotFather = user.getResults(result['adminName'], result['caseNumber'], result['nationalNumber'])[2]
            result = user.getResults(result['adminName'], result['caseNumber'], result['nationalNumber'])[3]
            if(check):
                return render_template('viewResults.html', probFather=probFather, probNotFather=probNotFather, result=result)
            else:
                return render_template('results.html')
                    
        return render_template('results.html')
   

@app.route("/welcome", methods=["POST", "GET"])
def welcome():
     if request.method == "POST":
        session = request.form
        email = str(session['email'])
        password = hashlib.sha256(str(session['password']).encode('utf-8')).hexdigest()
        if(user.logIn(email, password)):
             return render_template('menu.html', email=email)

        else:
            return redirect(url_for('login'))        
        # else:
        #     return redirect(url_for('login'))

'''
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
'''

if __name__ == "__main__":
    app.run(debug=True)
