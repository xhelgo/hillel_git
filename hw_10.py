from additions import imdb_rank

# Task 4
filtered_movies = [movie for movie in imdb_rank if float(movie["rating"]) > 8.5]
rating_over_85 = list(sorted(filtered_movies, key=lambda x: x["rating"], reverse=True))


# Task 5
def film_trailer_search(film_name):
    for film in imdb_rank:
        if film["title"] == film_name:
            return film["trailer"]


# Task 6
def writers_or_director_search(person_name, all_movies):
    result = {"name": person_name, "number_of_films": 0, "films": []}
    for movie in all_movies:
        if movie["director"] == person_name or [x for x in movie["writers"] if person_name in x]:
            result["number_of_films"] += 1
            information = {"title": movie["title"],
                           "rank": movie["rank"]}
            result["films"].append(information)
    return result
