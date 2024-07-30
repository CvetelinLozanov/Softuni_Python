from project2.tennis_player import TennisPlayer
from unittest import main, TestCase


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player = TennisPlayer("Novak Djokovic", 37, 11750)

    def test_initializer_with_valid_data(self):
        self.assertEqual("Novak Djokovic", self.player.name)
        self.assertEqual(37, self.player.age)
        self.assertEqual(11750, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_with_less_than_two_symbols(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "t"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_name_with_two_symbols(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "tt"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_with_value_less_than_eighteen(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_method_with_existing_tournament(self):
        self.player.wins.append("Wimbledon")
        result = self.player.add_new_win("Wimbledon")
        self.assertEqual("Wimbledon has been already added to the list of wins!", result)
        self.assertEqual(1, len(self.player.wins))

    def test_add_new_win_method_with_non_existing_tournament(self):
        self.player.add_new_win("Wimbledon")
        self.assertEqual(1, len(self.player.wins))
        self.assertIn("Wimbledon", self.player.wins)
        self.player.add_new_win("Roland Garros")
        self.assertEqual(2, len(self.player.wins))
        self.assertIn("Roland Garros", self.player.wins)

    def test_lt_method_with_less_points(self):
        tennis_player = TennisPlayer("Rafael Nadal", 38, 1000)
        self.assertEqual('Novak Djokovic is a top seeded player and he/she is better than Rafael Nadal', tennis_player < self.player)

    def test_lt_method_with_more_points(self):
        tennis_player = TennisPlayer("Rafael Nadal", 38, 1000)
        self.assertEqual('Novak Djokovic is a better player than Rafael Nadal', self.player < tennis_player)

    def test_str_method_with_no_tournaments(self):
        self.assertEqual([], self.player.wins)

        expected_result = f"Tennis Player: Novak Djokovic\n" \
                          f"Age: 37\n" \
                          f"Points: 11750.0\n" \
                          f"Tournaments won: "
        result = str(self.player)
        self.assertEqual(result, expected_result)

    def test_str_method_with_one_tournament(self):
        self.player.add_new_win("Wimbledon")
        self.assertEqual(['Wimbledon'], self.player.wins)
        expected_result = f"Tennis Player: Novak Djokovic\n" \
               f"Age: 37\n" \
               f"Points: 11750.0\n" \
               f"Tournaments won: Wimbledon"
        result = str(self.player)
        self.assertEqual(expected_result, result)

    def test_str_method_with_two_tournaments(self):
        self.player.add_new_win("Wimbledon")
        self.player.add_new_win("Roland Garros")
        self.assertEqual(['Wimbledon', 'Roland Garros'], self.player.wins)
        expected_result = f"Tennis Player: Novak Djokovic\n" \
               f"Age: 37\n" \
               f"Points: 11750.0\n" \
               f"Tournaments won: Wimbledon, Roland Garros"
        result = str(self.player)
        self.assertEqual(expected_result, result)

    def test_str_method_with_three_tournaments(self):
        self.player.add_new_win("Wimbledon")
        self.player.add_new_win("Roland Garros")
        self.player.add_new_win("US Open")
        self.assertEqual(['Wimbledon', 'Roland Garros', 'US Open'], self.player.wins)
        expected_result = f"Tennis Player: Novak Djokovic\n" \
               f"Age: 37\n" \
               f"Points: 11750.0\n" \
               f"Tournaments won: Wimbledon, Roland Garros, US Open"
        result = str(self.player)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
