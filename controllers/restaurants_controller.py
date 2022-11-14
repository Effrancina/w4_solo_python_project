from flask import Blueprint, Flask, redirect, render_template, request
from models.restaurant import Restaurant
import repositories.restaurant_repository as restaurant_repository
import repositories.city_repository as city_repository

restaurants_blueprint = Blueprint("restaurants", __name__)


#index
@restaurants_blueprint.route("/restaurants")
def restaurants():
    restaurants = restaurant_repository.select_all()
    return render_template("restaurants/index.html", restaurants = restaurants)

#new restaurant
@restaurants_blueprint.route("/restaurants/new")
def new_restaurant():
    cities = city_repository.select_all()
    return render_template("restaurants/new.html", cities=cities)


#create restaurant
@restaurants_blueprint.route("/restaurants", methods=["POST"])
def create_restaurant():
    name = request.form["name"]
    city = request.form["city"]
    cuisine = request.form["cuisine"]
    tried = request.form["tried"]
    new_restaurant = Restaurant(name, city, cuisine, tried)
    city_repository.save(new_restaurant)
    return redirect("/restaurants")


# #update restaurant
# @restaurants_blueprint.route

# #delete restaurant
# @restaurants_blueprint.route

# #delete all restaurant
# @restaurants_blueprint.route:
