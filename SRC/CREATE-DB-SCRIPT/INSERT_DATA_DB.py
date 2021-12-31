import pymysql
import json


def insert_data_Actors_table(connectionObject):
    actors_json_file = open('../API-DATA-RETRIEVE/actors.json')
    actors_data = json.load(actors_json_file)

    for movie_id, actors_list in actors_data.items():
        actors = []
        for actor in actors_list:
            try:
                actor_id = actor['id']
                actor_name = actor['name']
                actor_popularity = actor['popularity']
                actors.append((actor_id, actor_name, actor_popularity))
            except Exception as e:
                print("ERROR! wasn't able to insert actor: {}".format(e))
                continue

        actors = sorted(actors, key=lambda tup: tup[2], reverse=True)
        for i in range(3):
            try:
                cursorObject = connectionObject.cursor()
                sqlQuery = "INSERT INTO Actors (actorID, actorName, popularity) VALUES (%s,%s,%s)"
                values = (actors[i][0], actors[i][1], actors[i][2])
                cursorObject.execute(sqlQuery, values)
                connectionObject.commit()
            except Exception as e:
                print("ERROR! wasn't able to insert actor: {}".format(e))
                continue


def insert_data_Directors_table(connectionObject):
    directors_json_file = open('../API-DATA-RETRIEVE/directors.json')
    directors_data = json.load(directors_json_file)

    for movie_id, directors_list in directors_data.items():
        for actor in directors_list:
            try:
                director_id = actor['id']
                director_name = actor['name']
                cursorObject = connectionObject.cursor()
                sqlQuery = "INSERT INTO Directors (directorID, directorName) VALUES (%s,%s)"
                values = (director_id, director_name)
                cursorObject.execute(sqlQuery, values)
                connectionObject.commit()
            except Exception as e:
                print("ERROR! wasn't able to insert director: {}".format(e))
                continue


def insert_data_Genres_table(connectionObject):
    movies_json_file = open('../API-DATA-RETRIEVE/movies.json')
    movies_data = json.load(movies_json_file)
    for movie_id, movie_data in movies_data.items():
        try:
            genres_list = movie_data['genres']
            for genre in genres_list:
                genre_id = genre['id']
                genre_name = genre['name']
                cursorObject = connectionObject.cursor()
                sqlQuery = "INSERT INTO Genres (genreID, genreName) VALUES (%s,%s)"
                values = (genre_id, genre_name)
                cursorObject.execute(sqlQuery, values)
                connectionObject.commit()
        except Exception as e:
            print("ERROR! wasn't able to insert genre: {}".format(e))
            continue


def insert_data_Collection_table(connectionObject):
    movies_json_file = open('../API-DATA-RETRIEVE/movies.json')
    movies_data = json.load(movies_json_file)
    for movie_id, movie_data in movies_data.items():
        try:
            collection_data = movie_data['belongs_to_collection']
            if collection_data is None:
                continue
            collection_id = collection_data['id']
            collection_name = collection_data['name']
            cursorObject = connectionObject.cursor()
            sqlQuery = "INSERT INTO Collection (collectionID, collectionName) VALUES (%s,%s)"
            values = (collection_id, collection_name)
            cursorObject.execute(sqlQuery, values)
            connectionObject.commit()

        except Exception as e:
            print("ERROR! wasn't able to insert collection: {}".format(e))
            continue


def insert_data_MovieCollection_table(connectionObject):
    movies_json_file = open('../API-DATA-RETRIEVE/movies.json')
    movies_data = json.load(movies_json_file)
    for movie_id, movie_data in movies_data.items():
        try:
            id = movie_data['id']
            collection_data = movie_data['belongs_to_collection']
            if collection_data is None:
                continue
            collection_id = collection_data['id']
            cursorObject = connectionObject.cursor()
            sqlQuery = "INSERT INTO MovieCollection (movieID, collectionID) VALUES (%s,%s)"
            values = (id, collection_id)
            cursorObject.execute(sqlQuery, values)
            connectionObject.commit()

        except Exception as e:
            print("ERROR! wasn't able to insert to MovieCollection: {}".format(e))
            continue


def insert_data_MoviesActors_table(connectionObject):
    actors_json_file = open('../API-DATA-RETRIEVE/actors.json')
    actors_data = json.load(actors_json_file)

    for movie_id, actors_list in actors_data.items():
        actors = []
        for actor in actors_list:
            try:
                actor_id = actor['id']
                actor_name = actor['name']
                actor_popularity = actor['popularity']
                actors.append((actor_id, actor_name, actor_popularity))
            except Exception as e:
                print("ERROR! wasn't able to insert actor: {}".format(e))
                continue

        actors = sorted(actors, key=lambda tup: tup[2], reverse=True)
        for i in range(3):
            try:
                cursorObject = connectionObject.cursor()
                sqlQuery = "INSERT INTO MoviesActors (movieID, actorID) VALUES (%s,%s)"
                values = (int(movie_id), actors[i][0])
                cursorObject.execute(sqlQuery, values)
                connectionObject.commit()
            except Exception as e:
                print("ERROR! wasn't able to insert to MoviesActors: {}".format(e))
                continue


def insert_data_MoviesDirectors_table(connectionObject):
    directors_json_file = open('../API-DATA-RETRIEVE/directors.json')
    directors_data = json.load(directors_json_file)

    for movie_id, directors_list in directors_data.items():
        for actor in directors_list:
            try:
                director_id = actor['id']
                director_name = actor['name']
                cursorObject = connectionObject.cursor()
                sqlQuery = "INSERT INTO MovieDirector (movieID, directorID) VALUES (%s,%s)"
                values = (int(movie_id), director_id)
                cursorObject.execute(sqlQuery, values)
                connectionObject.commit()
            except Exception as e:
                print("ERROR! wasn't able to insert to MovieDirector: {}".format(e))
                continue


def insert_data_MovieGenres_table(connectionObject):
    movies_json_file = open('../API-DATA-RETRIEVE/movies.json')
    movies_data = json.load(movies_json_file)
    for movie_id, movie_data in movies_data.items():
        try:
            id = movie_data['id']
            genres_list = movie_data['genres']
            for genre in genres_list:
                genre_id = genre['id']
                genre_name = genre['name']
                cursorObject = connectionObject.cursor()
                sqlQuery = "INSERT INTO MovieGenres (movieID, genreID) VALUES (%s,%s)"
                values = (id, genre_id)
                cursorObject.execute(sqlQuery, values)
                connectionObject.commit()
        except Exception as e:
            print("ERROR! wasn't able to insert to MovieGenres: {}".format(e))
            continue


def insert_data_Movies_table(connectionObject):
    movies_json_file = open('../API-DATA-RETRIEVE/movies.json')
    movies_data = json.load(movies_json_file)

    for movie_id, movie_data in movies_data.items():
        try:
            id = movie_data['id']
            title = movie_data['title']
            if movie_data['adult']:
                adult = 1
            else:
                adult = 0
            overview = movie_data['overview']
            if len(overview) > 512:
                overview = overview[:512]
            popularity = movie_data['popularity']
            releaseDate = movie_data['release_date']
            if releaseDate == "":
                releaseDate = "1900-01-01"
            runtime = movie_data['runtime']
            cursorObject = connectionObject.cursor()
            sqlQuery = "INSERT INTO Movies (movieID, title, adult, overview, popularity, releaseDate, runtime) VALUES (%s,%s,%s,%s, %s, %s, %s)"
            values = (id, title, adult, overview, popularity, releaseDate, runtime)
            cursorObject.execute(sqlQuery, values)
            connectionObject.commit()
        except Exception as e:
            print("ERROR! wasn't able to insert to MovieGenres: {}".format(e))
            continue


# connectionObject = pymysql.connect(host="mysqlsrv1.cs.tau.ac.il", user="DbMysql45", password="DbMysql45", db="DbMysql45",
#                                    port=3306)
#
# insert_data_Movies_table(connectionObject)
# insert_data_Actors_table(connectionObject)
# insert_data_Directors_table(connectionObject)
# insert_data_Genres_table(connectionObject)
# insert_data_Collection_table(connectionObject)
# insert_data_MovieCollection_table(connectionObject)
# insert_data_MoviesActors_table(connectionObject)
# insert_data_MoviesDirectors_table(connectionObject)
# insert_data_MovieGenres_table(connectionObject)
