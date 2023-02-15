import os
import string


def create_a_z_directories():
    for item in os.listdir():
        os.chdir(item)
        for letter in string.ascii_uppercase:
            os.mkdir(letter)
        os.chdir("..")


class MapMagic:
    def __init__(self):
        self.__map_open = "I solemnly swear that I am up to no good."
        self.__map_close = "Mischief managed."


class MarauderMap(MapMagic):
    films_titles = {
        "results": [
            {
                "imdb_id": "tt1201607",
                "title": "Harry Potter and the Deathly Hallows: Part 2"
            },
            {
                "imdb_id": "tt0241527",
                "title": "Harry Potter and the Sorcerer's Stone"
            },
            {
                "imdb_id": "tt0926084",
                "title": "Harry Potter and the Deathly Hallows: Part 1"
            },
            {
                "imdb_id": "tt0304141",
                "title": "Harry Potter and the Prisoner of Azkaban"
            },
            {
                "imdb_id": "tt0417741",
                "title": "Harry Potter and the Half-Blood Prince"
            },
            {
                "imdb_id": "tt0295297",
                "title": "Harry Potter and the Chamber of Secrets"
            },
            {
                "imdb_id": "tt0330373",
                "title": "Harry Potter and the Goblet of Fire"
            },
            {
                "imdb_id": "tt0373889",
                "title": "Harry Potter and the Order of the Phoenix"
            }
        ]
    }

    def __init__(self, path):
        super().__init__()
        self.path = path

    def create_film_directory(self):
        for film in self.films_titles["results"]:
            os.mkdir(film["title"])

    def map_generator(self):
        print(self._MapMagic__map_open)
        os.chdir(self.path)
        self.create_film_directory()
        create_a_z_directories()
        print(self._MapMagic__map_close)

