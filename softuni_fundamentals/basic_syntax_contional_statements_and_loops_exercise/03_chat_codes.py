n = int(input())

for _ in range(n):
    num = input()

    if num == '88':
        print('Hello')

    elif num == '86':
        print('How are you?')

    elif int(num) not in [86, 88] and int(num) < 88:
        print('GREAT!')

    elif int(num) not in [86, 88] and int(num) > 88:
        print('Bye.')
