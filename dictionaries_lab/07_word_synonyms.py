count_of_words = int(input())
synonyms = {}

for _ in range(count_of_words):
    word = input()
    synonym = input()

    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

[print(f"{word} - {', '.join(synonym)}") for word, synonym in synonyms.items()]
