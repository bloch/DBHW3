import pymysql


def create_indexes_Movies_Table(connectionObject):
    try:
        # index for query 1: hash index on titles
        cursorObject = connectionObject.cursor()
        sqlQuery = "CREATE INDEX titles_index USING HASH ON Movies(title)"
        cursorObject.execute(sqlQuery)
        connectionObject.commit()
        # index for query 5: btree index for range query over dates
        cursorObject = connectionObject.cursor()
        sqlQuery = "CREATE INDEX releaseDates_index USING BTREE ON Movies(releaseDate)"
        cursorObject.execute(sqlQuery)
        connectionObject.commit()
        # index for query 4: fulltext index for the overview column
        cursorObject = connectionObject.cursor()
        sqlQuery = "CREATE FULLTEXT INDEX overview_index ON Movies(overview)"
        cursorObject.execute(sqlQuery)
        connectionObject.commit()

    except Exception as e:
        print("ERROR! wasn't able to define an index for Movies table: {}".format(e))


def create_indexes_Actors_Table(connectionObject):
    try:
        # index for query 2 and 6: hash index on actor names
        cursorObject = connectionObject.cursor()
        sqlQuery = "CREATE INDEX actor_names_index USING HASH ON Actors(actorName)"
        cursorObject.execute(sqlQuery)
        connectionObject.commit()

    except Exception as e:
        print("ERROR! wasn't able to define an index for Actors table: {}".format(e))


def create_indexes_Directors_Table(connectionObject):
    try:
        # index for query 6: hash index on directors names
        cursorObject = connectionObject.cursor()
        sqlQuery = "CREATE INDEX director_names_index USING HASH ON Directors(directorName)"
        cursorObject.execute(sqlQuery)
        connectionObject.commit()

    except Exception as e:
        print("ERROR! wasn't able to define an index for Directors table: {}".format(e))


def create_indexes_Genres_Table(connectionObject):
    try:
        # index for query 6: hash index on directors names
        cursorObject = connectionObject.cursor()
        sqlQuery = "CREATE INDEX genre_names_index USING HASH ON Genres(genreName)"
        cursorObject.execute(sqlQuery)
        connectionObject.commit()

    except Exception as e:
        print("ERROR! wasn't able to define an index for Genres table: {}".format(e))

# connectionObject = pymysql.connect(host="mysqlsrv1.cs.tau.ac.il", user="DbMysql45", password="DbMysql45", db="DbMysql45",
#                                    port=3306)

# create_indexes_Movies_Table(connectionObject)
# create_indexes_Actors_Table(connectionObject)
# create_indexes_Directors_Table(connectionObject)
# create_indexes_Genres_Table(connectionObject)
# connectionObject.close()
