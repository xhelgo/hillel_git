import os
from create_directories_additions import films_awards
from spells import unforgivable_curses

os.chdir("HW_13/Harry Potter")
unforgivable_curses.avada_kedavra()

os.chdir("/home/admin_o/PycharmProjects/hillel_git")
unforgivable_curses.save_json(data=films_awards, json_file="films_awards.json")
unforgivable_curses.imperius('films_awards.json')
