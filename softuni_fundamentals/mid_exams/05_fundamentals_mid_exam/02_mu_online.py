def process_rooms(initial_health, bitcoins, dungeons_rooms):
    is_dead = False
    for room_number, room in enumerate(dungeons_rooms, start=1):
        command, number = room.split()
        number = int(number)
        if command == 'potion':
            current_health = initial_health
            initial_health += number
            if initial_health > 100:
                initial_health = 100
            healed_amount = initial_health - current_health
            print(f'You healed for {healed_amount} hp.')
            print(f'Current health: {initial_health} hp.')

        elif command == 'chest':
            print(f'You found {number} bitcoins.')
            bitcoins += number

        else:
            initial_health -= number

            if initial_health > 0:
                print(f'You slayed {command}.')
            else:
                print(f'You died! Killed by {command}.')
                print(f'Best room: {room_number}')
                is_dead = True
                break

    if not is_dead:
        print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {initial_health}")


def main():
    initial_health = 100
    bitcoins = 0
    dungeons_rooms = input().split('|')
    process_rooms(initial_health, bitcoins, dungeons_rooms)


if __name__ == '__main__':
    main()
