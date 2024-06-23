from project.truck_driver import TruckDriver
import unittest


class TestTruckDriver(unittest.TestCase):
    def setUp(self):
        self.truck_driver = TruckDriver("Bai Ivan", 100)

    def test_initializer_with_valid_data(self):
        self.assertEqual("Bai Ivan", self.truck_driver.name)
        self.assertEqual(100, self.truck_driver.money_per_mile)
        self.assertEqual({}, self.truck_driver.available_cargos)
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

    def test_earned_money_with_negative_value(self):
        with self.assertRaises(ValueError) as ve:
            self.truck_driver.earned_money = -1

        self.assertEqual("Bai Ivan went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_with_existing_offer(self):
        self.truck_driver.available_cargos = {"Sofia": 100}

        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer("Sofia", 100)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_with_non_existing_offer(self):
        result = self.truck_driver.add_cargo_offer("Sofia", 100)
        self.assertEqual("Cargo for 100 to Sofia was added as an offer.", result)
        self.assertIn("Sofia", self.truck_driver.available_cargos)
        self.assertEqual(100, self.truck_driver.available_cargos["Sofia"])

    def test_drive_best_cargo_offer_without_offers(self):
        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer_with_offers(self):
        self.truck_driver.available_cargos = {"Varna": 20, "Sofia": 10_000}
        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual("Bai Ivan is driving 10000 to Sofia.", result)
        self.assertEqual(988250, self.truck_driver.earned_money)
        self.assertEqual(10000, self.truck_driver.miles)

    def test_eat_method(self):
        self.truck_driver.earned_money = 1000
        self.truck_driver.eat(250)
        self.assertEqual(980, self.truck_driver.earned_money)

    def test_sleep_method(self):
        self.truck_driver.earned_money = 1000
        self.truck_driver.sleep(1000)
        self.assertEqual(955, self.truck_driver.earned_money)

    def test_pump_gas_method(self):
        self.truck_driver.earned_money = 1000
        self.truck_driver.pump_gas(1500)
        self.assertEqual(500, self.truck_driver.earned_money)

    def test_repair_truck_method(self):
        self.truck_driver.earned_money = 10000
        self.truck_driver.repair_truck(10000)
        self.assertEqual(2500, self.truck_driver.earned_money)

    def test_check_for_activities_method(self):
        self.truck_driver.earned_money = 1000000
        self.truck_driver.check_for_activities(10000)
        self.assertEqual(988250, self.truck_driver.earned_money)

    def test_repr_method(self):
        self.truck_driver.available_cargos = {"Varna": 20, "Sofia": 10_000}
        self.truck_driver.drive_best_cargo_offer()
        self.assertEqual("Bai Ivan has 10000 miles behind his back.", repr(self.truck_driver))


if __name__ == '__main__':
    unittest.main()