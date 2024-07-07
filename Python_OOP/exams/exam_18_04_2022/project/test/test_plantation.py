from project.plantation import Plantation
import unittest


class TestPlantation(unittest.TestCase):
    def setUp(self):
        self.plantation = Plantation(10)

    def test_initializer_with_valid_data(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_initializer_with_invalid_size(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -5

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_method_with_existing_worker(self):
        self.plantation.workers.append("test")
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("test")

        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_method_with_non_existing_worker(self):
        result = self.plantation.hire_worker("test")
        self.assertEqual("test successfully hired.", result)
        self.assertIn("test", self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

    def test_len_method(self):
        self.plantation.plants["test"] = ["test_1", "test_2", "test_3", "test_4", "test_5"]
        self.plantation.plants["test1"] = ["test_6", "test_7", "test_8", "test_9", "test_10"]
        self.assertEqual(10, len(self.plantation))

    def test_len_method_without_plants(self):
        self.assertEqual(0, len(self.plantation))

    def test_len_method_without_addition(self):
        self.plantation.plants["test"] = ["test_1", "test_2", "test_3", "test_4", "test_5"]
        self.plantation.plants["test1"] = ["test_6", "test_7", "test_8", "test_9", "test_10", "test_11"]
        self.assertEqual(11, len(self.plantation))

    def test_planting_method_with_non_existing_worker(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("test_name", "test_plant")

        self.assertEqual("Worker with name test_name is not hired!", str(ve.exception))

    def test_planting_method_with_full_plantation(self):
        self.plantation.workers = ["test", "test_1"]
        self.plantation.plants["test"] = ["test_1", "test_2", "test_3", "test_4", "test_5"]
        self.plantation.plants["test1"] = ["test_6", "test_7", "test_8", "test_9"]

        self.plantation.planting("test", "test_10")
        self.assertIn("test_10", self.plantation.plants["test"])
        self.assertEqual(10, len(self.plantation))

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("test", "test_11")

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_method_with_first_planted_plant(self):
        self.plantation.workers = ["test", "test_1"]
        result = self.plantation.planting("test", "test_1")
        self.assertEqual("test planted it's first test_1.", result)
        self.assertIn("test", self.plantation.plants)
        self.assertIn("test_1", self.plantation.plants["test"])
        result = self.plantation.planting("test_1", "test_2")
        self.assertEqual("test_1 planted it's first test_2.", result)
        self.assertIn("test_1", self.plantation.plants)
        self.assertIn("test_2", self.plantation.plants["test_1"])

    def test_planting_method_with_already_planted_plants(self):
        self.plantation.workers = ["test", "test_1"]
        self.plantation.plants["test"] = ["test_1", "test_2", "test_3", "test_4", "test_5"]
        result = self.plantation.planting("test", "test_6")
        self.assertEqual("test planted test_6.", result)
        self.assertIn("test_6", self.plantation.plants["test"])

    def test_str_method(self):
        self.plantation.plants["test"] = ["test_1", "test_2", "test_3", "test_4", "test_5"]
        self.plantation.workers = ["test", "test_1"]
        self.assertEqual('Plantation size: 10\ntest, test_1\ntest planted: test_1, test_2, test_3, test_4, test_5',
                         str(self.plantation))

    def test_repr_method(self):
        self.plantation.workers = ["test", "test_1"]
        self.assertEqual("Size: 10\nWorkers: test, test_1", repr(self.plantation))


if __name__ == '__main__':
    unittest.main()