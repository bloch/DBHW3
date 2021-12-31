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
    try:
        # MovieCollection(collectionID) is a foreign key of Collection(collectionID)
        cursorObject = connectionObject.cursor()
        sqlQuery = "ALTER TABLE MovieCollection ADD FOREIGN KEY (collectionID) REFERENCES Collection(collectionID);"
        cursorObject.execute(sqlQuery)
        connectionObject.commit()
    except Exception as e:
        print("ERROR! wasn't able to define foreign key for MovieCollection: {}".format(e))


def create_foreign_keys_MoviesActors_Table(connectionObject):

    try:
        # MoviesActors(movieID) is a foreign key of Movie(movieID)
        # cursorObject = connectionObject.cursor()
        # sqlQuery = "ALTER TABLE MoviesActors ADD FOREIGN KEY (movieID) REFERENCES Movies(movieID);"
        # cursorObject.execute(sqlQuery)
        # connectionObject.commit()

        # MoviesActors(actorID) is a foreign key of Actors(actorID)
        cursorObject = connectionObject.cursor()
        sqlQuery = "ALTER TABLE MoviesActors ADD FOREIGN KEY (actorID) REFERENCES Actors(actorID);"
        cursorObject.execute(sqlQuery)
        connectionObject.commit()

    except Exception as e:
        print("ERROR! wasn't able to define foreign key for MovieActors: {}".format(e))


def create_foreign_keys_MovieDirector_Table(connectionObject):
    try:
        # MovieDirector(movieID) is a foreign key of Movie(movieID)
        # cursorObject = connectionObject.cursor()
        # sqlQuery = "ALTER TABLE MovieDirector ADD FOREIGN KEY (movieID) REFERENCES Movies(movieID);"
        # cursorObject.execute(sqlQuery)
        # connectionObject.commit()

        # MovieDirector(directorID) is a foreign key of Directors(directorID)
        cursorObject = connectionObject.cursor()
        sqlQuery = "ALTER TABLE MovieDirector ADD FOREIGN KEY (directorID) REFERENCES Directors(directorID);"
        cursorObject.execute(sqlQuery)
        connectionObject.commit()
    except Exception as e:
        print("ERROR! wasn't able to define foreign key for MovieDirector: {}".format(e))

def create_foreign_keys_MovieGenres_Table(connectionObject):
    try:
        # MovieGenres(movieID) is a foreign key of Movie(movieID)
        # cursorObject = connectionObject.cursor()
        # sqlQuery = "ALTER TABLE MovieGenres ADD FOREIGN KEY (movieID) REFERENCES Movies(movieID);"
        # cursorObject.execute(sqlQuery)
        # connectionObject.commit()

        # MovieGenres(genreID) is a foreign key of Genres(genreID)
        cursorObject = connectionObject.cursor()
        sqlQuery = "ALTER TABLE MovieGenres ADD FOREIGN KEY (genreID) REFERENCES Genres(genreID);"
        cursorObject.execute(sqlQuery)
        connectionObject.commit()
    except Exception as e:
        print("ERROR! wasn't able to define foreign key for MovieGenres: {}".format(e))

def create_foreign_keys_Movies_Table(connectionObject):
    # no foreign keys
    pass



# connectionObject = pymysql.connect(host="mysqlsrv1.cs.tau.ac.il", user="DbMysql45", password="DbMysql45", db="DbMysql45",
#                                    port=3306)
#
#
# create_foreign_keys_Actors_Table(connectionObject)
# create_foreign_keys_Directors_Table(connectionObject)
# create_foreign_keys_Genres_Table(connectionObject)
# create_foreign_keys_Collection_Table(connectionObject)
# create_foreign_keys_MovieCollection_Table(connectionObject)
# create_foreign_keys_MoviesActors_Table(connectionObject)
# create_foreign_keys_MovieDirector_Table(connectionObject)
# create_foreign_keys_MovieGenres_Table(connectionObject)
# create_foreign_keys_Movies_Table(connectionObject)
