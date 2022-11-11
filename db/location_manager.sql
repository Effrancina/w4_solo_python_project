DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS restaurants;


CREATE TABLE city (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    been_to BOOLEAN DEFAULT FALSE
);

CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    cuisine VARCHAR (255),
    tried BOOLEAN DEFAULT FALSE,
    city_id INT REFERENCES city(id)
);

