def build_query_1(title):
    nested_query = "select MC2.collectionID " \
            "from Movies as M2 , MovieCollection as MC2 " \
            "where M2.movieID = MC2.movieID AND " + title + " = M2.title"

    query = "select M1.title " \
             "from MovieCollection as MC1 , Movies as M1 " \
             "where M1.movieID = MC1.movieID AND MC1.collectionID IN (" + nested_query +") " \

    return query

def build_query_2(actor_name):
    nested_query = "select MA2.movieID " \
                   "from MoviesActors as MA2 , Actors as A2 " \
                   "where MA2.actorID = A2.actorID AND A2.actorName = " + actor_name + " "

    query = "select M1.movieName " \
            "from Movie as M1 " \
            "where M1.movieID IN (" + nested_query +") " \
            "order by M1.popularity desc " \
            "limit(5)" \


    print(query)

build_query_2("nb")