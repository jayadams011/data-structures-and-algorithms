from .node import Node


class Stack:
    def __init__(self, iterable=[]):
        self.top = None
        self.len = 0 

    def __len__(self):
        return self.len

    def __str__(self):
        pass

    # define out magics here

    def push(self, val):
        """ push adds one item to the top of the stack"""

        node = Node(val)
        self.len += 1

        node._next = self.top
        self.top = node

        return self.top

    def pop(self):
        """ pop removes the first itme in the stack """
        if self.top is None:
            raise IndexError('Stack is empty')
        self._len -= 1
        node = self.top
        self.top = self.top._next

        return node.val

    def peek(self):
        """ Peek returns the value of what is at the end pass """
        return self.top
