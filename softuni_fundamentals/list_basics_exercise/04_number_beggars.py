numbers = [int(num) for num in input().split(', ')]
number_of_beggars = int(input())
beggars = [0 for _ in range(number_of_beggars)]

for index, num in enumerate(numbers):
    beggars[index % number_of_beggars] += num

print(beggars)