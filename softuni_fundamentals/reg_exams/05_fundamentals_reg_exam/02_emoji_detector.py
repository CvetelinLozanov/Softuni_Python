import re
from functools import reduce
from typing import List


def calculate_threshold(text_: str) -> int:
    pattern = r'[0-9]'
    numbers = [int(num) for num in re.findall(pattern, text_)]
    return reduce(lambda a, b: a * b, numbers)


def get_emojis(text_: str) -> List[str]:
    pattern = r'([:]{2}|[*]{2})([A-Z][a-z]{2,})\1'
    matches = re.findall(pattern, text_)
    return matches


def calculate_emoji_threshold(emoji_: str):
    threshold = 0
    for letter in emoji_:
        threshold += ord(letter)

    return threshold


def fill_cool_emojis(cool_emojis_: List[str], emojis_: List[str], cool_threshold_: int) -> List[str]:
    for emoji in emojis_:
        emoji_threshold = calculate_emoji_threshold(emoji[1])
        if emoji_threshold >= cool_threshold_:
            cool_emojis_.append(emoji)

    return cool_emojis_


def print_result(cool_threshold_: int, emojis_: List[str], cool_emojis_: List[str]):
    print(f'Cool threshold: {cool_threshold_}')
    print(f'{len(emojis_)} emojis found in the text. The cool ones are:')
    if cool_emojis_:
        [print(f'{emoji[0]}{emoji[1]}{emoji[0]}') for emoji in cool_emojis_]


text = input()
cool_emojis = []
cool_threshold = calculate_threshold(text)
emojis = get_emojis(text)
fill_cool_emojis(cool_emojis, emojis, cool_threshold)
print_result(cool_threshold, emojis, cool_emojis)