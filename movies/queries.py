SELECT_ALL_MOVIES_QUERY = '''
    SELECT id, name, rating
        FROM movies
        ORDER BY rating;
'''

SELECT_MOVIE_BY_TITLE_QUERY = '''
    SELECT id, name, rating
        FROM movies
        WHERE name = ?;
'''

INSERT_MOVIE_QUERY = '''
    INSERT INTO movies (name, rating)
        VALUES ( ? , ? );
'''

DELETE_MOVIE_QUERY = '''
    DELETE
        FROM movies
        WHERE id = ?;
'''

SEARH_FOR_EXISTING_MOVIE = '''
    SELECT *
        FROM movies
        WHERE name = ?;
'''
