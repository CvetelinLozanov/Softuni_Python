from math import ceil, floor


def main():
    budget = float(input())
    students = float(input())
    price_for_package_flour = float(input())
    price_for_single_egg = float(input())
    price_for_single_apron = float(input())
    free_flour = 0
    apron_number = ceil(students * 1.20)
    aprons_needed_price = price_for_single_apron * apron_number
    eggs_needed_price = (price_for_single_egg * 10) * students
    if students >= 5:
        free_flour = floor(students / 5)
    flour_needed_price = price_for_package_flour * (students - free_flour)

    total_price = aprons_needed_price + eggs_needed_price + flour_needed_price

    if budget >= total_price:
        print(f'Items purchased for {total_price:.2f}$.')
    else:
        print(f'{total_price - budget:.2f}$ more needed.')


if __name__ == '__main__':
    main()