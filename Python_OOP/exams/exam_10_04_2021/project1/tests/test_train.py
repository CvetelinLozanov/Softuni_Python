from project1.train.train import Train
import unittest


class TestTrain(unittest.TestCase):
    def setUp(self):
        self.train = Train("jelezenKon", 2)

    def test_initializer(self):
        self.assertEqual("jelezenKon", self.train.name)
        self.assertEqual(2, self.train.capacity)

    def test_add_method_with_full_capacity(self):
        self.train.passengers.append("Pesho")
        self.train.passengers.append("Gosho")
        self.assertEqual(2, len(self.train.passengers))
        with self.assertRaises(ValueError) as ve:
            self.train.add("Mitio")

        self.assertEqual("Train is full", str(ve.exception))
        self.assertEqual(2, len(self.train.passengers))

    def test_add_method_with_existing_name(self):
        self.train.passengers.append("Pesho")
        self.assertEqual(1, len(self.train.passengers))
        with self.assertRaises(ValueError) as ve:
            self.train.add("Pesho")

        self.assertEqual("Passenger Pesho Exists", str(ve.exception))
        self.assertEqual(1, len(self.train.passengers))

    def test_add_method_with_valid_passenger(self):
        result = self.train.add("Pesho")
        self.assertEqual(1, len(self.train.passengers))
        self.assertEqual("Added passenger Pesho", result)
        result = self.train.add("Mitio")
        self.assertEqual(2, len(self.train.passengers))
        self.assertEqual("Added passenger Mitio", result)

    def test_remove_method_with_non_existing_passenger(self):
        with self.assertRaises(ValueError) as ve:
            self.train.remove("Bai Mitio")

        self.assertEqual("Passenger Not Found", str(ve.exception))

    def test_remove_method_with_existing_passenger(self):
        self.train.add("Pesho")
        self.train.add("Mitio")
        self.assertEqual(2, len(self.train.passengers))
        result = self.train.remove("Pesho")
        self.assertEqual("Removed Pesho", result)
        self.assertEqual(1, len(self.train.passengers))
        result = self.train.remove("Mitio")
        self.assertEqual("Removed Mitio", result)
        self.assertEqual(0, len(self.train.passengers))


if __name__ == '__main__':
    unittest.main()