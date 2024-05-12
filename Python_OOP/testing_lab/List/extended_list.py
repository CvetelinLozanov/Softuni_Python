class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self):
        self.integer_list = IntegerList(1, 2, 3, 4)

    def test_initializing_with_correct_data(self):
        self.assertEqual([1, 2, 3, 4], self.integer_list.get_data())

    def test_initializing_with_multiple_data_types(self):
        test_list = IntegerList("Azis", 4.66, False, {"Fiki": 10}, [])

        self.assertEqual([], test_list.get_data())

    def test_add_method_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.add("Galena")

        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual([1, 2, 3, 4], self.integer_list.get_data())

    def test_add_method_without_exception(self):
        self.integer_list.add(5)
        self.assertEqual(5, len(self.integer_list.get_data()))
        self.assertEqual(5, self.integer_list.get_data()[-1])
        self.assertIn(5, self.integer_list.get_data())

    def test_remove_index_method_with_index_greater_than_list_length(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(10)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(4, len(self.integer_list.get_data()))

    def test_remove_index_method_with_index_equal_to_list_length(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(4)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(4, len(self.integer_list.get_data()))

    def test_remove_index_method_with_correct_index(self):
        expected_num = self.integer_list.remove_index(0)
        self.assertEqual(2, self.integer_list.get_data()[0])
        self.assertNotIn(1, self.integer_list.get_data())
        self.assertEqual(3, len(self.integer_list.get_data()))
        self.assertEqual(1, expected_num)

    def test_get_method_exception_with_index_greater_than_list_length(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(6)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_method_with_correct_index(self):
        expected_value = self.integer_list.get(0)

        self.assertEqual(1, expected_value)

    def test_insert_method_exception_for_index_with_greater_value_than_list_length(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(50, 100)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(4, len(self.integer_list.get_data()))

    def test_insert_method_exception_for_index_with_equal_to_list_length(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(4, 100)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(4, len(self.integer_list.get_data()))

    def test_insert_method_type_check_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(0, "Filaret")

        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual(4, len(self.integer_list.get_data()))

    def test_insert_method_with_correct_data(self):
        self.integer_list.insert(0, 101)
        self.assertIn(101, self.integer_list.get_data())
        self.assertEqual(101, self.integer_list.get_data()[0])
        self.assertEqual(5, len(self.integer_list.get_data()))

    def test_get_biggest_method(self):
        test_list = IntegerList(12, 105, 1, 456)
        value = test_list.get_biggest()
        self.assertEqual(456, value)

    def test_get_index_method(self):
        value = self.integer_list.get_index(2)
        self.assertEqual(1, value)

if __name__ == '__main__':
    unittest.main()
