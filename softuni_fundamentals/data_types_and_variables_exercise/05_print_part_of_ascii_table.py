start_num = int(input())
end_num = int(input())

symbols = []

for num in range(start_num, end_num + 1):
    symbols.append(chr(num))

print(*symbols)