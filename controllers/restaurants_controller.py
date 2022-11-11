from flask import Blueprint, Flask, redirect, render_template, request
from models.restaurant import Restaurant
import repositories.restaurant_repository as restaurant_repository

restaurants_blueprint = Blueprint("restaurants", __name__)


#index
@restaurants_blueprint.route("/restaurants")
def restaurants():
    restaurants = restaurant_repository.select_all()
    return render_template("restaurants/index.html", restaurants = restaurants)

#new city
@restaurants_blueprint.route("/restaurants/new")
def new_restaurant():
    return render_template("restaurants/new.html")
