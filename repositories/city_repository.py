from db.run_sql import run_sql
from models.city import City

def save(city):
    sql = """INSERT INTO cities (name, been_to)
    VALUES (%s, %s) RETURNING *"""
    values = [city.name, city.been_to]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return results

def select_all():
    cities = []
    sql = """SELECT * FROM cities"""
    results = run_sql(sql)
    for row in results:
        city = City(row['name'], row['been_to'])
        cities.append(city)
    return cities

def select(id):
    city = None
    sql = """SELECT * FROM cities WHERE id = %s"""
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        city = City(result['name'], result['been_to'])
    return city

def delete(id):
    sql = """DELETE FROM cities WHERE id = %s"""
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql) 

def update(city):
    sql = """UPDATE cities SET (name, been to) = (%s, %s)
    WHERE id = %s"""
    values = [city.name, city.been_to, city.id]
    run_sql(sql, values)

