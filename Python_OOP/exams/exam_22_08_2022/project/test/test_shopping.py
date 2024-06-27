from project.shopping_cart import ShoppingCart
import unittest


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.shopping_cart = ShoppingCart("Mentastiko", 10000)

    def test_initializer_with_valid_data(self):
        self.assertEqual("Mentastiko", self.shopping_cart.shop_name)
        self.assertEqual(10000, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_initializer_with_shop_name_only_of_lower_letters(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = 'ewwerwrwrw'

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_initializer_with_shop_name_with_digits(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = 'E432342'

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_method_with_product_price_equal_a_hundred(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart("Minion", 100)

        self.assertEqual("Product Minion cost too much!", str(ve.exception))

    def test_add_to_cart_method_with_product_price_more_than_a_hundred(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart("Minion", 100000)

        self.assertEqual("Product Minion cost too much!", str(ve.exception))

    def test_add_to_cart_method_with_valid_input(self):
        result = self.shopping_cart.add_to_cart("Minion", 50)
        self.assertEqual("Minion product was successfully added to the cart!", result)
        self.assertIn("Minion", self.shopping_cart.products)
        self.assertEqual(50, self.shopping_cart.products["Minion"])

    def test_remove_from_cart_with_non_existing_product(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart("tomato")

        self.assertEqual("No product with name tomato in the cart!", str(ve.exception))

    def test_remove_from_cart_method_with_valid_product(self):
        self.shopping_cart.add_to_cart("Minion", 50)
        self.shopping_cart.add_to_cart("tomato", 10)
        result = self.shopping_cart.remove_from_cart("Minion")
        self.assertEqual("Product Minion was successfully removed from the cart!", result)
        self.assertNotIn("Minion", self.shopping_cart.products)
        self.assertIn("tomato", self.shopping_cart.products)
        self.assertEqual({"tomato": 10}, self.shopping_cart.products)
        self.assertEqual(10, self.shopping_cart.products["tomato"])

    def test_buy_products_method_with_less_budget(self):
        self.shopping_cart.budget = 10
        self.shopping_cart.add_to_cart("Minion", 50)

        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()

        self.assertEqual("Not enough money to buy the products! Over budget with 40.00lv!", str(ve.exception))

    def test_buy_products_with_valid_budget(self):
        self.shopping_cart.add_to_cart("Minion", 50)
        self.shopping_cart.add_to_cart("tomato", 50)

        result = self.shopping_cart.buy_products()
        self.assertEqual("Products were successfully bought! Total cost: 100.00lv.", result)

    def test_add_method(self):
        test_shop = ShoppingCart("Boklucharnikland", 100)
        test_shop.add_to_cart("Minion", 10)
        self.shopping_cart.add_to_cart("tomato", 50)
        new_shop = self.shopping_cart + test_shop

        self.assertEqual(10100, new_shop.budget)
        self.assertEqual("MentastikoBoklucharnikland", new_shop.shop_name)
        self.assertEqual({"Minion": 10, "tomato": 50}, new_shop.products)
        self.assertIn("Minion", new_shop.products)
        self.assertIn("tomato", new_shop.products)


if __name__ == '__main__':
    unittest.main()