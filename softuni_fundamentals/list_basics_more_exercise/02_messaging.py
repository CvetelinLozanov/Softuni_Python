numbers = [num for num in input().split()]
text = list(input())
final_word = ''

numbers_sum = 0

for number in numbers:
    text_length = len(text)
    for index in range(len(number)):
        numbers_sum += int(number[index])
    index_to_remove = numbers_sum % text_length
    final_word += text[index_to_remove]
    text.pop(index_to_remove)
    numbers_sum = 0

print(final_word)
