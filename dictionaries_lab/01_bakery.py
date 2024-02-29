from typing import List


def make_dictionary_with_products(products_: List[str]):
    stocks_in_bakery = {}
    for index in range(0, len(products_), 2):
        product = products_[index]
        quantity = int(products_[index + 1])
        stocks_in_bakery[product] = quantity

    return stocks_in_bakery


products = input().split()
bakery_stocks = make_dictionary_with_products(products)
print(bakery_stocks)

