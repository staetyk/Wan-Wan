import csv
import alchemy
from collections import OrderedDict

recipes = OrderedDict()

with open("combos.csv") as file:
    reader = csv.reader(file)
    for line in reader:
        recipes[tuple(sorted((line[0], line[1])))] = line[2]

def find(target: str, current: list[str] = alchemy.starting) -> tuple[int, ...]:
    return (0,)

def display(path: tuple[int, ...]) -> str:
    out = ""
    for x in path:
        out += "\u001b[1m"
        out += list(recipes.keys())[x][0] + "\u001b[m + \u001b[1m"
        out += list(recipes.keys())[x][1] + "\u001b[m = \u001b[1m"
        out += list(recipes.values())[x] + "\u001b[m\n"
    out = out.rstrip("\n")
    return out