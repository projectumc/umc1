from datetime import datetime
from flask import Flask, flash, render_template, url_for, flash, redirect, request
import csv


# using those forms created here in our application


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
@app.route('/index')
def home():
    return render_template("index.html")


@app.route('/contact')
def cont():
    return render_template("contact.html")


@app.route('/register', methods=['GET', 'POST'])
def reg():
    errors = {}
    if request.method == "POST":
        username = request.form["username"]
        #print("username=", request.form["username"])
        email = request.form["email"]

        first_name = request.form["firstname"]
        last_name = request.form["lastname"]
        location = request.form["location"]
        dob = request.form["dateofbirth"]

        #print("Email=", request.form["email"])
        password = request.form["psw"]
        print("Confirm_password=", request.form["cpsw"])
        Aadhar = request.form['Aadhar']
        #print("Aadhaar=", request.form["Aadhaar"])
        print("phone_code=", request.form["phoneCode"])
        phone_number = request.form['phone_number']
        #print("phone_number=", request.form["phone"])

        fieldnames = ['username', 'password']

        with open('nameListUser.csv', 'a') as inFile:
            # DictWriter will help you write the file easily by treating the
            # csv as a python's class and will allow you to work with
            # dictionaries instead of having to add the csv manually.
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            # writerow() will write a row in your csv file
            # while()
            writer.writerow({'username': username, 'password': password})

    return render_template('register.html', title='Register', errors=errors)


@app.route('/doctor', methods=['GET', 'POST'])
def doc():
    errors = {}
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["psw"]

        first_name = request.form["firstname"]
        last_name = request.form["lastname"]
        location = request.form["location"]
        dob = request.form["dateofbirth"]
        hospitalname = request.form['hospitalname']

        print("User=", request.form["username"])
        print("Email=", request.form["email"])
        print("Password=", request.form["psw"])
        print("Confirm_password=", request.form["cpsw"])
        print("Aadhaar=", request.form["Aadhaar"])
        print("phone_code=", request.form["phoneCode"])
        print("phone_number=", request.form["phone"])

        fieldnames = ['first_name', 'last_name', 'location',
                      'hospitalname', 'username', 'password']

        with open('nameListDoc.csv', 'a') as inFile:
            # DictWriter will help you write the file easily by treating the
            # csv as a python's class and will allow you to work with
            # dictionaries instead of having to add the csv manually.
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            # writerow() will write a row in your csv file
            # while()
            writer.writerow({'first_name': first_name, 'last_name': last_name, 'location': location, 'hospitalname': hospitalname,
                            'username': username, 'password': password})

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
            with open('nameListDoc.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == username and row[1] == password:
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
                    if row[0] == username and row[1] == password:
                        return redirect('/dashboardUser/{}'.format(username))
                    else:
                        error = 'Invalid Credentials. Please try again.'
                        flash(error, "error")
        return render_template('login.html', error=error)

    #print("check=", request.form["check"], False)
    #print("check=", request.form["check"], False)
    return render_template("login.htmlz")


@app.route('/dashboardUser/<username>', methods=['GET', 'POST'])
def dashboard(username):
    return render_template("dashboardUser.html", username=username)


@app.route('/dashboardDoc/<username>', methods=['GET', 'POST'])
def dashboardDoc(username):
    return render_template("dashboardDoc.html", username=username)


if __name__ == '__main__':
    app.run(debug=True)
