while True:
    word = input()

    if word == 'End':
        break

    if word == 'SoftUni':
        continue

    for ch in word:
        print(ch * 2, end='')

    print()
