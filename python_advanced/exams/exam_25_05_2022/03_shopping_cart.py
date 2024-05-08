def shopping_cart(*args):
    meals = {"Soup": [], "Pizza": [], "Dessert": []}
    for arg in args:

        if arg == 'Stop':
            break

        meal = arg[0]
        product = arg[1]

        if meal not in meals:
            meals[meal] = []

        if meal == 'Soup' and len(meals[meal]) < 3:
            if product not in meals[meal]:
                meals[meal].append(product)

        elif meal == 'Pizza' and len(meals[meal]) < 4:
            if product not in meals[meal]:
                meals[meal].append(product)

        elif meal == 'Dessert' and len(meals[meal]) < 2:
            if product not in meals[meal]:
                meals[meal].append(product)

    sorted_meals = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []

    for key, value in sorted_meals:
        result.append(f"{key}:")
        for product in sorted(value):
            result.append(f" - {product}")

    if result:
        return "\n".join(result)
    return "No products in the cart!"



print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))