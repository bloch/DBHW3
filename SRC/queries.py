def build_query_1():
    nested_query = "select MC2.collectionID " \
            "from Movies as M2 , MovieCollection as MC2 " \
            "where M2.movieID = MC2.movieID AND %s = M2.title"

    query = "select M1.title " \
             "from MovieCollection as MC1 , Movies as M1 " \
             "where M1.movieID = MC1.movieID AND MC1.collectionID IN (" + nested_query + ")"
    return query

def build_query_2():
    nested_query = "select MA2.movieID " \
                   "from MoviesActors as MA2 , Actors as A2 " \
                   "where MA2.actorID = A2.actorID AND A2.actorName = %s "

    query = "select M1.title " \
            "from Movies as M1 " \
            "where M1.movieID IN (" + nested_query +") " \
            "order by M1.popularity desc " \
            "limit 5 "

    return query


def build_query_3():
    nested_query = "select M2.movieID " \
                   "from MovieGenres as MG2 , Movies as M2 , Genres as G2 " \
                   "where M2.movieID = MG2.movieID AND MG2.genreID = G2.genreID AND G2.genreName = %s"

    query = "select M1.title " \
            "from Movies as M1 " \
            "where M1.runtime <= %s AND M1.movieID IN (" + nested_query + ") " \
            "order by M1.popularity desc " \
            "limit 5"

    return query


def build_query_4():
    query = "select M.title " \
            "from Movies as M " \
            "where INSTR(M.overview , %s) " \
            "order by M.popularity desc " \
            "limit 5"
    print(query)
    return query


def build_query_5():
    nested_query = "select MD2.directorID " \
                   "from Movies as M2 , MovieDirector as MD2 " \
                   "where MD2.movieID = M2.movieID AND M2.releaseDate BETWEEN %s AND %s " \
                   "group by MD2.directorID " \
                   "order by AVG(M2.popularity) desc "

    query = "select D.directorName " \
            "from Directors as D " \
            "where D.directorID IN (" + nested_query + ") " \
            "limit 5 "
    return query


def build_query_6():
    query = "select M.title " \
                   "from Directors as D , Actors as A , MoviesActors as MA , MovieDirector as MD , Movies as M " \
                   "where %s = A.actorName AND A.actorID = MA.actorID AND MA.movieID = M.movieID " \
                                           "AND M.movieID = MD.movieID AND MD.directorID = D.directorID " \
                                           "AND D.directorName = %s " \
                                           "order by M.popularity desc " \
                                           "limit 10 "
    return query

""" list of movie titles which <director_name> has directed them ,
    in genre <genre> in range <start_date> - <end_date>
    and also the actors with the highest po 
"""
def build_query_7():
    nested_query_1 = "select M2.movieID as movie_id " \
                    "from Movies as M2 , Directors D2 , MovieDirector as MD2 , Genres G2 , MovieGenres as MG2 " \
                    "where M2.movieID = MD2.movieID AND D2.directorID = MD2.directorID AND D2.directorName = %s AND MD2.movieID = MG2.movieID " \
                    "AND G2.genreID = MG2.genreID AND G2.genreName = %s AND M2.releaseDate BETWEEN %s AND %s "


    query = "select M1.title " \
            "from MoviesActors as MA1 , Movies as M1 , (" + nested_query_1 + ") as Query1 , Actors as A1 " \
            "where MA1.movieID = M1.movieID AND MA1.movieID = Query1.movie_id AND A1.actorID = MA1.actorID " \
            "group by M1.movieID " \
            "order by AVG(A1.popularity) " \
            "limit 10"

    return query