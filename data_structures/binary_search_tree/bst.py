
class Node:
    """ Node class for bst, this allows BST to create an empty Node whne there
     is not a node. """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        """ creates a representaton of the node to return"""
        return '<Node Val: {}'.format(self.val)

    def __str__(self):
        """ these return a string representtaion of Node value"""


class BST:
    """ BST will traverse the tree using functions to return the val of
    nodes at respective palces.  """
    def __init__(self, iter=[]):
        self.root = None
        if iter:
            for item in iter:
                self.insert(item)

        else:
            return None

    def __repr__(self):
        return '<Node Val: {}'.format(self.val)

    def pre_order(self, operation):
        # import pdb; pdb.set_trace()
        """ the preorder operation.  travereses
        the tree retruning root, left right """

        def _walk(node=None):

            if node is None:
                return False

            current = node
            operation(current.val)
            if current.left:
                _walk(current.left)

            if current.right:
                _walk(current.right)

        _walk(self.root)

    def in_order(self, operation):
        # import pdb; pdb.set_trace()
        """ traveres and returns values in order"""
        def _walk(node=None):
            if node is None:
                return False
            current = node
            """ if current has a left child or a right child, traverse
            #  through those childern and returns the current value as it get
            # to the last left or right node """

            if current.left:
                _walk(current.left)
            operation(current.val)
            if current.right:
                _walk(current.right)

        _walk(self.root)

    def post_order(self, operation):
        # import pdb; pdb.set_trace()
        """ traveres and returns values left, right and root """
        def _walk(node=None):
            if node is None:
                return False
            current = node
            """ if current has a left child or a right child,
            # traverse through those childern """
            if current.left:
                _walk(current.left)

            if current.right:
                _walk(current.right)

            operation(current.val)
        _walk(self.root)

    def insert(self, val):
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
