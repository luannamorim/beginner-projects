import json
from functools import reduce

f = open("./filter-map/aquarium.json", encoding="utf8")
data_aquarium = json.load(f)
animals = data_aquarium["data"]


def pick_animal_type(animal):
    return animal["type"], 1


def reducer(acc, val):
    if val[0] in acc.keys():
        acc[val]


typ_animals = list(map(pick_animal_type, animals))
print(typ_animals)
reduce(reducer, typ_animals, {})