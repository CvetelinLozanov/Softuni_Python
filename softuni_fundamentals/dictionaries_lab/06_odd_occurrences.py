words = input().split()
dict_with_words = {}


for word in words:
    if word.lower() not in dict_with_words:
        dict_with_words[word.lower()] = 0
    dict_with_words[word.lower()] += 1

keys = [key for key, value in dict_with_words.items() if value % 2 != 0]

print(' '.join(keys))