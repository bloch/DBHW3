import pymysql


def drop_Actors_table():
    connectionObject = pymysql.connect(host="mysqlsrv1.cs.tau.ac.il", user="DbMysql45", password="DbMysql45",
                                       db="DbMysql45",
                                       port=3306)
    cursorObject = connectionObject.cursor()
    sqlQuery = "DROP TABLE Actors"
    cursorObject.execute(sqlQuery)
    connectionObject.commit()

def drop_Movies_table():
    connectionObject = pymysql.connect(host="mysqlsrv1.cs.tau.ac.il", user="DbMysql45", password="DbMysql45",
                                       db="DbMysql45",
                                       port=3306)
    cursorObject = connectionObject.cursor()
    sqlQuery = "DROP TABLE Movies"
    cursorObject.execute(sqlQuery)
    connectionObject.commit()

def drop_Genres_table(connectionObject):

    cursorObject = connectionObject.cursor()
    sqlQuery = "DROP TABLE Genres"
    cursorObject.execute(sqlQuery)
    connectionObject.commit()

connectionObject = pymysql.connect(host="mysqlsrv1.cs.tau.ac.il", user="DbMysql45", password="DbMysql45", db="DbMysql45",
                                   port=3306)


drop_Genres_table()
