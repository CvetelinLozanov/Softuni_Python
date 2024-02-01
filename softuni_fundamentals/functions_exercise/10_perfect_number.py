def is_number_perfect(_number: int):
    divisors_sum = 0
    for num in range(1, _number + 1):
        if _number % num == 0:
            divisors_sum += num

    return divisors_sum / 2 == _number


number = int(input())
if is_number_perfect(number):
    print('We have a perfect number!')
else:
    print("It's not so perfect.")