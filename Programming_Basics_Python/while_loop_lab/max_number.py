from sys import maxsize

biggest_number = -maxsize
input_text = input()
while input_text != 'Stop':
    number = int(input_text)

    if number > biggest_number:
        biggest_number = number

    input_text = input()

print(biggest_number)