import unittest
from collections import deque

from project.railway_station import RailwayStation


class RailwayStationTest(unittest.TestCase):
    def setUp(self):
        self.railway_station = RailwayStation('test_name')

    def test_initializer_with_correct_data(self):
        self.assertEqual("test_name", self.railway_station.name)
        self.assertEqual(deque(), self.railway_station.arrival_trains)
        self.assertEqual(deque(), self.railway_station.departure_trains)

    def test_initializer_with_name_shorter_than_four_symbols(self):

        with self.assertRaises(ValueError) as ve:
            self.railway_station.name = "BDJ"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board_method(self):
        self.railway_station.new_arrival_on_board("test_train")
        self.assertIn("test_train", self.railway_station.arrival_trains)
        self.railway_station.new_arrival_on_board("test_bdj_train")
        self.assertIn("test_bdj_train", self.railway_station.arrival_trains)
        self.assertEqual(len(self.railway_station.arrival_trains), 2)

    def test_train_has_arrived_method_with_train_before_other_train(self):
        self.railway_station.new_arrival_on_board("test_train")
        self.railway_station.new_arrival_on_board("test_bdj_train")
        result = self.railway_station.train_has_arrived("test_bdj_train")
        self.assertEqual("There are other trains to arrive before test_bdj_train.", result)

    def test_train_has_arrived_method_with_arrived_train(self):
        self.railway_station.new_arrival_on_board("test_train")
        self.railway_station.new_arrival_on_board("test_bdj_train")
        result = self.railway_station.train_has_arrived("test_train")
        self.assertEqual("test_train is on the platform and will leave in 5 minutes.", result)
        self.assertIn("test_train", self.railway_station.departure_trains)
        self.assertNotIn("test_train", self.railway_station.arrival_trains)
        self.assertEqual(1, len(self.railway_station.arrival_trains))
        self.assertEqual(1, len(self.railway_station.departure_trains))

    def test_train_has_left_method_with_departure_train(self):
        self.railway_station.departure_trains.append("test_train")
        self.railway_station.departure_trains.append("test_bdj_train")
        result = self.railway_station.train_has_left("test_train")
        self.assertNotIn("test_train", self.railway_station.departure_trains)
        self.assertTrue(result)

    def test_train_has_left_method_with_train_in_queue(self):
        self.railway_station.departure_trains.append("test_train")
        self.railway_station.departure_trains.append("test_bdj_train")
        result = self.railway_station.train_has_left("test_bdj_train")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()