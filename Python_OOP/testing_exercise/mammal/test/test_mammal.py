from project.mammal import Mammal
import unittest


class MammalTest(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("Great_Ape", "apes", "uga_buga")

    def test_initializer(self):
        self.assertEqual("Great_Ape", self.mammal.name)
        self.assertEqual("apes", self.mammal.type)
        self.assertEqual("uga_buga", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_method(self):
        result = self.mammal.make_sound()
        self.assertEqual("Great_Ape makes uga_buga", result)

    def test_get_kingdom_method(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_get_info_method(self):
        result = self.mammal.info()
        self.assertEqual("Great_Ape is of type apes", result)

if __name__ == '__main__':
    unittest.main()

