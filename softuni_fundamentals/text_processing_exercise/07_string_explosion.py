def is_valid_index(index, text):
    return 0 <= index < len(text)


def process_bomb_explosion(bomb_strength, index, text):
    counter = 0
    while counter < bomb_strength:
        if index >= len(text):
            break

        if text[index] == '>':
            index += 1
            bomb_strength += int(text[index])

        if is_valid_index(index, text):
            text.pop(index)
        counter += 1

    return index - 1, text


def process_explosions(text):
    text = list(text)
    index = 0
    while index < len(text):
        if text[index] == '>':
            bomb_strength = int(text[index + 1])
            index, text = process_bomb_explosion(bomb_strength, index + 1, text)
        index += 1
    return text


text = input()
text = process_explosions(text)
print(''.join(text))