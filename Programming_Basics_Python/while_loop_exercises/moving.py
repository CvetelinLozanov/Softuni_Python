free_width = int(input())
free_length = int(input())
free_height = int(input())

total_free_volume = free_width * free_length * free_height

text = input()

while text != 'Done':
    boxes = int(text)
    total_free_volume -= boxes

    if total_free_volume < 0:
        print(f'No more free space! You need {abs(total_free_volume)} Cubic meters more.')
        break

    text = input()
else:
    print(f'{total_free_volume} Cubic meters left.')