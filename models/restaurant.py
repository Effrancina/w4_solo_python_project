class Restaurant:
    def __init__(self, name, cuisine, city, tried = False, id = None):
        self.name = name
        self.city = city
        self.cuisine = cuisine
        self.tried = tried
        self.id = id