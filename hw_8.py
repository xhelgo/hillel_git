# Task 1
num = 1
sum = 0

while num <= 100:
    sum += num
    num += 1


# Task 2
lst = [10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95, 12, 255, 124, 466, 9]
num = 0

while num < len(lst):
    if lst[num] == 100:
        print("Знайшов 100 під індексом №:", str(num))
        break
    num += 1


# Task 3
from additions import film_desc

keywords = []
film_keywords = film_desc["results"]["keywords"]
i = 0

while i < len(film_keywords):
    keywords.append(film_keywords[i]["keyword"])
    i += 1


# Task 4
from additions import film_awards
films_awards = [award['award_name'] for award in film_awards["results"]]

# Task 5
films_awards_type = [{award['award_name']: award["type"]} for award in film_awards["results"]]
