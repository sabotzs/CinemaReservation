import unittest
from movies import MoviesGateway
from bootstrap import bootstrap, drop


class MoviesTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        bootstrap()

    @classmethod
    def tearDownClass(cls):
        drop()


class TestAddMovie(MoviesTestCase):
    def test_successfully_adding_movie_returns_true(self):
        gateway = MoviesGateway()
        title = 'Interstellar'
        rating = 7.9
        expected = None

        added = gateway.add_movie(name=title, rating=rating)
        all_movies = gateway.show_movies()
        for movie in all_movies:
            if movie.name == title and movie.rating == rating:
                expected = movie

        self.assertTrue(added)
        self.assertIsNotNone(expected)

    def test_adding_existing_movie_returns_false(self):
        gateway = MoviesGateway()
        title = 'Inception'
        rating = 8.5
        gateway.add_movie(name=title, rating=rating)

        added = gateway.add_movie(name=title, rating=rating)

        self.assertFalse(added)


class TestDeleteMovie(MoviesTestCase):
    def test_deleting_existing_movie_succesfully_returns_true(self):
        gateway = MoviesGateway()
        title = 'Titanic'
        rating = 7.9
        gateway.add_movie(name=title, rating=rating)

        deleted = gateway.delete_movie(movie_id=1)

        self.assertTrue(deleted)

    def test_trying_to_delete_non_existgin_movie_returns_false(self):
        gateway = MoviesGateway()

        deleted = gateway.delete_movie(movie_id=10)

        self.assertFalse(deleted)


class TestShowMovies(MoviesTestCase):
    def test_show_all_movies_returns_list_of_all_existing_movies_in_descending_order_by_ratings(self):
        gateway = MoviesGateway()
        titles = ['Titanic', 'Inception', 'The Revenant']
        ratings = [7.9, 8.5, 8.2]

        gateway.add_movie(name=titles[0], rating=ratings[0])
        gateway.add_movie(name=titles[1], rating=ratings[1])
        gateway.add_movie(name=titles[2], rating=ratings[2])

        movies = gateway.show_movies()

        self.assertEqual(
            (movies[0].name, movies[0].rating),
            ('Inception', 8.5)
        )
        self.assertEqual(
            (movies[1].name, movies[1].rating),
            ('The Revenant', 8.2)
        )
        self.assertEqual(
            (movies[2].name, movies[2].rating),
            ('Titanic', 7.9)
        )


if __name__ == '__main__':
    unittest.main()
