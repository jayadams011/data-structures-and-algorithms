from .node import Node


class Stack:
    """ created class.  Init class"""
    def __init__(self, iterable=[]):
        self.top = None
        self.len = 0
    """define magics """
    def __len__(self):
        return self.len

    def __str__(self):
        pass

    def push(self, val):
        """ push adds one item to the top of the stack"""
        self.top = Node(val, self.top)
        self.len += 1

    def pop(self):
        """ pop removes the first itme in the stack """
        curr = self.top
        self.top = self.top._next
        self.len -= 1
        return curr

    def peek(self):
        """ Peek returns the value of what is at the end pass """
        return self.top
