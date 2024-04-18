def cookbook(*args):
    cookbook_info = {}
    for arg in args:
        recipe_name = arg[0]
        cuisine = arg[1]
        ingredients = arg[2]

        if cuisine not in cookbook_info:
            cookbook_info[cuisine] = {}
        if recipe_name not in cookbook_info[cuisine]:
            cookbook_info[cuisine][recipe_name] = ingredients
        else:
            cookbook_info[cuisine][recipe_name].update(ingredients)

    sorted_cookbook = dict(sorted(cookbook_info.items(), key=lambda x: (-len(x[1]), x[0])))
    for cuisine, recipes in sorted_cookbook.items():
        sorted_recipes = dict(sorted(recipes.items(), key=lambda x: x[0]))
        sorted_cookbook[cuisine] = sorted_recipes

    result = []
    for cuisine, recipes in sorted_cookbook.items():
        result.append(f'{cuisine} cuisine contains {len(recipes)} recipes:')
        for recipe, ingredients in recipes.items():
            ingredients_info = ', '.join(ingredients)
            result.append(f'  * {recipe} -> Ingredients: {ingredients_info}')

    return "\n".join(result)


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))


from unittest import TestCase, main


class Test(TestCase):
    def test_cookbook(self):
        result = cookbook(
            ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
            ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
            ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
            ("Croissant", "French", ["flour", "butter", "yeast"]),
            ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
        )

        expected = """Italian cuisine contains 3 recipes:
  * Margherita Pizza -> Ingredients: pizza dough, tomato sauce, mozzarella
  * Spaghetti Bolognese -> Ingredients: spaghetti, tomato sauce, ground beef
  * Tiramisu -> Ingredients: ladyfingers, mascarpone, coffee
French cuisine contains 2 recipes:
  * Croissant -> Ingredients: flour, butter, yeast
  * Ratatouille -> Ingredients: eggplant, zucchini, tomatoes"""

        self.assertEqual(result.strip(), expected)

if __name__ == '__main__':
    main()