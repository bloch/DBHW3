import pymysql

from DBHW3.SRC.queries import *

""" input :  <movie_title> that the user give to the app
    output : list of movies' titles which belong to the
             the collection of <title>
"""
def show_query_1(movie_title , connectionObject):
    try:
        sql_query = build_query_1(movie_title)
        cursorObject = connectionObject.cursor()
        cursorObject.execute(sql_query)

        records = cursorObject.fetchall()

        print("Total number of rows in table: ", cursorObject.rowcount)
        print("\nPrinting each Movie's title")

        for row in records:
            print("Movie title = ", row[0])
    except pymysql.connect.Error as e:
        print("Error reading data from DbMysql45 Server ...", e)
    finally:
        if connectionObject.open():
            connectionObject.close()
            cursorObject.close()
            print("Connection to DbMysql45 server is close")


def show_query_2(actor_name, connectionObject):
    try:
        sql_query = build_query_2(actor_name)
        cursorObject = connectionObject.cursor()
        cursorObject.execute(sql_query)

        records = cursorObject.fetchall()

        print("Total number of rows in table: ", cursorObject.rowcount)
        print("\nPrinting each Movie's title")

        for row in records:
            print("Movie title = ", row[0])
    except pymysql.connect.Error as e:
        print("Error reading data from DbMysql45 Server ...", e)
    finally:
        if connectionObject.open():
            connectionObject.close()
            cursorObject.close()
            print("Connection to DbMysql45 server is close")


def show_query_3(user_runtime , genre, connectionObject):
    try:
        sql_query = build_query_3(user_runtime , genre)
        cursorObject = connectionObject.cursor()
        cursorObject.execute(sql_query)

        records = cursorObject.fetchall()

        print("Total number of rows in table: ", cursorObject.rowcount)
        print("\nPrinting each Movie's title")

        for row in records:
            print("Movie title = ", row[0])
    except pymysql.connect.Error as e:
        print("Error reading data from DbMysql45 Server ...", e)
    finally:
        if connectionObject.open():
            connectionObject.close()
            cursorObject.close()
            print("Connection to DbMysql45 server is close")

def show_query_4(short_description, connectionObject):
    try:
        sql_query = build_query_4()
        cursorObject = connectionObject.cursor()
        value = (short_description)
        cursorObject.execute(sql_query,value)

        records = cursorObject.fetchall()

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
        sql_query = build_query_5(start_date , end_date)
        cursorObject = connectionObject.cursor()
        cursorObject.execute(sql_query)

        records = cursorObject.fetchall()

        print("Total number of rows in table: ", cursorObject.rowcount)
        print("\nPrinting each Director's name")

        for row in records:
            print("Director name = ", row[0])
    except pymysql.connect.Error as e:
        print("Error reading data from DbMysql45 Server ...", e)
    finally:
        if connectionObject.open():
            connectionObject.close()
            cursorObject.close()
            print("Connection to DbMysql45 server is close")

def show_query_6(actor_name , director_name, connectionObject):
    try:
        sql_query = build_query_6(actor_name , director_name)
        cursorObject = connectionObject.cursor()
        cursorObject.execute(sql_query)

        records = cursorObject.fetchall()

        print("Total number of rows in table: ", cursorObject.rowcount)
        print("\nPrinting each Movie's title")

        for row in records:
            print("Movie title = ", row[0])
    except pymysql.connect.Error as e:
        print("Error reading data from DbMysql45 Server ...", e)
    finally:
        if connectionObject.open():
            connectionObject.close()
            cursorObject.close()
            print("Connection to DbMysql45 server is close")

connectionObject = pymysql.connect(host="127.0.0.1", user="DbMysql45", password="DbMysql45", db="DbMysql45",
                                   port=3305)


#show_query_1("Tom Holland" , connectionObject)