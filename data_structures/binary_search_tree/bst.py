from .node import Node


class Bst:
    def __init__(self, iter=[]):
        self.root = None
        if iter:
            for item in iter:
                self.insert(item)

    def insert(root, val):
        if val >= current.val:
            current.right is None
            current.right = Node(val)
        else:
            current = current.right
            _insert(current, val)
        if val < self.root:
            if self.root.left is None:
                self.root.left = Node(val)
            else:
                current = current.left
                _insert(current.val)


def in_order():
    pass


def pre_order():
    pass


def post_order():
    pass

