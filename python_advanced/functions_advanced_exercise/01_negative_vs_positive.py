def get_negative_and_positive_sum(*args):

    positive_numbers = []
    negative_numbers = []

    for num in args:
        if num < 0:
            negative_numbers.append(num)
        else:
            positive_numbers.append(num)

    positive_numbers_sum = sum(positive_numbers)
    negative_numbers_sum = sum(negative_numbers)

    print(negative_numbers_sum)
    print(positive_numbers_sum)

    if abs(negative_numbers_sum) > positive_numbers_sum:
        print('The negatives are stronger than the positives')
    else:
        print('The positives are stronger than the negatives')


numbers = [int(el) for el in input().split()]
get_negative_and_positive_sum(*numbers)
