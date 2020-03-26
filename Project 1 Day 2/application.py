import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import render_template
from flask import request

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://sgrwbvfpglusrx:579f0fd0edc0214e2642000c00ec1734a0206342eb055c5bf214596697441880@ec2-18-213-176-229.compute-1.amazonaws.com:5432/d5na60isuu66op'

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
    timezone = db.Column(db.DateTime(timezone=True), nullable=False)
    def __init__ (self, name, email, password, time):
        # self.IndexNo = sno

        self.Name = name
        self.Email = email
        self.password = bcrypt.encrypt(password)
        self.timezone = time

    def validate_password(self, password):
        return bcrypt.verify(password, self.password)

db.create_all()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register" , methods=['POST'])
def register():
    # print(request.form['Username'])
    result = request.form
    # print(result.items())
    return render_template("result.html", result = result.items())

