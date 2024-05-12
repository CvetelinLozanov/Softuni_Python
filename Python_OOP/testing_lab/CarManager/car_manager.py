class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
    
    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed

car = Car("a", "b", 1, 4)
car.refuel(10)
print(car.fuel_amount)


import unittest


class CarTests(unittest.TestCase):
    def setUp(self):
        self.car = Car("Peugeot", "205", 5, 50)

    def test_initializing_with_correct_data(self):
        self.assertEqual("Peugeot", self.car.make)
        self.assertEqual("205", self.car.model)
        self.assertEqual(5, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_initializing_with_empty_make(self):
        with self.assertRaises(Exception) as ex:
            car = Car("", "Samara", 10, 100)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_initializing_with_none_make(self):
        with self.assertRaises(Exception) as ex:
            car = Car(None, "Samara", 10, 100)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_initializing_with_empty_model(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Lada", "", 10, 100)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_initializing_with_none_model(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Lada", None, 10, 100)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_initializing_with_negative_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Lada", "Niva", -10, 100)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_initializing_with_zero_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Lada", "Niva", 0, 100)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_initializing_with_negative_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Lada", "Niva", 10, -1)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_initializing_with_zero_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Lada", "Niva", 10, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_refuel_method_with_negative_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
        self.assertEqual(0, self.car.fuel_amount)

    def test_refuel_method_with_zero_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
        self.assertEqual(0, self.car.fuel_amount)

    def test_refuel_method_with_fuel_greater_than_fuel_capacity(self):
        self.car.refuel(10000)

        self.assertEqual(50, self.car.fuel_amount)
        self.assertEqual(50, self.car._Car__fuel_amount)

    def test_drive_method_with_greater_distance_than_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_method_when_distance_is_equal_to_fuel_amount(self):
        self.car.refuel(50)
        self.car.drive(1000)
        self.assertEqual(0, self.car.fuel_amount)
        self.assertEqual(0, self.car._Car__fuel_amount)

    def test_drive_method_with_distance_less_than_fuel_amount(self):
        self.car.refuel(50)
        self.car.drive(500)
        self.assertEqual(25, self.car.fuel_amount)
        self.assertEqual(25, self.car._Car__fuel_amount)


if __name__ == '__main__':
    unittest.main()