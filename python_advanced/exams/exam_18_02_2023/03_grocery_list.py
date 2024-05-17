from typing import List


def shop_from_grocery_list(budget: int, grocery_list: List[str],  *args):
    bought_products = []

    for arg in args:
        product_name = arg[0]
        product_price = float(arg[1])
        if product_name not in grocery_list or product_price > budget:
            continue

        if product_price <= budget:
            bought_products.append(product_name)
            grocery_list.remove(product_name)
            budget -= product_price
        else:
            break

    if grocery_list:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."
    else:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."




print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))