first_num = int(input())
second_num = int(input())
number = int(input())


for n in range(first_num , second_num):
    letter = chr(n)
    for nu in range(1, number):
        for num in range(1, number // 2):
            sum_symbols = n + nu + num

            if n % 2 == 1 and sum_symbols % 2 == 1:
                print(f'{letter}-{nu}{num}{ord(letter)}')
