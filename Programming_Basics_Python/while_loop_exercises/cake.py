cake_width = int(input())
cake_length = int(input())

total_cake_volume = cake_length * cake_width
text = input()
while text != 'STOP':

    total_cake_volume -= int(text)

    if total_cake_volume < 0:
        print(f'No more cake left! You need {abs(total_cake_volume)} pieces more.')
        break

    text = input()

else:
    print(f'{total_cake_volume} pieces are left.')