import pymysql


def create_Movies_table(connectionObject):
    sqlQuery = "create TABLE IF NOT EXISTS Movies(movieID int PRIMARY KEY, title varchar(128), adult boolean, overview varchar(512), popularity float, releaseDate DATETIME, runtime int);"
    cursorObject = connectionObject.cursor()
    cursorObject.execute(sqlQuery)
    connectionObject.commit()


def create_MovieGenres_table(connectionObject):
    sqlQuery = "create TABLE IF NOT EXISTS MovieGenres(movieID int, genreID int, PRIMARY KEY(movieID, genreID));"
    cursorObject = connectionObject.cursor()
    cursorObject.execute(sqlQuery)
    connectionObject.commit()


def create_Genres_table(connectionObject):
    sqlQuery = "create TABLE IF NOT EXISTS Genres(genreID int PRIMARY KEY, genreName varchar(64));"
    cursorObject = connectionObject.cursor()
    cursorObject.execute(sqlQuery)
    connectionObject.commit()


def create_Actors_table(connectionObject):
    sqlQuery = "create TABLE IF NOT EXISTS Actors(actorID int PRIMARY KEY, actorName varchar(64), popularity float);"
    cursorObject = connectionObject.cursor()
    cursorObject.execute(sqlQuery)
    connectionObject.commit()


def create_MoviesActors_table(connectionObject):
    sqlQuery = "create TABLE IF NOT EXISTS MoviesActors(movieID int, actorID int, PRIMARY KEY(movieID, actorID));"
    cursorObject = connectionObject.cursor()
    cursorObject.execute(sqlQuery)
    connectionObject.commit()


def create_Directors_table(connectionObject):
    sqlQuery = "create TABLE IF NOT EXISTS Directors(directorID int PRIMARY KEY, directorName varchar(64));"
    cursorObject = connectionObject.cursor()
    cursorObject.execute(sqlQuery)
    connectionObject.commit()


def create_MovieDirector_table(connectionObject):
    sqlQuery = "create TABLE IF NOT EXISTS MovieDirector(movieID int, directorID int, PRIMARY KEY (movieID, directorID));"
    cursorObject = connectionObject.cursor()
    cursorObject.execute(sqlQuery)
    connectionObject.commit()


def create_MovieCollection_table(connectionObject):
    sqlQuery = "create TABLE IF NOT EXISTS MovieCollection(movieID int PRIMARY KEY, collectionID int);"
    cursorObject = connectionObject.cursor()
    cursorObject.execute(sqlQuery)
    connectionObject.commit()


def create_Collection_table(connectionObject):
    sqlQuery = "create TABLE IF NOT EXISTS Collection(collectionID int PRIMARY KEY, collectionName varchar(128));"
    cursorObject = connectionObject.cursor()
    cursorObject.execute(sqlQuery)
    connectionObject.commit()


connectionObject = pymysql.connect(host="127.0.0.1", user="DbMysql45", password="DbMysql45", db="DbMysql45",
                                   port=3305)

create_Movies_table(connectionObject)
create_MovieGenres_table(connectionObject)
create_Genres_table(connectionObject)
create_Actors_table(connectionObject)
create_MoviesActors_table(connectionObject)
create_Directors_table(connectionObject)
create_MovieDirector_table(connectionObject)
create_MovieCollection_table(connectionObject)
create_Collection_table(connectionObject)

