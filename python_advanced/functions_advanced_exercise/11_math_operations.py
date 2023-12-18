def math_operations(*args, **kwargs):
    counter = 1
    for num in args:
        if counter == 1:
            kwargs['a'] += num
        elif counter == 2:
            kwargs['s'] -= num
        elif counter == 3:
            try:
                kwargs['d'] /= num
            except ZeroDivisionError:
                counter += 1
                continue
        elif counter == 4:
            kwargs['m'] *= num

        if counter == 4:
            counter = 0
        counter += 1

    sorted_result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    result = ""

    for k, v in sorted_result:
        result += f'{k}: {v:.1f}\n'

    return (result)



print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print()
print(math_operations(6.0, a=0, s=0, d=5, m=0))