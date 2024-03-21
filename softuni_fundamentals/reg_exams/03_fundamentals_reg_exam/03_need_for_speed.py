from typing import Dict


def fill_garage(garage: Dict[str, Dict], number_of_cars: int):
    for _ in range(number_of_cars):
        car, mileage, fuel = input().split('|')
        mileage = int(mileage)
        fuel = int(fuel)
        if car not in garage:
            garage[car] = {}
            garage[car]['mileage'] = mileage
            garage[car]['fuel'] = fuel


def process_commands(garage: Dict[str, Dict]):
    while True:
        text = input()

        if text == 'Stop':
            return garage

        command_args = text.split(' : ')

        if command_args[0] == 'Drive':
            car = command_args[1]
            distance = int(command_args[2])
            fuel = int(command_args[3])
            if car in garage:
                if garage[car]['fuel'] < fuel:
                    print('Not enough fuel to make that ride')
                else:
                    garage[car]['fuel'] -= fuel
                    garage[car]['mileage'] += distance
                    print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')

                if garage[car]['mileage'] >= 100_000:
                    print(f'Time to sell the {car}!')
                    del garage[car]

        elif command_args[0] == 'Refuel':
            car = command_args[1]
            fuel = int(command_args[2])
            if car in garage:
                current_fuel = garage[car]['fuel']
                if garage[car]['fuel'] + fuel > 75:
                    garage[car]['fuel'] = 75
                else:
                    garage[car]['fuel'] += fuel

                print(f'{car} refueled with {garage[car]["fuel"] - current_fuel} liters')

        elif command_args[0] == 'Revert':
            car = command_args[1]
            kilometers = int(command_args[2])
            if car in garage:
                if garage[car]['mileage'] - kilometers < 10000:
                    garage[car]['mileage'] = 10000
                else:
                    garage[car]['mileage'] -= kilometers
                    print(f'{car} mileage decreased by {kilometers} kilometers')


def print_cars_in_garage(garage:Dict[str, Dict]):
    for car, car_info in garage.items():
        print(f'{car} -> Mileage: {garage[car]["mileage"]} kms, Fuel in the tank: {garage[car]["fuel"]} lt.')


number_of_cars = int(input())

garage = {}

fill_garage(garage, number_of_cars)
garage = process_commands(garage)
print_cars_in_garage(garage)