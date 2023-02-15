import os
from spells import marauder_map
os.chdir("HW_15")
os.mkdir("Harry Potter")

mischief = marauder_map.MarauderMap("Harry Potter")
mischief.map_generator()
