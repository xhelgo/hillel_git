import os
import string
import json


def avada_kedavra():
    for item in os.listdir():
        os.chdir(item)
        for letter in string.ascii_uppercase:
            try:
                os.rmdir(letter)
            except OSError as e:
                pass
        os.chdir("..")


def imperius(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)

    for i, film in enumerate(data):
        for k, result in enumerate(film["results"]):
            data[i]["results"][k]["type"] = "Winner"

    with open(json_file, "w") as file:
        json.dump(data, file)


def save_json(data, json_file):
    with open(json_file, "w") as file:
        json.dump(data, file)
