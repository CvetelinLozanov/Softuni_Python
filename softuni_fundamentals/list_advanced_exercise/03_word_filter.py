def word_filter_by_even_length():
    text = [word for word in input().split() if len(word) % 2 == 0]
    return '\n'.join(text)


print(word_filter_by_even_length())