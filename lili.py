import alchemy
from random import randint

llang = False
def lil_language(l: bool):
    global llang
    llang = l

taken = set()

def options():
    out = set()
    for x, y in alchemy.combine.items():
        if y not in out & \
        y not in taken & \
        y not in alchemy.unlocked & \
        x[0] in alchemy.unlocked & \
        x[1] in alchemy.unlocked:
            out.add(y)
    return out

def hint():
    print("\u001b[2J\u001b[H\u001b[m", end = "")
    opt = options()
    if len(opt) == 0:
        print("\u001b[2;3m" + ("sona lili ala li awen." if llang else "No remaining hints.") + "\u001b[22;23m")
    else:
        opt = tuple(opt)
        word = opt[randint(0, len(opt) - 1)]
        print(f"\u001b[1m{word}\u001b[22m")
        global taken
        taken.add(word)
    input("\u001b[8m")
    print("\u001b[2J\u001b[H\u001b[m", end = "")