from typing import List


def count_chars_in_a_string(text: List[str]):
    chars = {}

    for char in text:
        if char == ' ':
            continue
        if char not in chars:
            chars[char] = 0

        chars[char] += 1

    return chars


text = list(input())
result_dict = count_chars_in_a_string(text)

[print(f"{char} -> {count}") for char, count in result_dict.items()]