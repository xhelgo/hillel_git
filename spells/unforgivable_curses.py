import os
import string
import json
from hw_13 import films_awards_json

def avada_kedavra():
    for item in os.listdir():
        os.chdir(item)
        for letter in string.ascii_uppercase:
            try:
                os.rmdir(letter)
            except OSError as e:
                pass
        os.chdir("..")

avada_kedavra()

def imperius(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)
        data["file"] = "Winner"