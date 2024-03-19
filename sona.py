import csv
from time import sleep

dlang = False
def dic_language(l: bool):
    global dlang
    dlang = l

ku = {}
with open("toki.csv", "r") as file:
    reader = csv.reader(file)
    for line in reader:
        ku.update({line[0] : line[1:]})

def define():
    print("\u001b[2J\u001b[H\u001b[m", end = "")
    word = input("\u001b[2;3m" + ("nimi: " if dlang else "Word: ") + "\u001b[22;23m").lower().replace(" ", "")
    print("\u001b[2J\u001b[H\u001b[m", end = "")
    if word in ku:
        for x in ku[word]: print(x)
        input("\u001b[8m")
        print("\u001b[2J\u001b[H\u001b[m", end = "")
        return
    else:
        print("\u001b[1;38;2;255;0;0m" + ("nimi ike." if dlang else "Invalid Word.") + '\u001b[m')
        sleep(2)
        print("\u001b[2J\u001b[H\u001b[m", end = "")
        return