first_str, second_str = [list(test) for test in input().split()]

smallest_len = min(len(first_str), len(second_str))
result = 0

for index in range(smallest_len):
    result += ord(first_str.pop(0)) * ord(second_str.pop(0))

if first_str:
    for char in first_str:
        result += ord(char)

if second_str:
    for char in second_str:
        result += ord(char)

print(result)
