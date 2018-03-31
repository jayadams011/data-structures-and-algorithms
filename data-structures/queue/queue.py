from .node import Node


class Queue:
    def __init__(self, iterable=[]):
        self.front = None
        self.back = None
        self._len = 0

        for item in iterable:
            self.enqueue(item)

    def __len__(self):
        """ return the length of the queue """
        return self._len

    def __str__(self):
        """ return the items in the queue """
        string = ""
        current = self.front
        for _ in range(self._len):
            string += str(current.val) + " "
            current = current._next
        return string.rstrip()

    def enqueue(self, val):
        """ adds to a queue much like push """
        node = Node(val)
        if self._len == 0:
            self.back = node
            self.front = node
        else:
            self.back = node
        self._len += 1
        return self.back.val, self.front.val
        
    def dequeue(self):
        """ removes an item form the queue like pop """
        if len(self) == 0:
            return False
            raise IndexError('Queue is empty')
        else:
            current = self.front
            self.front = current._next
            return current


