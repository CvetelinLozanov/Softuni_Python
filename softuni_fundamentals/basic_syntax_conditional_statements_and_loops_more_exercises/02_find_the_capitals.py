word = input()

capital_letter_indexes = []

for index in range(len(word)):
    if word[index].isupper():
        capital_letter_indexes.append(index)


print(capital_letter_indexes)