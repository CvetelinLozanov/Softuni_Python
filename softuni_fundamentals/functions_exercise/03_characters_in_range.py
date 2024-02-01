def print_characters_in_range(first_char: str, second_char: str) -> str:
    first_char_to_num = ord(first_char) + 1
    second_char_to_num = ord(second_char)
    result_characters = []
    for char in range(first_char_to_num, second_char_to_num):
        result_characters.append(chr(char))

    return ' '.join(result_characters)


first_character = input()
second_character = input()
print(print_characters_in_range(first_character, second_character))