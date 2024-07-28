from project1.pet_shop import PetShop
from unittest import main, TestCase


class TestPetShop(TestCase):
    def setUp(self):
        self.pet_shop = PetShop("test")

    def test_initializer(self):
        self.assertEqual("test", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_method_with_negative_quantity(self):
        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food("some_food", -1)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_food_method_with_zero_quantity(self):
        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food("some_food", 0)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_food_method_with_valid_food(self):
        result = self.pet_shop.add_food("some_food", 10)
        self.assertEqual(1, len(self.pet_shop.food))
        self.assertEqual({"some_food": 10}, self.pet_shop.food)
        self.assertEqual("Successfully added 10.00 grams of some_food.", result)
        result = self.pet_shop.add_food("some_food", 15)
        self.assertEqual(1, len(self.pet_shop.food))
        self.assertEqual({"some_food": 25}, self.pet_shop.food)
        self.assertEqual("Successfully added 15.00 grams of some_food.", result)

    def test_add_pet_method_with_non_existing_pet(self):
        result = self.pet_shop.add_pet("some_pet")
        self.assertEqual("Successfully added some_pet.", result)
        self.assertEqual(1, len(self.pet_shop.pets))

    def test_add_pet_method_with_existing_pet(self):
        result = self.pet_shop.add_pet("some_pet")
        self.assertEqual("Successfully added some_pet.", result)
        self.assertEqual(1, len(self.pet_shop.pets))

        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("some_pet")

        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_method_with_invalid_pet(self):
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("some_food", "some_pet")

        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_method_with_invalid_food(self):
        self.pet_shop.add_pet("some_pet")
        result = self.pet_shop.feed_pet("some_food", "some_pet")

        self.assertEqual("You do not have some_food", result)

    def test_feed_pet_method_with_food_quantity_less_than_hundred(self):
        self.pet_shop.add_food("some_food", 10)
        self.pet_shop.add_pet("some_pet")
        result = self.pet_shop.feed_pet("some_food", "some_pet")
        self.assertEqual("Adding food...", result)
        self.assertEqual(1010, self.pet_shop.food["some_food"])
        result = self.pet_shop.feed_pet("some_food", "some_pet")
        self.assertEqual("some_pet was successfully fed", result)
        self.assertEqual(910, self.pet_shop.food["some_food"])

    def test_repr_method_with_pets(self):
        self.pet_shop.add_pet("some_pet")
        self.pet_shop.add_pet("some_pet_1")
        expected = f'Shop test:\nPets: some_pet, some_pet_1'
        self.assertEqual(expected, repr(self.pet_shop))

    def test_repr_method_without_pets(self):
        expected = f'Shop test:\nPets: '
        self.assertEqual(expected, repr(self.pet_shop))


if __name__ == '__main__':
    main()