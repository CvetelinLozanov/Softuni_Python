best_player = ''
player_goals = 0

hattrick = False
command = input()

while command != 'END':
    goals = int(input())

    if goals >= 10:
        print(f'{command} is the best player!')
        print(f'He has scored {goals} goals and made a hat-trick !!!')
        break

    if goals > player_goals:

        if goals >= 3:
            hattrick = True

        best_player = command
        player_goals = goals

    command = input()

else:
    print(f'{best_player} is the best player!')

    if hattrick:
        print(f'He has scored {player_goals} goals and made a hat-trick !!!')

    else:
        print(f'He has scored {player_goals} goals.')