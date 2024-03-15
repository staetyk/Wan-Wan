import alchemy
from alchemy import starting, combine, elements
from pygraph import *

alchemy.import_combos()

for x in elements:
    nimi(x)
for x, y in combine.items():
    nasin((x[0], x[1], y))