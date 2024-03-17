from time import sleep

print("""\u001b[38;2;255;0;0;48;2;0;0;100m                      
       ██        ██   
     ████      ████   
   ██  ██    ██  ██   
       ██        ██   
       ██        ██   
       ██        ██   
       ██        ██   
                      
   \u001b[38;2;255;255;0;1m  MUSI WAN WAN     
                      \u001b[39;49;22m""", end = "" )
sleep(2)

lang = ""
while lang not in ["en", "tp", "english", "tokipona"]:
    print("\u001b[2J\u001b[H\u001b[m", end = "")
    lang = input("toki seme? | Which language?\n\u001b[2;3m(en/tp/english/toki pona)\u001b[m\n").lower().replace(" ", "")
lang = lang == "tp" or lang == "tokipona"

from alchemy import *
alc_language(lang)
#from shortest import kepeken, sho_language
#sho_language(lang)
from kulupu import kule, pana, pini, kul_language
kul_language(lang)
import tutorial
tutorial.tut_language(lang)
tutorial.use()

for endgame in range(2):
    while len(unlocked) < len(set(elements)) or endgame:
        #print('-'*20)
        print('\u001b[1m' + ("nimi sina" if lang else "Your Words") + ' ({}/{}):\u001b[22m'.format(len(unlocked), len(set(elements))))
        print("\u001b[3m", end = "")
        print(*kule(unlocked), sep=', ', end = "\u001b[23m\n")
        a = input('\n\u001b[2m' + ("nimi nanpa wan" if lang else "First Word") + ': \u001b[22m').lower()
        #if a == "?":
            #kepeken()
            #continue
        if a == "!":
            pana()
            continue
        b = input('\u001b[2m' + ("nimi nanpa tu" if lang else "Second Word") + ': \u001b[22m').lower()
        find_match(a, b)
        pini()
        score += 1
    else:
        print("\u001b[4;38;2;255;228;18m" + ("sina alasa pini e nimi ale a!" if lang else "You've found all the words!"))
        sleep(1)
        #print("YOU FOUND ALL THE WORDS!\u001b[m")
        #sleep(1)
        print("\n\u001b[3m" + ("nanpa pali" if lang else "Moves") + ":", end = " \u001b[4m")
        sleep(1)
        print(score, end = "\u001b[m")
        if score == len(set(elements)):
            print()
            sleep(1)
            print("\u001b[M\u001b[38;2;0;200;0;1m" + ("pali nanpa li lili" if lang else "Fewest Moves") + "!\u001b[m")
        if len(set(recipes)) == len(combine):
            print()
            sleep(1)
            print("\u001b[M\u001b[38;2;0;200;0;1m" + ("nasin ale" if lang else "Every Recipe") + "!\u001b[m", end = "")
        input("\u001b[8m")
        print("\u001b[2J\u001b[H\u001b[m", end = "")
        continue