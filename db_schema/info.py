INSERT_MOVIES = f'''
    INSERT INTO movies(name, rating)
        VALUES("Titanic", 6.7),
        ("Green Mile", 9.7),
        ("Inception", 8.9);
'''

INSERT_PROJECTIONS = f'''
    INSERT INTO projections (movie_id, type, day, hour)
        VALUES(1, "3D", "2020-05-10", "20:00"),
        (1, "2D", "2020-05-10", "22:30"),
        (2, "3D", "2020-05-12", "18:10"),
        (2, "3D", "2020-05-10", "21:20"),
        (3, "3D", "2020-05-11", "17:30");
'''

INSERT_RESERVATIONS = f'''
    INSERT INTO reservations (user_id, projection_id, row, col)
        VALUES(1, 2, 3, 4),
        (1, 2, 3, 3);
'''
