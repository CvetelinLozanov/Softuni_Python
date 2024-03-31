import re


def decrypt_message(matches):
    text_with_numbers = matches[0][2]
    pattern = r'\d+'
    digits_matches = re.findall(pattern, text_with_numbers)
    message = ''
    for digit in digits_matches:
        message += chr(int(digit))

    tag = matches[0][1]
    return f'{tag}: {message}'


num_of_lines = int(input())
pattern = r'^([$]|[%])([A-Z][a-z]{2,})\1:\s((\[[0-9]+\][|]){3})$'
for _ in range(num_of_lines):
    command = input()

    matches = re.findall(pattern, command)
    if matches:
        print(decrypt_message(matches))
    else:
        print('Valid message not found!')
