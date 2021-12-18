import requests

def movie_api_to_csv():
    url = "https://api.themoviedb.org/3/discover/movie"
    data = {'api_key': '6f5ab34a391be0d0e270142cbcf12323',
            'page': '1'}
    req = requests.get(url, data)
    movie_list = req.json()
    movie_id = movie_list['results'][0]['id']

    movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    data = {'api_key': '6f5ab34a391be0d0e270142cbcf12323'}
    req = requests.get(movie_url, data)
    movie_data = req.json()
    print(movie_data)


movie_api_to_csv()
