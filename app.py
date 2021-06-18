##importing modules
from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Float, String
import os


basedir = os.path.abspath(os.path.dirname(__file__))


##creating an object to initialize the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(basedir+"planets.db")


db = SQLAlchemy(app)

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










if __name__ == "__main__":
    app.run()