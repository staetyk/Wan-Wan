from alchemy import *
#from shortest import kepeken
from kulupu import kule, pana, pini

import tutorial

for endgame in range(2):
    while len(unlocked) < len(set(elements)) or endgame:
        #print('-'*20)
        print('\u001b[1;4mnimi ken ({}/{}):\u001b[22;24m'.format(len(unlocked), len(set(elements))))
        print("\u001b[3m", end = "")
        print(*kule(unlocked), sep=', ', end = "\u001b[23m\n")
        a = input('\n\u001b[1mnimi nanpa wan: \u001b[22m').lower()
        #if a == "?":
            #kepeken()
            #continue
        if a == "!":
            pana()
            continue
        b = input('\u001b[1mnimi nanpa tu: \u001b[22m').lower()
        find_match(a, b)
        pini()
        score += 1
    else:
        print("\u001b[4;38;2;255;228;18msina alasa pini e nimi ale a!")
        sleep(1)
        #print("YOU FOUND ALL THE WORDS!\u001b[m")
        #sleep(1)
        print("\n\u001b[3mpali nanpa:", end = " \u001b[4m")
        sleep(1)
        print(score, end = "\u001b[m")
        if score == len(set(elements)):
            print()
            sleep(1)
            print("\u001b[M\u001b[38;2;0;200;0;1mpali nanpa li lili!\u001b[m")
        if len(set(recipes)) == len(combine):
            print()
            sleep(1)
            print("\u001b[M\u001b[38;2;0;200;0;1mnasin ale!\u001b[m", end = "")
        input("\u001b[8m")
        print("\u001b[2J\u001b[H\u001b[m", end = "")
        continue