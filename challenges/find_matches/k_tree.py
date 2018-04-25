from queue import Queue


class Node:
    def __init__(self, val, children=[]):
        """ Node init """
        self.val = val
        children = []

    def __repr__(self):
        """ Node repr """
        return 'node {}'.format(self.val)


class Ktree:
    def __init__(self):
        """ magic init """
        self.root = None
        return None

    def __str__():
        """ magic str """
        pass

    def __repr__():
        """ magic repr """"
        pass

    def pre_order(self, operation):
        """ the preorder operation.  """

        def _walk(node=None):
            if node is None:
                return False
            operation(node.val)
            for child in node.children:
                _walk(child)
        _walk(self.root)

    def post_order(self, operation):
        """ traveres and returns values  """
        def _walk(node=None):
            if node is None:
                return False
            for child in node.children:
                _walk(child)
            operation(node.val)
        _walk(self.root)

    def breadth_first_traversal(tree, action=print):
        """define function to print nodes in the breadth first order"""
        if tree.root is None:
            return False
        action(tree.root.val)
        q = Queue()
        for child in children:
            q.enqueue(tree.root.children[0])
        if tree.root.children[1]:
            q.enqueue(tree.root.children[1])
        top = q.front
        while top:
            node = top.val
            action(node.val)
            if node.children[0]:
                q.enqueue(node.children[0])
            if node.children[1]:
                q.enqueue(node.children[1])
            top = top.next

    def insert(self, value, parent=None):
        """insert value in the tree"""
        node = Node(value)
        if self.root is None:
            self.root = node
            return
        if self.root.val == parent or parent is None:
            self.root.children.append(node)
            return
