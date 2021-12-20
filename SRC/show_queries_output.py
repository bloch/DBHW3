import pymysql

from queries import *

""" input :  <movie_title> that the user give to the app
    output : list of movies' titles which belong to the
             the collection of <title>
"""
def show_query_1(movie_title , connectionObject):
    try:
        sql_query = build_query_1()
        cursorObject = connectionObject.cursor()
        values = (movie_title)
        cursorObject.execute(sql_query, values)

        records = cursorObject.fetchall()
        if len(records) == 0:
            print("We are sorry, no collection found for the movie " + movie_title + "!")
            return

        print("Total number of rows in table: ", cursorObject.rowcount)
        print("\nPrinting each Movie's title")

        for row in records:
            print("Movie title = ", row[0])
    except pymysql.connect.Error as e:
        print("Error reading data from DbMysql45 Server ...", e)
    finally:
        if connectionObject.open:
            connectionObject.close()
            cursorObject.close()
            print("Connection to DbMysql45 server closed")


def show_query_2(actor_name, connectionObject):
    try:
        sql_query = build_query_2()
        cursorObject = connectionObject.cursor()
        values = (actor_name)
        cursorObject.execute(sql_query, values)

        records = cursorObject.fetchall()
        if len(records) == 0:
            print("We are sorry, no movies DB in which " + actor_name + "played in!")
            return

        print("Total number of rows in table: ", cursorObject.rowcount)
        print("\nPrinting each Movie's title")

        for row in records:
            print("Movie title = ", row[0])
    except pymysql.connect.Error as e:
        print("Error reading data from DbMysql45 Server ...", e)
    finally:
        if connectionObject.open:
            connectionObject.close()
            cursorObject.close()
            print("Connection to DbMysql45 server closed")


def show_query_3(user_runtime, genre, connectionObject):
    try:
        sql_query = build_query_3()
        cursorObject = connectionObject.cursor()
        values = (user_runtime, genre)
        cursorObject.execute(sql_query, values)

        records = cursorObject.fetchall()
        if len(records) == 0:
            print("We are sorry, no movies DB shorter then " + str(user_runtime) + " minutes and from genre " + genre + "!")
            return

        print("Total number of rows in table: ", cursorObject.rowcount)
        print("\nPrinting each Movie's title")

        for row in records:
            print("Movie title = ", row[0])
    except pymysql.connect.Error as e:
        print("Error reading data from DbMysql45 Server ...", e)
    finally:
        if connectionObject.open:
            connectionObject.close()
            cursorObject.close()
            print("Connection to DbMysql45 server is close")

def show_query_4(short_description, connectionObject):
    try:
        sql_query = build_query_4()
        cursorObject = connectionObject.cursor()
        values = (short_description)
        cursorObject.execute(sql_query, values)

        records = cursorObject.fetchall()
        if len(records) == 0:
            print("We are sorry, no movies in DB that include '" + short_description + "' in their overview!")
            return

        print("Total number of rows in table: ", cursorObject.rowcount)
        print("\nPrinting each Movie's title")

        for row in records:
            print("Movie title = ", row[0])
    except pymysql.connect.Error as e:
        print("Error reading data from DbMysql45 Server ...", e)
    finally:
        if connectionObject.open:
            connectionObject.close()
            cursorObject.close()
            print("Connection to DbMysql45 server is close")

def show_query_5(start_date , end_date, connectionObject):
    try:
        sql_query = build_query_5()
        cursorObject = connectionObject.cursor()
        values = (start_date, end_date)
        cursorObject.execute(sql_query, values)

        records = cursorObject.fetchall()
        if len(records) == 0:
            print("We are sorry, your range of dates yields no data in DB!")
            return

        print("Total number of rows in table: ", cursorObject.rowcount)
        print("\nPrinting each Director's name")

        for row in records:
            print("Director name = ", row[0])
    except pymysql.connect.Error as e:
        print("Error reading data from DbMysql45 Server ...", e)
    finally:
        if connectionObject.open:
            connectionObject.close()
            cursorObject.close()
            print("Connection to DbMysql45 server is close")

def show_query_6(actor_name , director_name, connectionObject):
    try:
        sql_query = build_query_6()
        cursorObject = connectionObject.cursor()
        values = (actor_name, director_name)
        cursorObject.execute(sql_query, values)

        records = cursorObject.fetchall()
        if len(records) == 0:
            print("We are sorry, there are no films in which " + actor_name + " was an actor and " + director_name + " was a director!")
            return

        print("Total number of rows in table: ", cursorObject.rowcount)
        print("\nPrinting each Movie's title")

        for row in records:
            print("Movie title = ", row[0])
    except pymysql.connect.Error as e:
        print("Error reading data from DbMysql45 Server ...", e)
    finally:
        if connectionObject.open:
            connectionObject.close()
            cursorObject.close()
            print("Connection to DbMysql45 server is close")


def show_query_7(director_name, genre_name, start_date, end_date, connectionObject):
    try:
        sql_query = build_query_7()
        cursorObject = connectionObject.cursor()
        values = (director_name, genre_name, start_date, end_date)
        cursorObject.execute(sql_query, values)

        records = cursorObject.fetchall()
        if len(records) == 0:
            print("We are sorry, there are no relevant movies for your requirements!")
            return

        print("Total number of rows in table: ", cursorObject.rowcount)
        print("\nPrinting each Movie's title")

        for row in records:
            print("Movie title = ", row[0])
    except pymysql.connect.Error as e:
        print("Error reading data from DbMysql45 Server ...", e)
    finally:
        if connectionObject.open:
            connectionObject.close()
            cursorObject.close()
            print("Connection to DbMysql45 server is close")

# connectionObject = pymysql.connect(host="mysqlsrv1.cs.tau.ac.il", user="DbMysql45", password="DbMysql45", db="DbMysql45",
#                                    port=3306)
# show_query_1("Spider-Man: No Way Home", connectionObject)
#
# connectionObject = pymysql.connect(host="mysqlsrv1.cs.tau.ac.il", user="DbMysql45", password="DbMysql45", db="DbMysql45",
#                                    port=3306)
# show_query_2("Tom Holland", connectionObject)
#
# connectionObject = pymysql.connect(host="mysqlsrv1.cs.tau.ac.il", user="DbMysql45", password="DbMysql45", db="DbMysql45",
#                                    port=3306)
# show_query_3(100, "Comedy", connectionObject)
#

# connectionObject = pymysql.connect(host="mysqlsrv1.cs.tau.ac.il", user="DbMysql45", password="DbMysql45", db="DbMysql45",
#                                    port=3306)
# show_query_4("Peter Parker", connectionObject)

# connectionObject = pymysql.connect(host="mysqlsrv1.cs.tau.ac.il", user="DbMysql45", password="DbMysql45", db="DbMysql45",
#                                    port=3306)
# show_query_5("2019-01-01", "2021-01-01", connectionObject)
#
# connectionObject = pymysql.connect(host="mysqlsrv1.cs.tau.ac.il", user="DbMysql45", password="DbMysql45", db="DbMysql45",
#                                    port=3306)
# show_query_6("Tom Holland", "Jon Watts", connectionObject)

connectionObject = pymysql.connect(host="mysqlsrv1.cs.tau.ac.il", user="DbMysql45", password="DbMysql45", db="DbMysql45",
                                   port=3306)
show_query_7("Quentin Tarantino", "Action", "2005-01-01", "2021-01-01", connectionObject)
