def which_are_in():
    searched_words = input().split(', ')
    words = input().split(', ')
    substrings = []

    for s_word in searched_words:
        for word in words:
            if s_word in word:
                substrings.append(s_word)
                break

    print(substrings)


which_are_in()