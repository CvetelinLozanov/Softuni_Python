from project.second_hand_car import SecondHandCar
from unittest import main, TestCase


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar("fairlane", "sedan", 300_000, 10_000)

    def test_initializer_with_valid_data(self):
        self.assertEqual("fairlane", self.car.model)
        self.assertEqual("sedan", self.car.car_type)
        self.assertEqual(300_000, self.car.mileage)
        self.assertEqual(10_000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_initializer_with_price_less_than_one(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0

        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_initializer_with_mileage_less_than_one_hundred(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 50

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_initializer_with_mileage_equal_to_one_hundred(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price_method_with_new_price_greater_than_current_price(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(100000000)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_method_with_new_price_equal_to_current_price(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(10000)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_method_with_correct_new_price(self):
        result = self.car.set_promotional_price(8000)
        self.assertEqual(8000, self.car.price)
        self.assertEqual('The promotional price has been successfully set.', result)

    def test_need_repair_method_with_bigger_repair_price(self):
        result = self.car.need_repair(100000000000, "Retrofit")
        self.assertEqual('Repair is impossible!', result)

    def test_need_repair_method_with_good_repair_price(self):
        result = self.car.need_repair(500, 'The oil and all filters have been changed')
        self.assertEqual('Price has been increased due to repair charges.', result)
        self.assertIn('The oil and all filters have been changed', self.car.repairs)
        self.assertEqual(10500, self.car.price)
        self.assertEqual(1, len(self.car.repairs))

    def test__gt__method_with_different_car_types(self):
        test_car = SecondHandCar("Niva", "SUV", 10000000, 20000)
        result = test_car > self.car
        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test__gt__method_with_same_car_types(self):
        test_car = SecondHandCar("Avensis", "sedan", 10000, 25000)
        result = test_car > self.car
        self.assertTrue(result)
        self.assertFalse(self.car > test_car)

    def test__str__method(self):
        expected_result = """Model fairlane | Type sedan | Milage 300000km
Current price: 10000.00 | Number of Repairs: 0"""
        self.assertEqual(str(self.car), expected_result)
        result = self.car.need_repair(500, 'The oil and all filters have been changed')
        expected_result = """Model fairlane | Type sedan | Milage 300000km
Current price: 10500.00 | Number of Repairs: 1"""
        self.assertEqual(str(self.car), expected_result)


if __name__ == '__main__':
    main()
