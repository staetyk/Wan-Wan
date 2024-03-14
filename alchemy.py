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
            print('\n\u001b[1;38;2;0;200;0mCombination Success!!!', end = "\u001b[22m")
            print()
            if out not in unlocked:
                print('New word unlocked: ' + out, end = '\u001b[m\n')
                unlocked.append(out)
            else:
                print('Word already unlocked: ' + out, end = '\u001b[m\n')
            
        except KeyError:
            print('\n\u001b[1;38;2;255;0;0mCombination Failed!', end = '\u001b[m\n')
    else:
        print('\n\u001b[1;38;2;255;0;0mInvalid word used.', end = '\u001b[m\n')
    sleep(1.5)
    print("\u001b[2J\u001b[H\u001b[m", end = "")

import_combos()

while len(unlocked) < len(set(elements)):
    #print('-'*20)
    print('\u001b[1;4mAvailable Words ({}/{}):\u001b[22;24m'.format(len(unlocked), len(set(elements))))
    print("\u001b[3m", end = "")
    print(*unlocked, sep=', ', end = "\u001b[23m\n")
    a = input('\n\u001b[1mInput One: \u001b[22m').lower()
    b = input('\u001b[1mInput Two: \u001b[22m').lower()
    find_match(a, b)
    score += 1
else:
    print("\u001b[4;38;2;255;228;18mSINA ALASA PINI E NIMI ALE A!")
    sleep(1)
    print("YOU FOUND ALL THE WORDS!\u001b[m")
    sleep(1)
    print("\n\u001b[3mTotal Combinations:", end = " \u001b[4m")
    sleep(1)
    print(score, end = "\u001b[m")
    if score == len(set(elements)):
        print()
        sleep(1)
        print("\u001b[M\u001b[38;2;0;200;0;1mPERFECT SCORE!\u001b[m")
    if len(set(recipes)) == len(combine):
        print()
        sleep(1)
        print("\u001b[M\u001b[38;2;0;200;0;1mEVERY RECIPE!\u001b[m", end = "")