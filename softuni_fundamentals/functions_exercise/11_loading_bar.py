def loading_bar(loading_value: int):
    loading_divisor = loading_value // 10
    status = 'Still loading...'
    return f'{loading_value}% [{"%" * loading_divisor}{"." * (10 - loading_divisor)}]\n{status}' if loading_value != 100 \
        else f'100% Complete!\n[{"%" * loading_divisor}{"." * (10 - loading_divisor)}]'


loading_value = int(input())
print(loading_bar(loading_value))