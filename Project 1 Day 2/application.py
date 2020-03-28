import os

from flask import Flask, session,,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import render_template
from flask import request
from passlib.hash import bcrypt
from flask_sqlalchemy import SQLAlchemy
import sys
from datetime import datetime

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL") 

Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
Session = scoped_session(sessionmaker(bind=engine))
session = Session()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#TASK - 4 CREATING A DATABASE TABLE 
class Dataentry(db.Model):
    __tablename__ = "dataentry"
    # IndexNo = db.Column(db.Integer)
    Name = db.Column(db.String() , nullable=False)
    Email = db.Column(db.String(), primary_key=True, nullable=False)
    password = db.Column(db.String() , nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), nullable=False)
    def __init__ (self, name, email, password, time):
        # self.IndexNo = sno

        self.Name = name
        self.Email = email
        self.password = bcrypt.encrypt(password)
        self.timestamp = datetime.now()

    def validate_password(self, password):
        return bcrypt.verify(password, self.password)

db.create_all()


@app.route("/")
def index():
    return render_template("index.html")

#TASK - 5 INSERTING RECORDSINTO DATABASE
@app.route("/register" , methods=['POST'])
def register():
	indata = Dataentry(request.form['Username'], request.form['Email'], request.form['password'])
    try:
        db.session.add(indata)
        db.session.commit()
    except Exception as e:
        print(e)
        sys.stdout.flush()
        return 'Registration Failed'
    return 'Registration Success'
 
#TASK - 6 DISPLAY RECORDS FOR ADMIN USING ADMIN.html page 
@app.route("/admin")
def admin():
    try:
        users = Dataentry.query.all()

    except Exception as e:
        print(e)
        sys.stdout.flush()
        return 'Admin Failed'
    return render_template("admin.html", users = users)

#Day4 - TASK-1 Directing Login route
@app.route('/auth', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = Dataentry.query.filter_by(Email=email).first()
    print(user)
    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    # or not bcrypt.verify(password , user.password)
    if not user:
        flash('User is not present. Please register to login.')
        return redirect('/') # if user doesn't exist reload the page
    if not bcrypt.verify(password, user.password):
        flash('Wrong Login credentials')
        return redirect('/') # if user gives wrong password exist reload the page

    return redirect('/welcome')

@app.route("/welcome")
def welcome():
    return "WELCOME TO HOME PAGE"