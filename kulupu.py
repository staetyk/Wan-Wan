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

def kule(words: list[str]):
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
            out += f"\t• sina jo e \u001b[1;3m{y['look'].format(f'kulupu {x}')}\u001b[22;23m ale a!\n"
    if len(unlocked) == len(set(elements)):
        out += f"\t• sina jo e \u001b[1;3;38;2;255;228;18mnimi ale\u001b[22;23;39m a!\n"
    if len(set(recipes)) == len(combine):
        out += f"\t• sina jo e \u001b[1;3;38;2;255;228;18mnasin ale\u001b[22;23;39m a!"
    out = out.rstrip("\n")
    if out == "":
        out = "\u001b[2;3msina jo ala e pali pini tenpo sama.\u001b[22;23m"
    else:
        out = "f\u001b[1;3mpali pini sina:\u001b[m\n" + out
    print(out)
    input("\u001b[8m")
    print("\u001b[2J\u001b[H\u001b[m", end = "")