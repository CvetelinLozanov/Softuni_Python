def forecast(*args):
    locations_weather = {}

    for arg in args:
        city = arg[0]
        weather = arg[1]

        if weather not in locations_weather:
            locations_weather[weather] = []
        locations_weather[weather].append(city)

    sunny_locations = [f"{location} - {k}" for k, v in locations_weather.items() if k == 'Sunny' for location in
                       sorted(v)]
    cloudy_locations = [f"{location} - {k}" for k, v in locations_weather.items() if k == 'Cloudy' for location in
                       sorted(v)]
    rainy_locations = [f"{location} - {k}" for k, v in locations_weather.items() if k == 'Rainy' for location in
                       sorted(v)]
    result = sunny_locations + cloudy_locations + rainy_locations
    return '\n'.join(result)



print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))