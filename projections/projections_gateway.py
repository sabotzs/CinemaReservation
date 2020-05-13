from db_schema import Database


class ProjectionsGateway:
    def __init__(self):
        pass

    def add_projection(self, *, movie_id, movie_type, day, hour):
        db = Database()
        check_movie_id_exists = '''
            SELECT id
            FROM movies
            WHERE id = ?;
        '''
        db.cursor.execute(check_movie_id_exists, (movie_id,))
        info = db.cursor.fetchall()
        if len(info) == 0:
            return "There is no movie with such id"

        if not isinstance(movie_type, str) or not isinstance(day, str) or not isinstance(hour, str):
            raise ValueError("Wrong input! ")
        movie_id = info[0][0]
        insert_projection = '''
            INSERT INTO projections (movie_id, movie_type, day, hour)
            VALUES(?, ?, ?, ?);
        '''
        db.cursor.execute(insert_projection, (movie_id, movie_type, day, hour))
        db.connection.commit()
        db.connection.close()

    def delete_projection(self, *, projection_id):
        db = Database()
        check_projection_id_exists = '''
            SELECT id
                FROM projections
                WHERE id = ?;
        '''
        db.cursor.execute(check_projection_id_exists, (projection_id,))
        info = db.cursor.fetchone()
        if info is None:
            return "No projection with such id!"

        delete_projection_query = '''
            DELETE FROM projections
                WHERE id = ?;
        '''
        db.cursor.execute(delete_projection_query, (projection_id,))
        db.connection.commit()
        db.connection.close()
