from alchemy import combine, elements, unlocked
from pygraph import *
from time import sleep

for x in elements:
    nimi(x)
for x, y in combine.items():
    nasin((x[0], x[1], y))

cache = {}
path = []
def alasa(target: str, current: list[str] = unlocked, _og: bool = True) -> set | list:
    global cache
    global path
    if target in current: return set()
    elif ale[target] in cache: return cache[ale[target]]
        
    crnt = [pointers[ale[x]] for x in current]
    trgt = pointers[ale[target]]
    if _og:
        for x in crnt:
            cache[x.id] = set()

    step = -1
    for x in trgt.parents:
        pre = pointers[x].parents
        for y in pointers[x].parents:
            try:
                pre = pre.union(alasa(str(pointers[y]), current, False))
            except RecursionError or IndexError or ValueError:
                # raise ValueError
                continue
        if trgt.id not in cache or len(cache[trgt.id]) > len(pre):
            cache[trgt.id] = pre
            step = x
    if step not in path and step != -1:
        path.append(step)

    if _og:
        cache = {}
        path = path[::-1]
        out = path
        path = []
    else:
        out = cache[trgt.id]
    return out

def lukin(target: str, current: list[str] = unlocked):
    try:
        data = alasa(target, current) # type: list[int] # type: ignore
    except ValueError:
        raise Exception(target + " is not reachable.")

    steps = []
    #data = data[::-1]
    for x in data:
        recipe = list(pointers[x].parents)
        if len(recipe) == 1:
            recipe += recipe
        recipe.append(tuple(pointers[x].children)[0])
        steps.append(tuple((str(pointers[recipe[i]]) for i in range(3))))

    print(*("{}. \u001b[1m{}\u001b[m + \u001b[1m{}\u001b[m → \u001b[1m{}\u001b[m".format(i + 1, *steps[i]) for i in range(len(steps))), sep = "\n")

def kepeken():
    print("\u001b[2J\u001b[H\u001b[m", end = "")
    target = input("\u001b[1mTarget Word: \u001b[22m").replace(" ", "")
    print("\u001b[2J\u001b[H\u001b[m", end = "")
    try:
        lukin(target)
    except:
        print('\n\u001b[1;38;2;255;0;0mInvalid word used.', end = '\u001b[m\n')
        sleep(1.5)
        return
    input()
    print("\u001b[2J\u001b[H\u001b[m", end = "")
    return