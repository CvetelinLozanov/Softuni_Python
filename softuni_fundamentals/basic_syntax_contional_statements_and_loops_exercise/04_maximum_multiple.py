divisor = int(input())
boundary = int(input())

biggest_num = 0

for num in range(1, boundary + 1):
    if num % divisor == 0:
        biggest_num = num

print(biggest_num)
