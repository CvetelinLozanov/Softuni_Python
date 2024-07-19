from project.movie import Movie
import unittest


class TestMovie(unittest.TestCase):
    def setUp(self):
        self.movie = Movie("The Purge", 2013, 10)

    def test_initializer_with_valid_data(self):
        self.assertEqual("The Purge", self.movie.name)
        self.assertEqual(2013, self.movie.year)
        self.assertEqual(10, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_initializer_with_invalid_name(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''

        self.assertEqual('Name cannot be an empty string!', str(ve.exception))

    def test_initializer_with_invalid_year(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1800

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_method_with_existing_actor(self):
        self.movie.actors = ['test']
        result = self.movie.add_actor('test')
        self.assertEqual("test is already added in the list of actors!", result)
        self.assertEqual(1, len(self.movie.actors))

    def test_add_actor_with_non_existing_actors(self):
        self.movie.add_actor('test')
        self.assertEqual(['test'], self.movie.actors)
        self.assertIn('test', self.movie.actors)
        self.assertEqual(1, len(self.movie.actors))
        self.movie.add_actor('test_1')
        self.assertEqual(['test', 'test_1'], self.movie.actors)
        self.assertIn('test_1', self.movie.actors)
        self.assertEqual(2, len(self.movie.actors))

    def test_gt_method(self):
        other_movie = Movie("some_movie", 1999, 5)
        result = self.movie > other_movie
        self.assertEqual('"The Purge" is better than "some_movie"', result)
        other_movie.rating = 15
        result = self.movie > other_movie
        self.assertEqual('"some_movie" is better than "The Purge"', result)

    def test_repr_method(self):
        self.movie.add_actor('test')
        self.movie.add_actor('test_1')
        result = repr(self.movie)
        expected = f"Name: The Purge\n" \
                   f"Year of Release: 2013\n" \
                   f"Rating: 10.00\n" \
                   f"Cast: test, test_1"
        self.assertEqual(expected, result)

    def test_repr_method_without_actors(self):
        result = repr(self.movie)
        expected = f"Name: The Purge\n" \
                   f"Year of Release: 2013\n" \
                   f"Rating: 10.00\n" \
                   f"Cast: "
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
