import unittest
from exams.exam_16_04_2024.project.restaurant import Restaurant


class RestaurantTest(unittest.TestCase):
    def setUp(self):
        self.restaurant = Restaurant("some_name", 10)

    def test_correct_initializing(self):
        self.assertEqual("some_name", self.restaurant.name)
        self.assertEqual(10, self.restaurant.capacity)
        self.assertEqual([], self.restaurant.waiters)

    def test_initializing_with_empty_name(self):

        with self.assertRaises(ValueError) as ve:
            test_restaurant = Restaurant('', 100)

        self.assertEqual("Invalid name!", str(ve.exception))

    def test_initializing_with_none_name(self):

        with self.assertRaises(ValueError) as ve:
            test_restaurant = Restaurant(None, 100)

        self.assertEqual("Invalid name!", str(ve.exception))

    def test_initializing_with_negative_capacity(self):
        with self.assertRaises(ValueError) as ve:
            test_restaurant = Restaurant("some_name", -100)

        self.assertEqual("Invalid capacity!", str(ve.exception))

    def test_add_waiter_with_new_waiter(self):
        result = self.restaurant.add_waiter("Ivan")
        self.assertIn("Ivan", [waiter['name'] for waiter in self.restaurant.waiters])
        self.assertEqual("The waiter Ivan has been added.", result)

    def test_add_waiter_with_existing_waiter(self):
        self.restaurant.waiters.append({'name': "Ivan"})

        result = self.restaurant.add_waiter("Ivan")
        self.assertEqual("The waiter Ivan already exists!", result)
        self.assertEqual(1, len(self.restaurant.waiters))

    def test_add_waiter_with_no_capacity(self):
        self.restaurant.capacity = 1
        self.restaurant.add_waiter("Ivan")

        result = self.restaurant.add_waiter("Pesho")
        self.assertEqual("No more places!", result)

    def test_remove_waiter_with_valid_waiter(self):
        self.restaurant.add_waiter("Ivan")
        result = self.restaurant.remove_waiter("Ivan")
        self.assertNotIn("Ivan", [waiter['name'] for waiter in self.restaurant.waiters])
        self.assertEqual("The waiter Ivan has been removed.", result)

    def test_remove_waiter_with_invalid_name(self):
        result = self.restaurant.remove_waiter("Ivan")
        self.assertEqual("No waiter found with the name Ivan.", result)

    def test_get_total_earnings(self):
        self.restaurant.add_waiter("Ivan")
        result = self.restaurant.get_total_earnings()
        self.assertEqual(0, result)

    def test_get_total_earnings_with_value(self):
        self.restaurant.waiters.append({"name": "Ivan", "total_earnings": 1000})
        self.restaurant.waiters.append({"name": "Pesho", "total_earnings": 1000})
        self.assertEqual(2000, self.restaurant.get_total_earnings())

    def test_get_waiters(self):
        self.restaurant.waiters.append({"name": "Ivan", "total_earnings": 1000})
        self.restaurant.waiters.append({"name": "Pesho", "total_earnings": 1000})
        result = self.restaurant.get_waiters(10, 10)
        self.assertEqual([], result)

    def test_get_waiters_with_zero_earnings(self):
        self.restaurant.waiters.append({"name": "Ivan"})
        self.restaurant.waiters.append({"name": "Pesho"})
        result = self.restaurant.get_waiters(10, 10)
        self.assertEqual([], result)

    def test_get_waiters_with_valid_earnings(self):
        self.restaurant.waiters.append({"name": "Ivan", "total_earnings": 1000})
        self.restaurant.waiters.append({"name": "Pesho"})
        result = self.restaurant.get_waiters(10, 1100)
        self.assertIn("Ivan", [waiter['name'] for waiter in result])

    def test_get_waiters_with_none_value(self):
        self.restaurant.waiters.append({"name": "Ivan", "total_earnings": 1000})
        self.restaurant.waiters.append({"name": "Pesho"})
        result = self.restaurant.get_waiters()
        self.assertIn("Ivan", [waiter['name'] for waiter in result])
        self.assertIn("Pesho", [waiter['name'] for waiter in result])

    def test_get_waiters_with_max_earnings_none_value(self):
        self.restaurant.waiters.append({"name": "Ivan", "total_earnings": 1000})
        self.restaurant.waiters.append({"name": "Pesho"})
        result = self.restaurant.get_waiters(10)
        self.assertIn("Ivan", [waiter['name'] for waiter in result])
        self.assertNotIn("Pesho", [waiter['name'] for waiter in result])

    def test_get_waiters_with_min_earnings_none_value(self):
        self.restaurant.waiters.append({"name": "Ivan", "total_earnings": 1000})
        self.restaurant.waiters.append({"name": "Pesho"})
        result = self.restaurant.get_waiters(min_earnings=None, max_earnings=10000)
        self.assertIn("Ivan", [waiter['name'] for waiter in result])
        self.assertIn("Pesho", [waiter['name'] for waiter in result])

if __name__ == '__main__':
    unittest.main()