import csv
from alchemy import unlocked, elements, recipes, combine

klang = False
def kul_language(l: bool):
    global klang
    klang = l
    lanpan()

def lanpan():
    global groups
    groups = {}
    with open("categories.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            start = f"\u001b[{line[2]}m"
            end = f"\u001b[{line[3]}m"
            look = start + "{}" + end
            groups[line[not klang]] = {
                "look" : look,
                "words" : set(line[4:]),
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
        title = ("kulupu {}" if klang else "{} Words")
        if y["done"]:
            out += "\t• " + ("sina jo e " if klang else "You have all ") + f"\u001b[1;3m{y['look'].format(title.format(x))}\u001b[22;23m{(' ale a' if klang else '')}!\n"
    if len(unlocked) == len(set(elements)):
        out += "\t• " + ("sina jo e " if klang else "You have ") + f"\u001b[1;3;38;2;255;228;18m{('nimi ale' if klang else 'All Words')}\u001b[22;23;39m{(' a' if klang else '')}!\n"
    if len(set(recipes)) == len(combine):
        out += "\t• " + ("sina jo e " if klang else "You have ") + f"\u001b[1;3;38;2;255;228;18m{('nasin ale' if klang else 'All Recipes')}\u001b[22;23;39m{(' a' if klang else '')}!"
    out = out.rstrip("\n")
    if out == "":
        out = "\u001b[2;3m" + ("sina jo ala e pali pini tenpo sama" if klang else "You don't have any achievements yet") + ".\u001b[22;23m"
    else:
        out = "f\u001b[1m" + ("pali pini sina" if klang else "Your Achievements") + ":\u001b[m\n" + out
    print(out)
    input("\u001b[8m")
    print("\u001b[2J\u001b[H\u001b[m", end = "")