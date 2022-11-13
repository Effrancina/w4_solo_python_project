from flask import Blueprint, Flask, redirect, render_template, request
from models.city import City
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)
app = Flask(__name__)


@app.route('/')
def welcome():
   return 'Welcome'
   
#index
@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities = cities)

#new city
@cities_blueprint.route("/cities/new")
def new_city():
    return render_template("cities/new.html")

