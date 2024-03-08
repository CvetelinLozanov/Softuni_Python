from typing import List
import re


def process_input():
    return [s for s in input().split() if s.strip() != '']


def process_number_with_first_letter(first_letter: str, number: float):
    sum = 0
    if first_letter.isupper():
        letter_number = ord(first_letter) - 64
        sum = number / letter_number
    elif first_letter.islower():
        letter_number = ord(first_letter) - 96
        sum = number * letter_number

    return sum


def process_number_with_last_letter(last_letter: str, number: float):
    sum = 0
    if last_letter.isupper():
        letter_number = ord(last_letter) - 64
        sum = number - letter_number
    elif last_letter.islower():
        letter_number = ord(last_letter) - 96
        sum = number + letter_number

    return sum


def process_operations(total_numbers_: List[int], text_: List[str]):
    p = re.compile("([0-9]+)")
    sum = 0
    for word in text_:
        digits = p.search(word)
        number = float(digits.group(1))
        first_letter = word[0]
        last_letter = word[-1]
        sum = process_number_with_first_letter(first_letter, number)
        sum = process_number_with_last_letter(last_letter, sum)
        total_numbers_.append(sum)



total_numbers = []
text = process_input()
process_operations(total_numbers, text)
print(f'{sum(total_numbers):.2f}')
