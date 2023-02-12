import os
import requests
import json

url = "https://movie-database-alternative.p.rapidapi.com/"
querystring = {"s": "Avengers Endgame", "r": "json", "page": "1"}
headers = {
    "X-RapidAPI-Key": "390fed045bmsh823ad6022efcebap15957cjsn8118bcdd4b76",
    "X-RapidAPI-Host": "movie-database-alternative.p.rapidapi.com"
}

BASE_PATH = "film_player/film_storage/"


class Film:
    def __init__(self, film_name):
        querystring["s"] = film_name
        response = requests.request("GET", url, headers=headers, params=querystring)
        content = response.content
        results = json.loads(content)
        film = results["Search"][0]
        self.title = film["Title"]
        self.year = film["Year"]
        self.type = film["Type"]
        self.imdb = "https://www.imdb.com/title/" + film["imdbID"] + "/"
        self.poster = film["Poster"]
        self.storage = BASE_PATH + self.title[0] + "/" + self.title + ".txt"

    def get_film_address(self):
        return self.storage

    def upload_file(self):
        os.chdir(self.title[0])
        with open(self.title + ".txt", "w") as file:
            pass
