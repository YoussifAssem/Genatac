#import pyrebase
import hashlib
from flask import Flask,  redirect, render_template, request, url_for
from Models.User import User
app = Flask(__name__)  # Initialze flask constructor
user = User()
    
userName = {"n": ""}

@app.route("/")
def login():
    return render_template("login.html")

# Sign up/ Register


@app.route("/signup")
def signup():
    return render_template("signup.html")

# Welcome page


@app.route("/welcome")
def welcome():
        return render_template("welcome.html", name=userName["n"])
    
# If someone clicks on login, they are redirected to /result


@app.route("/result", methods=["POST", "GET"])
def result():
    test = True
    if request.method == "POST":  # Only if data has been posted
        result = request.form  # Get the data
        userName["n"] = str(result["name"])
        password = hashlib.sha256(result["pass"].encode('utf-8')).hexdigest()
        test = user.logIn(userName["n"], password)
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
