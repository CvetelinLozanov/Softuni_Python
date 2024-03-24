def fill_cities(cities_):
    while True:
        text = input()
        if text == 'Sail':
            return cities_

        city, population, gold = text.split('||')
        population = int(population)
        gold = int(gold)

        if city not in cities_:
            cities_[city] = {}
            cities_[city]['population'] = population
            cities_[city]['gold'] = gold
        else:
            cities_[city]['population'] += population
            cities_[city]['gold'] += gold


def plunder_city(cities, town, people, gold):
    if town in cities:
        cities[town]['population'] -= people
        cities[town]['gold'] -= gold
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')

        if cities[town]['population'] <= 0 or cities[town]['gold'] <= 0:
            print(f'{town} has been wiped off the map!')
            del cities[town]

        return cities


def prosper_city(cities, town, gold):
    if gold <= 0:
        print('Gold added cannot be a negative number!')
        return cities

    cities[town]['gold'] += gold
    print(f'{gold} gold added to the city treasury. {town} now has {cities[town]["gold"]} gold.')
    return cities


def print_result(cities):
    if cities:
        print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
        for city, city_info in cities.items():
            print(f'{city} -> Population: {cities[city]["population"]} citizens, Gold: {cities[city]["gold"]} kg')
    else:
        print('Ahoy, Captain! All targets have been plundered and destroyed!')


cities = {}
cities = fill_cities(cities)
while True:
    text = input()

    if text == 'End':
        break

    command_args = text.split('=>')

    if command_args[0] == 'Plunder':
        town = command_args[1]
        people = int(command_args[2])
        gold = int(command_args[3])
        cities = plunder_city(cities, town, people, gold)

    elif command_args[0] == 'Prosper':
        town = command_args[1]
        gold = int(command_args[2])
        cities = prosper_city(cities, town, gold)

print_result(cities)
