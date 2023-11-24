from sys import maxsize

smallest_number = maxsize
input_text = input()
while input_text != 'Stop':
    number = int(input_text)

    if number < smallest_number:
        smallest_number = number

    input_text = input()

print(smallest_number)