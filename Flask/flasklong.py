# importing the flask class
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
# using those forms created here in our application
from forms import Registrationform, Loginform
app = Flask(__name__)
from datetime import datetime


# creating app variable and setting it to the instance of flask class
# learn more about  __name__


# ideally the secret key for you application should be some random characters
app.config['SECRET_KEY'] = 'fdd8d8ad3c791dbeb8104472cc7203ca'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20),nullable = False,default = 'default.jpg') # nullable -> Flase, since they have to have atleast the default image
    # size = 20 String, since we are going to use a hashing algorithm that will make it 20 characters long
    password = db.Column(db.String(60),nullable = False)
    post = db.relationship('Post',backref = 'author', lazy = True)
    
    def __repr__(self): 
        # speicifes how are objects are printed when we print it out.
        return f"User('{self.Username}','{self.email}','{self.image_file}') "
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text , nullable = False)
    
    def __repr__(self):
        # speicifes how are objects are printed when we print it out.
        return f"Post('{self.title}','{self.date_posted}') "
    
    
    
    
        
    


# dummy data
post = [
    {
        'author': 'Abhishek Singh',
        'title': 'Blog post 1',
        'content': 'First content post ',
        'date_posted': '15 Feb 2023'
    },
    {
        'author': 'Abhishek Singh 2',
        'title': 'Blog post 2',
        'content': 'second content post ',
        'date_posted': '16 Feb 2023'
    }

]


@app. route("/home")
@app. route("/")
# route are what we type in our browser to get to different pages
# learn about flask decorators
# but the "/" means return to the home page
def home():
    return render_template('home.html', posts=post)

# about page creation:


@app.route("/alsoabout")  # can have multiple names/routes for a single webpage
@app.route("/about")
def abou():  # function name should be different
    return render_template("about.html", title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    # creating instance of our form that we are going to send to our application
    form = Registrationform()
    if form.validate_on_submit():
        #flash(f'Account created for {form.username.data}!', 'success')
        flash(f'Account Created for {form.username.data}!', 'success')
        # https://flask.palletsprojects.com/en/2.2.x/patterns/flashing/
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():  # creating instance of our form that we are going to send to our application
    form = Loginform()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    # to run the flask app from the python file itself without using terminal
    app.run(debug=True)
