word = input()

letter_counter = {}

for letter in word:

    if letter not in letter_counter:
        letter_counter[letter] = 1

    else:
        letter_counter[letter] += 1

[print(f'{letter}: {count} time/s') for letter,count in sorted(letter_counter.items())]