pointers = []
ale = {}

class node:
    def __init__(self):
        self.children = set()
        self.parents = set()
        global pointers
        self.id = len(pointers)
        pointers.append(self)

    def __add__(self, other: "node | int"):
        if isinstance(other, type(self)):
            self.children.add(other.id)
            other.parents.add(self.id)
        else:
            self.children.add(other)
            pointers[other].parents.add(self.id) # type: ignore

    def __radd__(self, other: int):
        self.parents.add(other)
        pointers[other].children.add(self.id)

class nimi(node):
    def __init__(self, word: str):
        super().__init__()
        self.word = word
        global ale
        ale.update({word : self.id})

    def __str__(self): return self.word

class nasin(node):
    def __init__(self, words: tuple[str, str, str]):
        super().__init__()
        ale[words[0]] + self
        ale[words[1]] + self
        self + ale[words[2]]