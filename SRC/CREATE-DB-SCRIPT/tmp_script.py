import pymysql


def drop_Actors_table():
    connectionObject = pymysql.connect(host="127.0.0.1", user="DbMysql45", password="DbMysql45", db="DbMysql45",
                                       port=3305)
    cursorObject = connectionObject.cursor()
    sqlQuery = "DROP TABLE Actors"
    cursorObject.execute(sqlQuery)
    connectionObject.commit()

def drop_Genres_table():
    connectionObject = pymysql.connect(host="127.0.0.1", user="DbMysql45", password="DbMysql45", db="DbMysql45",
                                       port=3305)
    cursorObject = connectionObject.cursor()
    sqlQuery = "DROP TABLE Genres"
    cursorObject.execute(sqlQuery)
    connectionObject.commit()

drop_Genres_table()
