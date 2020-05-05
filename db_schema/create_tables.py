CREATE_MOVIES = f'''
    CREATE TABLE IF NOT EXISTS movies (
        id integer primary key AUTOINCREMENT,
        name varchar(50) unique,
        rating real
    );
'''

CREATE_USERS = f'''
    CREATE TABLE IF NOT EXISTS users (
        id integer primary key AUTOINCREMENT,
        email varchar(50) unique,
        password varchar(64),
        salt varchar(50)
    );
'''

CREATE_PROJECTIONS = f'''
    CREATE TABLE IF NOT EXISTS projections (
        id integer primary key AUTOINCREMENT,
        movie_id integer,
        type varchar(10),
        day varchar(50),
        hour varchar(50),
        FOREIGN KEY (movie_id) REFERENCES movies(id)
    );
'''

CREATE_RESERVATIONS = f'''
    CREATE TABLE IF NOT EXISTS reservations (
        id integer primary key AUTOINCREMENT,
        user_id integer,
        projection_id integer,
        row integer NOT NULL CHECK (0 < row AND row < 11),
        col integer NOT NULL CHECK (0 < col AND col < 11),
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (projection_id) REFERENCES projections(id)
    );
'''
