from typing import List
import re


def process_text(text_: List[str]):
    current_index = 0
    result = ''
    #p = re.findall("[0-9]+", text_)
    for index in range(len(text_)):
        if index < len(text_) - 1 and text_[index].isdigit() and text[index + 1].isdigit():
            times_to_repeat = int(str(text_[index]) + str(text_[index + 1]))
            text_to_add = ''.join(text_[current_index:index] * times_to_repeat)
            result += text_to_add
            current_index = index + 2
        elif text[index].isdigit():
            times_to_repeat = int(text_[index])
            text_to_add = ''.join(text_[current_index:index] * times_to_repeat)
            result += text_to_add
            current_index = index + 1

    return result


def get_unique_symbols_count(rage_message: str):
    return len(set(list(rage_message)))



text = [ch.upper() for ch in list(input())]
rage_message = process_text(text)
unique_symbols_count = get_unique_symbols_count(rage_message)
print(f'Unique symbols used: {unique_symbols_count}')
print(rage_message)