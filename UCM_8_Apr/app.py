from datetime import datetime
from flask import Flask, flash, render_template, url_for, flash, redirect, request
import csv
import pandas as pd
import cv2
import pyzbar.pyzbar as pyzbar

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
    errors = {}
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
        email = request.form['email']
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        location = request.form["location"]
        dateofbirth = request.form["dateofbirth"]
        aadhaar = request.form['aadhaar']
        phone = request.form['phone']

        fieldnamesU = ['username', 'email', 'firstname', 'lastname',
                       'location', 'dateofbirth', 'password', 'aadhaar', 'phone']

        with open('nameListDoc.csv', 'a', newline='') as inFile:
            # DictWriter will help you write the file easily by treating the
            # csv as a python's class and will allow you to work with
            # dictionaries instead of having to add the csv manually.
            writer = csv.DictWriter(inFile, fieldnames=fieldnamesU)
            # writerow() will write a row in your csv file
            # while()
            writer.writerow({'username': username, 'email': email, 'firstname': firstname, 'lastname': lastname,
                            'location': location, 'dateofbirth': dateofbirth, 'password': password,  'aadhaar': aadhaar,  'phone': phone})

    return render_template('doctor.html', title='Register', errors=errors, data=df)


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
            if row[0] == username:
                firstname = row[2]
                lastname = row[3]
                location = row[4]
                dateofbirth = row[5]
                email = row[1]
                phone = row[8]
                aadhaar = row[7]

    return render_template("dashboardUser.html", username=username, firstname=firstname, lastname=lastname, location=location, dateofbirth=dateofbirth, email=email, phone=phone, aadhaar=aadhaar)


@app.route('/dashboardDoc/<username>', methods=['GET', 'POST'])
def dashboarddoc(username):
    with open('nameListDoc.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                firstname = row[2]
                lastname = row[3]
                location = row[4]
                dateofbirth = row[5]
                email = row[1]
                phone = row[8]
                aadhaar = row[7]

    return render_template("dashboardDoc.html", username=username, firstname=firstname, lastname=lastname, location=location, dateofbirth=dateofbirth, email=email, phone=phone, aadhaar=aadhaar)


@app.route('/doctorhistory', methods=['GET', 'POST'])
def history():
    return render_template('historyDoctor.html')


@app.route('/userhistory', methods=['GET', 'POST'])
def userhistory():
    return render_template("historyUser.html")


<<<<<<< Updated upstream
@app.route('/scanner', methods=['GET', 'POST'])
def scan():
    cap = cv2.VideoCapture(0)

# Keep track of detected QR codes
    detected_qr_codes = set()

    while True:
        # Read the current frame from camera
        _, frame = cap.read()

        # Use pyzbar to decode any QR codes in the frame
        decoded_objs = pyzbar.decode(frame)

        # Loop over all the detected QR codes
        for decoded_obj in decoded_objs:
            # Extract the QR code's data
            data = decoded_obj.data.decode('utf-8')
            if data not in detected_qr_codes:
                # Print the QR code's data if it hasn't been printed already
                print(f"Found QR code: {data}")
                cv2.destroyAllWindows()
                cap.release()
                exit()

        # Show the frame
        cv2.imshow('QR Code Reader', frame)

        # Check for the 'q' key to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    exit()
    cv2.destroyAllWindows()
    return render_template("qrscanner.html",data= data)


    




    

=======
>>>>>>> Stashed changes
if __name__ == '__main__':

    app.run(debug=True)
