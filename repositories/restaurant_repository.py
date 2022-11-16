from db.run_sql import run_sql
from models.restaurant import Restaurant
import repositories.city_repository as city_repository 

def save(restaurant):
    sql = """INSERT INTO restaurants (name, cuisine, tried, city_id)
    VALUES (%s, %s, %s, %s) RETURNING id"""
    values = [restaurant.name, restaurant.cuisine, restaurant.tried, restaurant.city.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    restaurant.id = id
    return 

def select_all():
    restaurants = []
    sql = "SELECT * FROM restaurants"
    results = run_sql(sql)
    for row in results:
        city = city_repository.select(row['city_id'])
        restaurant = Restaurant(row['name'], row['cuisine'], city, row['tried'], row['id'])
        restaurants.append(restaurant)
    return restaurants

def select(id):
    restaurant = None
    sql = "SELECT * FROM restaurants WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        city = city_repository.select(result['city_id'])
        restaurant = Restaurant(result['name'], result['cuisine'], city, result['tried'], result['id'])
    return restaurant

def delete(id):
    sql = "DELETE FROM restaurants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM restaurants"
    run_sql(sql) 

def update_restaurant(restaurant):
    sql = """UPDATE restaurants SET (name, city_id, cuisine, tried) = (%s, %s, %s, %s)
    WHERE id = %s"""
    values = [restaurant.name, restaurant.city.id, restaurant.cuisine, restaurant.tried, restaurant.id]
    run_sql(sql, values)
