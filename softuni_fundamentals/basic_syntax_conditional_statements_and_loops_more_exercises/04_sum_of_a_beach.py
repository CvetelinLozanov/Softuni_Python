txt = input().lower()
searched_words = ["Sand", "Water", "Fish", "Sun"]

word_counter = 0

for word in searched_words:
    for index, letter in enumerate(txt):
        if word.lower()[0] == letter:
            cur_word = txt[index:index + len(word)]
            if cur_word == word.lower():
                word_counter += 1

print(word_counter)

