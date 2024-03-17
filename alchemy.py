# A simple infintely expandable alchemy sim :)
import csv
from time import sleep

starting = ['ala', 'ijo']
unlocked = starting.copy()
combine = {}
score = 0
elements = []
recipes = []

def import_combos():
    global elements
    elements = []
    with open('combos.csv') as file:
        reader = csv.reader(file)
        for line in reader:
            combo = tuple(sorted((line[0].replace(" ", ""), line[1].replace(" ", ""))))
            combine[combo] = line[2]
            elements.append(line[2])
    elements += starting

def find_match(a, b):
    if a in unlocked and b in unlocked:
        try:
            recipes.append(tuple(sorted((a,b))))
            out = combine[tuple(sorted((a, b)))]
            print('\n\u001b[1;38;2;0;200;0mpona!', end = "\u001b[22m")
            print()
            if out not in unlocked:
                print('nimi sin: ' + out, end = '\u001b[m\n')
                unlocked.append(out)
            else:
                print('nimi majuna: ' + out, end = '\u001b[m\n')
            
        except KeyError:
            print('\n\u001b[1;38;2;255;0;0mike!', end = '\u001b[m\n')
    else:
        print('\n\u001b[1;38;2;255;0;0mnimi ike.', end = '\u001b[m\n')
    sleep(1.5)
    print("\u001b[2J\u001b[H\u001b[m", end = "")

import_combos()