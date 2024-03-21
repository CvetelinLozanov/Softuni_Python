import re

text = input()
pattern = r'([#@])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'
matches = re.findall(pattern, text)

mirror_words = {}

for index in range(len(matches)):
    first_word = matches[index][1]
    second_word = matches[index][2]

    if first_word == second_word[::-1]:
        mirror_words[first_word] = second_word


if matches:
    print(f'{len(matches)} word pairs found!')
else:
    print('No word pairs found!')
if mirror_words:
    print('The mirror words are:')
    print(", ".join(f'{key} <=> {value}'for key, value in mirror_words.items()))
else:
    print('No mirror words!')
