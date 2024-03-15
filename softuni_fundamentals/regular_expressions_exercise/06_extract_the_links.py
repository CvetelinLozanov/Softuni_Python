import re


def read_input():
    text = ''
    while True:
        line = input()
        if line:
            text += line + '\n'
        else:
            break

    return text


def main():
    text = read_input()
    pattern = r'(www)\.([A-Za-z0-9-]+)(\.([a-z]+)+)?(\.[a-z]+)((\.[a-z]+)+)?'
    compiled_regex = re.compile(pattern, re.DOTALL | re.MULTILINE)
    matches = compiled_regex.finditer(text)

    for match in matches:
        print(match.group())


if __name__ == '__main__':
    main()
