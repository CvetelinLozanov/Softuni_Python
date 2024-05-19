from testing_exercise.vehicle.project.vehicle import Vehicle
import unittest


class VehicleTest(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(10, 100)

    def test_initializer(self):
        self.assertEqual(10, self.vehicle.fuel)
        self.assertEqual(10, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_method_with_valid_distance(self):
        self.vehicle.drive(4)
        self.assertEqual(5, self.vehicle.fuel)
        self.vehicle.drive(4)
        self.assertEqual(0, self.vehicle.fuel)

    def test_drive_method_with_invalid_distance(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))
        self.assertEqual(10, self.vehicle.fuel)

    def test_refuel_method_with_valid_fuel(self):
        self.vehicle.drive(4)
        self.assertEqual(5, self.vehicle.fuel)
        self.vehicle.refuel(2)
        self.assertEqual(7, self.vehicle.fuel)
        self.vehicle.refuel(1)
        self.assertEqual(8, self.vehicle.fuel)

    def test_refuel_method_with_invalid_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)

        self.assertEqual("Too much fuel", str(ex.exception))
        self.assertEqual(10, self.vehicle.fuel)

    def test_str_representing_method(self):
        self.assertEqual("The vehicle has 100 horse power with 10 fuel"
                         " left and 1.25 fuel consumption", str(self.vehicle))
        self.vehicle.drive(4)
        self.assertEqual("The vehicle has 100 horse power with 5.0 fuel"
                         " left and 1.25 fuel consumption", str(self.vehicle))
        self.vehicle.refuel(1)
        self.assertEqual("The vehicle has 100 horse power with 6.0 fuel"
                         " left and 1.25 fuel consumption", str(self.vehicle))


if __name__ == '__main__':
    unittest.main()