class Node(object):
    def __init__(self, animalName=None, animalKind=None, pointer=None):
        self.animalName = animalName
        self.animalKind = animalKind
        self.pointer = pointer
        self.timestamp = 0

    def __repr__(self):
        return self.val
