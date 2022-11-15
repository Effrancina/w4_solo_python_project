from flask import Blueprint, Flask, redirect, render_template, request
from models.city import City
import repositories.city_repository as city_repository
import repositories.restaurant_repository as restaurant_repository
import pdb

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

#create city
@cities_blueprint.route("/cities", methods=["POST"])
def create_city():
    name = request.form["name"]
    if request.form.get("visited"):
        visited = True
    else:
        visited = False
    new_city = City(name, visited)
    city_repository.save(new_city)
    return redirect("cities")

#restaurants in a specific city
@cities_blueprint.route("/cities/<id>/restaurants")
def cities_restaurants(id):
    restaurants = city_repository.show_restaurants(id)
    return render_template("restaurants/index.html", restaurants=restaurants)

#edit city
@cities_blueprint.route("/cities/<id>/edit")
def edit_city(id):
    cities = city_repository.select(id)
    return render_template("cities/edit.html", cities=cities)

#update city
@cities_blueprint.route("/cities/<id>", methods=["POST"])
def update_city(id):
    name = request.form["name"]
    if request.form.get("visited"):
        visited = True
    else:
        visited = False
    city = City(name, visited, id)
    city_repository.update_city(city)
    return redirect("/cities")


# # #delete city
# @cities_blueprint.route("/cities/<id>/delete", methods=["POST"])
# def delete_city(id):
#     if city_repository.show_restaurants(id):
#         print("Before removing this city, please make sure you have no restaurants you want to try!")
#     else:
#         city_repository.delete(id)
#     return redirect("cities")


# #delete all cities
# @cities_blueprint.route
# def delete_all():

