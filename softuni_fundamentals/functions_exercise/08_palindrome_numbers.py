from typing import List


def palindrome_integers(numbers: List[str]):

    result = []
    for num in numbers:
        is_palindrome = 'True'
        for index in range(len(num) // 2):
            if num[0 + index] != num[-1 - index]:
                is_palindrome = 'False'
                break
        result.append(is_palindrome)
    return '\n'.join(result)


integers = input().split(', ')
print(palindrome_integers(integers))