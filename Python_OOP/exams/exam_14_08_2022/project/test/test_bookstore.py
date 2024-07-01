from project.bookstore import Bookstore
import unittest


class TestBookstore(unittest.TestCase):
    def setUp(self):
        self.bookstore = Bookstore(20)

    def test_initializer_with_valid_data(self):
        self.assertEqual(20, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)

    def test_initializer_with_books_limit_equal_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_initializer_with_books_limit_less_than_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -10

        self.assertEqual("Books limit of -10 is not valid", str(ve.exception))

    def test_len_method(self):
        self.bookstore.availability_in_store_by_book_titles = {"test1": 10, "test2": 10, "test3": 30}
        self.assertEqual(50, len(self.bookstore))

    def test_receive_book_method_with_invalid_book_limit(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Test_1", 25)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_method_with_valid_book_limit(self):
        result = self.bookstore.receive_book("Test_1", 10)
        self.assertEqual("10 copies of Test_1 are available in the bookstore.", result)
        self.assertIn("Test_1", self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(10, self.bookstore.availability_in_store_by_book_titles["Test_1"])
        self.assertEqual(10, len(self.bookstore))

        result = self.bookstore.receive_book("Test_2", 5)
        self.assertEqual("5 copies of Test_2 are available in the bookstore.", result)
        self.assertIn("Test_2", self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(5, self.bookstore.availability_in_store_by_book_titles["Test_2"])
        self.assertEqual(15, len(self.bookstore))

        result = self.bookstore.receive_book("Test_1", 5)
        self.assertEqual("15 copies of Test_1 are available in the bookstore.", result)
        self.assertIn("Test_1", self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(15, self.bookstore.availability_in_store_by_book_titles["Test_1"])
        self.assertEqual(20, len(self.bookstore))

    def test_sell_book_with_non_existing_book(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Test", 5)

        self.assertEqual("Book Test doesn't exist!", str(ex.exception))
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_sell_book_with_invalid_quantity(self):
        self.bookstore.receive_book("Test_1", 10)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Test_1", 15)

        self.assertEqual("Test_1 has not enough copies to sell. Left: 10", str(ex.exception))
        self.assertEqual(0, self.bookstore.total_sold_books)
        self.assertEqual(10, self.bookstore.availability_in_store_by_book_titles["Test_1"])

    def test_sell_book_with_valid_data(self):
        self.bookstore.receive_book("Test_1", 10)
        result = self.bookstore.sell_book("Test_1", 5)
        self.assertEqual("Sold 5 copies of Test_1", result)
        self.assertEqual(5, self.bookstore.availability_in_store_by_book_titles["Test_1"])
        self.assertEqual(5, len(self.bookstore))
        self.assertEqual(5, self.bookstore.total_sold_books)

        result_1 = self.bookstore.sell_book("Test_1", 5)
        self.assertEqual("Sold 5 copies of Test_1", result_1)
        self.assertEqual(0, self.bookstore.availability_in_store_by_book_titles["Test_1"])
        self.assertEqual(0, len(self.bookstore))
        self.assertEqual(10, self.bookstore.total_sold_books)

    def test_str_method(self):
        self.bookstore.receive_book("Test_1", 10)
        self.bookstore.receive_book("Test_1", 5)
        self.bookstore.receive_book("Test_2", 5)
        self.bookstore.sell_book("Test_1", 5)
        self.bookstore.sell_book("Test_2", 5)
        self.assertEqual("Total sold books: 10\nCurrent availability: 10\n - Test_1: 10 copies\n - Test_2: 0 copies", str(self.bookstore))


if __name__ == '__main__':
    unittest.main()