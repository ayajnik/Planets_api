##importing modules
from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Float, String
import os
from flask_marshmallow import Marshmallow



basedir = os.path.abspath(os.path.dirname(__file__))
##creating an object to initialize the app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(basedir,"planets.db")


db = SQLAlchemy(app)
ma = Marshmallow(app)


##creating a route for home page
@app.route("/home")
def home():
    welcome_page = "Hello world!"
    return welcome_page

## creating a home page route with json output to test in postman
@app.route("/home_json")
def home_json():
    welcome_page_json = "Hello world!"
    return jsonify(message = welcome_page_json)



## creating a route with variables
@app.route("/parameters")
def parameters():
    name = request.args.get("name")
    age = int(request.args.get("age"))

    if age > 18:
        entry_message = "Welcome to this API"
        return jsonify(message = entry_message)
    else:
        denial_message = "You are under age"
        return jsonify(message = denial_message)


##creating a routing with parameters with modern day approach
@app.route("/parameters_modern//<string:name>//<int:age>")
def parameters_modern(name:str,age:int):
        name = request.args.get("name")
        age = int(request.args.get("age"))

        if age > 18:
            entry_message = "Welcome to this API"
            return jsonify(message = entry_message)
        else:
            denial_message = "You are under age"
            return jsonify(message = denial_message)


##creating the ORM template for databases
class Planet(db.Model):
    __tablename__ = "planets"
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    home_star = Column(String)
    mass = Column(Float)
    distance = Column(Float)
    radius = Column(Float)

class Users(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique = True)
    password = Column(String)


##creating the schema to retrieve data 
class Userschema(ma.Schema):
    class meta:
        fields = ("id", "first_name", "last_name", "email", "password")

class Planetschema(ma.Schema):
    class meta:
        fields = ("planet_id", "planet_name", "planet_type", "home_star", "mass", "distance", "radius")

user_schema = Userschema()
users_schema = Userschema(many=True)

planet_schema = Planetschema()
planets_schema = Planetschema(many=True)













if __name__ == "__main__":
    app.run()