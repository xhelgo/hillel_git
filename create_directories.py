import os
import string
from create_directories_additions import films_titles, films_awards

os.chdir("HW_13")

os.mkdir("Harry Potter")
os.chdir("Harry Potter")


def create_film_directory():
    for film in films_titles["results"]:
        os.mkdir(film["title"])


def create_a_z_directories():
    for item in os.listdir():
        os.chdir(item)
        for letter in string.ascii_uppercase:
            os.mkdir(letter)
        os.chdir("..")


def movie_awards_to_dict():
    movies_awards = {}

    for part in films_awards:
        awards_list = []
        for film in part["results"]:
            title = film["movie"]["title"]
            awards_list.append({
                "type": film["type"],
                "award_name": film["award_name"],
                "award": film["award"]
            })

        movies_awards[title] = awards_list

    return movies_awards


def create_award_directory():
    for movie, awards in sorted_movies_awards.items():
        os.chdir(movie)
        for award in awards:
            award_first_letter = award["award_name"][0]
            os.chdir(award_first_letter)

            filename = award["award_name"]

            def write_award_name_to_file():
                with open(filename, "w") as file:
                    for award2 in awards:
                        if award2["award_name"] == filename:
                            award_string = award2["award"] + "\n"
                            file.write(award_string)
            write_award_name_to_file()

            os.chdir("..")
        os.chdir("..")


create_film_directory()
create_a_z_directories()
movies_awards = movie_awards_to_dict()

# Sort lists by award_name
sorted_movies_awards = {key: sorted(value, key=lambda x: x["award_name"]) for key, value in movies_awards.items()}

create_award_directory()
