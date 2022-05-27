#import pyrebase
import hashlib
from lib2to3 import refactor
from flask import Flask,  redirect, render_template, request, url_for
from Models.User import User
from firebase_admin import credentials, firestore

app = Flask(__name__)  # Initialze flask constructor
user = User()
    
db = firestore.client()

userName = {"n": ""}
getid = {"d": ""}

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/welcome")
def welcome():
        hashedID = hashlib.sha256(getid["d"].encode('utf-8')).hexdigest()

        result_related= db.collection('adminUsers').document(userName["n"]).collection('Results'
        ).document(hashedID).get({
            'probabilityFather'
    })  
        result_not_related= db.collection('adminUsers').document(userName["n"]).collection('Results'
        ).document(hashedID).get({
            'probabilityNotFather'
    }) 
        return render_template("welcome.html", name=userName["n"], result1=result_related.to_dict(),result2=result_not_related.to_dict())
    
# If someone clicks on login, they are redirected to /result


@app.route("/result", methods=["POST", "GET"])
def result():
    test = True
    if request.method == "POST":  # Only if data has been posted
        
        # Get the data
        result = request.form  
        userName["n"] = str(result["name"])
        getid["d"] = str(result["id"])
        #password = hashlib.sha256(result["pass"].encode('utf-8')).hexdigest()
        #test = user.logIn(userName["n"], password)
        
        try:
            if(test):
              return redirect(url_for('result'))
        except:
            return redirect(url_for('login'))
    else:
        if (test):
            return redirect(url_for('welcome'))
        else:
           return redirect(url_for('login'))

# If someone clicks on register, they are redirected to /register


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":  # Only listen to POST
        result = request.form  # Get the data submitted
        password = result["pass"]
        name = result["name"]
        try:
           if(user.logIn(name, password)):
            return redirect(url_for('welcome'))
        except:
            # If there is any error, redirect to register
            return redirect(url_for('register'))

    else:
        if user.Registration(name, password):
            return redirect(url_for('welcome'))
        else:
            return redirect(url_for('register'))


if __name__ == "__main__":
    app.run()
