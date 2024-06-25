from project.toy_store import ToyStore
import unittest


class TestToyStore(unittest.TestCase):
    def setUp(self):
        self.toy_store = ToyStore()

    def test_initializer(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy_store.toy_shelf)

    def test_add_toy_with_invalid_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("test_shelf", "Minion")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_with_existing_toy(self):
        self.toy_store.toy_shelf["A"] = "Minion"
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Minion")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_with_taken_shelf(self):
        self.toy_store.toy_shelf["A"] = "Minion"
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_with_valid_toy(self):
        result = self.toy_store.add_toy("A", "Minion")
        self.assertEqual("Toy:Minion placed successfully!", result)
        self.assertIn("Minion", self.toy_store.toy_shelf["A"])

    def test_remove_toy_with_non_existing_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("Z", "Minion")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_with_non_existing_toy(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "Minion")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_with_valid_input(self):
        self.toy_store.toy_shelf["A"] = "Minion"
        result = self.toy_store.remove_toy("A", "Minion")
        self.assertEqual("Remove toy:Minion successfully!", result)
        self.assertIsNone(self.toy_store.toy_shelf["A"])


if __name__ == '__main__':
    unittest.main()

