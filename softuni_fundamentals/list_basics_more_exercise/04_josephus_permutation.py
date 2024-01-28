numbers = [int(num) for num in input().split()]
person_to_execute = int(input())
initial_length = len(numbers)
result_list = []
#counter = 1
counter = 0
index = 0

while len(numbers) > 0:
    counter += 1
    if counter % person_to_execute == 0:
        result_list.append(numbers.pop(index))
    else:
        index += 1

    if index >= len(numbers):
        index = 0
    # if counter >= initial_length:
    #     initial_length = len(numbers)
    #     counter = counter % person_to_execute
    #
    # index += 1
    # counter += 1
    #
    # if index == initial_length:
    #     index = 0
    # elif index > initial_length:
    #     index = index - initial_length


print(f"[{','.join([str(result) for result in result_list])}]")