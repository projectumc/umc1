from flask import Flask,render_template,url_for,flash,redirect,request
from flask_sqlalchemy import SQLAlchemy
# using those forms created here in our application
app = Flask(__name__)
from datetime import datetime





app  = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template("index.html")



@app.route('/contact')
def cont():
    return render_template("contact.html")


@app.route('/register' , methods=['GET','POST'])
def reg():
    errors = {}
    if request.method == "POST":
        print("User=", request.form["username"])
        print("Email=", request.form["email"])
        print("Password=", request.form["psw"])
        print("Confirm_password=", request.form["cpsw"])
        print("Aadhaar=", request.form["Aadhaar"])
        print("phone_code=", request.form["phoneCode"])
        print("phone_number=", request.form["phone"])

    

    return render_template('register.html', title='Register', errors = errors)

@app.route('/login', methods=['GET','POST'])
def log():
    errors = {}
    if request.method == "POST":
        print("username=", request.form["username"])
        print("password=", request.form["password"])
        print("check=", request.form["check"])
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug = True) 