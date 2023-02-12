import os
from string import ascii_uppercase
from film_player import films_worker


def create_a_z_directories(path):
    """"Creates uppercase directories in letters range from A to Z in the provided path"""
    os.chdir(path)
    for letter in ascii_uppercase:
        os.mkdir(letter)


create_a_z_directories("film_player/film_storage")

wolf_wall_street = films_worker.Film("The Wolf of Wall Street")
wolf_wall_street.upload_file()
wolf_wall_street.get_film_address()
