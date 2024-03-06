searched_word = input()
word = input()

while searched_word in word:
    word = word.replace(searched_word, '')

print(word)