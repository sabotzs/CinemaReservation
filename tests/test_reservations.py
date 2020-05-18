import unittest
from bootstrap import bootstrap, drop
from reservations import ReservationsGateway
from movies import MoviesGateway
from projections import ProjectionsGateway
from users import UserGateway


class ReservationsTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        bootstrap()
        MoviesGateway().add_movie(name='Titanic', rating=7.9)
        MoviesGateway().add_movie(name='Interstellar', rating=8.3)
        ProjectionsGateway().add_projection(movie_id=1, movie_type='2D', day='2020-05-18', hour='20:30')
        ProjectionsGateway().add_projection(movie_id=2, movie_type='3D', day='2020-05-19', hour='23:30')
        UserGateway().create(email='user1@abv.bg', password='User1pass')
        UserGateway().make_client(email='user1@abv.bg')
        UserGateway().create(email='user2@abv.bg', password='User2pass')
        UserGateway().make_client(email='user2@abv.bg')

    @classmethod
    def tearDownClass(cls):
        drop()

    def setUp(self):
        self.gateway = ReservationsGateway()
        self.client1 = UserGateway().login(email='user1@abv.bg', password='User1pass')
        self.client2 = UserGateway().login(email='user2@abv.bg', password='User2pass')


class TestReserveSeats(ReservationsTestCase):
    def test_succesfully_reserve_one_seat(self):
        seats = [(2, 3)]
        user_id = self.client1.user_id
        projection_id = 1

        self.gateway.reserve_seats(user_id, projection_id, seats)
        reservation = self.gateway.show_user_reservations(user_id)[0][0]

        self.assertEqual(reservation.user_id, user_id)
        self.assertEqual(reservation.projection_id, projection_id)
        self.assertEqual((reservation.row, reservation.col), seats[0])

    def test_successfully_reserve_more_than_one_seat(self):
        seats = [(1, 1), (1, 2)]
        user_id = self.client2.user_id
        projection_id = 2

        self.gateway.reserve_seats(user_id, projection_id, seats)
        reservations = [pair[0] for pair in self.gateway.show_user_reservations(user_id)]

        self.assertEqual(reservations[0].user_id, user_id)
        self.assertEqual(reservations[0].projection_id, projection_id)
        self.assertEqual((reservations[0].row, reservations[0].col), seats[0])

        self.assertEqual(reservations[1].user_id, user_id)
        self.assertEqual(reservations[1].projection_id, projection_id)
        self.assertEqual((reservations[1].row, reservations[1].col), seats[1])


if __name__ == '__main__':
    unittest.main()
