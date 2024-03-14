import re

text = input()
searched_word = input()

matches = re.findall(searched_word, text, re.I)

print(len(matches))