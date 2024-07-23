from project.library import Library
from unittest import main, TestCase


class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library("some_name")

    def test_initializer_with_valid_data(self):
        self.assertEqual("some_name", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_initializer_with_empty_name(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ''

        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book_method_with_non_existing_author_and_title(self):
        self.library.add_book("some_author", "some_title")
        self.assertEqual({"some_author": ["some_title"]}, self.library.books_by_authors)
        self.assertEqual(1, len(self.library.books_by_authors))

    def test_add_book_method_with_existing_author(self):
        self.library.add_book("some_author", "some_title")
        self.assertEqual(1, len(self.library.books_by_authors["some_author"]))
        self.library.add_book("some_author", "some_title1")
        self.assertEqual({"some_author": ["some_title", "some_title1"]}, self.library.books_by_authors)
        self.assertEqual(2, len(self.library.books_by_authors["some_author"]))

    def test_add_reader_method_with_non_existing_reader(self):
        self.library.add_reader("some_reader")
        self.assertEqual({"some_reader": []}, self.library.readers)
        self.assertEqual(1, len(self.library.readers))
        self.assertEqual({"some_reader_1": []}, self.library.readers)
        self.assertEqual(2, len(self.library.readers))

    def test_add_reader_method_with_already_existing_reader(self):
        self.library.add_reader("some_reader")
        self.assertEqual(1, len(self.library.readers))
        result = self.library.add_reader("some_reader")
        self.assertEqual("some_reader is already registered in the some_name library.", result)
        self.assertEqual(1, len(self.library.readers))

    def test_rent_book_method_with_non_existing_reader(self):
        result = self.library.rent_book("some_reader", "some_author", "some_book")
        self.assertEqual("some_reader is not registered in the some_name Library.", result)

    def test_rent_book_method_with_non_existing_author(self):
        self.library.add_reader("some_reader")
        result = self.library.rent_book("some_reader", "some_author", "some_book")
        self.assertEqual("some_name Library does not have any some_author's books.", result)

    def test_rent_book_method_with_non_existing_book(self):
        self.library.add_reader("some_reader")
        self.library.add_book("some_author", "some_title")
        result = self.library.rent_book("some_reader", "some_author", "some_book")
        self.assertEqual("""some_name Library does not have some_author's "some_book".""", result)

    def test_rent_book_with_valid_data(self):
        self.library.add_reader("some_reader")
        self.library.add_reader("some_reader_2")
        self.library.add_book("some_author", "some_title")
        self.library.add_book("some_author", "some_title_1")
        self.assertEqual(0, len(self.library.readers["some_reader"]))
        self.assertEqual(2, len(self.library.books_by_authors["some_author"]))
        self.assertIn("some_title", self.library.books_by_authors["some_author"])
        self.library.rent_book("some_reader", "some_author", "some_title")
        self.assertEqual(1, len(self.library.readers["some_reader"]))
        self.assertEqual(1, len(self.library.books_by_authors["some_author"]))
        self.assertNotIn("some_title", self.library.books_by_authors["some_author"])
        self.library.rent_book("some_reader", "some_author", "some_title_1")
        self.assertEqual(2, len(self.library.readers["some_reader"]))
        self.assertEqual(0, len(self.library.books_by_authors["some_author"]))
        self.assertNotIn("some_title", self.library.books_by_authors["some_author"])


if __name__ == '__main__':
    main()
