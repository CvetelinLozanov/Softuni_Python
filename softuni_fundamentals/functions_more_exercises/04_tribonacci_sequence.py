def print_fibonacci(number: int):
    result = [0, 1]
    first_num = 0
    second_num = 1
    sum = 0

    for num in range(2, number):
        sum = first_num + second_num
        first_num = second_num
        second_num = sum
        result.append(sum)

    return ' '.join(map(str, result))


def tribonacci_sequence(def_num):
    sequence = [1]
    for i in range(1, def_num):
        if len(sequence) < 3:
            sequence.append(i)
        else:
            sequence.append(sum(sequence[-3:]))
    return ' '.join([str(num) for num in sequence])


number = int(input())
print(tribonacci_sequence(number))
