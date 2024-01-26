result = []

for _ in range(3):
    result.append(input())

result[0], result[2] = result[2], result[0]

print(result)