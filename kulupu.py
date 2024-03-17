import csv
from alchemy import unlocked, elements, recipes, combine

groups = {}
with open("categories.csv", "r") as file:
    reader = csv.reader(file)
    for line in reader:
        start = f"\u001b[{line[1]}m"
        end = f"\u001b[{line[2]}m"
        look = start + "{}" + end
        groups[line[0]] = {
            "look" : look,
            "words" : set(line[3:]),
            "done" : False
        }

def kule(*words: tuple[str, ...]):
    out = []
    for word in words:
        w = word
        for x,y in groups.items():
            if word in y["words"]: w = y["look"].format(w)
        out.append(w)
    return tuple(out)

def pini():
    global groups
    for x,y in groups.items():
        if not y["done"] and y["words"].issubset(unlocked): y["done"] = True

def pana():
    print("\u001b[2J\u001b[H\u001b[m", end = "")
    out = ""
    for x,y in groups.items():
        if y["done"]:
            out += f"•sina jo e {y['look'].format(f'kulupu {x}')} ale a!\n"
    if len(unlocked) == len(set(elements)):
        out += f"•sina jo e \u001b[1mnimi ale\u001b[22m a!\n"
    if len(set(recipes)) == len(combine):
        out += f"•sina jo e \u001b[1mnasin ale\u001b[22m a!"
    out = out.rstrip("\n")
    print(out)
    input()
    print("\u001b[2J\u001b[H\u001b[m", end = "")