from db.run_sql import run_sql
from models.city import City
from models.restaurant import Restaurant
import pdb

def save(city):
    sql = """INSERT INTO cities (name, visited)
    VALUES (%s, %s) RETURNING *"""
    values = [city.name, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return results

def select_all():
    cities = []
    sql = "SELECT * FROM cities"
    results = run_sql(sql)
    for row in results:
        city = City(row['name'], row['visited'], row['id'])
        cities.append(city)
    return cities

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        city = City(result['name'], result['visited'], result['id'])
    return city

def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql) 

def update_city(city):
    sql = "UPDATE cities SET (name, visited) = (%s, %s) WHERE id = %s"
    values = [city.name, city.visited, city.id]
    run_sql(sql, values)

def show_restaurants(city_id):
    sql = "SELECT restaurants.* FROM restaurants WHERE city_id = %s"
    values = [city_id]
    city_restaurants = []
    restaurants = run_sql(sql, values)
    for row in restaurants:
        city = select(city_id)
        new_restaurant = Restaurant(row['name'], row['cuisine'], city, row['tried'], row['id'])
        city_restaurants.append(new_restaurant)
    return city_restaurants
