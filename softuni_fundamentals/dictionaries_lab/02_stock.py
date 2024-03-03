from typing import List, Dict


def make_dictionary_with_products(products_: List[str]):
    stocks_in_bakery = {}
    for index in range(0, len(products_), 2):
        product = products_[index]
        quantity = int(products_[index + 1])
        if product not in stocks_in_bakery:
            stocks_in_bakery[product] = 0
        stocks_in_bakery[product] += quantity

    return stocks_in_bakery


def check_if_product_in_dictionary_with_products(products_: List[str], dict_with_products: Dict[str, int]):
    for prod in products_:
        if prod in dict_with_products:
            print(f"We have {dict_with_products[prod]} of {prod} left")
        else:
            print(f"Sorry, we don't have {prod}")


products = input().split()
products_to_search = input().split()
bakery_stocks = make_dictionary_with_products(products)
check_if_product_in_dictionary_with_products(products_to_search, bakery_stocks)

