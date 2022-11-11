import pdb

from models.city import City
import repositories.city_repository as city_repository

from models.restaurant import Restaurant
import repositories.restaurant_repository as restaurant_repository

city_repository.delete_all()
restaurant_repository.delete_all()

city_1 = City('Seoul', True)
city_repository.save(city_1)

city_2 = City('Jeonju', False)
city_repository.save(city_2)

city_3 = City('Hwaseong', False)
city_repository.save(city_3)

city_4 = City('Busan', False)
city_repository.save(city_4)



restaurant_1 = Restaurant('Plant Cafe', 'Western vegan', city_1, True)
restaurant_repository.save(restaurant_1)

restaurant_2 = Restaurant('Vegetus', 'Asian vegan', city_1, False)
restaurant_repository.save(restaurant_2)

restaurant_3 = Restaurant('Present', 'Asian vegan', city_2, False)
restaurant_repository.save(restaurant_3)

restaurant_4 = Restaurant('Pool', 'Korean vegan', city_2, False)
restaurant_repository.save(restaurant_4)

restaurant_5 = Restaurant('Vreeze', 'Vegan bakery', city_3, False)
restaurant_repository.save(restaurant_5)

restaurant_6 = Restaurant('Pyeonhan Jipbap', 'Vegan Korean comfort food', city_4, False)
restaurant_repository.save(restaurant_6)

restaurant_7 = Restaurant('Dajeon Cafe', 'Asian vegan', city_4, False)
restaurant_repository.save(restaurant_7)

restaurant_7 = Restaurant('April and mAY 45', 'Asian vegan', city_4, False)
restaurant_repository.save(restaurant_7)

restaurant_7 = Restaurant('Vegenarang', 'Korean temple-style vegan', city_4, False)
restaurant_repository.save(restaurant_7)

pdb.set_trace()