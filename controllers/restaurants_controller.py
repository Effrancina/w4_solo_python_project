from flask import Blueprint, Flask, redirect, render_template, request
from models.restaurant import Restaurant
import repositories.restaurant_repository as restaurant_repository
import repositories.city_repository as city_repository
import pdb

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
    city = city_repository.select(request.form["city_id"])
    cuisine = request.form["cuisine"]
    if request.form.get("tried"):
        visited = True
    else:
        visited = False
    new_restaurant = Restaurant(name, cuisine, city, visited)
    restaurant_repository.save(new_restaurant)
    return redirect("/restaurants")


# #update restaurant


# #delete restaurant
@restaurants_blueprint.route("/cities/<id>/delete", methods=["POST"])
def delete_restaurant(id):
    restaurant_repository.delete(id)
    return redirect("/restaurants")

@restaurants_blueprint.route("/restaurants/<id>/edit")
def edit_restaurant(id):
    restaurants = restaurant_repository.select(id)
    return render_template("/restaurants/edit.html", restaurants=restaurants)

# #delete all restaurant
# @restaurants_blueprint.route:
