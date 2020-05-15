from .reservations_gateway import ReservationsGateway


class ResercationsController:
    def __init__(self):
        self.res_gateway = ReservationsGateway()

    def reserve_seats(self, *args):
        if len(args) != 3:
            return False
        else:
            user_id = args[0]
            projection_id = args[1]
            seats = args[2]
            self.res_gateway.reserve_seats(user_id, projection_id, seats)

    def show_user_reservations(self, user_id):
        user_reservations = self.res_gateway.show_user_reservations(user_id)
        return user_reservations

    def cancel_reservations(self, user_id, reservations):
        self.res_gateway.cancel_reservations(user_id, reservations)

    def show_seats(self, number_seats, projection_id):
        taken_seats = self.res_gateway.get_seats(projection_id)
        if number_seats > 100 - len(taken_seats):
            return None
        else:
            return taken_seats
