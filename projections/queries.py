CHECH_MOVIE_EXISTS_BY_ID = '''
    SELECT id
        FROM movies
        WHERE id = ?;
'''

INSERT_PROJECTION = '''
    INSERT INTO projections (movie_id, movie_type, day, hour)
        VALUES(?, ?, ?, ?);
'''

CHECK_PROJECTION_EXISTS_BY_ID = '''
    SELECT id
        FROM projections
        WHERE id = ?;
'''

DELETE_PROJECTION = '''
    DELETE FROM projections
        WHERE id = ?;
'''

SELECT_PROJECTIONS = '''
    SELECT movies.name, projections.id, day, hour, movie_type, COUNT(reservations.id) AS reserv_count
        FROM projections
        LEFT JOIN reservations
            ON projections.id = reservations.projection_id
        JOIN movies
            ON projections.movie_id = movies.id
        WHERE movie_id = ?
        GROUP BY projections.id;
'''

SLECT_TAKEN_SEATS = '''
    SELECT name, rating, day, hour, movie_type
        FROM projections
        JOIN movies
            ON movies.id = projections.movie_id
        WHERE projections.id = ?;
'''

GET_ALL_PROJECTIONS = '''
    SELECT name, projections.id AS id, day, hour, movie_type, COUNT(reservations.id) AS reserv_count
        FROM projections
        JOIN movies
            ON projections.movie_id = movies.id
        LEFT JOIN reservations
            ON projections.id = reservations.projection_id
        GROUP BY projections.id;
'''

SLECT_MOVIES = '''
    SELECT id, name, rating
        FROM movies
        ORDER BY rating;
'''
