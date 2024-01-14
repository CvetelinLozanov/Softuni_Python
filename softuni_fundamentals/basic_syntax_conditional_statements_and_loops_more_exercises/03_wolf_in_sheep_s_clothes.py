animals = [animal for animal in reversed(input().split(', '))]

sheep_index = 0

for index in range(len(animals)):
    if animals[index] == 'wolf':
        sheep_index = index


if sheep_index == 0:
    print('Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number {sheep_index}! You are about to be eaten by a wolf!')