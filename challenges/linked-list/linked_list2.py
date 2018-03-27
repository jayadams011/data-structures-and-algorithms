from node import Node


class LinkedList:
    """This will be a link list class """
    def __init__(self, iter=[]):
        self._current = None
        self.head = None
        self._size = 0

# l = LinkedList([1, 2, 3, 4])

        for item in reversed(iter):
            self.insert(item)
            # l.head => 1 -> 2 -> 3 -> 4 ->

    def __repr__(self):
        # assuming head will have a val (- need to handle the case of None)
        return '<head> => {}' .format(self.head.val)

    def __len__(self):
        return self.size

    def __str__(self):
        pass

    def find(self, val):
        pass

    def insert(self, val):
        self.head = Node(val, self.head)
        self._size += 1

# still need to handle error handling
