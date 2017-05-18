"""
Exercício 5
Autor: Lucien Constantino
"""

class City():
    def __int__(self, code, passenger_cars, traffic_accidents_with_victim):
        self.code = code
        self.passenger_cars = passenger_cars
        self.traffic_accidents_with_victim = traffic_accidents_with_victim

    def __eq__(self, other):
        return (self.code == other.code and
                self.passenger_cars == other.passenger_cars and
                self.traffic_accidents_with_victim == other.traffic_accidents_with_victim)


# INPUT
def get_positive_integer_number(msg):
    while True:
        n = int(input(msg))
        if n < 0:
            print("Número deve ser positivo")
        else:
            return n


cities: [City] = []
for i in range(5):
    city_code = get_positive_integer_number("Digite o código da cidade: ")
    passenger_cars = get_positive_integer_number("Digite o número de veículos de passeio: ")
    traffic_accidents_with_victim = get_positive_integer_number("Digite o número de acidentes de trânsito com vítima: ")

    city = City(city_code,
                passenger_cars,
                traffic_accidents_with_victim)
    cities.append(city)


def city_with_most_traffic_accidents(cities: [City]):
    target_city: City = cities[0]
    for city in cities:
        if city.traffic_accidents_with_victim > target_city.traffic_accidents_with_victim:
            target_city = city
    return target_city


def city_with_least_traffic_accidents(cities: [City]):
    target_city: City = cities[0]
    for city in cities:
        if city.traffic_accidents_with_victim < target_city.traffic_accidents_with_victim:
            target_city = city
    return target_city


def average_number_of_passenger_cars(cities: [City]):
    total_passenger_cars = 0
    for city in cities:
        total_passenger_cars += city.passenger_cars
    return total_passenger_cars / len(cities)


def average_traffic_accidents_in_cities_with_less_then_twok_cars(cities: [City]):
    traffic_accidents = 0
    cities = 0
    for city in cities:
        if city.passenger_cars < 2000:
            traffic_accidents += city.traffic_accidents_with_victim
            cities += 1

    return traffic_accidents / cities

# TESTING

# city1 = City(1, 100, 50)
# city2 = City(2, 1000, 20)
# city3 = City(3, 10000, 700)
#
# cities = [city1, city2, city3]
# assert city_with_least_traffic_accidents(cities) == city2
# assert city_with_most_traffic_accidents(cities) == city3
# assert average_number_of_passenger_cars(cities) == (100 + 1000 + 10000) / 3.0
# assert average_traffic_accidents_in_cities_with_less_then_twok_cars(cities) == (50 + 20) / 2.0
