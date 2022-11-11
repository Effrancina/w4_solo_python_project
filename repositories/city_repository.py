from db.run_sql import run_sql


def save(city):
    sql = """INSERT INTO cities (name, been_to)
    VALUES (%s, %s) RETURNING *"""
    values = [city.name, city.been_to]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return results