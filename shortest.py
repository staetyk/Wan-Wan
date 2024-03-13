import csv
import alchemy

recipes = {}

with open("combos.csv") as file:
    reader = csv.reader(file)
    for line in reader:
        recipes[tuple(sorted((line[0], line[1])))] = line[2]

def find(target: str, current: list[str] = alchemy.starting) -> tuple[int, ...]:
    return (0,)