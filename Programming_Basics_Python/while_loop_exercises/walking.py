text = input()
steps = 0

while True:
    if text == 'Going home':
        steps += int(input())
        if steps < 10000:
            print(f'{abs(steps - 10000)} more steps to reach goal.')
            break
        else:
            print(f'Goal reached! Good job!\n{abs(steps - 10000)} steps over the goal!')
            break

    steps += int(text)

    if steps >= 10000:
        print(f'Goal reached! Good job!\n{abs(steps - 10000)} steps over the goal!')
        break
    text = input()