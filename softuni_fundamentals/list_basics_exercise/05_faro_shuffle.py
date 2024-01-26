cards = input().split()
number_of_shuffles = int(input())
counter = 0

for _ in range(number_of_shuffles):
    for index in range(1, len(cards) - 1, 2):
        num = cards.pop(len(cards) // 2 + counter)
        cards.insert(index, num)
        counter += 1

    counter = 0

print(cards)
