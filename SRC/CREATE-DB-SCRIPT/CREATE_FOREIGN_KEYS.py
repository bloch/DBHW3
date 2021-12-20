import pymysql

def create_foreign_keys_Actors_Table(connectionObject):
    # no foreign keys
    pass


def create_foreign_keys_Directors_Table(connectionObject):
    # no foreign keys
    pass


def create_foreign_keys_Genres_Table(connectionObject):
    # no foreign keys
    pass


def create_foreign_keys_Collection_Table(connectionObject):
    # no foreign keys
    pass


def create_foreign_keys_MovieCollection_Table(connectionObject):
    cursorObject = connectionObject.cursor()
    sqlQuery = "ALTER TABLE MovieCollection ADD FOREIGN KEY (collectionID) REFERENCES Collection(collectionID);"
    cursorObject.execute(sqlQuery)
    connectionObject.commit()


def create_foreign_keys_MoviesActors_Table(connectionObject):
    # MoviesActors(movieID) is a foreign key of Movie(movieID)
    cursorObject = connectionObject.cursor()
    sqlQuery = "ALTER TABLE MoviesActors ADD FOREIGN KEY (movieID) REFERENCES Movies(movieID);"
    cursorObject.execute(sqlQuery)
    connectionObject.commit()

    # MoviesActors(actorID) is a foreign key of Actors(actorID)
    cursorObject = connectionObject.cursor()
    sqlQuery = "ALTER TABLE MoviesActors ADD FOREIGN KEY (actorID) REFERENCES Actors(actorID);"
    cursorObject.execute(sqlQuery)
    connectionObject.commit()


def create_foreign_keys_MovieDirector_Table(connectionObject):
    # MovieDirector(movieID) is a foreign key of Movie(movieID)
    cursorObject = connectionObject.cursor()
    sqlQuery = "ALTER TABLE MovieDirector ADD FOREIGN KEY (movieID) REFERENCES Movies(movieID);"
    cursorObject.execute(sqlQuery)
    connectionObject.commit()

    # MovieDirector(directorID) is a foreign key of Directors(directorID)
    cursorObject = connectionObject.cursor()
    sqlQuery = "ALTER TABLE MovieDirector ADD FOREIGN KEY (directorID) REFERENCES Directors(directorID);"
    cursorObject.execute(sqlQuery)
    connectionObject.commit()


def create_foreign_keys_MovieGenres_Table(connectionObject):
    # MovieGenres(movieID) is a foreign key of Movie(movieID)
    cursorObject = connectionObject.cursor()
    sqlQuery = "ALTER TABLE MovieGenres ADD FOREIGN KEY (movieID) REFERENCES Movies(movieID);"
    cursorObject.execute(sqlQuery)
    connectionObject.commit()

    # MovieGenres(genreID) is a foreign key of Genres(genreID)
    cursorObject = connectionObject.cursor()
    sqlQuery = "ALTER TABLE MovieGenres ADD FOREIGN KEY (genreID) REFERENCES Genres(genreID);"
    cursorObject.execute(sqlQuery)
    connectionObject.commit()


def create_foreign_keys_Movies_Table(connectionObject):
    # no foreign keys
    pass



connectionObject = pymysql.connect(host="127.0.0.1", user="DbMysql45", password="DbMysql45", db="DbMysql45",
                                   port=3305)


create_foreign_keys_Actors_Table(connectionObject)
create_foreign_keys_Directors_Table(connectionObject)
create_foreign_keys_Genres_Table(connectionObject)
create_foreign_keys_Collection_Table(connectionObject)
create_foreign_keys_MovieCollection_Table(connectionObject)
create_foreign_keys_MoviesActors_Table(connectionObject)
create_foreign_keys_MovieDirector_Table(connectionObject)
create_foreign_keys_MovieGenres_Table(connectionObject)
create_foreign_keys_Movies_Table(connectionObject)
