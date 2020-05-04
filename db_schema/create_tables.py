CREATE_MOVIES = f'''
    CREATE TABLE IF NOT EXISTS movies (
        id integer primary key,
        name varchar(50) unique,
        rating real
    );
'''

CREATE_USERS = f'''
    CREATE TABLE IF NOT EXISTS users (
        id integer primary key,
        username varchar(50) unique,
        password varchar(100),
        salt varchar(50) 
    );
'''

CREATE_PROJECTIONS = f'''
    CREATE TABLE IF NOT EXISTS projections (
        id integer primary key,
        movie_id integer,
        type varchar(10),
        date varchar(50),
        time varchar(50)
    );
'''

CREATE_RESERVATIONS = f'''
    CREATE TABLE IF NOT EXISTS reservations (
        id integer primary key,
        user_id integer,
        projection_id integer,
        row integer NOT NULL,
        col integer NOT NNLL
    );
'''
