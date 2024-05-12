class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):

    def setUp(self):
        self.cat = Cat("Tom")

    def test_initializing(self):
        self.assertEqual("Tom", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eat_method_without_exception(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_eat_method_with_exception(self):
      self.cat.eat()

      with self.assertRaises(Exception) as ex:
        self.cat.eat()

      self.assertEqual("Already fed.", str(ex.exception))

      self.assertTrue(self.cat.fed)
      self.assertTrue(self.cat.sleepy)
      self.assertEqual(1, self.cat.size)

    def test_sleep_method_without_exception(self):
      self.cat.eat()
      self.cat.sleep()

      self.assertFalse(self.cat.sleepy)

    def test_sleep_method_with_exception(self):
      with self.assertRaises(Exception) as ex:
        self.cat.sleep()

      self.assertEqual("Cannot sleep while hungry", str(ex.exception))
      self.assertFalse(self.cat.sleepy)

if __name__ == '__main__':
    unittest.main()

