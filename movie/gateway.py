from cinema_reservation.db_schema import Database


class MovieGateway:
    def __init__(self):
        pass

    def get_all_movies(self):
        db = Database()
        select_all_movies_query = '''
            SELECT id, name, rating
                FROM movies
                ORDER BY rating;
        '''
        db.cursor.execute(select_all_movies_query)
        movies_info = db.cursor.fetchall()

        db.connection.commit()
        db.connection.close()

        return movies_info

    def add_movie(self, title, rating):
        db = Database()
        insert_movie_query = '''
            INSERT INTO movies (name, rating)
                VALUES ( ? , ? );
        '''
        db.cursor.execute(insert_movie_query, (title, rating))
        db.connection.commit()
        db.connection.close()
