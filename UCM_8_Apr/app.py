from datetime import datetime
from flask import Flask, flash, render_template, url_for, flash, redirect, request
import csv
import pandas as pd

# using those forms created here in our application


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

df = pd.read_csv('nameListDoc.csv')


@app.route('/')
@app.route('/index')
def home():
    return render_template("index.html")


@app.route('/contact')
def cont():
    return render_template("contact.html")


@app.route('/register', methods=['GET', 'POST'])
def reg():
    phone = request.form['phone']
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["psw"]
        email = request.form['email']
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        location = request.form["location"]
        dateofbirth = request.form["dateofbirth"]
        aadhaar = request.form['aadhaar']
        phone = request.form['phone']

        fieldnamesU = ['username', 'email', 'firstname', 'lastname',
                       'location', 'dateofbirth', 'password', 'aadhaar', 'phone']

        with open('nameListUser.csv', 'a', newline='') as inFile:
            # DictWriter will help you write the file easily by treating the
            # csv as a python's class and will allow you to work with
            # dictionaries instead of having to add the csv manually.
            writer = csv.DictWriter(inFile, fieldnames=fieldnamesU)
            # writerow() will write a row in your csv file
            # while()
            writer.writerow({'username': username, 'email': email, 'firstname': firstname, 'lastname': lastname,
                            'location': location, 'dateofbirth': dateofbirth, 'password': password,  'aadhaar': aadhaar,  'phone': phone})

    return render_template('register.html', title='Register', errors=errors, data=df)


@app.route('/doctor', methods=['GET', 'POST'])
def doc():
    errors = {}
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["psw"]
        print("User=", request.form["username"])
        print("Email=", request.form["email"])
        # added new
        first_name = request.form["firstname"]
        last_name = request.form["lastname"]
        location = request.form["location"]
        dob = request.form["dateofbirth"]
        print("Password=", request.form["psw"])
        print("Confirm_password=", request.form["cpsw"])
        print("Aadhaar=", request.form["Aadhaar"])
        print("phone_code=", request.form["phoneCode"])
        print("phone_number=", request.form["phone"])

        fieldnames = ['username', 'password']

        with open('nameListDoc.csv', 'a') as inFile:
            # DictWriter will help you write the file easily by treating the
            # csv as a python's class and will allow you to work with
            # dictionaries instead of having to add the csv manually.
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            # writerow() will write a row in your csv file
            # while()
            writer.writerow({'username': username, 'password': password})

    return render_template('doctor.html', title='Register', errors=errors)


@app.route('/login', methods=['GET', 'POST'])
def log():
    errors = {}
    if request.method == "POST":
        print("username=", request.form["username"])
        print("password=", request.form["password"])

    if 'check' in request.form:
        check = request.form['check']

        error = ""
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            with open('nameListDoc.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == username and row[6] == password:
                        return redirect('/dashboardDoc/{}'.format(username))
                    else:
                        error = 'Invalid Credentials. Please try again.'
                        flash(error, "error")
        return render_template('login.html', error=error)

# Checking for UserCondition
    else:
        error = ""
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            with open('nameListUser.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == username and row[6] == password:
                        return redirect('/dashboardUser/{}'.format(username))
                    else:
                        error = 'Invalid Credentials. Please try again.'
                        flash(error, "error")
        return render_template('login.html', error=error)


@app.route('/dashboardUser/<username>', methods=['GET', 'POST'])
def dashboard(username):
    with open('nameListUser.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            firstname = row[0]
            lastname = row[3]
            location = row[4]
            dateofbirth = row[5]
            email = row[1]
            phone = row[8]
            aadhaar = row[7]

    return render_template("dashboardUser.html", username=username, firstname=firstname, lastname=lastname, location=location, dateofbirth=dateofbirth, email=email, phone=phone, aadhaar=aadhaar)


@app.route('/dashboardDoc/<username>', methods=['GET', 'POST'])
def dashboardDoc(fname, lname, loc, dob, email, pno, ano):

    return render_template("dashboardDoc.html")


if __name__ == '__main__':
    app.run(debug=True)
