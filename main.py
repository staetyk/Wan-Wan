from alchemy import *
from shortest import kepeken

while len(unlocked) < len(set(elements)):
    #print('-'*20)
    print('\u001b[1;4mAvailable Words ({}/{}):\u001b[22;24m'.format(len(unlocked), len(set(elements))))
    print("\u001b[3m", end = "")
    print(*unlocked, sep=', ', end = "\u001b[23m\n")
    a = input('\n\u001b[1mInput One: \u001b[22m').lower()
    """if a == "?":
        kepeken()
        continue"""
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