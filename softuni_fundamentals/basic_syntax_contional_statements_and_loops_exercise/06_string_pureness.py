n = int(input())
special_characters = ',_.'
for _ in range(n):
    word = input()

    if any(c in special_characters for c in word):
        print(f'{word} is not pure!')
    else:
        print(f'{word} is pure.')