n = int(input()) + 1

even_set = set()
odd_set = set()

for number in range(1, n):
    name = input()
    letters_sum = 0

    for letter in name:
        letters_sum += ord(letter)

    letters_sum //= number

    if letters_sum % 2 == 0:
        even_set.add(letters_sum)

    else:
        odd_set.add(letters_sum)


even_set_sum = sum(even_set)
odd_set_sum = sum(odd_set)

if even_set_sum == odd_set_sum:
    union_set = even_set | odd_set
    print(', '.join([str(item) for item in union_set]))

elif odd_set_sum > even_set_sum:
    diff_set = odd_set - even_set
    print(', '.join([str(item) for item in diff_set]))

elif even_set_sum > odd_set_sum:
    sym_diff_set = even_set ^ odd_set
    print(', '.join([str(item) for item in sym_diff_set]))