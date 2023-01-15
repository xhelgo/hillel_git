from additions import film_awards, actor_films


# Task 4
def award_search(award_name):
    for award in film_awards["results"]:
        if award["award_name"] == award_name:

            actors = []

            if award["actor"]:
                for actor in award["actor"]:
                    actors.append(actor["name"])
            else:
                actors = None

    return (award["award_name"], award["year"], actors, award["type"])


# Task 5
def rating_filter(number):
    films = []

    if number > 10:
        print("Rating cannot be more than '10'. Choose a smaller number.")

    else:

        for film in actor_films["results"]:
            if film[0]["rating"] > number:
                films.append((film[0]["title"], film[0]["rating"]))

        if films:
            return films
        else:
            print("Nothing found")
