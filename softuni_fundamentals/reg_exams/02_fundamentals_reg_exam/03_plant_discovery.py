from typing import Dict, List


def fill_plants_information(plants_: Dict, n: int):
    for _ in range(n):
        plant, rarity = input().split('<->')
        if plant not in plants_:
            plants_[plant] = {}
            plants_[plant]['raiting'] = []
        plants_[plant]['rarity'] = rarity

    return plants_


def process_commands(plants):
    while True:
        text = input()

        if text == 'Exhibition':
            return plants

        command_args = text.split(': ')

        if command_args[0] == 'Rate':
            plant = command_args[1].split(' - ')[0]
            raiting = float(command_args[1].split(' - ')[1])
            if plant in plants:
                plants[plant]['raiting'].append(raiting)
            else:
                print('error')

        elif command_args[0] == 'Update':
            plant = command_args[1].split(' - ')[0]
            rarity = command_args[1].split(' - ')[1]
            if plant in plants:
                plants[plant]['rarity'] = rarity
            else:
                print('error')

        elif command_args[0] == 'Reset':
            plant = command_args[1]
            if plant in plants:
                plants[plant]['raiting'].clear()
            else:
                print('error')


def print_plants(plants: Dict):
    print('Plants for the exhibition:')
    for plant, plant_info in plants.items():
        plant_raiting = sum(plants[plant]["raiting"]) / len(plants[plant]["raiting"]) if plants[plant]["raiting"] else 0
        print(f'- {plant}; Rarity: {plants[plant]["rarity"]}; Rating: {plant_raiting:.2f}')


def main():
    n = int(input())
    plants = {}
    plants = fill_plants_information(plants, n)
    plants = process_commands(plants)
    print_plants(plants)


if __name__ == '__main__':
    main()