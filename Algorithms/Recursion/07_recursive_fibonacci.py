def calc_fib(number):
    if number <= 1:
        return 1
    return calc_fib(number - 1) + calc_fib(number - 2)


fib0 = 1
fib1 = 1

n = int(input())
print(calc_fib(n))