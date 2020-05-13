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
