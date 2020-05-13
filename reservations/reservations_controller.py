from .reservations_gateway import ReservationsGateway
from .reservations_model import ReservationsModel


class ResercationsController:
    def __init__(self):
        self.res_model = ReservationsModel

    def reserve_seats(self, *args):
        print("HERE")
        if len(args) != 3:
            return False
        else:
            user_id = args[0]
            projection_id = args[1]
            seats = args[2]
            self.res_model.reserve_seats(user_id, projection_id, seats)

    def show_user_reservations(self, user_id):
        user_reservations = self.res_model.show_user_reservations(user_id)
        return user_reservations

    def cancel_reservations(self, user_id, reservations):
        self.res_model.cancel_reservations(user_id, reservations)

    def show_seats(self, number_seats, projection_id):
        taken_seats = self.res_model.get_seats(projection_id)
        if number_seats > 100 - len(taken_seats):
            return None
        else:
            lst_tpls = []
            for i in range(len(taken_seats)):
                seat = (taken_seats[i]['row'], taken_seats[i]['col'])
                lst_tpls.append(seat)
            return lst_tpls
