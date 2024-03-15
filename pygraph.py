pointers = []

class node:
    def __init__(self):
        self.children = set()
        self.parents = set()
        global pointers
        self.id = len(pointers)
        pointers.append(self)

    def __add__(self, other: "node"):
        self.children.add(other.id)
        other.parents.add(self.id)

class nimi(node):
    def __init__(self, word: str):
        super().__init__()
        self.word = word

    def __str__(self): return self.word

class nasin(node):
    def __init__(self, words: tuple[nimi, nimi, nimi]):
        super().__init__()
        words[0] + self
        words[1] + self
        self + words[2]