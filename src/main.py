import os

import requests
from dotenv import load_dotenv

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_ACCESS_TOKEN = os.getenv("TMDB_ACCESS_TOKEN")
# plan
# 1. get database of movies
# 2. ask user for movie name
# 3. get movie attributes
# 4. search for similar movies
# 5. add one more mode for saving movies
# 6. means adding database of saved movies
# 7. make interface for command line


def get_popular_movies():
    url = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_ACCESS_TOKEN}",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Popular Movies:")
        for movie in response.json()["results"]:
            print(f"- {movie['title']}")
    else:
        print("Failed to fetch popular movies:", response.json())


def find_similar_movies(movie_name):
    url = "https://api.themoviedb.org/3/search/movie"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_ACCESS_TOKEN}",
    }
    params = {"query": movie_name, "api_key": TMDB_API_KEY}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        results = response.json()["results"]
        if results:
            movie_id = results[0]["id"]
            similar_url = f"https://api.themoviedb.org/3/movie/{movie_id}/similar"
            similar_response = requests.get(similar_url, headers=headers)
            if similar_response.status_code == 200:
                print(f"Similar movies to '{movie_name}':")
                for movie in similar_response.json()["results"]:
                    print(f"- {movie['title']}")
            else:
                print("Failed to fetch similar movies:", similar_response.json())
        else:
            print(f"No movies found for '{movie_name}'")
    else:
        print("Failed to search for movies:", response.json())


def main():
    print("Welcome to Movie Bot!")
    print("Enter a movie name to search for similar movies:")
    movie_name = input()
    find_similar_movies(movie_name)


if __name__ == "__main__":
    main()
