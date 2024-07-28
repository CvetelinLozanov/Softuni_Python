from project2.trip import Trip
import unittest


class TripTest(unittest.TestCase):
    def setUp(self):
        self.trip = Trip(10000, 10, True)

    def test_initializer_with_valid_data(self):
        self.assertEqual(10000, self.trip.budget)
        self.assertEqual(10, self.trip.travelers)
        self.assertTrue(self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_initializer_with_travelers_less_than_one(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        self.assertEqual("At least one traveler is required!", str(ve.exception))

    def test_initializer_with_number_of_travelers_less_than_2(self):
        test_trip = Trip(100, 1, True)

        self.assertFalse(test_trip.is_family)

    def test_book_a_trip_method_with_invalid_destination(self):
        result = self.trip.book_a_trip("test")
        self.assertEqual('This destination is not in our offers, please choose a new one!', result)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_book_a_trip_method_with_less_budget(self):
        result = self.trip.book_a_trip('New Zealand')
        self.assertEqual('Your budget is not enough!', result)

    def test_book_a_trip_method_with_family(self):
        result = self.trip.book_a_trip('Bulgaria')
        self.assertEqual(4500, self.trip.booked_destinations_paid_amounts['Bulgaria'])
        self.assertEqual(5500, self.trip.budget)
        self.assertEqual('Successfully booked destination Bulgaria! Your budget left is 5500.00', result)

    def test_book_a_trip_method_without_family(self):
        test_trip = Trip(1000, 1, True)
        result = test_trip.book_a_trip('Bulgaria')
        self.assertEqual(500, test_trip.booked_destinations_paid_amounts['Bulgaria'])
        self.assertEqual(500, test_trip.budget)
        self.assertEqual('Successfully booked destination Bulgaria! Your budget left is 500.00', result)

    def test_booking_status_method(self):
        result = self.trip.booking_status()
        self.assertEqual('No bookings yet. Budget: 10000.00', result)

    def test_book_status_method_with_trip(self):
        test_trip = Trip(100_000, 5, True)
        test_trip.book_a_trip('Bulgaria')
        test_trip.book_a_trip('New Zealand')
        expected_result = """Booked Destination: Bulgaria\nPaid Amount: 2250.00\nBooked Destination: New Zealand\nPaid Amount: 33750.00\nNumber of Travelers: 5\nBudget Left: 64000.00"""
        result = test_trip.booking_status()
        self.assertEqual(2, len(test_trip.booked_destinations_paid_amounts))
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()