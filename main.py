from time import sleep
#import json
import csv

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

import alchemy
alchemy.alc_language(lang)
#from shortest import kepeken, sho_language
#sho_language(lang)
from kulupu import kule, pana, pini, kul_language
kul_language(lang)
import tutorial
tutorial.tut_language(lang)
tutorial.use()

def loadsave():
    with open("awen.csv", "r") as file:
        reader = csv.reader(file)
        awen = [x for x in reader]
        unlockedL = set(awen[0])
        endgameL = int(awen[1][0])
        scoreL = int(awen[1][1])
        try:
            recipesL = [tuple(x.split(" ")) for x in awen[2]]
        except:
            recipesL = []
        alchemy.loada(unlockedL, scoreL, recipesL)
        pini()
        return endgameL

def savegame(endgame):
    with open("awen.csv", "w") as file:
        reader = csv.writer(file)
        reader.writerow(list(alchemy.unlocked))
        reader.writerow([str(endgame), str(alchemy.score)])
        reader.writerow(["{} {}".format(x) for x in alchemy.recipes])

def restart():
    with open("awen.csv", "w") as file:
        reader = csv.writer(file)
        reader.writerow(list(alchemy.starting))
        reader.writerow(["0", "0"])
        reader.writerow("")

def play():
    load = ""
    while load not in ["yes", "no", "lon", "ala"]:
        load = input(("sina wile lanpan ala lanpan e lipu awen?\n\u001b[2;3m(lon/ala)\u001b[22;23m\n" if lang else "Load save file?\n\u001b[2;3m(yes/no)\u001b[22;23m\n"))
    load = load == "yes" or load == "lon"
    print("\u001b[2J\u001b[H\u001b[m", end = "")
    
    if load: endgame = loadsave()
    else: endgame = 0
    while endgame < 2:
        while len(alchemy.unlocked) < len(set(alchemy.elements)) or endgame:
            #print('-'*20)
            print('\u001b[1m' + ("nimi sina" if lang else "Your Words") + ' ({}/{}):\u001b[22m'.format(len(alchemy.unlocked), len(set(alchemy.elements))))
            print("\u001b[3m", end = "")
            print(*kule(alchemy.unlocked), sep=', ', end = "\u001b[23m\n")
            a = input('\n\u001b[2m' + ("nimi nanpa wan" if lang else "First Word") + ': \u001b[22m').lower()
            #if a == "?":
                #kepeken()
                #continue
            if a == "!":
                pana()
                continue
            elif a == "*":
                save()
                print("\u001b[2J\u001b[H\u001b[m", end = "")
                continue
            elif a == "***":
                sure = ""
                while sure not in ["yes", "no", "lon", "ala"]:
                    print("\u001b[2J\u001b[H\u001b[m", end = "")
                    sure = input(("sina wile ala wile ala e lipu awen?\n\u001b[2;3m(lon/ala)\u001b[22;23m\n" if lang else "Do you want to delete your save file?\n\u001b[2;3m(yes/no)\u001b[22;23m\n"))
                sure = sure == "yes" or sure == "lon"
                print("\u001b[2J\u001b[H\u001b[m", end = "")
                if sure: restart(); break
                else: continue
            elif a == "**":
                sure = ""
                while sure not in ["yes", "no", "lon", "ala"]:
                    print("\u001b[2J\u001b[H\u001b[m", end = "")
                    sure = input(("sina wile ala wile lanpan e lipu awen?\n\u001b[2;3m(lon/ala)\u001b[22;23m\n" if lang else "Do you want to load your save file?\n\u001b[2;3m(yes/no)\u001b[22;23m\n"))
                sure = sure == "yes" or sure == "lon"
                print("\u001b[2J\u001b[H\u001b[m", end = "")
                if sure: endgame = loadsave()
                continue
            b = input('\u001b[2m' + ("nimi nanpa tu" if lang else "Second Word") + ': \u001b[22m').lower()
            alchemy.find_match(a, b)
            pini()
            alchemy.score += 1
            #awen.write(json.dumps(vars()))
        else:
            print("\u001b[4;38;2;255;228;18m" + ("sina alasa pini e nimi ale a!" if lang else "You've found all the words!"))
            sleep(1)
            #print("YOU FOUND ALL THE WORDS!\u001b[m")
            #sleep(1)
            print("\n\u001b[3m" + ("nanpa pali" if lang else "Moves") + ":", end = " \u001b[4m")
            sleep(1)
            print(alchemy.score, end = "\u001b[m")
            if alchemy.score == len(set(alchemy.elements)):
                print()
                sleep(1)
                print("\u001b[M\u001b[38;2;0;200;0;1m" + ("pali nanpa li lili" if lang else "Fewest Moves") + "!\u001b[m")
            if len(set(alchemy.recipes)) == len(alchemy.combine):
                print()
                sleep(1)
                print("\u001b[M\u001b[38;2;0;200;0;1m" + ("nasin ale" if lang else "Every Recipe") + "!\u001b[m", end = "")
            input("\u001b[8m")
            print("\u001b[2J\u001b[H\u001b[m", end = "")
            #awen.write(json.dumps(vars()))
        endgame += 1

while True:
    play()