from queue import Queue


class Node:
    def __init__(self, val, children=[]):
        self.val = val
        children = []

    def __repr__(self):
        return 'node {}'.format(self.val)


class Ktree:
    def __init__(self):
        self.root = None
        return None

    def __str__():
        pass

    def __repr__():
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
        if tree.root.left:
            q.enqueue(tree.root.left)
        if tree.root.right:
            q.enqueue(tree.root.right)
        top = q.front
        while top:
            node = top.val
            action(node.val)
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
            top = top.next

    def insert(self, parent, val):
        """ inserts a value in the correct place based on val and the
        tree paramerters """
        node = Node(val)
        current = self.root

        if self.root is None:
            self.root = node
            return node

        while current:
            if val >= current.val:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = node
                    break

            elif val < current.val:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = node
                    break

        return node
