from time import sleep
from kulupu import groups

tlang = False
def tut_language(l: bool):
    global tlang
    tlang = l

def use():
    watch = ""
    while watch not in ["lon", "ala", "yes", "no"]:
        print("\u001b[2J\u001b[H\u001b[m", end = "")
        watch = input(("sina wile ala wile lukin e open sona?" if tlang else "See tutorial?") + "\n\u001b[2;3m" + ("(lon/ala)" if tlang else "(yes/no)") + "\u001b[m\n").lower().replace(" ", "")
    print("\u001b[2J\u001b[H\u001b[m", end = "")
    watch = watch == "lon" or watch == "yes"

    if watch:
        if tlang:
            txt = [
                "sina jo e nimi tu la open.",
                "o pana e nimi tu tan wan e nimi.",
                "o pana e '!' la sina wile lukin e pali pini sina.",
                #"o pana e '?' la sina wile lukin e sona lili.",
                f"linja lon anpa \u001b[1m{groups['pu']['look'].format('nimi pu')}\u001b[22m.\nnimi kulupu ante li kule.",
                f"kulupu loje li \u001b[1m{groups['soweli']['look'].format('nimi soweli')}\u001b[22m.\nkulupu jelo li \u001b[1m{groups['sijelo']['look'].format('nimi sijelo')}\u001b[22m.\nkulupu laso loje li \u001b[1m{groups['kule']['look'].format('nimi kule')}\u001b[22m.\nkulupu laso jelo li \u001b[1m{groups['nasin']['look'].format('nimi nasin')}\u001b[22m.\nkulupu laso li \u001b[1m{groups['lipu']['look'].format('nimi lipu')}\u001b[22m.\nkulupu kapesi li \u001b[1m{groups['lili']['look'].format('nimi lili')}\u001b[22m.",
                "o alasa alasa pini e nimi ale li musi a!"
            ]
        else:
            txt = [
                "You start with two words.",
                "Enter two words to combine them.",
                "Type '!' if you want to see your achievements.",
                #"Type '?' if you want a hint.",
                f"Underlined words are \u001b[1m{groups['Original']['look'].format('Original Words')}\u001b[22m.\nWords in other groups are colored.",
                f"Red words are \u001b[1m{groups['Animal']['look'].format('Animal Words')}\u001b[22m.\nYellow words are \u001b[1m{groups['Body Part']['look'].format('Body Part Words')}\u001b[22m.\nPurple words are \u001b[1m{groups['Color']['look'].format('Color Words')}\u001b[22m.\nGreen words are \u001b[1m{groups['Direction']['look'].format('Direction Words')}\u001b[22m.\nBlue words are \u001b[1m{groups['Book']['look'].format('Book Words')}\u001b[22m.\nBrown words are \u001b[1m{groups['Particle']['look'].format('Particle Words')}\u001b[22m.",
                "Try to find every word, and have fun!"
            ]
        for x in txt:
            lines = x.split("\n")
            for i in range(len(lines)):
                print(lines[i])
                if i + 1 < len(lines):
                    sleep(1)
            input("\u001b[8m")
            print("\u001b[2J\u001b[H\u001b[m", end = "")