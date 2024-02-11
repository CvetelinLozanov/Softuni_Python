def decipher():
    words = input().split()
    result = []

    for word in words:
        end_index = 0
        for index, letter in enumerate(word):
            if letter.isalpha():
                end_index = index
                break

        digits_to_replace = int(word[:end_index])
        digit_to_letter = chr(digits_to_replace)
        new_word = digit_to_letter + word[end_index:]
        new_word = list(new_word)
        new_word[1], new_word[-1] = new_word[-1], new_word[1]
        new_word = ''.join(new_word)
        result.append(new_word)

    return ' '.join(result)


print(decipher())