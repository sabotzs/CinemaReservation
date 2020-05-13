from db_schema import Database


class MoviesGateway:
    def __init__(self):
        pass

    def add_movie(self, *, name_of_the_movie, rating):
        db = Database()
        search_for_existing_movie = '''
            SELECT *
                FROM movies
                where name = ?;
        '''
        db.cursor.execute(search_for_existing_movie, (name_of_the_movie,))
        info = db.cursor.fetchone()
        if info is not None:
            return False
        if not self.validate_movie_info(name_of_the_movie, rating):
            return False
        insert_movie_query = '''
            INSERT INTO movies (name, rating)
                VALUES(? ,?);
        '''
        db.cursor.execute(insert_movie_query, (name_of_the_movie, rating))
        db.connection.commit()
        db.connection.close()
        return True

    def validate_movie_info(self, name, rating):
        if not isinstance(name, str) or not isinstance(rating, float):
            return False
        return True

    def delete_movie(self, *, movie_id):
        db = Database()
        get_movie_query = '''
            SELECT id
                FROM movies
                WHERE id = ?
        '''
        db.cursor.execute(get_movie_query, (movie_id,))
        info = db.cursor.fetchone()
        if info is None:
            return False

        delete_movie_query = '''
            DELETE
            FROM movies
            WHERE id = ?;
        '''
        db.cursor.execute(delete_movie_query, (movie_id,))
        db.connection.commit()
        db.connection.close()
        return "Successfully deleted!"