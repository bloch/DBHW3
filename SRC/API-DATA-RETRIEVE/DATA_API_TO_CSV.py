import requests
import json

def movies_api_to_json():
    url = "https://api.themoviedb.org/3/discover/movie"
    index = 0
    movies = {}
    for i in range(1, 500):
        headers = {'api_key': '6f5ab34a391be0d0e270142cbcf12323', 'page': str(i)}
        try:
            req = requests.get(url, headers)
            movie_list = req.json()
            movie_list = movie_list['results']
            movie_ids = [movie['id'] for movie in movie_list]
            for movie_id in movie_ids:
                movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
                headers = {'api_key': '6f5ab34a391be0d0e270142cbcf12323'}
                try:
                    req = requests.get(movie_url, headers)
                    movie_json = req.json()
                    movies[str(index)] = movie_json
                    index += 1

                    with open('movies.json', 'w') as f:
                        data = json.dump(movies, f, indent=4)
                except Exception as e:
                    print("Exeception occured in inner loop: {}".format(e))
                    continue

        except Exception as e:
            print("Exeception occured in outer loop:{}".format(e))
            continue


def credits_api_to_json():
    url = "https://api.themoviedb.org/3/discover/movie"
    actors = {}
    directors = {}

    # movies_json_file = open('movies.json')
    # movies_data = json.load(movies_json_file)

    movies_data = ['580489', '634649', '566525']

    for index, movie_data in movies_data:
        movie_index = movie_data['id']
        movie_url = f"https://api.themoviedb.org/3/movie/{str(movie_index)}/credits"
        headers = {'api_key': '6f5ab34a391be0d0e270142cbcf12323'}
        req = requests.get(movie_url, headers)
        cast_data = req.json()
        print(cast_data)
        actors_current_movie = []
        directors_current_movie = []
        for entry in cast_data["cast"]:
            if entry["known_for_department"] == "Acting":
                actors_current_movie.append({'id': entry['id'], 'name':entry['name'], 'popularity': entry['popularity']})

        for entry in cast_data["crew"]:
            if entry["known_for_department"] == "Directing" and entry["job"] == "Director":
                directors_current_movie.append({'id': entry['id'], 'name': entry['name']})

        actors[str(movie_index)] = actors_current_movie
        directors[str(movie_index)] = directors_current_movie

        with open('actors.json', 'w') as f:
            data = json.dump(actors, f, indent=4)

        with open('directors.json', 'w') as f:
            data = json.dump(directors, f, indent=4)


credits_api_to_json()
